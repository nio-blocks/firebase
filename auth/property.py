from .authenticator import FirebaseAuthenticator
from nio.properties import PropertyHolder, StringProperty


class FirebaseAuthProperty(PropertyHolder):
    """ This is a property holder that holds Firebase authentication details.

    It also contains a method that returns an Authenticator object that
    can be passed to the firebase SDK to perform authentication.
    """

    app_secret = StringProperty(title="Firebase App Secret", allow_none=True)
    user_id = StringProperty(title="User ID", allow_none=True)

    def get_auth_object(self):
        """ Return an Authenticator that can be passed to the firebase SDK

        Returns:
            FirebaseAuthenticator if authentication details were provided,
            None otherwise. Note that None is a valid argument to the firebase
            SDK's authenticator argument, it just won't use authentication.
        """
        secret = self.app_secret()
        uid = self.user_id()
        if secret and uid:
            return FirebaseAuthenticator(secret, uid)
        else:
            return None
