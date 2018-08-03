from nio.properties import VersionProperty
from nio.block.mixins import EnrichSignals
from nio.block.base import Block

from .firebase_base import FirebaseBase


class FirebaseRead(FirebaseBase, Block, EnrichSignals):

    version = VersionProperty("2.1.1")

    def process_signals(self, signals):
        out_sigs = []
        for sig in signals:
            collection = self._get_collection(sig)
            try:
                res = self.db.child(collection).get(self.user['idToken']).val()
            except:
                self.logger.exception("Couldn't get from collection")
                continue
            out_sigs.append(self.get_output_signal(res, sig))
        self.notify_signals(out_sigs)
