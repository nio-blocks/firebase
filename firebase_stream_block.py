from nio.properties import VersionProperty
from nio.signal.base import Signal

from .firebase_base import FirebaseBase


class FirebaseStream(FirebaseBase):

    version = VersionProperty("1.0.0")

    def start(self):
        self.stream = self.db.child(self.collection()).\
            stream(self.stream_handler, self.user['idToken'])

    def stop(self):
        self.stream.close()

    def stream_handler(self, message):
        signal = Signal({
            "event": message['event'],
            "path": message['path'],
            "data": message['data']
        })
        self.notify_signals([signal])
