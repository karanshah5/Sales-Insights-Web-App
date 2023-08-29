import streamlit as st
st.set_option('deprecation.showPyplotGlobalUse', False)
from eda import run_eda
from plots import show_plots


def main():
    st.title("Simple EDA App")
    st.subheader("EDA Web App with Streamlit ")
    st.markdown("""
        #### Description
        -  Utilized Streamlit framework to create an interactive interface for data exploration.
        -  Employed Python Pandas for efficient data preprocessing, organization, and analysis.
        -  Generated informative visualizations using Matplotlib, enabling trend and pattern identification.
        -  Extracted key insights from sales data, supporting data-driven decision-making.
        -  Streamlined data exploration process, enhancing efficiency and clarity.
        """)
    menu = ["EDA","Plots"]
    choice = st.sidebar.selectbox("Menu",menu)

    if choice == "EDA":
        run_eda()
        pass
    elif choice == "Plots":
        show_plots()


if __name__ == '__main__':
    main()










