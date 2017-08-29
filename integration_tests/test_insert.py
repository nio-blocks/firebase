from unittest import skipUnless

from nio import Signal
from nio.testing.block_test_case import NIOBlockTestCase
from nio.block.terminals import Terminal, TerminalType

from . import MY_APPLICATION, MY_AUTH
from ..firebase_insert_block import FirebaseInsert


@skipUnless(MY_APPLICATION, "No application details provided")
class TestFirebaseInsert(NIOBlockTestCase):

    def test_base(self):
        blk = FirebaseInsert()
        self.configure_block(blk, {
            "application": MY_APPLICATION,
            "auth": MY_AUTH,
            "collection": "integration_tests/blah",
            "enrich": {
                "exclude_existing": False,
                "enrich_field": "output"
            }
        })
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
        self.assertIsNotNone(out_sig.output["name"])
        blk.stop()
