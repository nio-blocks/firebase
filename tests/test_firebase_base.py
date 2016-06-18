from ..firebase_base import FirebaseBase
from unittest.mock import patch
from nio.testing.block_test_case import NIOBlockTestCase


class TestFirebaseBase(NIOBlockTestCase):

    # def test_base(self):
        # blk = FirebaseBase()
        # with patch.object(blk, '_create_firebase'):
            # self.configure_block(blk, {
                # "application": "test"
            # })

    def test_base(self):
        blk = FirebaseBase()
        with patch(self.get_firebase_import()) as mock_fbase:
            self.configure_block(blk, {
                "application": "test"
            })
            mock_fbase.FirebaseApplication.assert_called_once_with(
                "test", authentication=None)

    def get_firebase_import(self):
        return "{}.{}".format(FirebaseBase.__module__, 'firebase')
