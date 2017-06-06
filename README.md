Firebase
===================
The Firebase Insert block takes incoming signals and saves them to the Firebase database under the specified `collection`. 
If no `collection` is specified, each signal will be saved in the database under a uniquely generated key. 

Properties
-------------------
**credentials**: Firebase user id and app secret
**application**: Firebase url
**collection**: Object key for accessing elements in the database tree

Dependencies
-------------------
[python-firebase](https://pypi.python.org/pypi/python-firebase/1.2)
[firebase-token-generator](https://github.com/firebase/firebase-token-generator-python)

Commands
-------------------
None

Input
-------------------
Any list of signals.

Output
-------------------
The result of the insert. See the following example:

Input Signal
-------------------
```
{ 'sim': 0 }
```

Block Config
-------------------
```
"application": "https://nio-test.firebaseio.com/",
"auth": {
    "app_secret": "",
    "user_id": ""
},
"collection": "test"
```

Output Signal
-------------------
```
{ 'test': '-KPJ0pT5spU1BieanqHN' }
```
Where the `-KPJ0pT5spU1BieanqHN` is a unique ID generated by Firebase.

Resulting Firebase
-------------------
```
{
  'test': {
    '-KPJ0pT5spU1BieanqHN': {
      'sim': 0
    }
  }
}
```
