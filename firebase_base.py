import pyrebase
from datetime import timedelta

from nio.block.base import Base
from nio.command import command
from nio.properties import ObjectProperty, StringProperty, IntProperty
from nio.util.discovery import not_discoverable
from nio.modules.scheduler.job import Job

from .auth.property import FirebaseAuthProperty


@not_discoverable
@command('refresh_auth')
class FirebaseBase(Base):

    config = ObjectProperty(FirebaseAuthProperty, title="Authentication", order=0)
    collection = StringProperty(title='Database Collection',
                                default='[[FIREBASE_COLLECTION]]', order=3)
    userEmail = StringProperty(title='Authenticated User Email',
                               default='[[USER_EMAIL]]', order=1)
    userPassword = StringProperty(title='Authenticated User Password',
                                  default='[[USER_PASSWORD]]', order=2)
    authRefresh = IntProperty(title='Auth Refresh Interval', default=1800,
                              advanced=True, order=4)

    def __init__(self):
        super().__init__()
        self.user = None
        self.db = None
        self.auth = None
        self._refresh_job = None

    def configure(self, context):
        super().configure(context)
        self._create_firebase()

    def start(self):
        """ Starts the block

        Begin the job to refresh the auth token every hour
        """
        super().start()
        self._refresh_job = Job(self.refresh_auth,
                                timedelta(seconds=self.authRefresh()),
                                True)

    def stop(self):
        """ Stops the block

        Cancel the token refresh job
        """
        self._refresh_job.cancel()
        super().stop()

    def refresh_auth(self):
        self.logger.info("Refeshing user token")
        self.user = self.auth.refresh(self.user['refreshToken'])
        return {'user': self.user}

    def _create_firebase(self):
        firebase = pyrebase.initialize_app(self.config().get_auth_object())
        self.auth = firebase.auth()
        self.user = self.auth.sign_in_with_email_and_password(self.userEmail(),
                                                         self.userPassword())
        self.db = firebase.database()

    def _get_collection(self, signal=None):
        collection = self.collection(signal)
        if not collection.startswith('/'):
            return "/{}".format(collection)
        else:
            return collection
