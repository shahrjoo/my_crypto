#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 11:15:49 2018

@author: alishahrjoo

Using this package, you can store passwords and connection strings on your 
local machine and avoid hardcoding them in your python scripts.
it will save them into a file in your local machine.
Use the get_crypto() functin to retreive and use your credentials in your code.
"""

import json
import os.path
import git
import os

class my_crypto():
    __datafilename = '.crypto' # filename to store the data
    __mydatafile=''            # absolute filepath
       
    def __write_crypto(self):
        '''>  Wrtie into the file'''
        try:
            with open(self.__mydatafile, 'w') as f:
                json.dump(self.mycrypto, f)
        except OSError as err:
            print("Error Writing file: {0}".format(err))
       
    def __read_crypto(self):
        '''>  Read from the file'''    
        try:
            with open(self.__mydatafile) as f:
                self.mycrypto = json.load(f)
        except OSError as err:
            print("Error Reading File: {0}".format(err))
            
    def add_crypto(self,name,value):
        '''
        Add an item to the file
        input:
            name  : key name
            
            value : key value
        '''
        if name in self.mycrypto.keys():
            print('>  item already exist')
            return
        try:
            self.mycrypto[name]=value
            self.__write_crypto()
            print('>  items addred successfully')
        except:
            print('>  error adding item')

    def update_crypto(self,name,Newvalue):
        '''
        Update an items
        input:
            name  : key name
            
            Newvalue : key value
        '''        
        if name not in self.mycrypto.keys():
            print('>  item does exist')
            return
        try:
            self.mycrypto[name]=Newvalue
            self.__write_crypto()
            print('>  items updated successfully')
        except:
            print('>  error updating item {}')


    def del_crypto(self,name):
        ''''
        delete an item
        input:
            name : key name
        '''
        if name not in self.mycrypto.keys():
            print('Item not found')
            return
        else:
            try:
                del self.mycrypto[name]
                self.__write_crypto()
                print('>  items deleted successfully')
            except:
                print('>  error deleting item')

    def print_crypto(self):
        '''print all the keys and values'''
        if len(self.mycrypto)<1:
            print('You hae not entered any record')
            return
        for key in self.mycrypto.keys():
            print('_________________________________________________________')
            print(key + ' ---> ' + str(self.mycrypto[str(key)]))

    def print_keys(self):
        ''' print all the keys'''
        if len(self.mycrypto)<1:
            print('You hae not entered any record')
            return
        for key in self.mycrypto.keys():
            print(key)

    def __get_repo_root(self):
        ''' 
        if current path is in a git repository returns the root path,
        otherwise, returns the current path
        '''
        try:
            curpath=os.getcwd()
            git_repo = git.Repo(curpath, search_parent_directories=True)
            git_root = git_repo.git.rev_parse("--show-toplevel")
            print('Gir Repo found. Repo path: ' + git_root)
            return([True,git_root])
        except:
            print('>  Not a git repo. Use the current path to store files')
            return(False,curpath)
    
    def __update_gitignore(self,rootpath):
        '''add __datafilename to the .gitignore file'''
        gitignorepath = os.path.join(rootpath,'.gitignore')
        
        if os.path.exists(gitignorepath):       
            if self.__datafilename not in open(gitignorepath).read():
                with open(gitignorepath, "a") as myfile:
                    myfile.write(self.__datafilename)
                print('>  .gitignore file updated.')
            else:
                print('>  .gitignore already updated')
        else:
            with open(gitignorepath, "w") as myfile:
                myfile.write(self.__datafilename)
            print('>  .gitignore file created and updated.')
            
    
    def get_crypto(self,name):
        '''
        get an item value
        input:
            name : key name
        '''
        if name in self.mycrypto.keys():
            return self.mycrypto[name]
        else:
            return(-1)
    
    def __init__(self):
        '''initialize the class'''
        repo,rootpath = self.__get_repo_root()
        if repo:
            self.__update_gitignore(rootpath)
        
        self.__mydatafile=os.path.join(rootpath,self.__datafilename)
        
        if os.path.exists(self.__mydatafile):
            self.__read_crypto() 
        else:
            print('>  There is not any history file saved. Add items to generate a new file.')
            self.mycrypto={}
    
    def backup_crypto(self):
        '''
        backup the crypto into a file
        '''
        filePath = input('Enter the backup file path: ')
        if os.path.exists(filePath):
            print('File already exist')
        elif os.access(os.path.dirname(filePath),os.W_OK):
            try:
                with open(filePath, 'w') as f:
                    json.dump(self.mycrypto, f)
                    print('backup file created')
            except OSError as err:
                print("Error Writing file: {0}".format(err))            
        else:    
            print('>  file path does not exist: %s' % filePath)
            
    def restore_crypto(self):
        '''
        restore the crypto from a backup file
        '''
        filePath = input('Enter the file to restore: ')
        if os.path.exists(filePath):
            try:
                with open(filePath) as f:
                    self.mycrypto = json.load(f)
                    self.__write_crypto()
                    print('backup successfully restored')
            except OSError as err:
                print("Error Reading File: {0}".format(err))        
        else:
            print('>  file path does not exist: %s' % filePath)
            






     
     
 
     