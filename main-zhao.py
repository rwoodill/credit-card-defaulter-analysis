
import pandas as pd
import matplotlib

main_df = pd.read_csv("raw\\application_data_cleaned_v1.csv")

main_df.isnull().sum()
main_df.dropna(axis=0,inplace=True)
main_df.isnull().sum()

df_dfaulters = main_df[main_df['TARGET']==1]
df_normal = main_df[main_df['TARGET']==0]

#Statistical summary
stat_normal = df_normal.agg({
    "AMT_INCOME_TOTAL":["min", "max", 'mean',"median","std"],
    "AMT_CREDIT":["min", "max", 'mean',"median","std"],
    "AMT_ANNUITY":["min", "max", 'mean',"median","std"],
    "AMT_GOODS_PRICE":["min", "max", 'mean',"median","std"]
    })
stat_defaulters = df_dfaulters.agg({
    "AMT_INCOME_TOTAL":["min", "max", 'mean',"median","std"],
    "AMT_CREDIT":["min", "max", 'mean',"median","std"],
    "AMT_ANNUITY":["min", "max", 'mean',"median","std"],
    "AMT_GOODS_PRICE":["min", "max", 'mean',"median","std"]
    })

barfigure_age_all = main_df['DAYS_BIRTH'].plot.bar()


