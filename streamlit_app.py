
import streamlit;

streamlit.title('My Parents New Healthy Diner');

streamlit.header('this');


streamlit.text('🤞 this');
streamlit.text('🍞 this');


import pandas;
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt");
my_fruit_list = my_fruit_list.set_index('Fruit')



streamlit.multiselect("Pick fruit:", list(my_fruit_list.index),['Avocado','Strawberries'])


fruits_selected = streamlit.multiselect("Pick fruit:", list(my_fruit_list.index),['Avocado','Strawberries'])

fruits_to_show = my_fruit_list.loc[fruits_selected]


streamlit.dataframe(my_fruit_list)
 
