import streamlit as st
import streamlit.components.v1 as components
from streamlit_js_eval import streamlit_js_eval
import time
st.set_page_config(layout="wide")
components.iframe("""https://app.powerbi.com/view?r=eyJrIjoiOGQ5ODkyZDUtYzU5Mi00YTJjLWI4ZWMtNWIzN2JkOTBkNmI1IiwidCI6IjdjZTQ0MmYwLTExNTAtNGRjYS1iYzBiLWIxMTgwMzdiZTk1NSIsImMiOjl9""", width=1920, height=1080, scrolling=True)
a = st.empty()
c_time = time.time()
while True:
    if time.time()-c_time >= 5:
        streamlit_js_eval(js_expressions="parent.window.location.reload()")
