import streamlit as st
from st_on_hover_tabs import on_hover_tabs
from src.app import classificador, analise_exploratoria, analise_comparativa, sobre


st.markdown('<style>' + open('./style.css').read() + '</style>', unsafe_allow_html=True)
with st.sidebar:
    tabs = on_hover_tabs(
        tabName=['Classificador', 'Análise exploratória', 'Análise comparativa', 'Sobre'],
        iconName=['check_circle', 'search', 'analytics', 'info'],
        default_choice=0,
        styles = {
            'navtab': {'text-transform': 'Captalize'}
        }
    )
if tabs == 'Classificador':
    classificador.page()
if tabs == 'Análise exploratória':
    analise_exploratoria.page()
if tabs == 'Análise comparativa':
    analise_comparativa.page()
if tabs == 'Sobre':
    sobre.page()