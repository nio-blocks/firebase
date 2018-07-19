from nio.properties import VersionProperty
from nio.block.mixins import EnrichSignals
from nio.block.base import Block

from .firebase_base import FirebaseBase


class FirebaseInsert(FirebaseBase, Block, EnrichSignals):

    version = VersionProperty("2.0.1")

    def process_signals(self, signals):
        out_sigs = []
        for sig in signals:
            # The collection may be different for different signals,
            # so we need to compute it inside the loop
            collection = self._get_collection(sig)
            try:
                res = self.db.child(collection).push(sig.to_dict(),
                                                     self.user['idToken'])
            except:
                self.logger.exception("Couldn't save signal")
                continue
            # Take the result of the save and enrich our incoming signal
            # with the data
            out_sigs.append(self.get_output_signal(res, sig))
        self.notify_signals(out_sigs)
