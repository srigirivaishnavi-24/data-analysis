#how to create a datafram
#index=false-> it dont display the index nums
"""import pandas as pd
data={
    "name":['ram','raj','shyam'],
    "age":[34,56,78],
    "city":['hyd','ramnagar','vnagar']
}
df=pd.DataFrame(data,index=false)
print(df)"""

#how to read a file
#encoding->it use to convent the text into the computer language-->"utf-8"(or)"latin1"
#import pandas as pd
#df=pd.read_csv(r"C:\Users\sathv\Downloads\Superstore_Sales_with_errors.csv")
#print(df)

#explore the dataset
"""
roles:
->understand the dataset
->identify the problems like missing values,infinitevalues..etc
->plan next steps
"""

#rows-->head(),tail()
#n=1,2,...n numbers
#.head(n):it is use to display first n no of rows
#.head():it is use to display only first 5 rows

#.tail(n):it is use to display last n no of rows
#.tail():it is use to display only last 5 rows


import pandas as pd
df=pd.read_csv(r"C:\Users\sathv\Downloads\Superstore_Sales_with_errors.csv")
"""print(df.head())
print(df.head(7))
print(df.tail())
print(df.tail(9))"""

#.info()-->by this we can find the no of rows,cols with names,data type,missing values and non null values
#print(df.info())

#describe()->summary of described statistics for numerical columns in a dataframe
#print(df.describe())

#shapes-> it is used to know the shape of the datafram like dimensions to quickly understand
#print(df.shape)
#columns-> it is used to know the how many col's with names present in the dataframe to understand the structur
#print(df.columns)

#selecting columns-> to select any specific col or col's from dataframe
#single col->df["col name"]
#multiple col's->df[["col1","col2"....]]
#print(df["Customer Name"])

"""subset=df[["Order ID", "C#ustomer Name"]]
print(subset)
print(df.columns)"""

#filtering-> it use to print on the condition that are applyed on the dataframe
#single conditon-> df["col name"]>condition (we can use any kind of operators)
#multiple conditions->df["col1 name"]>condition  and ["col2 name"]>condition(we can use the logical operators)
"""print(df[df["Sales"]>500])
print(df[(df["Sales"]>500) & (df["Discount"]>100)])
print(df[(df["Sales"]>500) or (df["Discount"]>100)])"""
