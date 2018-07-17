import pyrebase
from datetime import timedelta

from nio import Block
from nio.properties import ObjectProperty, StringProperty, IntProperty
from nio.util.discovery import not_discoverable
from nio.modules.scheduler.job import Job

from .auth.property import FirebaseAuthProperty


@not_discoverable
class FirebaseBase(Block):

    config = ObjectProperty(FirebaseAuthProperty, title="Authentication", order=0)
    collection = StringProperty(title='Database Collection',
                                default='[[FIREBASE_COLLECTION]]', order=3)
    userEmail = StringProperty(title='Authenticated User Email',
                               default='[[USER_EMAIL]]', order=1)
    userPassword = StringProperty(title='Authenticated User Password',
                                  default='[[USER_PASSWORD]]', order=2)
    authRefresh = IntProperty(title='Auth Refresh Interval', default=3600,
                              advanced=True, order=4)

    def __init__(self):
        super().__init__()
        self.stream = None
        self.user = None
        self.db = None
        self.stream_start = False
        self._refresh_job = None

    def configure(self, context):
        super().configure(context)
        self._create_firebase()

    def start(self):
        """ Starts the block

        Begin the job to refresh the auth token every hour
        """
        super().start()
        self._refresh_job = Job(self._refresh_auth,
                                timedelta(seconds=self.authRefresh()),
                                True)

    def stop(self):
        """ Stops the block

        Cancel the token refresh job
        """
        self._refresh_job.cancel()
        super().stop()

    def _refresh_auth(self):
        self.user = auth.refresh(self.user['refreshToken'])

    def _create_firebase(self):
        firebase = pyrebase.initialize_app(self.config().get_auth_object())
        auth = firebase.auth()
        self.user = auth.sign_in_with_email_and_password(self.userEmail(),
                                                         self.userPassword())
        self.db = firebase.database()

    def _get_collection(self, signal=None):
        collection = self.collection(signal)
        if not collection.startswith('/'):
            return "/{}".format(collection)
        else:
            return collection
