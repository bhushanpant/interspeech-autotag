#!/usr/bin/env python

# Importing builtin packages
from sqlalchemy import create_engine
import pandas as pd


class DatabaseFunction(object):

    def __init__(self, userServer):
        self.userServer = userServer

    ## MySQL connection as data is not present in our Data Server. ##
    def sqlAlchemyMySQL(self):
        return create_engine("mysql+pymysql://root:ronaktanna@localhost/twitter?host=localhost?port=3306;charset='utf8'")

    ## Retrieve Only Message and Message Flag from the tables ##
    def getSQLData(self):
        mysql = self.sqlAlchemyMySQL()
        print ("Fetching data from MySQL")
        df = pd.read_sql('select * from twitter_corpus limit 10000',mysql)
        return df

