import streamlit as st
from PIL import Image
from gtts import gTTS
import os

# Configuración inicial de la página
st.set_page_config(page_title="Lector Accesible - Samuel", layout="centered")

# --- CONTROLES DE ACCESIBILIDAD EN LA BARRA LATERAL ---
st.sidebar.header("⚙️ Ajustes de Accesibilidad")
font_size = st.sidebar.slider("Tamaño del texto (px)", min_value=16, max_value=32, value=22)
high_contrast = st.sidebar.checkbox("Modo Alto Contraste (Fondo Negro / Texto Amarillo)")

# Aplicar estilos CSS personalizados según la configuración seleccionada
if high_contrast:
    bg_color = "#000000"
    text_color = "#FFFF00"
else:
    bg_color = "#0E0D0D"
    text_color = "#E8DFDF"

st.markdown(
    f"""
    <style>
    .stApp {{
        background-color: {bg_color};
        color: {text_color};
    }}
    p, span, label, h1, h2, h3, div {{
        font-size: {font_size}px !important;
        color: {text_color} !important;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# --- INTERFAZ PRINCIPAL ---
st.title("📖 Lector y Descrito Accesible para Samuel")
st.write("Sube una imagen o diagrama del libro de texto:")

# Carga de la imagen del libro
uploaded_file = st.file_uploader("Selecciona una imagen (PNG, JPG, JPEG)", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Página o diagrama cargado", width="stretch")
    
    st.subheader("🤖 Descripción e Interpretación de la IA")
    
    descripcion_ia = (
        "Hola. "
        "En la parte inferior se observa el océano, de donde el agua se evapora con el calor del sol "
        "y sube a la atmósfera formando nubes para luego precipitarse en forma de lluvia."
    )
    
    st.write(descripcion_ia)
    
    # --- BOTÓN DE TEXTO A VOZ (gTTS) ---
    if st.button("🔊 Escuchar descripción en voz alta"):
        with st.spinner("Generando audio para Samuel..."):
            # Crear el archivo de audio usando gTTS
            tts = gTTS(text=descripcion_ia, lang='es', slow=False)
            audio_path = "voz_Samuel.mp3"
            tts.save(audio_path)
            
            # Reproductor de audio integrado en Streamlit
            st.audio(audio_path, format="audio/mp3", autoplay=True)