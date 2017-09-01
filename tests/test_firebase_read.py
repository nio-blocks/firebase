from unittest.mock import patch

from nio import Signal
from nio.block.terminals import Terminal, TerminalType
from nio.testing.block_test_case import NIOBlockTestCase

from ..firebase_read_block import FirebaseRead


class TestFirebaseRead(NIOBlockTestCase):

    def test_read(self):
        blk = FirebaseRead()
        fbase_imp = self.get_absolute_import('firebase_base.pyrebase')
        with patch(fbase_imp) as mock_fbase:
            self.configure_block(blk, {
                "collection": "COLLECTION",
                "userEmail": "USER_EMAIL",
                "userPassword": "USER_PASSWORD",
                "config": {
                    "apiKey": "API_KEY",
                    "databaseURL": "DATABASE_URL",
                    "projectId": "PROJECT_ID"
                },
                "enrich": {
                    "exclude_existing": False
                }
            })
            # We will simulate the post returning a name with a fake ID
            mock_fbase.initialize_app.return_value.database.return_value.\
                child.return_value.get.return_value.\
                val.return_value = {"fake_id": "fake_value"}

            blk.start()

            blk.process_signals([Signal({
                "test_key": "test_val"
            })])

            # We should get an output signal from the insert
            self.assert_num_signals_notified(1)

            out_sig = self.last_notified["__default_terminal_value"][0]
            # Make sure the details of our input signal were notified
            self.assertEqual(out_sig.test_key, "test_val")
            # Make sure the ID/name of the saved signal was included on the
            # output signal under the "name" field
            self.assertEqual(out_sig.fake_id, "fake_value")
            blk.stop()

    def get_absolute_import(self, import_loc):
        """ Get an absolute import from one relative to the block root """
        block_root = '.'.join(__name__.split('.')[:-2])
        return "{}.{}".format(block_root, import_loc)
