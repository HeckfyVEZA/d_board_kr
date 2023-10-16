import streamlit as st
import streamlit.components.v1 as components
from streamlit_js_eval import streamlit_js_eval
import time
st.set_page_config(layout="wide")
st.markdown("""<iframe title="Рабочий день" width="100%" height="100%" src="https://app.powerbi.com/view?r=eyJrIjoiMGNlZGVlMGEtNDc3Mi00NDllLThjODEtMWFkMTEwNjhlNzgxIiwidCI6IjdjZTQ0MmYwLTExNTAtNGRjYS1iYzBiLWIxMTgwMzdiZTk1NSIsImMiOjl9" frameborder="0" allowFullScreen="true"></iframe>""", unsafe_allow_html=True)
a = st.empty()
c_time = time.time()
while True:
    if time.time()-c_time >= 1200:
        streamlit_js_eval(js_expressions="parent.window.location.reload()")
