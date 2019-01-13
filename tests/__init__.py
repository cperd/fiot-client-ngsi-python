import unittest
from os.path import dirname, realpath, join
from fiotclient.context import FiwareContextClient
from fiotclient.iot import FiwareIotClient


class TestCommonMethods(unittest.TestCase):

    files_dir_path = join(dirname(realpath(__file__)), 'files')

    def setUp(self):
        self._remove_all_entities()
        self._remove_all_devices()

    def _build_file_path(self, filename):
        return join(self.files_dir_path, filename)

    def _remove_all_entities(self):
        context_client = FiwareContextClient(self._build_file_path('config.ini'))
        response = context_client.get_entities()
        data = response['response']

        for entity in data:
            context_client.remove_entity(entity['type'], entity['id'])

    def _remove_all_devices(self):
        iot_client = FiwareIotClient(self._build_file_path('config.ini'))
        response = iot_client.list_devices()
        data = response['response']
        devices = data['devices']

        for device in devices:
            iot_client.remove_device(device['device_id'])
