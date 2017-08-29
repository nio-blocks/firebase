FirebaseInsert
==============

The Firebase Insert block takes incoming signals and saves them to the Firebase database under the specified `collection`. If no `collection` is specified, each signal will be saved in the database under a uniquely generated key.

Properties
----------
- **application**: Firebase url
- **auth**: Firebase user id and app secret
- **collection**: Object key for accessing elements in the database tree
- **enrich**: Options for enriching signals

Inputs
------
- **default**: Any list of signals.

Outputs
-------
- **default**: Results of the insert.

Commands
--------
None

Dependencies
------------
python-firebase
firebase-token-generator

FirebaseRead
============

The Firebase Read block takes incoming signals and uses them to read from the Firebase database under the specified `collection`.

Properties
----------
- **application**: Firebase url
- **auth**: Firebase user id and app secret
- **collection**: Object key for accessing elements in the database tree
- **enrich**: Options for enriching signals

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
python-firebase
firebase-token-generator
