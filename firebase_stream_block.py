from nio.util.discovery import discoverable
from nio.properties import VersionProperty
from nio.signal.base import Signal

from .firebase_base import FirebaseBase


@discoverable
class FirebaseStream(FirebaseBase):

    version = VersionProperty("2.0.0")

    def start(self):
        self.stream = self.db.child(self.collection()).stream(self.stream_handler, self.user['idToken'])

    def stop(self):
        self.stream.close()

    def stream_handler(self, message):
        signal = Signal({
            "event": message['event'],
            "path": message['path'],
            "data": message['data']
        })
        self.notify_signals([signal])

    # def process_signals(self, signals):
    #     out_sigs = []
    #     for sig in signals:
    #         collection = self._get_collection(sig)
    #         try:
    #             #res = self._firebase.get(collection, None)
    #             res = self.db.child(collection).get(self.user['idToken']).val()
    #         except:
    #             self.logger.exception("Couldn't get from collection")
    #             continue
    #         out_sigs.append(self.get_output_signal(res, sig))
    #     self.notify_signals(out_sigs)
