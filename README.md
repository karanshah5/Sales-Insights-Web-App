# Sales Insights Interactive Web App
Explore sales trends and insights with an interactive web app built using Streamlit, Python Pandas, and Matplotlib. Analyze 12 months of data effortlessly.


## Background Information:

We use Python Pandas & Python Matplotlib to analyze and answer business questions about 12 months worth of sales data. The data contains hundreds of thousands of electronics store purchases broken down by month, product type, cost, purchase address, etc. 
And after that we use Streamlit to create an intuitive and user-friendly interface for data exploration.

We start by cleaning our data. Tasks during this section include:
- Drop NaN values from DataFrame
- Removing rows based on a condition
- Change the type of columns (to_numeric, to_datetime, astype)

Once we have cleaned up our data a bit, we move the data exploration section. In this section we explore 5 high level business questions related to our data:
- What was the best month for sales? How much was earned that month?
- What city sold the most product?
- What time should we display advertisemens to maximize the likelihood of customer’s buying product?
- What products are most often sold together?
- What product sold the most? Why do you think it sold the most?

To answer these questions we walk through many different pandas & matplotlib methods. They include:
- Concatenating multiple csvs together to create a new DataFrame (pd.concat)
- Adding columns
- Parsing cells as strings to make new columns (.str)
- Using the .apply() method
- Using groupby to perform aggregate analysis
- Plotting bar charts and lines graphs to visualize our results
- Labeling our graphs

Once we have done the analysis,
- We integrate Matplotlib plots into Streamlit using the st.pyplot() function.
- Create widgets (e.g., dropdowns, sliders) in the Streamlit sidebar for user interaction.
- Utilize Streamlit's built-in components (e.g., st.line_chart(), st.bar_chart()) to create dynamic and interactive charts.
- Enable charts to update instantly as users interact with widgets.
- Use markdown text in Streamlit to provide context, explanations, and actionable recommendations.
- Click on this link to see the video of how this app works: https://bit.ly/4519qk9

