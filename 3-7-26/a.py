import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split,cross_val_score,GridSearchCV,RandomizedSearchCV
df=pd.read_csv('Corporate_AI_Employee_Dataset.csv')
print(df.head())
print(df.tail())
print(df.info(),"\n",df.describe(),"\n",df.columns,"\n",df.shape, "\n", df.describe(include=object))


quantitative=df.select_dtypes(include=np.number)
print(quantitative)
print(df.info())
qualitative=df.select_dtypes(include=str)
print(qualitative)


print(df.select_dtypes(include=object))
#this are objects (Gender Department Job_Role Education_Level Promotion_Last_3Y Attrition_Risk) now we are going to convert into categorys
print(df.memory_usage(deep=True))
df[["Department","Gender","Job_Role","Education_Level","Promotion_Last_3Y","Attrition_Risk"]] = df[["Department","Gender","Job_Role","Education_Level","Promotion_Last_3Y","Attrition_Risk"]].astype("category")
print(df.memory_usage(deep=True))


print(df.duplicated().sum())#there are no duplicates

print(df.isnull().sum())
print(df.nunique())
print(df[df["Gender"]!="Other"])

import seaborn as sns
import matplotlib.pyplot as plt
print(df.skew(numeric_only=True))

# sns.histplot(df["Salary"])

# plt.show()

from statsmodels.stats.outliers_influence import variance_inflation_factor

X = df.select_dtypes(include=np.number)
print(X.shape)
vif = pd.DataFrame()

vif["Feature"] = X.columns

vif["VIF"] = [variance_inflation_factor(X.values,i)
              for i in range(X.shape[1])]

print(vif)

corr = df.corr(numeric_only=True)

print(corr)

# sns.heatmap(corr)

# plt.show()

# sns.boxplot(data=df,
#             x="Department",
#             y="Employee_Performance_Score")

# plt.show()

# sns.boxplot(data=df,
#             x="Education_Level",
#             y="Employee_Performance_Score")

# plt.show()

df["Experience_Level"]=pd.cut(df['Experience_Years'],bins=[0,2,5,10,50],labels=['Junior','mid','Senior','expert'])
print(df)

df["Performance_Index"] = (
    df["Coding_Test_Score"] +
    df["AI_Training_Hours"] +
    df["Communication_Score"]
)/3
print(df)

df["Coding_AI"] = (
    df["Coding_Test_Score"] *
    df["AI_Training_Hours"]
)
print(df)


from sklearn.preprocessing import OneHotEncoder

from sklearn.feature_selection import mutual_info_regression,RFE
X=df.drop("Employee_Performance_Score",axis=1)
X = pd.get_dummies(X, drop_first=True)
y=df['Employee_Performance_Score']
mi=mutual_info_regression(X,y)
print(mi)


lr=LinearRegression()
rfe=RFE(lr,n_features_to_select=8)
r=rfe.fit(X,y)
print(r)

from sklearn.feature_selection import SelectKBest,f_regression

from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score
selector = SelectKBest(
            score_func=f_regression,
            k=15)

selector.fit(X,y)


print(rfe.support_)

print(selector.get_support())

selected_features = X.columns[rfe.support_]

print(selected_features)



model = LinearRegression()
x_train,x_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
sc=StandardScaler()
x_trains=sc.fit_transform(x_train)
x_tests=sc.transform(x_test)
model.fit(x_trains,y_train)

pred = model.predict(x_tests)

print(mean_squared_error(y_test,pred))
print(mean_absolute_error(y_test,pred))
print(r2_score(y_test,pred))

from sklearn.linear_model import Ridge,Lasso,ElasticNet

ridge = Ridge()

ridge.fit(x_trains,y_train)


lasso = Lasso()

lasso.fit(x_trains,y_train)


elastic = ElasticNet()

elastic.fit(x_trains,y_train)

print(ridge.coef_,lasso.coef_,elastic.coef_)
print(mean_absolute_error(y_test,pred))

print(np.sqrt(mean_squared_error(y_test,pred)))

print(r2_score(y_test,pred))

from sklearn.tree import DecisionTreeRegressor

tree = DecisionTreeRegressor()

tree.fit(x_train,y_train)
print(mean_absolute_error(y_test,pred))

print(np.sqrt(mean_squared_error(y_test,pred)))

print(r2_score(y_test,pred))

from sklearn.ensemble import RandomForestRegressor

rf = RandomForestRegressor()

rf.fit(x_trains,y_train)
print(mean_absolute_error(y_test,pred))

print(np.sqrt(mean_squared_error(y_test,pred)))

print(r2_score(y_test,pred))

from sklearn.ensemble import ExtraTreesRegressor,GradientBoostingRegressor

extra = ExtraTreesRegressor()

extra.fit(x_trains,y_train)


gb = GradientBoostingRegressor()

gb.fit(x_trains,y_train)
print(mean_absolute_error(y_test,pred))

print(np.sqrt(mean_squared_error(y_test,pred)))

print(r2_score(y_test,pred))
from xgboost import XGBRegressor

xgb = XGBRegressor()

xgb.fit(x_trains,y_train)

print(mean_absolute_error(y_test,pred))

print(np.sqrt(mean_squared_error(y_test,pred)))

print(r2_score(y_test,pred))

plt.scatter(y_test,pred)

plt.show()

residual = y_test-pred

sns.histplot(residual)

plt.show()

print(model.score(x_trains,y_train))

print(model.score(x_tests,y_test))


print(cross_val_score(model,X,y,cv=10))

parms={'alpha':[1.0,0.05,0.5,100,10]}
grid=GridSearchCV(rf,param_grid=parms,cv=5)
grid.fit(x_trains,y_train)
random=RandomizedSearchCV(xgb,param_distributions=parms,cv=5)
random.fit(x_trains,y_train)


print('searchcv scores')
print(grid.best_score_,random.best_score_,grid.best_params_,random.best_params_)


import shap

explainer = shap.TreeExplainer(rf)

shap_values = explainer.shap_values(x_test)

shap.summary_plot(
    shap_values,
    x_test
)


pipeline=RandomForestRegressor()
pipeline.fit(x_trains,y_train)

print(pipeline.predict(x_test))

import joblib

joblib.dump(
    pipeline,
    "employee_model.pkl"
)