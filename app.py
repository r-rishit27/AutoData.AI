import streamlit as st
import pandas as pd
from pandasai.llm.openai import OpenAI
from dotenv import load_dotenv
import os
import matplotlib.pyplot as plt
plt.switch_backend('agg')
from pandasai import SmartDataframe

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_API_KEY"] = ""

def chat_with_csv(df,prompt):
    llm = OpenAI(api_token=openai_api_key)
    pandas_ai = SmartDataframe(df, config={"llm": llm})
    result = pandas_ai.chat(prompt)
    return result

st.set_page_config(layout='wide')
st.title("AutoData.AI 🤖")
st.markdown('<style>h1{color: white; text-align: center;}</style>', unsafe_allow_html=True)
st.subheader('Built for All Data Analysis📊 and Visualizations📈')
st.markdown('<style>h3{color: Orange;  text-align: center;}</style>', unsafe_allow_html=True)

input_csvs = st.sidebar.file_uploader("Upload your CSV files", type=['csv'], accept_multiple_files=True)

if input_csvs:
    selected_file = st.selectbox("Select a CSV file", [file.name for file in input_csvs])
    selected_index = [file.name for file in input_csvs].index(selected_file)

    try:
        data = pd.read_csv(input_csvs[selected_index], encoding='ISO-8859-1')
        st.info("CSV uploaded successfully")

        st.info("Chat Below")
        input_text = st.text_area("Enter the query")

        if input_text:
            if st.button("Chat with csv"):
                st.info("Your Query: "+ input_text)
                result = chat_with_csv(data,input_text)
                fig_number = plt.get_fignums()
            if fig_number:
                st.pyplot(plt.gcf())
            else:
                st.success(result)
    except UnicodeDecodeError:
        st.error("Error: Unable to decode the CSV file. Please ensure that the file encoding is correct.")
