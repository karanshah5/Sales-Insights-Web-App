import streamlit as st
import pandas as pd
import os

# Our Dataset
my_dataset = "updated.csv"
group = "grouped.csv"

# To Improve speed and cache data
@st.cache(persist=True,allow_output_mutation=True)
def explore_data(dataset):
    	df = pd.read_csv(os.path.join(dataset))
    	return df

# Load Our Dataset
data = explore_data(my_dataset)
data_g = explore_data(group)

def run_eda():
	data_dim = st.radio('What Dimension Do You Want to Show', ('Rows', 'Columns'))
	if data_dim == 'Rows':
		st.text("Showing Length of Rows")
		st.write(len(data))
	if data_dim == 'Columns':
		st.text("Showing Length of Columns")
		st.write(data.shape[1])
#Show Dataframe
	if st.checkbox("Preview DataFrame"):
		if st.button("Head"):
			st.write(data.head())
		if st.button("Tail"):
			st.write(data.tail())
		else:
			st.write(data.head(2))

# Show Entire Dataframe
	if st.checkbox("Show All DataFrame"):
		st.dataframe(data)

# Show All Column Names
	if st.checkbox("Show All Column Name"):
		st.text("Columns:")
		st.write(data.columns)

