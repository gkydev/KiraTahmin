import joblib
import pandas as pd
import numpy as np
from pandas.io.json import json_normalize


def predict(predict_data):
    jlb = joblib.load('rents.pkl')
    model_columns = joblib.load('rents-columns.pkl')
    print("Models Loaded")
    #test_data = {"BanyoSayısı": [2], "Depozito": [1.0], "Oda": [1.0], "BinaYaşı": [40], "IsınmaTipi": ["Kombi"], "YapınınDurumu": ["İkinciEl"], "Cephe": ["Güney"], "YakıtTipi": ["Doğalgaz"]}
    query = pd.get_dummies(pd.DataFrame(predict_data))
    query = query.reindex(columns=model_columns, fill_value=0)
    prec = list(jlb.predict(query))
    prec = prec[0][0]
    if prec < 0:
        prec = prec*-1
    print(prec)
    return prec