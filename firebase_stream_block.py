from nio.properties import VersionProperty, BoolProperty
from nio.signal.base import Signal

from .firebase_base import FirebaseBase


class FirebaseStream(FirebaseBase):

    version = VersionProperty("1.0.1")
    show_root = BoolProperty(title='Return Root Data?', default=True)

    def start(self):
        self.stream = self.db.child(self.collection()).\
            stream(self.stream_handler, self.user['idToken'])
        self.stream_start = True

    def stop(self):
        self.stream.close()

    def stream_handler(self, message):
        if not self.show_root() and self.stream_start:
            self.stream_start = False
            pass
        else:
            signal = Signal({
                "event": message['event'],
                "path": message['path'],
                "data": message['data']
            })
            self.notify_signals([signal])
