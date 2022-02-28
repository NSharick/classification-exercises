## Data Preperation Exercises ##

#Prepare Iris dataset function
df = get_iris_data()

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
    
#verify the returned cleaned dataframe
clean_iris = prep_iris(df)
clean_iris.head()


#Prepare Titanic dataset function
dff = get_titanic_data()

def prep_titanic(dff):
    '''
    takes in a dataframe and returns a cleaned dataframe 
    with unnecesary and duplicate columns removed 
    and categorical columns encoded
    '''
    drop_columns = ['passenger_id', 'class', 'embarked', 'deck', 'age']
    dff = dff.drop(columns = drop_columns)
    dum_df = pd.get_dummies(dff[['sex', 'embark_town']], drop_first = [True, True])
    dff = pd.concat([dff, dum_df], axis = 1)
    return dff.drop(columns = ['sex', 'embark_town'])

#verify the returned cleaned dataframe
prep_titanic(dff).head()


#Prepare Telco dataset function

