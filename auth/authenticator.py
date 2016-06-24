from firebase import firebase
from firebase_token_generator import create_token


class FirebaseAuthenticator(firebase.FirebaseAuthentication):

    """ An instance of FirebaseAuthentication that actually works.

    The new Firebase Authentication API has some new validation requirements
    that don't work with the firebase SDK we have.

    This class uses the firebase_token_generator (produced by Firebase) to
    generate a token and then creates an instance of FirebaseUser with that
    token so that the firebase SDK may use it.

    In essence, this class just overrides the get_user method of the
    FirebaseAuthentication class that is provided in the firebase SDK.
    """

    def __init__(self, secret, user_id):
        super().__init__(secret, user_id)
        self.secret = secret
        self.user_id = user_id

    def get_user(self):
        token = create_token(self.secret, {"uid": self.user_id})
        return firebase.FirebaseUser(self.user_id, token, None)
