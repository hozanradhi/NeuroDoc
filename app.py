import streamlit as st
import google.generativeai as genai

st.title("🔎 Modell-detektiven")

try:
    # Hämta nyckeln från kassaskåpet
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    
    st.write("Här är de modeller din nyckel har tillgång till:")
    
    # Skriv ut alla modeller
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            st.write(f"- `{m.name}`")
            
except Exception as e:
    st.error("Något gick fel:")
    st.write(e)
