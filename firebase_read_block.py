from .firebase_base import FirebaseBase


class FirebaseRead(FirebaseBase):

    def process_signals(self, signals):
        out_sigs = []
        for sig in signals:
            collection = self._get_collection(sig)
            try:
                res = self._firebase.get(collection, None)
            except:
                self.logger.exception("Couldn't get from collection")
                continue
            out_sigs.append(self.get_output_signal(res, sig))
        self.notify_signals(out_sigs)
