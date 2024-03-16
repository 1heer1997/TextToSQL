from dotenv import load_dotenv
load_dotenv() ## load all the environment variables

import streamlit as st
import os
import sqlite3

import google.generativeai as genai

## configure our API  Key

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# function to load google gemini model and provide SQL query as response

def get_gemini_response(question,prompt):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content([prompt[0],question]) 
# prompt[0] as only 1 propmpt (how this model should behaves like), quest - text to SQL query
    return response.text

## Function to retrieve SQL query from the SQL Database

def read_SQL_query(sql,db):
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    cur.execute(sql)
    rows=cur.fetchall() # keeping all the values in rows after fetching from db
    conn.commit()
    conn.close()

    for row in rows:
        print(row)
    return rows

## define your prompt in the form of list

prompt=[
    """

    You are an expert in converting English questions to SQL Query!
    The SQL database has the name STUDENT and has the following columns - NAME,CLASS, SECTION and MARKS \n\n
    For example, \nExample 1 - How many entries of records are present?,
    the SQL command will be something like this SELECT COUNT(*) FROM STUDENT;
    \nExample 2 - Tell me all the students studying in Data Science class?,
    the SQL command will be something like this SELECT * FROM STUDENT where CLASS="DATA SCIENCE";
    also the sql code should not have ``` in begining or end and sql word in the output.

    """


]


## Streamlit App

st.set_page_config(page_title="I can Retrieve Any SQL query")
st.header("Gemini App to Retrieve SQL Data")

question=st.text_input("Input: ",key="input")

submit=st.button("Ask the question")

# if submit is clicked

if submit:
    response=get_gemini_response(question,prompt) # will go to get_gemini_respons and fetch sql query
    print(response)
    data=read_SQL_query(response,"student.db")
    st.subheader("The Response is")
    for row in data:
        print(row)
        st.header(row)







