import pickle
from pandas import DataFrame,get_dummies

model = pickle.load(open('finalized_model.sav','rb'))
features_columns = pickle.load(open('features_columns.sav','rb'))
one_hot_columns = pickle.load(open('x_dummies_columns.sav','rb'))

def prediction(data):
    df = DataFrame(data,index=[0])
    df = get_dummies(df)
    df = df.reindex(columns=one_hot_columns, fill_value=0)
    hasil = model.predict(df)
    return round(hasil[0])