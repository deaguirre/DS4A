from sqlalchemy import create_engine
import pandas as pd


def select_table():
    """
    Make a query to the database and return the result in a dataframe.
    """
    try:
        connDB = dbconn()
        if(connDB):
                query='SELECT * FROM datos_proceso_consolidado'
                df = pd.read_sql(query, connDB)
                return df
        else:
                return False
    except:
        print("Error loading database table")
        return False


def dbconn():
    """
    Make the connection with the database.
    """
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
       

    
       