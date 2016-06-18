from ..firebase_insert_block import FirebaseInsert
from unittest.mock import patch
from nio import Signal
from nio.block.terminals import Terminal, TerminalType
from nio.testing.block_test_case import NIOBlockTestCase


class TestFirebaseInsert(NIOBlockTestCase):

    def test_insert(self):
        blk = FirebaseInsert()
        with patch.object(blk, '_create_firebase'):
            self.configure_block(blk, {
                "application": "test",
                "collection": "my_collection",
                "enrich": {
                    "exclude_existing": False,
                    "enrich_field": "output"
                }
            })
            # We will simulate the post returning a name with a fake ID
            blk._firebase.post.return_value = {"name": "fake id"}

            blk.start()
            blk.process_signals([Signal({
                "test_key": "test_val"
            })])

            # We should get an output signal from the insert
            self.assert_num_signals_notified(1)

            # TODO: Move this to the framework block unit test
            sigs_notified = self.last_notified[
                Terminal.get_default_terminal_on_class(
                    FirebaseInsert, TerminalType.input).id]

            out_sig = sigs_notified[0]
            # Make sure the details of our input signal were notified
            self.assertEqual(out_sig.test_key, "test_val")
            # Make sure the ID/name of the saved signal was included on the
            # output signal under the "name" field
            self.assertEqual(out_sig.output["name"], "fake id")
            blk.stop()
