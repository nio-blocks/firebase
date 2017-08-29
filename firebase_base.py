from firebase import firebase

from nio import Block
from nio.block.mixins import EnrichSignals
from nio.properties import ObjectProperty, StringProperty
from nio.util.discovery import not_discoverable

from .auth.property import FirebaseAuthProperty


@not_discoverable
class FirebaseBase(EnrichSignals, Block):

    auth = ObjectProperty(FirebaseAuthProperty, title="Authentication")
    application = StringProperty(title="Firebase Application",
                                 default='[[FIREBASE_APPLICATION]]')
    collection = StringProperty(title="Firebase Collection", default="/")

    def __init__(self):
        super().__init__()
        self._firebase = None

    def configure(self, context):
        super().configure(context)
        self._firebase = self._create_firebase()

    def _create_firebase(self):
        return firebase.FirebaseApplication(
            self.application(),
            authentication=self.auth().get_auth_object())

    def _get_collection(self, signal=None):
        collection = self.collection(signal)
        if not collection.startswith('/'):
            return "/{}".format(collection)
        else:
            return collection
