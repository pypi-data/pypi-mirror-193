from __future__ import annotations
import time
from typing import Any, List, TypedDict, Optional, Dict
import typing
import boto3
from mypy_boto3_dynamodb.type_defs import AttributeValueTypeDef
from gloo.pinecone_integration import EmbeddingChunk, Span
from gloo.types import EmbeddingType, StageType
import os

# Load AWS credentials from environment variables
access_key_id = os.environ.get("AWS_ACCESS_KEY_ID")
secret_access_key = os.environ.get("AWS_SECRET_ACCESS_KEY")

# Load AWS region from environment variable
region = os.environ.get("AWS_REGION", "us-east-1")

dynamodb = boto3.client(
    "dynamodb",
    aws_access_key_id=access_key_id,
    aws_secret_access_key=secret_access_key,
    region_name=region,
)

# create an S3 client
s3 = boto3.client(
    "s3",
    aws_access_key_id=access_key_id,
    aws_secret_access_key=secret_access_key,
    region_name=region,
)

ModelTableName = "documents-prod"
ModelBucketName = "gloo-documents-prod"


class Asset(typing.TypedDict):
    span: Span
    content: str


class EmbeddingStatus(typing.TypedDict):
    type: EmbeddingType
    stage: StageType
    updateTimeMs: int


class EmbeddingContent(EmbeddingStatus):
    chunks: Optional[List[EmbeddingChunk]]


def to_aws(e: EmbeddingContent) -> Dict[str, AttributeValueTypeDef]:
    as_aws = {
        "M": {
            "type": {"S": e["type"]},
            "stage": {"S": e["stage"]},
            "updateTimeMs": {"N": str(e["updateTimeMs"])},
        }
    }

    if e["chunks"]:
        chunks = []
        for c in e["chunks"]:
            chunk = {
                "M": {
                    "dbId": {"S": c["dbId"]},
                    "start": {"N": str(c["span"]["start"])},
                    "end": {"N": str(c["span"]["end"])},
                }
            }
            chunks.append(chunk)
        as_aws["M"]["chunks"] = {"L": chunks}

    return as_aws


def from_aws(r: Dict[str, AttributeValueTypeDef]) -> EmbeddingContent:
    chunks = []
    if "M" in r:
        m = r["M"]
        if "chunks" in m and "L" in m["chunks"]:
            chunks = [
                EmbeddingChunk(
                    dbId=s["M"]["dbId"]["S"],
                    span=Span(
                        start=int(s["M"]["start"]["N"]),
                        end=int(s["M"]["end"]["N"]),
                    ),
                )
                for s in m["chunks"]["L"]
            ]
    return {
        "type": EmbeddingType(m["type"]["S"]),
        "stage": StageType(m["stage"]["S"]),
        "updateTimeMs": int(m["updateTimeMs"]["N"]),
        "chunks": chunks,
    }


class DocumentModelItem:
    def __init__(
        self,
        appId: str,
        documentId: str,
        name: str,
        source: str,
        tags: List[str],
        assets: List[Asset],
        status: List[EmbeddingContent],
    ):
        self.appId = appId
        self.documentId = documentId
        self.name = name
        self.source = source
        self.tags = tags
        self.assets = assets
        self.status = status

    @staticmethod
    def load(appId: str, documentId: str):
        response = dynamodb.get_item(
            TableName=ModelTableName,
            Key={"appId": {"S": appId}, "documentId": {"S": documentId}},
        )
        if "Item" in response:
            return DocumentModelItem.fromAWS(response["Item"])
        else:
            raise Exception("Document not found")

    def asAWS(self) -> Dict[str, AttributeValueTypeDef]:
        aws_data = {
            "appId": {"S": self.appId},
            "documentId": {"S": self.documentId},
            "name": {"S": self.name},
            "source": {"S": self.source},
        }
        if self.tags:
            aws_data["tags"] = {"SS": self["tags"]}
        if self.assets:
            aws_data["assets"] = {
                "L": [
                    {
                        "M": {
                            "start": {"N": str(a["span"]["start"])},
                            "end": {"N": str(a["span"]["end"])},
                            "content": {"S": a["content"]},
                        }
                    }
                    for a in self["assets"]
                ]
            }
        if self.status:
            aws_data["status"] = {"L": [to_aws(s) for s in self.status]}

        return aws_data

    @staticmethod
    def fromAWS(raw: Dict[str, AttributeValueTypeDef]) -> DocumentModelItem:
        return DocumentModelItem(
            **{
                "appId": raw["appId"]["S"],
                "documentId": raw["documentId"]["S"],
                "name": raw["name"]["S"],
                "source": raw["source"]["S"],
                "tags": raw.get("tags", {}).get("SS", []),
                "assets": [
                    {
                        "span": {
                            "start": int(a["M"]["start"]["N"]),
                            "end": int(a["M"]["end"]["N"]),
                        },
                        "content": a["M"]["content"]["S"],
                    }
                    for a in raw.get("assets", {}).get("L", [])
                ],
                "status": [
                    from_aws(s) for s in raw.get("status", {}).get("L", [])
                ],
            }
        )

    def read(self):
        response = s3.get_object(
            Bucket=ModelBucketName,
            Key=f"app/{self.appId}/doc/{self.documentId}",
        )
        return response["Body"].read().decode("utf-8")

    def update_embedding_status(
        self,
        e_type: EmbeddingType,
        stage: StageType | None,
        chunks: typing.Optional[typing.List[Span]] = None,
        now: typing.Optional[int] = None,
    ):
        if stage is None:
            self.status = [s for s in self.status if s["type"] != e_type]
        else:
            now = now or time.time_ns() // 1000
            for e in self.status:
                if e["type"] == e_type:
                    e["stage"] = stage
                    e["updateTimeMs"] = now
                    if chunks is not None:
                        e["chunks"] = chunks
                    break
            else:
                self.status.append(
                    EmbeddingContent(
                        type=e_type,
                        stage=stage,
                        updateTimeMs=now,
                        chunks=chunks,
                    )
                )
        self.save()

    def save(self):
        dynamodb.put_item(TableName=ModelTableName, Item=self.asAWS())
