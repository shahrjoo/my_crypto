#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 14:23:04 2018

@author: alishahrjoo
"""

'''

myc= my_crypto()

Example:

# Add an item
myc.add_crypto('password#1',"yourpassword")

myc.add_crypto('sqlpassword,"yourpassword")

# Add an item (a dictionary)
config = {
    'host': 'localhost',
    'user': 'root',
    'passwd': 'password',
    'dbname': 'databasename'
}
myc.add_crypto('postgress_connectionstring',config)

# Add a connectionstring
myc.add_crypto('mysql_connection',"mysql://root:password@127.0.0.1/dbName")

# The dictionary
myc.mycrypto

# Print all items 
myc.print_crypto()

# Print the keys 
myc.print_keys()

# Delete an item
myc.del_crypto('pass1')

# Update an item
myc.add_crypto('password#1',"newpassword")

# Get an item value
myc.get_crypto('pass1')


#Example using connectin string
config = {
    'host': 'localhost',
    'user': 'root',
    'passwd': 'password',
    'dbname': 'databasename'
}
myc.add_crypto('postgress_connectionstring',config)

import pg
conn = pg.DB(**myc.get_crypto('postgress_connectionstring'))
#is the same as using
#conn = pg.DB(host="localhost", user="root", passwd="password", dbname="databasename")

#Example using for using saved password
myc.add_crypto('localsql_admin_password',"password")

import MySQLdb
db = MySQLdb.connect(user='root',password=myc.get_crypto('localsql_admin_password'),host='127.0.0.1',database='databasename')


'''