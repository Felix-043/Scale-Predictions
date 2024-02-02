import pandas 
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler
scale = StandardScaler()  

df = pandas.read_csv(r"C:\Users\User\Downloads\data.csv")

X = df[['Weight', 'Volume']]

scaledX  = scale.fit_transform(X)
print(scaledX)