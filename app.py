import streamlit as st
import google.generativeai as genai
import re

# --- KONFIGURASI HALAMAN ---
st.set_page_config(page_title="AI YouTube Optimizer", page_icon="📈", layout="wide")

# --- UI: BILAH SAMPING (SIDEBAR) ---
st.sidebar.title("⚙️ Pengaturan Akses")
api_key = st.sidebar.text_input("Masukkan API Key Gemini:", type="password")
if api_key:
    genai.configure(api_key=api_key)
st.sidebar.markdown("---")
st.sidebar.markdown("*API Key Anda diproses secara lokal di sesi ini dan tidak disimpan di server/database mana pun. Aman untuk repositori publik.*")

# --- UI: AREA UTAMA ---
st.title("📈 AI YouTube Title & SEO Optimizer")
st.markdown("Sempurnakan pengemasan visual dan teks video Anda setelah merakit *opening sequence* 30-60 detik beserta transisi logo. Pastikan CTR dan SEO sepadan dengan kualitas *editing* di dalamnya.")
st.markdown("---")

col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("Data Target")
    channel_choice = st.selectbox(
        "Pilih Channel YouTube:",
        ("Suara Filsuf", "Tutur Kyai", "Nalar Senyap")
    )
    old_title = st.text_input("Judul Lama / Draft Judul:", placeholder="Contoh: Penjelasan Stoikisme...")
    
    input_mode = st.radio(
        "Metode Input Materi:",
        ("Konteks Singkat (Manual)", "Transkrip Lengkap (Copy-Paste)")
    )

with col2:
    st.subheader("Materi Konten")
    if input_mode == "Konteks Singkat (Manual)":
        video_content = st.text_area("Jelaskan isi/sudut pandang video:", height=130, placeholder="Misal: Fokus pada rasa lelah bekerja dan bagaimana filsafat melihatnya...")
        prompt_instruction = "Gunakan ringkasan ini sebagai acuan materi:"
    else:
        video_content = st.text_area("Paste seluruh transkrip video di sini:", height=130, placeholder="Paste teks lengkap di sini agar AI tidak mengarang bebas...")
        prompt_instruction = "Gunakan transkrip ini sebagai acuan mutlak (jangan berhalusinasi di luar transkrip):"

# --- LOGIKA SYSTEM PROMPT & DNA CHANNEL ---
def get_system_prompt(channel):
    base_instruction = """
    Kamu adalah Pakar YouTube SEO & Copywriter. Analisis input dan berikan output dalam format tag XML ketat berikut ini:
    
    <JUDUL>
    [Tuliskan analisis singkat mengapa judul lama lemah, lalu berikan 3 opsi judul baru. WAJIB hitung karakter tiap judul dan cantumkan di akhir (contoh: "... (60 Karakter)"). Batas maksimal 70 karakter!]
    </JUDUL>
    
    <THUMBNAIL>
    [Berikan deskripsi visual thumbnail yang kontras dan teks thumbnail maksimal 4 kata]
    </THUMBNAIL>
    
    <SEO>
    [Tuliskan 2 paragraf deskripsi YouTube SEO-friendly, daftar kata kunci (tags), dan 5 hashtag]
    </SEO>
    """
    
    if channel == "Suara Filsuf":
        rules = """
        ATURAN SUARA FILSUF: Bahasa reflektif. Wajib sebut nama tokoh jika relevan. Pakai struktur 'X, Tapi Y'. LARANGAN: JANGAN tulis nama 'Dr. Fahruddin Faiz' di judul/deskripsi manapun. Batas 70 karakter.
        """
    elif channel == "Tutur Kyai":
        rules = """
        ATURAN TUTUR KYAI: Bahasa santun & menyejukkan. Fokus hikmah Islam. LARANGAN: Dilarang menakut-nakuti soal azab.
        """
    else:
        rules = """
        ATURAN NALAR SENYAP: Bahasa personal
