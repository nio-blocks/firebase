from ..firebase_base import FirebaseBase
from unittest.mock import patch
from nio.testing.block_test_case import NIOBlockTestCase


class TestFirebaseBase(NIOBlockTestCase):

    def test_base(self):
        blk = FirebaseBase()
        fbase_imp = self.get_absolute_import('firebase_base.firebase')
        with patch(fbase_imp) as mock_fbase:
            self.configure_block(blk, {
                "application": "test"
            })
            mock_fbase.FirebaseApplication.assert_called_once_with(
                "test", authentication=None)

    def test_auth_included(self):
        """ Make sure we can authenticate if needed """
        blk = FirebaseBase()
        token_imp = self.get_absolute_import('auth.authenticator.create_token')
        with patch(token_imp) as mock_token:
            mock_token.return_value = "SAMPLE TOKEN"
            self.configure_block(blk, {
                "application": "https://fakeproj.firebase",
                "auth": {
                    "app_secret": "SECRET_KEY",
                    "user_id": "USER_ID"
                }
            })
            # Our firebase instance should have been created
            self.assertIsNotNone(blk._firebase)
            # Trigger a call to authenticate to make sure our parameters were
            # passed properly
            blk._firebase._authenticate({}, {})
            mock_token.assert_called_once_with(
                "SECRET_KEY", {"uid": "USER_ID"})

    def test_auth_not_included(self):
        """ Make sure no authentication happens if not included """
        blk = FirebaseBase()
        token_imp = self.get_absolute_import('auth.authenticator.create_token')
        with patch(token_imp) as mock_token:
            self.configure_block(blk, {
                "application": "https://fakeproj.firebase",
                "auth": {
                    "app_secret": None,
                    "user_id": None
                }
            })
            # Our firebase instance should have been created
            self.assertIsNotNone(blk._firebase)
            # Trigger a call to authenticate to make sure our parameters were
            # passed properly
            blk._firebase._authenticate({}, {})
            mock_token.assert_not_called()

    def get_absolute_import(self, import_loc):
        """ Get an absolute import from one relative to the block root """
        block_root = '.'.join(__name__.split('.')[:-2])
        return "{}.{}".format(block_root, import_loc)
