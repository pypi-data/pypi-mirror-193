import json
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Dict, List

from marshmallow import EXCLUDE, Schema, fields, post_load

from navability.common.timestamps import TS_FORMAT
from navability.common.versions import payload_version


@dataclass()
class BlobEntry:
    id: str
    label: str
    description: str
    # createdTimestamp: datetime # = datetime.utcnow()
    # updatedTimestamp: datetime
    # size: int
    blobstore: str
    hash: str = ''
    mimeType: str = 'application/octet-stream'
    origin: str = ''

    def __repr__(self):
        return (
            f"<BlobEntry(label={self.label},"
            f"label={self.label},id={self.id})>"
        )

    def dump(self):
        return BlobEntrySchema().dump(self)

    def dumps(self):
        return BlobEntrySchema().dumps(self)

    @staticmethod
    def load(data):
        import pdb; pdb.set_trace()
        return BlobEntrySchema().load(data)


# Legacy BlobEntry_ contract
class BlobEntrySchema(Schema):
    id = fields.Str(required=True)
    label = fields.Str(required=True)
    description: str = fields.Str(required=True)
    # createdTimestamp: datetime = fields.Method("get_timestamp", "set_timestamp", required=True)
    # updatedTimestamp: datetime = fields.Method("get_timestamp", "set_timestamp", required=True)
    # size: int  = fields.Integer(required=True)
    blobstore: str = fields.Str(required=True)
    hash = fields.Str(required=False)
    mimeType = fields.Str(required=False)
    origin = fields.Str(required=False)

    class Meta:
        ordered = True

    def get_timestamp(self, obj):
        # Return a robust timestamp
        ts = obj.timestamp.isoformat(timespec="milliseconds")
        if not obj.timestamp.tzinfo:
            ts += "+00"
        return ts

    def set_timestamp(self, obj):
        return datetime.strptime(obj["formatted"], TS_FORMAT)

    @post_load
    def marshal(self, data, **kwargs):
        return BlobEntry(**data)