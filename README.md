# password-manager
Simple python script to save your login credentials in database

## Example

```
> python app.py new
Press [enter] to skip, ctrl-c to cancel

name: google
email: example@gmail.com
username: 
password: super_strong_pass
notes: phone number: ...

> python app.py list
ID | NAME | E-MAIL | USERNAME | PASSWORD | NOTES

1, google, example@gmail.com, , super_strong_pass, phone number: ..., 

```

## Setup
Set your database path at the beggining of `app.py` file.
```python
DB_PATH = './passwords.db'      # path to database file
```