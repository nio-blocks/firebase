from nio.properties import VersionProperty, BoolProperty
from nio.signal.base import Signal
from nio import GeneratorBlock

from .firebase_base import FirebaseBase


class FirebaseStream(FirebaseBase, GeneratorBlock):

    version = VersionProperty("1.1.0")
    show_root = BoolProperty(title='Return Root Data?', default=True)

    def __init__(self):
        super().__init__()
        self.stream = None
        self.stream_start = False

    def start(self):
        super().start()
        self._connect_stream()

    def stop(self):
        self.stream.close()
        super().stop()

    def _refresh_auth(self):
        self.logger.info("Closing database stream for auth refresh")
        self.stream.close()

        super()._refresh_auth()
        # Reopen the stream using the refreshed user credentials
        self._connect_stream()

    def _connect_stream(self):
        self.logger.info("Connecting to stream")
        self.stream_start = True
        self.stream = self.db.child(self.collection()).\
            stream(self.stream_handler, self.user['idToken'])
        self.logger.info("New database stream opened")

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
