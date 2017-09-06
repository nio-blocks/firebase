import pyrebase

from nio import Block
from nio.properties import ObjectProperty, StringProperty
from nio.util.discovery import not_discoverable

from .auth.property import FirebaseAuthProperty


@not_discoverable
class FirebaseBase(Block):

    config = ObjectProperty(FirebaseAuthProperty, title="Authentication")
    collection = StringProperty(title='Database Collection', default='[[FIREBASE_COLLECTION]]')
    userEmail = StringProperty(title='Authenticated User Email', default='[[USER_EMAIL]]')
    userPassword = StringProperty(title='Authenticated User Password', default='[[USER_PASSWORD]]')

    def __init__(self):
        super().__init__()
        self.stream = None
        self.user = None
        self.db = None

    def configure(self, context):
        super().configure(context)
        self._create_firebase()

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
