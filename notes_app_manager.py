import streamlit as st
import pandas as pd
from datetime import datetime
import os

st.set_page_config(page_title=" Notes Manager", layout="wide")

FILE = "notes_data.xlsx"

if os.path.exists(FILE):
    df = pd.read_excel(FILE)
else:
    df = pd.DataFrame(columns=["ID", "Title", "Category", "Content", "Timestamp"])

st.title("🧠 AI Notes Manager")

menu = st.sidebar.radio("Menu", ["Add", "View", "Search", "Delete"])

if menu == "Add":
    note_id = st.text_input("ID")
    title = st.text_input("Title")
    category = st.selectbox("Category", ["Work", "Personal", "Ideas"])
    content = st.text_area("Content")

    if st.button("Add Note"):
        new = pd.DataFrame({
            "ID":[note_id],
            "Title":[title],
            "Category":[category],
            "Content":[content],
            "Timestamp":[datetime.now()]
        })
        df = pd.concat([df, new], ignore_index=True)
        df.to_excel(FILE, index=False)
        st.success("Added!")

elif menu == "View":
    st.dataframe(df)

elif menu == "Search":
    key = st.text_input("Keyword")
    if key:
        st.dataframe(df[df["Content"].str.contains(key, case=False, na=False)])

elif menu == "Delete":
    note_id = st.text_input("Enter ID")
    if st.button("Delete"):
        df = df[df["ID"] != note_id]
        df.to_excel(FILE, index=False)
        st.success("Deleted!")
