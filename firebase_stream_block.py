from nio.properties import VersionProperty, BoolProperty
from nio.signal.base import Signal
from nio import GeneratorBlock

from .firebase_base import FirebaseBase


class FirebaseStream(FirebaseBase, GeneratorBlock):

    version = VersionProperty("1.1.1")
    show_root = BoolProperty(title='Return Root Data?', default=True)

    def __init__(self):
        super().__init__()
        self.stream = None
        self.stream_start = False

    def start(self):
        super().start()
        self._connect_stream()

    def stop(self):
        self._close_stream()
        super().stop()

    def refresh_auth(self):
        self.logger.info("Closing database stream for auth refresh")
        self._close_stream()

        result = super().refresh_auth()
        # Reopen the stream using the refreshed user credentials
        self._connect_stream()
        return result

    def _connect_stream(self):
        self.logger.info("Connecting to stream")
        self.stream_start = True
        self.stream = self.db.child(self.collection()).\
            stream(self.stream_handler, self.user['idToken'])
        self.logger.info("New database stream opened")

    def _close_stream(self):
        self.logger.info("Closing stream")
        try:
            self.stream.close()
        except:
            # ignore stream close failures, they sometimes occur with pyrebase
            self.logger.info(
                "Ignoring exception while closing stream", exc_info=True)
            pass

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
