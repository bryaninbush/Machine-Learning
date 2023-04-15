import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data/admission_data.csv")
df.head()
df.describe() #看資料
df.isnull().sum() #看空值
df.shape

df.corr()
sns.heatmap(df.corr(), annot=True,cmap="Blues") #看相關性
sns.pairplot(df)

#sns.boxplot(df["GRE Score"])
#sns.boxplot(df["TOEFL Score"])
#sns.boxplot(df["University Rating"])
#sns.boxplot(df["SOP"])
#sns.boxplot(df["LOR"])
#sns.boxplot(df["CGPA"])
#sns.boxplot(df["Research"])
#sns.boxplot(df["Chance of Admit "])

sns.boxplot(y=df['GRE Score'],x=df['Chance of Admit '])
sns.boxplot(y=df['Research'],x=df['Chance of Admit '])

#去掉極端值
#剔除outlier
Q1= df.quantile(0.25)
Q3 = df.quantile(0.75)
IQR = Q3-Q1
print(IQR) #觀察IQR
print((df<(Q1-1.5*IQR))|(df>(Q3+1.5*IQR))) #發現無離群值


X=df.drop(['Chance of Admit ','Research','SOP'] ,axis=1,inplace=False)
y=df['Chance of Admit ']
#嘗試drop LOR(相關性次低) 結果r2準確度從0.8429==>0.839

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=52)

#1==> linear
from sklearn.metrics import r2_score
from sklearn.linear_model import LinearRegression
reg = LinearRegression()
reg.fit(X_train, y_train)
predictions = reg.predict(X_test)
x1 = r2_score(y_test,predictions)
plt.scatter(y_test, predictions, color="brown")

#2 SVR
from sklearn.svm import SVR
model2 = SVR(kernel= 'rbf') #專屬線性
model2.fit(X_train, y_train)
x2 = model2.score(X_test, y_test) #0.71422 準確率低

#3 random

from sklearn.ensemble import RandomForestRegressor
outcome_var = 'Chance of Admit '
model3 = RandomForestRegressor(n_estimators=10)
model3.fit(X_train, y_train)
x3 = model3.score(X_test, y_test) #0.76

#4 tree

from sklearn.tree import DecisionTreeRegressor
model4 = DecisionTreeRegressor(random_state=0)
model4.fit(X_train, y_train)
x4 = model4.score(X_test, y_test) #0.62525

results = pd.DataFrame(columns=['R2-score'])
results.loc['LinearRegression']=[x1]
results.loc['SVR']=[x2]
results.loc['RandomForest']=[x3]
results.loc['DecisionTree']=[x4]

print(results)
results.sort_values('R2-score',ascending=False).style.background_gradient(cmap='Blues',subset=['R2-score'])