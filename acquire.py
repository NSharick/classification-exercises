##Data Aquisition Functions for Classification Exercises##

#imports#
import numpy as np
import pandas as pd
import seaborn as sns
from pydataset import data
from env import get_db_url
import os


#Get the Titanic dataset from the database
def get_titanic_data():
    filename = 'titanic.csv'
    
    if os.path.exists(filename):
        print('Reading from csv file...')
        return pd.read_csv(filename)
    
    print('Getting a fresh copy from SQL database...')
    df = pd.read_sql('SELECT * FROM passengers', get_db_url('titanic_db'))
    df.to_csv(filename, index=False)
    return df  
#Verify the data pulled correctly
get_titanic_data().head()


#Get Iris dataset from the database and include species name along with species ID
def get_iris_data():
    filename = 'iris.csv'
    
    if os.path.exists(filename):
        print('Reading from csv file...')
        return pd.read_csv(filename)
    
    print('Getting a fresh copy from SQL database...')
    df = pd.read_sql('SELECT * FROM measurements JOIN species USING(species_id)', get_db_url('iris_db'))
    df.to_csv(filename, index=False)
    return df  
#verify the data pulled correctly
get_iris_data().head()


#Get the Telco data from the database and join all four tables into the one dataframe
def get_telco_data():
    filename = 'telco.csv'
    
    if os.path.exists(filename):
        print('Reading from csv file...')
        return pd.read_csv(filename)
    
    query = '''
    SELECT * FROM customers
    JOIN contract_types USING (contract_type_id)
    JOIN internet_service_types USING (internet_service_type_id)
    JOIN payment_types USING (payment_type_id)
    '''
    
    print('Getting a fresh copy from SQL database...')
    df = pd.read_sql(query, get_db_url('telco_churn'))
    df.to_csv(filename, index=False)
    return df  
#verify data pulled correctly
get_telco_data().head()
