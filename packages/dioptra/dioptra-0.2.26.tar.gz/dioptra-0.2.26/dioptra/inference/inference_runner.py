import os
import orjson
import mgzip
import uuid
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor

import boto3

from dioptra.lake.utils import upload_to_lake_from_s3, wait_for_upload


class InferenceRunner():
    def __init__(self):

        api_key = os.environ.get('DIOPTRA_API_KEY', None)
        if api_key is None:
            raise RuntimeError('DIOPTRA_API_KEY env var is not set')

        s3_bucket = os.environ.get('DIOPTRA_UPLOAD_BUCKET', None)

        if s3_bucket is None:
            raise RuntimeError('DIOPTRA_UPLOAD_BUCKET env var is not set')

        s3_prefix_bucket = os.environ.get('DIOPTRA_UPLOAD_PREFIX', None)

        self.api_key = api_key
        self.s3_bucket = s3_bucket
        self.s3_prefix_bucket = s3_prefix_bucket
        self.max_batch_size = 1000
        self.uploads = {}

    def _ingest_data(self, records):
        print('ingesting data ...')

        s3_client = boto3.client('s3')
        file_name = f'{str(uuid.uuid4())}_{datetime.utcnow().isoformat()}.ndjson.gz'

        if self.s3_prefix_bucket is not None:
            file_name = f'{self.s3_prefix_bucket}{file_name}'

        payload = b'\n'.join([orjson.dumps(record, option=orjson.OPT_SERIALIZE_NUMPY)for record in records])
        compressed_payload = mgzip.compress(payload, compresslevel=2)

        s3_client.put_object(
            Body=compressed_payload,
            Bucket=self.s3_bucket,
            Key=file_name,
        )

        self.uploads[file_name] = upload_to_lake_from_s3(self.s3_bucket, file_name)

    def wait_for_uploads(self):
        with ThreadPoolExecutor() as executor:
            upload_ids = list(map(lambda u: u['id'], self.uploads.values()))
            
            return list(executor.map(wait_for_upload, upload_ids, timeout=900, chunksize=10))
