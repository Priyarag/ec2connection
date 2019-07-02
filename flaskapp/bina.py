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
# Session = sessionmaker(bind=engine)
# session = Session()

# Base = automap_base()
# # reflect the tables
# Base.prepare(engine, reflect=True)
# q = engine.execute('SHOW DATABASES')
# schemas = q.fetchall()
# print(schemas)
# engine.table_names()
# crypto= []

# conn = sqlite3.connect('/home/ubuntu/flaskapp/Meraki_CMX.db' )
# cur = conn.cursor()
# def create_table():
# 	sql_create = "CREATE TABLE IF NOT EXISTS  tbl_dat_MerakiTraffic_test_v2(ID INTEGER primary key Autoincrement NOT NULL,Ap_mac TEXT NULL , \
# 	          	Ap_tags  TEXT NULL, Client_mac TEXT NULL, Ipv4 TEXT NULL, Ipv6 TEXT NULL, LseenTime TEXT NULL, SeenEpoch INTEGER NULL,  \
#                         Ssid TEXT NULL, Rssi INTEGER NULL, Manufacturer TEXT NULL, Os TEXT NULL, Loc_lat NUMERIC NULL, Loc_lng NUMERIC, \
# 			Loc_unc NUMERIC NULL, CreatedDate_UTC TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL)"
# 	print sql_create
# 	cur.execute(sql_create)
#         conn.commit()
# create_table()

# Generate a secret random key for the session
# app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
# Meraki_secret = 'T2MerakiPosts!'
# Validator = 'c20f3a5c099e327f4837fa6212c2ef996c75e169'
# @app.route('/hel')
# def hello_world():
# 	return 'Dont Give up, AWS is killing me'
# # Render template
# @app.route('/getit')
# def binance():
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
# class Crypto(Base):
# 	__tablename__ = 'crypto'
# 	id = Column(Integer, primary_key=True)
# 	symbol = Column(String(50))
# 	price = Column(DECIMAL(10,2))
# 	crypto_timestamp = Column(DateTime, nullable=False)
	# def __repr__(self):
	# 	return "<crypto(symbol='%s', price='%f', crypto_timestamp='%s', " \
 #                   "source_from='%s')" % (self.symbol, self.price, self.address,
 #                                          self.source_from)

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
    # eth_obj = json.loads(eth_json)
    # crypto_obj = Crypto(id=obj.get("id"), symbol=obj.get("symbol"), price = obj.get("price"))
    # Session.add(crypto_obj)
    # Session.commit()
    # q = dbsession.query(crypto)
    # ins = table.insert().values(eth_json)
    conn = engine.connect()
    # conn.execute(ins)
    conn.execute(table.insert(),[
    	eth_json,xrp_json,ltc_json,bcc_json,eos_json,bnb_json])
    # result = engine.connect.execute("SELECT * from crypto").fechall()
	# print(result)
			    
		# 			postdata = request.data
		# 			pp = pprint.PrettyPrinter(indent=4)
		# 			decoded = json.loads(postdata)
		# #			pp.pprint (decoded)
		# 			Meraki = decoded['secret']
		# #			print "Meraki-->",Meraki
		# 			if Meraki == Meraki_secret:
		# 				print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
		# 				print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
		# 				print "!!!!!Secret Matched!!!!!!!!"
		# 				Ap_mac_uni = decoded["data"]["apMac"]
		# 				Ap_mac = Ap_mac_uni.encode('utf-8')
		# #				Ap_floors_uni= decoded['data']['apFloors']
		# #				Ap_floors = Ap_floors_uni.encode('utf-8')
		# 				Ap_tags_list = decoded['data']['apTags']
		# 				Ap_tags_map = map(str,Ap_tags_list)
		# 				Ap_tags = ','.join(filter(None,Ap_tags_map))
		# 				for dec in decoded['data']['observations']:
		# 					print "Meraki JSON parsed data"
		# 					Client_mac_uni = dec['clientMac']
		# 					Client_mac = Client_mac_uni.encode('utf-8')
		# 					LseenTime_uni  = dec['seenTime']
		# 					LseenTime =  LseenTime_uni.encode('utf-8')
		# 					Manufacturer_uni = dec['manufacturer']
		# 					Manufacturer = Manufacturer_uni.encode('utf-8')
		# 					Rssi = dec['rssi']
		# 					Os_uni = dec['os']
		# 					Os = str(Os_uni)
		# 					SeenEpoch = dec['seenEpoch']
		# 					Ssid_uni = dec['ssid']
		# 					Ssid =  str(Ssid_uni)
		# 					Ipv6_uni = dec['ipv6']
		# 					Ipv6 =  str(Ipv6_uni).strip('/')
		# 					Ipv4_uni = dec['ipv4']
		# 					Ipv4 = str(Ipv4_uni).strip('/')			
		# 					Loc_lat = dec['location']['lat']
		# 					Loc_lng = dec['location']['lng']
		# 					Loc_unc = dec['location']['unc']
		# 					print "-------------------------"
		# 					print "AP_MAC :",Ap_mac
		# 	#				print "Ap_Floors:", Ap_floors
		# 			    		print "Ap_tags = ", Ap_tags
		#                 	       	       	print "Client_mac:",Client_mac
		# 	                	      	print "Last_seen:", LseenTime
		#         		        	print "Manufacturer:",Manufacturer
		# 					print "Rssi:",Rssi
		# 					print "OS:", Os
		# 					print "SeenEpoch:", SeenEpoch
		# 					print "Ssid:", Ssid
		# 					print "Ipv6:", Ipv6
		# 					print "Ipv4:", Ipv4
		# 					print "Location - Lat:", Loc_lat
		# 					print "Location - Lng:", Loc_lng
		# 					print "Location - Unc:", Loc_unc
		# 					print "**************************"
		# 					sql_insert = ("INSERT INTO tbl_dat_MerakiTraffic_test_v2" 
		# 					"(Ap_mac,Ap_tags,Client_mac,LseenTime,Manufacturer,Rssi,Os,SeenEpoch,Ssid,Ipv6,Ipv4,Loc_lat,Loc_lng,Loc_unc)" 
		# 					 "VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,? )")
		# 					Values = [Ap_mac,Ap_tags,Client_mac,LseenTime,Manufacturer,Rssi,Os,SeenEpoch,Ssid,Ipv6,Ipv4,Loc_lat,Loc_lng,Loc_unc]
		# #					print "sql_insert --> ",sql_insert
		# 					cur.execute(sql_insert,Values)		
		# 				print"Meraki Posts for loop done"
		# 				conn.commit()
		# 				cur.close()
		# 				conn.close()
			# else:
			# 	print"Warning: Secret not matched!"

		# elif request.method == 'GET' :
		# 	return Validator 
		# else:
		# 	return'Something is not right'
		# except (ValueError, KeyError, TypeError)as error:
		# 	return"Error with the page: ", error

# binance()

if __name__ == '__main__':
	app.run(debug=True)    