import streamlit as st
from streamlit.components import v1 as components


def page():
    st.title('Análise comparativa')
    plot_file = open('src/app/comparative_analysis.html', 'r')
    plot = plot_file.read()
    components.html(plot, width=900, height=700, scrolling=True)
    plot_file.close()