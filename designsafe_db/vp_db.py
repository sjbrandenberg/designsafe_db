import pymysql
import pandas as pd
import sqlalchemy
from sqlalchemy import exc

def connect():
    try:
        print('We have phased out the vp_db.connect() command in favor of the vp_db.read_sql(sql, output) command.')
    except:
        pass
    
def read_sql(*args):
    if(len(args)<1):
        print('You must specify a sql string in the read_sql function')
        return
    if(len(args)>2):
        print('You must only specify sql and type in the read_sql function')
        return
    sql = args[0]
    if(len(args)==1):
        output = 'DataFrame'
    else:
        if(args[1] in ['DataFrame','dict']):
            output = args[1]
        else:
            print('type "' + str(args[1]) + '" is not a valid option. Must be either "DataFrame" or "dict". Using "DataFrame" type as default.')
            
    if(output=='DataFrame'):
        try:
            engine = sqlalchemy.create_engine('mysql+pymysql://dspublic:R3ad0nlY@129.114.52.174:3306/sjbrande_vpdb')
            data = pd.read_sql_query(sql, con=engine)
            engine.dispose()
            return(data)
        except exc.SQLAlchemyError as e:
            print(e)
            pass
    elif(output=='dict'):
        try:
            cnx = pymysql.connect(user='dspublic', password='R3ad0nlY', host='129.114.52.174', port=3306, db='sjbrande_vpdb')
            cur = cnx.cursor(pymysql.cursors.DictCursor)
            cur.execute(sql)
            data = cur.fetchall()
            cnx.close()
            return(data)
        except pymysql.Error as e:
            print("Error %d: %s" % (e.args[0], e.args[1]))
            pass
    else:
        print('In vp_db.read_sql(sql, output), output must be either "DataFrame" or "dict", not "' + output + '"')
        return
