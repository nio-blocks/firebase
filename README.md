# Firebase
The Firebase Insert block takes incoming signals and saves them to the Firebase database under the specified `collection`. 
If no `collection` is specified, each signal will be saved in the database under a different key. 

## Properties
* **Credentials**: Firebase user id and app secret
* **Application**: Firebase url
* **Collection**: object key for accessing elements in the database tree

## Dependencies
* [python-firebase](https://pypi.python.org/pypi/python-firebase/1.2)
* [firebase-token-generator](https://github.com/firebase/firebase-token-generator-python)

## Commands
None

## Input
Any list of signals.

## Output
The result of the save. See the following example:

#### Input Signal
```
{ 'sim': 0 }
```

#### Service Config
```
"application": "https://nio-test.firebaseio.com/",
"auth": {
    "app_secret": "",
    "user_id": ""
},
"collection": "test"
```

#### Output Signal
```
{ 'test': '-KPJ0pT5spU1BieanqHN' }
```

#### Resulting Database
```
{
  'test': {
    '-KPJ0pT5spU1BieanqHN': {
      'sim': 0
    }
  }
}
