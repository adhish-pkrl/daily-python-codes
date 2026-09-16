#DAta Frame
import pandas as pd
# df = pd.DataFrame("")
# df = pd.read_excel("darty_sales_data.xlsx")

# # print(df)
# df.head()



#reading source data
ff = pd.read_csv("unclean_data.csv")

#shows top 5 rows from the table
ff.head()

#shows last 5 rows from the table
print(ff.tail())
# ff.info()
# ff.columns

#jupitar notebook
#karnel