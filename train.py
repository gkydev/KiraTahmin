# verileri okumak için pandası import et

import pandas as pd

# verileri oku 

islenmemis_veri = pd.read_excel('Data.xlsx', sheet_name="Data")
islenmis_veri = pd.read_excel('Data.xlsx', sheet_name="Encoded Data2")

# index kolonlarını kaldır 

slenmemis_veri = islenmemis_veri.iloc[:, 1:]
islenmis_veri = islenmis_veri.iloc[:, 0:]

columns = ['Kira', 'BanyoSayısı', 'Depozito', 'Oda', 'BinaYaşı', 'IsınmaTipi', 'YapınınDurumu', 'Cephe', 'YakıtTipi']

print(islenmis_veri.head(5))
print(islenmemis_veri.head(5))

islenmemis_veri = islenmemis_veri[columns]

islenmis_veri = islenmis_veri[columns]

from sklearn.linear_model import LinearRegression

hedef = 'Kira'

# Bağımsız  değişkenler 
X = islenmis_veri[islenmis_veri.columns.difference([hedef])]

# Bağımlı değişkenler 

Y = islenmemis_veri[[hedef]]

print(X)
print(Y)

linReg = LinearRegression()

linReg.fit(X, Y)

import joblib 

joblib.dump(linReg, 'rents.pkl')
print("Model oluşturuldu")

# veri kolonlarını eğitimden kaydet
linReg = joblib.load('rents.pkl')
modelColumns = list(X.columns)
print(columns)
joblib.dump(modelColumns, 'rents-columns.pkl')
print("Model kolonlar oluşturuldu")


