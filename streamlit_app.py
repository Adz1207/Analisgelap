import streamlit as st
from google import genai  # Library baru

# --- BAGIAN INISIALISASI DI DALAM BUTTON ---
if st.button("GENERATE STRATEGY"):
    if not user_api_key:
        st.error("API Key wajib diisi.")
    else:
        try:
            # Inisialisasi Client dengan Library Baru
            client = genai.Client(api_key=user_api_key)
            
            with st.spinner("Menganalisis kegagalan logika Anda..."):
                # Pemanggilan Model (Syntax Baru)
                response = client.models.generate_content(
                    model="gemini-2.0-flash", # Gunakan model terbaru jika tersedia
                    contents=final_prompt
                )
                
                st.divider()
                # Tampilkan teks hasil
                st.markdown(response.text)
