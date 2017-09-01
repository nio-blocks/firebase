FirebaseInsert
==============
The Firebase Insert block takes incoming signals and saves them to the Firebase database under the specified `collection`. If no `collection` is specified, each signal will be saved in the database under a uniquely generated key.

Properties
----------
- **collection**: Object key for accessing elements in the database tree
- **config**: Object containing authentication data
- **enrich**: Options for enriching signals.
- **userEmail**: Authenticated user email set up in Firebase
- **userPassword**: Authenticated user password set up in Firebase

Inputs
------
- **default**: Any list of signals.

Outputs
-------
- **default**: The result of the insert.

Commands
--------
None

Dependencies
------------
pyrebase

FirebaseRead
============
The Firebase Read block takes incoming signals and uses them to read from the Firebase database under the specified `collection`.

Properties
----------
- **collection**: Object key for accessing elements in the database tree
- **config**: Object containing authentication data
- **enrich**: Options for enriching signals.
- **userEmail**: Authenticated user email set up in Firebase
- **userPassword**: Authenticated user password set up in Firebase

Inputs
------
- **default**: Any list of signals.

Outputs
-------
- **default**: Results of the read.

Commands
--------
None

Dependencies
------------
pyrebase

FirebaseStream
==============
The Firebase Stream block listens for changes to the specified `collection` and outputs all changes as a signal

Properties
----------
- **collection**: Object key for accessing elements in the database tree
- **config**: Object containing authentication data
- **enrich**: Options for enriching signals.
- **userEmail**: Authenticated user email set up in Firebase
- **userPassword**: Authenticated user password set up in Firebase

Inputs
------
- **default**: None.

Outputs
-------
- **default**: Results of new database changes.

Commands
--------
None

Dependencies
------------
pyrebase
