FirebaseInsert
==============
The Firebase Insert block takes incoming signals and saves them to the Firebase database under the specified `collection`. If no `collection` is specified, each signal will be saved in the database under a uniquely generated key.

Properties
----------
- **collection**: Object key for accessing elements in the database tree
- **config**:
- **enrich**: Options for enriching signals.
- **userEmail**:
- **userPassword**:

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
- **config**:
- **enrich**: Options for enriching signals.
- **userEmail**:
- **userPassword**:

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


Properties
----------
- **collection**:
- **config**:
- **enrich**:
- **userEmail**:
- **userPassword**:

Inputs
------
- **default**:

Outputs
-------
- **default**:

Commands
--------
None

Dependencies
------------
pyrebase
