from minio import Minio
from pathlib import Path
from glob import glob
from io import BytesIO
from PIL import Image

from .meta import Metadata, create_mongo_filter


class MinioClient(Minio):
    def __init__(self, access_key: str, secret_key: str, endpoint: str):
        super().__init__(
            endpoint,
            access_key=access_key,
            secret_key=secret_key,
            secure=True
        )

    def upload_file(self, bucket_name: str, file_path: str, metadata: Metadata):
        file_name = Path(file_path).name
        self.fput_object(bucket_name=bucket_name, object_name=file_name, file_path=file_path, metadata=metadata.dict())

    def upload_files(self, bucket_name: str, dir_path: str, metadata: Metadata):
        for file in glob(dir_path):
            self.upload_file(bucket_name, file, metadata)

    def upload_binary_file(self, bucket_name: str, file_path: str, metadata: Metadata):
        with open(file_path, 'rb') as f:
            data = f.read()
        # self.put_object(bucket_name, Path(file_path).name, BytesIO(data), length=len(data), metadata=metadata.dict())
        self.upload_binary(bucket_name, Path(file_path).name, BytesIO(data), len(data), metadata)

    def upload_binary(self, bucket_name: str, object_name: str, data: BytesIO, length: int, metadata: Metadata):
        self.put_object(bucket_name, object_name, data, length=length, metadata=metadata.dict())

    def get_all_images_by_example(self, obj, collection):
        """Returns a mongo query iterable object"""

        for item in collection.find(create_mongo_filter(obj)):
            # TODO check if that is an image
            image_hex_bytes = self.get_object(item["event"]["bucket"]["name"], item["event"]["object"]["key"])
            image_stream = BytesIO(image_hex_bytes.read())
            image_file = Image.open(image_stream)
            yield image_file, item
