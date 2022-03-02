## Data Preperation Exercises ##

#imports
import pandas as pd
import numpy as np


#Prepare Iris dataset function
def prep_iris(df):
    '''
    takes in a dataframe of the iris dataset and returns a cleaned dataframe
    with id columns removed and iris species encoded
    '''
    columns_to_drop = ['species_id', 'measurement_id']
    df = df.drop(columns = columns_to_drop)
    df = df.rename(columns = {'species_name': 'species'})
    dummy_df = pd.get_dummies(df[['species']], drop_first = True)
    df = pd.concat([df, dummy_df], axis=1)
    return df.drop(columns = ['species'])
    

#Prepare Titanic dataset function
def prep_titanic(df):
    '''
    takes in a dataframe and returns a cleaned dataframe 
    with unnecesary and duplicate columns removed 
    and categorical columns encoded
    '''
    drop_columns = ['passenger_id', 'class', 'embarked', 'deck', 'age']
    df = df.drop(columns = drop_columns)
    dum_df = pd.get_dummies(df[['sex', 'embark_town']], drop_first = [True, True])
    df = pd.concat([df, dum_df], axis = 1)
    return df.drop(columns = ['sex', 'embark_town'])


#Prepare Telco dataset function
def prep_telco(df):
    df.total_charges = df.total_charges.replace(' ', np.nan).astype(float)
    columns_drop = ['customer_id', 'payment_type_id', 'internet_service_type_id', 'contract_type_id']
    df = df.drop(columns = columns_drop)
    encode_cols = [col for col in df.columns if df[col].dtype == 'O']
    for col in encode_cols:
        dumb_df = pd.get_dummies(df[col], prefix = df[col].name, drop_first = True)
        df = pd.concat([df, dumb_df], axis=1)
        df = df.drop(columns=[col])
    return df

