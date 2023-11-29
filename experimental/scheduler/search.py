import requests
import streamlit as st
from typing import NamedTuple

# force wide mode
st.set_page_config(layout="wide")

if query := st.text_input("Query"):
    r = requests.get("http://localhost:8080/v1beta/search", params=dict(q=query))
    hits = r.json()["hits"]
    for x in hits:
        st.write(x)
