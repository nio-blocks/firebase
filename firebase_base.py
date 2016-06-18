from firebase import firebase
from nio import Block
from nio.block.mixins import EnrichSignals
from nio.properties import PropertyHolder, ObjectProperty, StringProperty


class FirebaseAuth(PropertyHolder):
    pass


class FirebaseBase(EnrichSignals, Block):

    auth = ObjectProperty(FirebaseAuth, title="Authentication")
    application = StringProperty(title="Firebase Application")
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
            authentication=None)

    def _get_collection(self, signal=None):
        collection = self.collection(signal)
        if not collection.startswith('/'):
            return "/{}".format(collection)
        else:
            return collection
