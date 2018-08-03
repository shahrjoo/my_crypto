# README


Using this package, you can store your passwords and connection strings on your 
local machine and avoid hardcoding them in your python scrips.
it will save them into a file in your local machine.
Use the get_crypto() functin to retreive and use your credentials in your code

# Examples:


## Initialize the class
```
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

