import pandas as pd
import matplotlib.pyplot as plt

file_path = 'data.txt'

df = pd.read_csv(file_path, names=['scramble', 'length', 'distance'])

df_dis = df.groupby(['length'])['distance'].value_counts(normalize=True)
df_dis.to_csv("df_dis.csv")

print(df_dis)
da = df_dis.unstack().fillna(0).to_numpy()

#print(da[0])
#print(da[1])

tv_list=[]
id_list=[]
for i in range(1,5):
 id_list.append(i)
 tv_list.append(sum(abs(da[i]-da[0]))/2.0)
 #print(id_list[i-1], tv_list[i-1])
