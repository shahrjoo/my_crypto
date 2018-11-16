# README


my_crypto gets your passwords and connection strings or any 
other text that you use oftenly in your code and store them in your local machine.
By using my_crypto, you can avoid hardcoding passwords, connections strings and other 
important information on your source code when you are implementing or validating your code. Instead of hardcoding, you can use 
get_crypto() functions in your code. 

you can use my_crypto in a local git repository or local folder. It will store 
whatever you want as a pair of key and value. It stores them on your local machine and retreive 
them whenever you want.

# Installation:
```
git clone https://github.com/shahrjoo/my_crypto
cd my_crypto
pip install .
```

# Examples:


## Initialize the class
```
from my_crypto import my_crypto
myc= my_crypto()
```

## Add an item
```
myc.add_crypto('password#1',"yourpassword")
```
```
myc.add_crypto('sqlpassword,"yourpassword")
```
## Add an item (a dictionary)

```
config = {
    'host': 'localhost',
    'user': 'root',
    'passwd': 'password',
    'dbname': 'databasename'
}
myc.add_crypto('postgress_connectionstring',config)
```
## Add a connectionstring
```
myc.add_crypto('mysql_connection',"mysql://root:password@127.0.0.1/dbName")
```

## The dictionary
```
myc.mycrypto
```

## Print all items 
```
myc.print_crypto()
```

## Print the keys 
```
myc.print_keys()
```

## Delete an item
```
myc.del_crypto('pass1')
```

## Update an item
```
myc.add_crypto('password#1',"newpassword")
```

## Get an item value
```
myc.get_crypto('pass1')
```


## Example for connectin string
```
config = {
    'host': 'localhost',
    'user': 'root',
    'passwd': 'password',
    'dbname': 'databasename'
}
#Saving config 
myc.add_crypto('postgress_connectionstring',config)
```

```
# Using the saved config
import pg
conn = pg.DB(**myc.get_crypto('postgress_connectionstring'))
#is the same as using the command below:
 conn = pg.DB(host="localhost", user="root", passwd="password", dbname="databasename")
```

## Example for password
```
myc.add_crypto('localsql_admin_password',"password")

import MySQLdb
db = MySQLdb.connect(user='root',password=myc.get_crypto('localsql_admin_password'),host='127.0.0.1',database='databasename')
```

