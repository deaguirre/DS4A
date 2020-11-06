from sqlalchemy import create_engine
import pandas as pd


def select_table(year):
    try:
        connDB = dbconn()
        if(connDB):
            if year==2018 or year==2019:
                query='SELECT * FROM datos_proceso'+'_'+str(year)
                df = pd.read_sql(query, connDB)
            elif year=='consolidado':
                query='SELECT * FROM datos_proceso'+'_'+str(year)
                df = pd.read_sql(query, connDB)   
            else:
                query='SELECT * FROM datos_proceso WHERE year=\''+str(year)+'\''
                df = pd.read_sql(query, connDB)
            return df
        else:
            return False
    except:
        print("Error loading database table")
        return False


def dbconn():
    host = 'ds4aprogel101.c7s9fkqnzrfg.us-east-2.rds.amazonaws.com'
    port = 5432
    user = 'progel_dev_user'
    password = 'progel123'
    database = 'progel_process'
    try:
        connDB = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{database}')
    except:
        print('We cannot connect with the database')
        return False
    else:
        return connDB
       

    
       