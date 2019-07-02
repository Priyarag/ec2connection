# from flask import Flask,request,jsonify, session, render_template
import os
import requests
import json
import pprint
import datetime
import time
import pandas
import threading
# import sqlite3
from datetime import datetime
import pandas as pd
from sqlalchemy import create_engine
# from matplotlib import pyplot as plt
import sqlalchemy
from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import inspect
from sqlalchemy.orm import sessionmaker
# import Base
from sqlalchemy import Column, Integer, String, DECIMAL, DateTime
# app = Flask(__name__)

rds_connection_string = 'mysql://flask:flasktest@awsflask.cpmhfsqdvkzl.us-east-2.rds.amazonaws.com/innodb'
engine = create_engine(rds_connection_string)
# Base.metadata.create_all(engine)
db_uri = "sqlite:///innodb.sqlite"
dbengine = create_engine(db_uri)
# Create a metadata instance
metadata = MetaData(engine)
table = Table('crypto', metadata,
               Column('id',Integer, primary_key=True),
               Column('symbol',String(50)),
               Column('price',DECIMAL(10,8)),
               Column('crypto_timestamp',DateTime, nullable=False))
metadata.create_all()
# metadata.commit()
for _t in metadata.tables:
   print("Table: ", _t)
inspector = inspect(engine)

# Get table information
print(inspector.get_table_names())

baseUrl = "https://api.binance.com/api/v1/ticker/price?symbol="
ethUrlAffix = "ETHBTC"
xrpUrlAffix = "XRPBTC"
ltcUrlAffix = "LTCBTC"
bccUrlAffix = "BCCBTC"
eosUrlAffix = "EOSBTC"
bnbUrlAffix = "BNBBTC"
"""
Ethereum           ETH
XRP                XRP
Litecoin           LTC
Bitcoin Cash       BCC
EOS                EOS
Binance Coin       BNB
"""
# conn = sqlite3.connect('/home/ubuntu/flaskapp/Meraki_CMX.db' )
# cur = conn.cursor()
starttime=time.time()
while True:
    eth_json = requests.get(baseUrl + ethUrlAffix).json()
    xrp_json = requests.get(baseUrl + xrpUrlAffix).json()
    ltc_json = requests.get(baseUrl + ltcUrlAffix).json()
    bcc_json = requests.get(baseUrl + bccUrlAffix).json()
    eos_json = requests.get(baseUrl + eosUrlAffix).json()
    bnb_json = requests.get(baseUrl + bnbUrlAffix).json()

    time_now = datetime.now()

    eth_json.update({'crypto_timestamp':time_now})  
    xrp_json.update({'crypto_timestamp' : time_now})  
    ltc_json.update({'crypto_timestamp':time_now})  
    bcc_json.update({'crypto_timestamp':time_now})  
    eos_json.update({'crypto_timestamp':time_now})  
    bnb_json.update({'crypto_timestamp':time_now})  

    print(eth_json)
    print(xrp_json)
    print(ltc_json)
    print(bcc_json)
    print(eos_json)
    print(bnb_json)
    print(time_now)
    # for eth in eth_json:
    # 	row = {}
    # 	row[]

    time.sleep(60.0 - ((time.time() - starttime) % 60.0))
    conn = engine.connect()
    # conn.execute(ins)
    conn.execute(table.insert(),[
    	eth_json,xrp_json,ltc_json,bcc_json,eos_json,bnb_json])
    
if __name__ == '__main__':
	app.run(debug=True)    
