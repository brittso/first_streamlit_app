
import streamlit

streamlit.title('My Parents New Healthy Diner')

streamlit.header('this')


streamlit.text('🤞 this')
streamlit.text('🍞 this')



import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe('my fruit list')
