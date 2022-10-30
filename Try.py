import matplotlib.pyplot as plt  
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import rcParams

office = pd.read_csv("office_supplies.csv")  
df = pd.DataFrame(office)

sns.set_style("darkgrid")

####
Date = pd.to_datetime(df["Order Date"]).dt.year
Total_Quantity_Year = df[df["Region"]=="West"]
#print(Total_Quantity_Year)
Total_Quantity = df["Quantity"]
#print(Total_Quantity)
hue_colors = {"Technology": "Blue",
              "Office Supplies": "Orange",
              "Furniture": "Green"}
sns.relplot(x=Date,
        	y=Total_Quantity,
            data=Total_Quantity_Year,
            kind="line",
            height=3,
            aspect=2,
            hue="Category",
            ci=None,
            style="Category",
            style_order=["Technology", "Office Supplies", "Furniture"],
            estimator = sum,
            markers=True,
            palette=hue_colors,
            hue_order=["Technology", "Office Supplies", "Furniture"])
plt.ylabel('Quantity',weight="bold")
plt.xlabel('Year',weight="bold")
plt.title('Quantity in each category over the years: West region',weight="bold")
plt.ylim([0,3000])
plt.xticks([2014,2015,2016,2017])
plt.savefig('West_Quantity_Year.pdf')
plt.show()


Date = pd.to_datetime(df["Order Date"]).dt.year
Total_Quantity_Year = df[df["Region"]=="South"]
Total_Quantity = df["Quantity"]
sns.relplot(x=Date,
        	y=Total_Quantity,
            data=Total_Quantity_Year,
            kind="line",
            height=3,
            aspect=2,
            hue="Category",
            ci=None,
            style="Category",
            style_order=["Technology", "Office Supplies", "Furniture"],
            estimator = sum,
            markers=True,
            palette=hue_colors,
            hue_order=["Technology", "Office Supplies", "Furniture"])
plt.ylabel('Quantity',weight="bold") 
plt.xlabel('Year',weight="bold")
plt.title('Quantity in each category over the years: South region',weight="bold")
plt.ylim([0,3000])
plt.xticks([2014,2015,2016,2017])
plt.show()
plt.savefig('South_Quantity_Year', format = 'pdf')

Date = pd.to_datetime(df["Order Date"]).dt.year
Total_Quantity_Year = df[df["Region"]=="East"]
Total_Quantity = df["Quantity"]
sns.relplot(x=Date,
        	y=Total_Quantity,
            data=Total_Quantity_Year,
            kind="line",
            height=3,
            aspect=2,
            hue="Category",
            ci=None,
            style="Category",
            style_order=["Technology", "Office Supplies", "Furniture"],
            estimator = sum,
            markers=True,
            palette=hue_colors,
            hue_order=["Technology", "Office Supplies", "Furniture"])
plt.ylabel('Quantity',weight="bold") 
plt.xlabel('Year',weight="bold")
plt.title('Quantity in each category over the years: East region',weight="bold")
plt.ylim([0,3000])
plt.xticks([2014,2015,2016,2017])
plt.show()
plt.savefig('East_Quantity_Year', format = 'pdf')

Date = pd.to_datetime(df["Order Date"]).dt.year
Total_Quantity_Year = df[df["Region"]=="Central"]
Total_Quantity = df["Quantity"]
sns.relplot(x=Date,
        	y=Total_Quantity,
            data=Total_Quantity_Year,
            kind="line",
            height=3,
            aspect=2,
            hue="Category",
            ci=None,
            style="Category",
            style_order=["Technology", "Office Supplies", "Furniture"],
            estimator = sum,
            markers=True,
            palette=hue_colors,
            hue_order=["Technology", "Office Supplies", "Furniture"])
plt.ylabel('Quantity',weight="bold") 
plt.xlabel('Year',weight="bold")
plt.title('Quantity in each category over the years: Central region',weight="bold")
plt.ylim([0,3000])
plt.xticks([2014,2015,2016,2017])
plt.show()
plt.savefig('Central_Quantity_Year', format = 'pdf')

#Data for West Region
#https://datavizpyr.com/bar-plots-with-matplotlib-in-python/
#Category = df[df["Region"]=="West"]["Sub-Category"]
#data_sorted = df.sort_values("Sales", ascending=False)

Total_Sales = df[df["Region"]=="West"].groupby("Sub-Category")["Sales"].sum()
Total_Sales_Sorted = Total_Sales.sort_values(ascending = False)
plt.figure(figsize=(20,5))
plt.ylabel('Sales',weight="bold") 
plt.xlabel('Sub-Category',weight="bold")
plt.title('Sales of Sub-Category by Region: West',weight="bold")
plt.ylim([0, 120000])
Total_Sales_Sorted.plot(kind='bar')
plt.xticks(rotation=0)
plt.savefig('West_Sales', format = 'pdf')


Total_Quantity = df[df["Region"]=="West"].groupby("Sub-Category")["Quantity"].sum()
Total_Quantity_Sorted = Total_Quantity.sort_values(ascending = False)
plt.figure(figsize=(20,5))
plt.ylabel('Quantity',weight="bold") 
plt.xlabel('Sub-Category',weight="bold")
plt.title('Quantity in each sub-category: West region',weight="bold")
plt.ylim([0, 2000])
Total_Quantity_Sorted.plot(kind='bar')
plt.xticks(rotation=0)
plt.savefig('West_Quantity', format = 'pdf')

#Data for East Region
Total_Sales = df[df["Region"]=="East"].groupby("Sub-Category")["Sales"].sum()
Total_Sales_Sorted = Total_Sales.sort_values(ascending = False)
plt.figure(figsize=(20,5))
plt.ylabel('Sales',weight="bold") 
plt.xlabel('Sub-Category',weight="bold")
plt.title('Sales of Sub-Category by Region: East',weight="bold")
plt.ylim([0, 120000])
Total_Sales_Sorted.plot(kind='bar')
plt.xticks(rotation=0)
plt.savefig('East_Sales', format = 'pdf')

Total_Quantity = df[df["Region"]=="East"].groupby("Sub-Category")["Quantity"].sum()
Total_Quantity_Sorted = Total_Quantity.sort_values(ascending = False)
plt.figure(figsize=(20,5))
plt.ylabel('Quantity',weight="bold") 
plt.xlabel('Sub-Category',weight="bold")
plt.title('Quantity in each sub-category: East region',weight="bold")
plt.ylim([0, 2000])
Total_Quantity_Sorted.plot(kind='bar')
plt.xticks(rotation=0)
plt.savefig('East_Quantity', format = 'pdf')

#Data for South Region
Total_Sales = df[df["Region"]=="South"].groupby("Sub-Category")["Sales"].sum()
Total_Sales_Sorted = Total_Sales.sort_values(ascending = False)
plt.figure(figsize=(20,5))
plt.ylabel('Sales',weight="bold") 
plt.xlabel('Sub-Category',weight="bold")
plt.title('Sales of Sub-Category by Region: South',weight="bold")
plt.ylim([0, 120000])
Total_Sales_Sorted.plot(kind='bar')
plt.xticks(rotation=0)
plt.savefig('South_Sales', format = 'pdf')

Total_Quantity = df[df["Region"]=="South"].groupby("Sub-Category")["Quantity"].sum()
Total_Quantity_Sorted = Total_Quantity.sort_values(ascending = False)
plt.figure(figsize=(20,5))
plt.ylabel('Quantity',weight="bold") 
plt.xlabel('Sub-Category',weight="bold")
plt.title('Quantity in each sub-category: South region',weight="bold")
plt.ylim([0, 2000])
Total_Quantity_Sorted.plot(kind='bar')
plt.xticks(rotation=0)
plt.savefig('South_Quantity', format = 'pdf')

#Data for Central Region
Total_Sales = df[df["Region"]=="Central"].groupby("Sub-Category")["Sales"].sum()
Total_Sales_Sorted = Total_Sales.sort_values(ascending = False)
plt.figure(figsize=(20,5))
plt.ylabel('Sales',weight="bold") 
plt.xlabel('Sub-Category',weight="bold")
plt.title('Sales of Sub-Category by Region: Central',weight="bold")
plt.ylim([0, 120000])
Total_Sales_Sorted.plot(kind='bar')
plt.xticks(rotation=0)
plt.savefig('Central_Sales', format = 'pdf')

Total_Quantity = df[df["Region"]=="Central"].groupby("Sub-Category")["Quantity"].sum()
Total_Quantity_Sorted = Total_Quantity.sort_values(ascending = False)
plt.figure(figsize=(20,5))
plt.ylabel('Quantity',weight="bold") 
plt.xlabel('Sub-Category',weight="bold")
plt.title('Quantity in each sub-category: Central region',weight="bold")
plt.ylim([0, 2000])
Total_Quantity_Sorted.plot(kind='bar')
plt.xticks(rotation=0)
plt.savefig('Central_Quantity', format = 'pdf')