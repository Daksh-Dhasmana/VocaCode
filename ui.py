import streamlit as st
import time
from datetime import datetime
import json
import re

from speech_to_text import get_voice
from lexer import lexer
from parser import parser
from intermediate import generate_ir
from codegen import generate_c
from ai_orchestrator import ai_orchestrator

st.set_page_config(page_title="VocaCode AI Studio", page_icon="✨", layout="wide", initial_sidebar_state="collapsed")

#  CSS
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Outfit', sans-serif;
    }
    
    .stApp {
        background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 100%);
        color: #e2e8f0;
    }
    
    [data-testid="column"]:nth-of-type(2) {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(16px);
        -webkit-backdrop-filter: blur(16px);
        border: 1px solid rgba(255, 255, 255, 0.05);
        border-top: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 24px;
        padding: 2.5rem;
        box-shadow: 0 4px 30px rgba(0, 0, 0, 0.3);
        margin-bottom: 2rem;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    
    [data-testid="column"]:nth-of-type(2):hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 40px rgba(139, 92, 246, 0.15);
    }
    
    h1 {
        background: -webkit-linear-gradient(45deg, #a78bfa, #f472b6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 600 !important;
        font-size: 3.5rem !important;
        margin-bottom: 0.5rem !important;
        text-align: center;
    }
    
    .subtitle {
        text-align: center;
        color: #94a3b8;
        font-size: 1.2rem;
        margin-bottom: 3rem;
        font-weight: 300;
    }
    
    .stButton>button, .stDownloadButton>button {
        background: linear-gradient(90deg, #8b5cf6 0%, #d946ef 100%);
        color: white;
        border: none;
        border-radius: 12px;
        padding: 0.5rem 2rem;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover, .stDownloadButton>button:hover {
        box-shadow: 0 0 20px rgba(217, 70, 239, 0.5);
        transform: scale(1.02);
        color: white;
    }
    
    .stRadio>div {
        justify-content: center;
    }
    
</style>
""", unsafe_allow_html=True)

st.markdown("<h1>✨ VocaCode AI Assistant</h1>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Transform your natural language into executable C code instantly.</div>", unsafe_allow_html=True)

# Layout
col1, col2, col3 = st.columns([1.5, 5, 1.5])

with col2:
    input_method = st.radio("Choose interaction mode", ["⌨ Type Instruction", "Speak Instruction"], horizontal=True, label_visibility="collapsed")
    
    st.markdown("<br>", unsafe_allow_html=True)
    input_text = ""
    submit_btn = False
    
    if "Speak" in input_method:
        st.write("<div style='text-align: center; color: #a78bfa; margin-bottom: 1rem;'>🎙️ Voice Mode Active</div>", unsafe_allow_html=True)
        text = get_voice()
        if text:
            input_text = text
            st.success(f"Recognized: {input_text}")
    else:
        # Utilizing st.form fixes submission bugs!
        with st.form("input_form", border=False):
            input_text = st.text_area(
                "Prompt:", 
                placeholder="e.g., 'declare rate equals 5, time equals 10, distance equals rate plus time, print distance'",
                height=120,
                label_visibility="collapsed"
            )
            st.markdown("<br>", unsafe_allow_html=True)
            submit_btn = st.form_submit_button("✨ Generate Code", use_container_width=True)

if input_text and (submit_btn or "Speak" in input_method):
    st.markdown("---")
    
    status_msg = st.empty()
    progress_bar = st.progress(0)
    
    status_msg.info(" **Gemini AI** is interpreting your instruction...")
    ai_response = ai_orchestrator.enhance_speech_output(input_text)
    voca_script = ai_response["enhanced"]
    progress_bar.progress(25)
    time.sleep(0.3)
    
    status_msg.info("**PLY Lexer** is analyzing syntax...")
    lexer.input(voca_script)
    tokens = list(iter(lexer.token, None))
    progress_bar.progress(50)
    time.sleep(0.3)
    
    status_msg.info(" **PLY Parser** is building the syntax tree...")
    parse_tree = parser.parse(voca_script)
    progress_bar.progress(75)
    time.sleep(0.3)
    
    if parse_tree is None:
        status_msg.error(" **Compilation failed! VocaScript syntax error.**")
        st.error(f"Gemini produced invalid syntax: \n```\n{voca_script}\n```")
        progress_bar.progress(100)
    else:
        status_msg.info(" **Generating C Code**...")
        ir = generate_ir(parse_tree)
        c_code = generate_c(ir)
        progress_bar.progress(100)
        status_msg.success("✨ **Compilation Engine Complete!**")
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        tab1, tab2, tab3 = st.tabs([" Result Output", " AI Analysis", " Compiler Pipeline"])
        
        with tab1:
            st.code(c_code, language="c")
            st.download_button("Download Source Code (.c)", data=c_code, file_name="voca.c")
            
        with tab2:
            rc1, rc2 = st.columns(2)
            with rc1:
                st.markdown("##### Detected Intent")
                st.info(ai_response["intent"])
            with rc2:
                st.markdown("##### AI Confidence")
                st.progress(float(ai_response["confidence"]))
                st.caption(f"{float(ai_response['confidence'])*100:.1f}% Confidence Match")
                
            st.markdown("##### AI Context Explanation")
            st.write(ai_response["explanation"])
            
        with tab3:
            st.markdown("##### Strict Intermediary VocaScript")
            st.code(voca_script, language="text")
            
            st.markdown("##### Tuple Abstract Syntax Tree (AST)")
            st.write(parse_tree)
            
            st.markdown("##### Flat Intermediate Representation (IR)")
            st.json(ir)
            