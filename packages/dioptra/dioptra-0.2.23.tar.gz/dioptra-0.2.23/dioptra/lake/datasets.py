import os
import requests

from dioptra.lake.utils import download_from_lake, _list_dataset_metadata

def list_datasets():
    """
    List all the datasets

    """

    dataset_list = []

    for metadata in _list_dataset_metadata():
        my_dataset = Dataset()
        my_dataset.dataset_id = metadata['uuid']
        my_dataset.dataset_name = metadata['display_name']
        dataset_list.append(my_dataset)

    return dataset_list

class Dataset():

    def __init__(self):

        api_key = os.environ.get('DIOPTRA_API_KEY', None)
        if api_key is None:
            raise RuntimeError('DIOPTRA_API_KEY env var is not set')

        self.api_key = api_key
        self.app_endpoint = os.environ.get('DIOPTRA_APP_ENDPOINT', 'https://app.dioptra.ai')
        self.dataset_id = None
        self.dataset_name = None

    def get_from_uuid(self, uuid):
        """
        Retreive a dataset using its uuid

        Parameters:
            uuid: uuid of the dataset
        """
        try:
            r = requests.get(f'{self.app_endpoint}/api/dataset/{uuid}', headers={
                'content-type': 'application/json',
                'x-api-key': self.api_key
            })
            r.raise_for_status()
        except requests.exceptions.RequestException as err:
            print('There was an error retreiving a dataset ...')
            raise err
        metadata = r.json()
        if len(metadata) == 0:
            raise ValueError(f'No Dataset exists for uuid {uuid}')
        self.dataset_name = metadata['display_name']
        self.dataset_id = uuid

    def get_from_name(self, name):
        """
        Retreive a dataset using its name

        Parameters:
            name: name of the dataset
        """

        for metadata in _list_dataset_metadata():
            if metadata['display_name'] == name:
                self.dataset_name = name
                self.dataset_id = metadata['uuid']
                return
        raise ValueError(f'No Dataset exists for name {name}')

    def create(self, name):
        """
        Creates a dataset. Datasets are collections of datapoints that are version controled by Dioptra

        Parameters:
            name: name of the dataset
        """

        try:
            r = requests.post(f'{self.app_endpoint}/api/dataset', headers={
                'content-type': 'application/json',
                'x-api-key': self.api_key
            }, json={
                'displayName': name
            })
            r.raise_for_status()
        except requests.exceptions.RequestException as err:
            print('There was an error creating a dataset ...')
            raise err
        self.dataset_name = name
        self.dataset_id = r.json()['uuid']

    def commit(self, message):
        """
        Commit the changes made to the dataset that are not committed

        Parameters:
            message: message of the commit
        """

        try:
            r = requests.post(f'{self.app_endpoint}/api/dataset/{self.dataset_id}/commit', headers={
                'content-type': 'application/json',
                'x-api-key': self.api_key
            }, json={
                'message': message
            })
            r.raise_for_status()
        except requests.exceptions.RequestException as err:
            print('There was an error committing a dataset ...')
            raise err

        # returns the commit uuid
        return r.json()['uuid']

    def history(self):
        """
        Get the dataset commit history

        """

        try:
            r = requests.get(f'{self.app_endpoint}/api/dataset/{self.dataset_id}/versions', headers={
                'content-type': 'application/json',
                'x-api-key': self.api_key
            })
            r.raise_for_status()
        except requests.exceptions.RequestException as err:
            print('There was an error creating a dataset ...')
            raise err

        return r.json()

    def download(self, fields=['*']):
        """
        Get the uuids of the datapoints in the dataset

        Parameters:
            fields: the list of fields to be downloaded.
                    By default all fields are returned, except embeddings & logits

        """

        try:
            r = requests.get(f'{self.app_endpoint}/api/dataset/{self.dataset_id}/datapoints', headers={
                'content-type': 'application/json',
                'x-api-key': self.api_key
            })
            r.raise_for_status()
        except requests.exceptions.RequestException as err:
            print('There was an error downloading a dataset ...')
            raise err

        request_ids = [entry['request_id'] for entry in r.json()]

        return download_from_lake(fields=fields, filters=[{
            'left': 'request_id',
            'op': 'in',
            'right': request_ids
        }])

    def add(self, uuids):
        """
        Add datapoints to the dataset using their uuids
        The datapoints will be uncommitted until a commit command is called

        Parameters:
            uuids: list of uuids
        """

        try:
            r = requests.post(f'{self.app_endpoint}/api/datapoints/from-event-uuids', headers={
                'content-type': 'application/json',
                'x-api-key': self.api_key
            }, json={
                'eventUuids': uuids
            })
            r.raise_for_status()
        except requests.exceptions.RequestException as err:
            print('There was an error adding datapoints to a dataset ...')
            raise err

        datapoints_uuids = [entity['uuid'] for entity in r.json()]

        try:
            r = requests.post(f'{self.app_endpoint}/api/dataset/{self.dataset_id}/add', headers={
                'content-type': 'application/json',
                'x-api-key': self.api_key
            }, json={
                'datapointIds': datapoints_uuids
            })
            r.raise_for_status()
        except requests.exceptions.RequestException as err:
            print('There was an error adding datapoints to a dataset ...')
            raise err

    def remove(self, uuids):
        """
        Remove datapoints to the dataset using their uuids
        The datapoints will be uncommitted until a commit command is called unless the datapoints are aleady uncommitted

        Parameters:
            uuids: list of uuids
        """

        try:
            r = requests.post(f'{self.app_endpoint}/api/datapoints/from-event-uuids', headers={
                'content-type': 'application/json',
                'x-api-key': self.api_key
            }, json={
                'eventUuids': uuids
            })
            r.raise_for_status()
        except requests.exceptions.RequestException as err:
            print('There was an error adding datapoints to a dataset ...')
            raise err

        datapoints_uuids = [entity['uuid'] for entity in r.json()]

        try:
            r = requests.post(f'{self.app_endpoint}/api/dataset/{self.dataset_id}/remove', headers={
                'content-type': 'application/json',
                'x-api-key': self.api_key
            }, json={
                'datapointIds': datapoints_uuids
            })
            r.raise_for_status()
        except requests.exceptions.RequestException as err:
            print('There was an error adding datapoints to a dataset ...')
            raise err

    def checkout(self, commit_id):
        """
        Checkout the dataset as of a commit id.
        This will delete the current uncommitted changes

        Parameters:
            commit_id: id of the commit to checkout
        """

        try:
            r = requests.post(f'{self.app_endpoint}/api/dataset/{self.dataset_id}/checkout/{commit_id}', headers={
                'content-type': 'application/json',
                'x-api-key': self.api_key
            })

            r.raise_for_status()
        except requests.exceptions.RequestException as err:
            print('There was an error checking out a dataset ...')
            raise err

        return r.json()

    def delete(self):
        """
        Delete the dataset. This is NOT reversible !!

        """

        try:
            r = requests.delete(f'{self.app_endpoint}/api/dataset/{self.dataset_id}', headers={
                'content-type': 'application/json',
                'x-api-key': self.api_key
            })

            r.raise_for_status()
        except requests.exceptions.RequestException as err:
            print('There was an error deleting a dataset ...')
            raise err


    def __str__(self):
        return f'Dataset with uuid {self.dataset_id} and name {self.dataset_name}'

    def __repr__(self):
        return self.__str__()

