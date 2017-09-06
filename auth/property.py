from nio.properties import PropertyHolder, StringProperty


class FirebaseAuthProperty(PropertyHolder):
    """ This is a property holder that holds Firebase authentication details.

    It also contains a method that returns an Authenticator object that
    can be passed to the firebase SDK to perform authentication.
    """

    apiKey = StringProperty(title='API Key',
                            default='[[FIREBASE_API_KEY]]')
    databaseURL = StringProperty(title='Database URL',
                                 default='[[FIREBASE_DATABASE_URL]]')
    projectId = StringProperty(title='Firebase Project ID',
                               default='[[FIREBASE_PROJECT_ID]]')

    def get_auth_object(self):
        """ Return an Authenticator that can be passed to the firebase SDK

        Returns:
            FirebaseAuthenticator if authentication details were provided,
            None otherwise. Note that None is a valid argument to the firebase
            SDK's authenticator argument, it just won't use authentication.
        """
        apiKey = self.apiKey()
        databaseURL = self.databaseURL()
        projectId = self.projectId()
        if apiKey and databaseURL and projectId:
            config = {
                "apiKey": apiKey,
                "authDomain": "{}.firebaseapp.com".format(projectId),
                "databaseURL": databaseURL,
                "storageBucket": "{}.appspot.com".format(projectId)
            }
            return config
        else:
            return None
