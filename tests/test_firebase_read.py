from unittest.mock import patch

from nio import Signal
from nio.block.terminals import Terminal, TerminalType
from nio.testing.block_test_case import NIOBlockTestCase

from ..firebase_read_block import FirebaseRead


class TestFirebaseRead(NIOBlockTestCase):

    def test_insert(self):
        blk = FirebaseRead()
        with patch.object(blk, '_create_firebase'):
            self.configure_block(blk, {
                "application": "test",
                "collection": "my_collection",
                "enrich": {
                    "exclude_existing": False,
                    "enrich_field": "output"
                }
            })
            # Firebase should return with a value id and the value it is
            # associated with
            blk._firebase.get.return_value = {"fake id": "fake value"}

            blk.start()

            # Simulate a test signal going into the block
            blk.process_signals([Signal({
                "test_key": "test_val"
            })])

            # We should get an output signal from the insert
            self.assert_num_signals_notified(1)

            # TODO: Move this to the framework block unit test
            sigs_notified = self.last_notified[
                Terminal.get_default_terminal_on_class(
                    FirebaseRead, TerminalType.input).id]

            out_sig = sigs_notified[0]
            # Make sure the details of our input signal were notified
            self.assertEqual(out_sig.test_key, "test_val")
            # Make sure the fake value was returned with the fake id from the
            # get request
            self.assertEqual(out_sig.output["fake id"], "fake value")
            blk.stop()
