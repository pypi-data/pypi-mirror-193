from typing import Optional
from pydantic import BaseModel


class Object(BaseModel):
    key: str
    size: int
    eTag: str
    contentType: str

    @staticmethod
    def load(object_obj):
        return Object.parse_obj({
            'key': object_obj['key'],
            'size': object_obj['size'],
            'eTag': object_obj['eTag'],
            'contentType': object_obj['contentType']
        })


class Bucket(BaseModel):
    name: str
    owner: str

    @staticmethod
    def load(bucket_obj):
        return Bucket.parse_obj({
            'name': bucket_obj['name'],
            'owner': bucket_obj['ownerIdentity']['principalId']
        })


class GpsData(BaseModel):
    x: float = 0.0
    y: float = 0.0
    yaw: Optional[float] = 0.0
    fix: int = 0
    velocity: Optional[float] = 0.0


class IdData(BaseModel):
    location: str
    device: str
    uploader: Optional[str]
    project: Optional[str]
    time: str
    gps: Optional[GpsData]


class EventData(BaseModel):
    type: str = ''
    time: str = ''
    sourceIp: str = ''
    bucket: Bucket = None
    object: Object = None

    @staticmethod
    def load(event_obj: dict):
        event_obj = event_obj['Records'][0]
        return EventData.parse_obj({
            'type': event_obj['eventName'],
            'time': event_obj['eventTime'],
            'sourceIp': event_obj['requestParameters']['sourceIPAddress'],
            'bucket': Bucket.load(event_obj['s3']['bucket']),
            'object': Object.load(event_obj['s3']['object'])
        })


class Metadata(BaseModel):
    id: IdData
    custom: Optional[dict]

    @staticmethod
    def load(id_data: IdData, custom_data: dict = None):
        if not custom_data:
            custom_data = {}

        return Metadata.parse_obj({
            'id': id_data,
            'custom': custom_data
        })


class MongoData(BaseModel):
    event: EventData
    meta: Metadata

    @staticmethod
    def load(event_data: EventData, meta_data: Metadata):
        return MongoData.parse_obj({
            'event': event_data,
            'meta': meta_data
        })


def create_mongo_filter(metadata_obj: Metadata = None, location=None, device=None, gps=None, time=None, source_ip=None,
                        bucket_name=None, file_name=None, **custom_metadata):
    """Returns a dictionary in mongo format

    Use the return dict as paramenter in mongo query funcitons such as find()

    Any other parameter passed will be interpreted as custom
    """

    if metadata_obj is not None:
        # As the user filled the metadata_obj, no other values must be filled in
        for parameter, value in locals().items():
            assert value is None or parameter in ["metadata_obj", "custom_metadata"], \
                "If you provide metadata_obj, leave any other parameter blank"
        assert custom_metadata == {}

        # Uncomment if you want to accept both metadata and metadata.dict() parameters
        # Make sure to change every metadata.x to metadata["x"] down here
        # if not isinstance(metadata_obj, dict):
        #     metadata_obj = metadata_obj.dict()
        location = metadata_obj.id.location
        device = metadata_obj.id.device
        gps = metadata_obj.id.gps
        time = metadata_obj.id.time
        # source_ip, bucket_name, file_name are in "event", not here...
        custom_metadata = metadata_obj.custom

    res = {
        "meta.id.location": location,
        "meta.id.device": device,
        "meta.id.gps": gps,
        "meta.id.time": time,
        "event.sourceIp": source_ip,
        "event.bucket.name": bucket_name,
        "event.object.key": file_name,
    }

    for k, v in custom_metadata.items():
        res["meta.custom." + k] = v

    for k, v in list(res.items()):
        if v is None:
            del res[k]

    return res
