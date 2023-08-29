import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
import os

# Our Dataset
my_dataset = "updated.csv"
#group = "grouped.csv"

# To Improve speed and cache data
@st.cache(persist=True,allow_output_mutation=True)
def explore_data(dataset):
        df = pd.read_csv(os.path.join(dataset))
        return df

# Load Our Dataset
data = explore_data(my_dataset)
#data_g = explore_data(group)

def show_plots():
    if st.checkbox("Best Month for Sales"):
        data = explore_data (my_dataset)
        data['Sales'] = data['Quantity Ordered'].astype('int') * data['Price Each'].astype('float')
        data.groupby(['Month']).sum()
        months = range(1, 13)
        plt.bar(months, data.groupby(['Month']).sum()['Sales'])
        plt.xticks(months)
        plt.ylabel('Sales in USD ($)')
        plt.xlabel('Month number')
        plt.show()
        st.pyplot()
        st.subheader("From the bar chart we can conclude that the best month for sales was December.")

    elif st.checkbox("What City sold the most product?"):
        data = explore_data(my_dataset)
        data.groupby(['City']).sum()
        keys = [city for city, df in data.groupby(['City'])]
        plt.bar(keys, data.groupby(['City']).sum()['Sales'])
        plt.ylabel('Sales in USD ($)')
        plt.xlabel('City')
        plt.xticks(keys, rotation='vertical', size=8)
        plt.show()
        st.pyplot()
        st.subheader("It is evident from the bar chart that most no. of products were sold in San Francisco.")

    elif st.checkbox("What time should we display advertisements to maximize likelihood of customer's buying product?"):
        data = explore_data(my_dataset)
        # Add hour column
        data['Hour'] = pd.to_datetime(data['Order Date']).dt.hour
        data['Minute'] = pd.to_datetime(data['Order Date']).dt.minute
        data['Count'] = 1
        data.head()

        keys = [pair for pair, df in data.groupby(['Hour'])]
        plt.plot(keys, data.groupby(['Hour']).count()['Count'])
        plt.xticks(keys)
        plt.ylabel('Number of Orders')
        plt.xlabel('Hour')
        plt.grid()
        plt.show()
        st.pyplot()
        st.subheader("My recommendation is to display advertisments slightly before 11 AM or 7 PM.")

    elif st.checkbox("What products are most often sold together?"):
        data = explore_data(my_dataset)
        df = data[data['Order ID'].duplicated(keep=False)]

        # Referenced: https://stackoverflow.com/questions/27298178/concatenate-strings-from-several-rows-using-pandas-groupby
        df['Grouped'] = df.groupby('Order ID')['Product'].transform(lambda x: ','.join(x))
        df2 = df[['Order ID', 'Grouped']].drop_duplicates()

        # Referenced: https://stackoverflow.com/questions/52195887/counting-unique-pairs-of-numbers-into-a-python-dictionary
        from itertools import combinations
        from collections import Counter

        count = Counter()

        for row in df2['Grouped']:
            row_list = row.split(',')
            count.update(Counter(combinations(row_list, 2)))

        lst1 = []
        lst2 = []

        for key, value in count.most_common(10):
            lst1.append(key)
            lst2.append(value)

        df = pd.DataFrame({'Group of Products': lst1, 'Count': lst2})
        df.to_csv('grouped.csv', index=False)
        group = "grouped.csv"
        data_g = explore_data(group)
        st.dataframe(data_g)
        st.subheader("We can offer smart deals on (Iphone, Lightning Charging Cable) and so-on.")

    elif st.checkbox("What product sold the most?"):
        data = explore_data(my_dataset)
        product_group = data.groupby('Product')
        quantity_ordered = product_group.sum()['Quantity Ordered']

        keys = [pair for pair, df in product_group]
        plt.bar(keys, quantity_ordered)
        plt.xticks(keys, rotation='vertical', size=8)
        plt.show()
        st.pyplot()



        # Referenced: https://stackoverflow.com/questions/14762181/adding-a-y-axis-label-to-secondary-y-axis-in-matplotlib

        prices = data.groupby('Product').mean()['Price Each']

        fig, ax1 = plt.subplots()

        ax2 = ax1.twinx()
        ax1.bar(keys, quantity_ordered, color='g')
        ax2.plot(keys, prices, color='b')

        ax1.set_xlabel('Product Name')
        ax1.set_ylabel('Quantity Ordered', color='g')
        ax2.set_ylabel('Price ($)', color='b')
        ax1.set_xticklabels(keys, rotation='vertical', size=8)

        fig.show()
        st.pyplot()
        st.subheader("From the above two graphs we can prove the hypothesis that the product whose price is high was sold the least and vice versa.")