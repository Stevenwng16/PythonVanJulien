import pandas as pd

import streamlit as st

#import custom library
from db_connect_streamlit.read_db import read_from_database_streamlit

def get_data(conn):
    # Data: bmi of men
    query_bmi_men = "SELECT * FROM bmi_men"
    data_bmi_men = read_from_database_streamlit(query_bmi_men, parse_dates=['Year'], conn=conn,)

    # Data: bmi of women
    query_bmi_women = "SELECT * FROM bmi_women"
    data_bmi_women = read_from_database_streamlit(query_bmi_women, parse_dates=['Year'], conn=conn)

    # Data: kind of food (food group)
    query_food_group = "SELECT * FROM food_groups"
    data_food_group = read_from_database_streamlit(query_food_group, parse_dates=['Year'], conn=conn)

    # Data: food macronutrients (For example fats)
    query_macronutrients = "SELECT * FROM macronutrients"
    data_macronutrients = read_from_database_streamlit(query_macronutrients, parse_dates=['Year'], conn=conn)

    # Data: covid
    query_covid_data = "SELECT * FROM covid_data"
    data_covid = read_from_database_streamlit(query_covid_data, parse_dates=['date'], conn=conn)

    # Data: overweight adults
    query_overweight = "SELECT * FROM share_overweight_adults"
    data_overweight_adults = read_from_database_streamlit(query_overweight, parse_dates=['Year'], conn=conn)

    # Data: bmi of men
    query_life_expectancy = "SELECT * FROM life_expectancy"
    data_life_expectancy = read_from_database_streamlit(query_life_expectancy, parse_dates=['Year'], conn=conn)

    return data_bmi_men, data_bmi_women, data_food_group, data_macronutrients, data_life_expectancy, data_covid, data_overweight_adults