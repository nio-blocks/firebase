from .firebase_base import FirebaseBase


class FirebaseInsert(FirebaseBase):

    def process_signals(self, signals):
        out_sigs = []
        for sig in signals:
            # The collection may be different for different signals,
            # so we need to compute it inside the loop
            collection = self._get_collection(sig)
            try:
                res = self._firebase.post(collection, sig.to_dict())
            except:
                self.logger.exception("Couldn't save signal")
            # Take the result of the save and enrich our incoming signal
            # with the data
            out_sigs.append(self.get_output_signal(res, sig))
        self.notify_signals(out_sigs)