from unittest.mock import patch, Mock
from time import sleep

from nio.testing.block_test_case import NIOBlockTestCase

from ..firebase_base import FirebaseBase


class TestFirebaseBase(NIOBlockTestCase):

    def test_base(self):
        blk = FirebaseBase()

        self.assertIsNone(blk.user)
        self.assertIsNone(blk.db)

        with patch(FirebaseBase.__module__+'.pyrebase') as mock_fbase:
            self.configure_block(blk, {
                "collection": "COLLECTION",
                "userEmail": "USER_EMAIL",
                "userPassword": "USER_PASSWORD",
                "config": {
                    "apiKey": "API_KEY",
                    "databaseURL": "DATABASE_URL",
                    "projectId": "PROJECT_ID"
                }
            })

            # We should now have user and db objects
            self.assertIsNotNone(blk.user)
            self.assertIsNotNone(blk.db)

    def test_auth_refresh(self):
        blk = FirebaseBase()

        with patch(FirebaseBase.__module__ + '.pyrebase') as mock_fbase:
            blk._create_firebase = Mock()
            blk.refresh_auth = Mock()

            self.configure_block(blk, {
                "authRefresh": 1
            })
            blk._create_firebase.assert_called_once_with()

            blk.start()
            sleep(1.5)
            blk.refresh_auth.assert_called_once_with()
            blk.stop()

    def get_absolute_import(self, import_loc):
        """ Get an absolute import from one relative to the block root """
        block_root = '.'.join(__name__.split('.')[:-2])

        return "{}.{}".format(block_root, import_loc)
