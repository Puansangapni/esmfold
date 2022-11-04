import streamlit as st
from stmol import showmol, render_pdb
import py3Dmol

st.title('🎈 ESMfold')

showmol(render_pdb(id = '1A2C'))
