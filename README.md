FirebaseInsert
==============
The FirebaseInsert block takes incoming signals and saves them to the Firebase database under the specified `collection`. If no `collection` is specified, each signal will be saved in the database under a uniquely generated key.

Properties
----------
- **collection**: Object key for accessing elements in the database tree.
- **config**: Object containing authentication data.
- **enrich**: If checked (true), the attributes of the incoming signal will be excluded from the outgoing signal. If unchecked (false), the attributes of the incoming signal will be included in the outgoing signal.
- **userEmail**: Authenticated user email set up in Firebase.
- **userPassword**: Authenticated user password set up in Firebase.

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

***

FirebaseRead
============
The FirebaseRead block takes incoming signals and uses them to read from the Firebase database under the specified `collection`.

Properties
----------
- **collection**: Object key for accessing elements in the database tree
- **config**: Object containing authentication data
- **enrich**: If checked (true), the attributes of the incoming signal will be excluded from the outgoing signal. If unchecked (false), the attributes of the incoming signal will be included in the outgoing signal.
- **userEmail**: Authenticated user email set up in Firebase.
- **userPassword**: Authenticated user password set up in Firebase.

Inputs
------
- **default**: Any list of signals.

Outputs
-------
- **default**: The results found from reading Firebase.

Commands
--------
None

Dependencies
------------
pyrebase

***

FirebaseStream
==============
The FirebaseStream block listens for changes to the specified `collection` and outputs all changes as a signal

Properties
----------
- **collection**: Object key for accessing elements in the database tree.
- **config**: Object containing authentication data.
- **userEmail**: Authenticated user email set up in Firebase.
- **userPassword**: Authenticated user password set up in Firebase.

Inputs
------
- **default**: None.

Outputs
-------
- **default**: Database changes output as a signal.

Commands
--------
None

Dependencies
------------
pyrebase

