from unittest.mock import patch

from nio import Signal
from nio.block.terminals import Terminal, TerminalType
from nio.testing.block_test_case import NIOBlockTestCase

from ..firebase_stream_block import FirebaseStream


class TestFirebaseStream(NIOBlockTestCase):

    def test_read(self):
        blk = FirebaseStream()
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
            # We will simulate the post returning a message with fake data
            mock_fbase.initialize_app.return_value.database.return_value.\
                child.return_value.stream.return_value = {
                                                "event": "fake_event",
                                                "path": "fake_path",
                                                "data": "fake_data"
                                                }

            blk.start()

            # Send mocked return message to the stream handler
            blk.stream_handler(mock_fbase.initialize_app.return_value.
                               database.return_value.child.
                               return_value.stream.return_value)

            out_sig = self.last_notified["__default_terminal_value"][0]

            self.assertEqual(out_sig.event, "fake_event")
            self.assertEqual(out_sig.path, "fake_path")
            self.assertEqual(out_sig.data, "fake_data")

    def get_absolute_import(self, import_loc):
        """ Get an absolute import from one relative to the block root """
        block_root = '.'.join(__name__.split('.')[:-2])
        return "{}.{}".format(block_root, import_loc)
