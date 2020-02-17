import pandas as pd

df=pd.read_csv('../datasets/Kalapa_s Credit_Scoring_challenge/train.csv',delimiter=',',header=None)

# display  
data_top  = df.head()
print(data_top)
print(df.columns)
print(df[25].unique())
# uniques = df[13].unique()
# for x in uniques :
# 	print(x)
	# pass