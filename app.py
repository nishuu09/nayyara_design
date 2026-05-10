import streamlit as st
import pandas as pd
import urllib.parse
import base64
import os

# ==========================================
# 1. PENGATURAN HALAMAN
# ==========================================
st.set_page_config(page_title="Nayyara Design - Custom Interior", page_icon="🛋️", layout="wide")

# ==========================================
# 2. FUNGSI UTILITAS & DATA (ADVANCE)
# ==========================================
def format_rupiah(angka):
    """Fungsi agar format uang seragam di seluruh aplikasi"""
    return f"Rp {angka:,.0f}".replace(",", ".")

def get_local_image(image_filename):
    """Memuat gambar lokal murni dengan Absolute Path agar terbaca di Codespaces"""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(current_dir, image_filename)
    
    if os.path.exists(image_path):
        with open(image_path, "rb") as img_file:
            ext = image_filename.split('.')[-1].lower()
            mime_type = "jpeg" if ext in ["jpg", "jpeg"] else ext
            return f"data:image/{mime_type};base64,{base64.b64encode(img_file.read()).decode()}"
    return "" 

def load_katalog():
    """Mengambil gambar dari folder lokal beserta Spesifikasi Lengkap"""
    data = [
        {
            "Nama": "Lemari Pakaian Minimalis", "Kategori": "Lemari Custom", "Harga": 3500000, 
            "Gambar": get_local_image("katalog_1.jpeg"),
            "Spesifikasi": "**Bahan:** Multiplek Premium 18mm\n**Finishing:** HPL Anti Gores (Solid/Woodgrain)\n**Aksesoris:** Engsel Slow Motion (Tutup perlahan), Rel Laci Tandem\n**Dimensi Standar:** P 120cm x T 200cm x L 55cm\n**Keunggulan:** Desain minimalis tanpa handle luar (finger groove), dilengkapi laci rahasia berenkripsi gembok."
        },
        {
            "Nama": "Kitchen Set Scandinavian", "Kategori": "Kitchen Set", "Harga": 8500000, 
            "Gambar": get_local_image("katalog_2.jpeg"),
            "Spesifikasi": "**Bahan Kabinet:** Blockboard 18mm (Tahan lembab)\n**Finishing Kabinet:** HPL kombinasi Putih Doff & Kayu Terang\n**Top Table (Meja):** Solid Surface putih / Granit Hitam\n**Dimensi:** Harga untuk ukuran standar lurus 2,5 meter.\n**Bonus:** Sudah termasuk rak piring tarik stenlis, rak sendok, dan laci bumbu."
        },
        {
            "Nama": "Meja Kerja Kayu Jati", "Kategori": "Meja & Kursi", "Harga": 1200000, 
            "Gambar": get_local_image("katalog_3.jpeg"),
            "Spesifikasi": "**Bahan Top Meja:** Kayu Jati Solid / Multiplek Lapis Melamik Jati\n**Kaki Meja:** Besi Hollow tebal gaya Industrial (Dicat Powder Coating Anti Karat)\n**Dimensi:** P 120cm x L 60cm x T 75cm\n**Fitur:** Dilengkapi lubang kabel (grommet) dan laci gantung tipis untuk alat tulis."
        },
        {
            "Nama": "Rak TV Industrial", "Kategori": "Lainnya", "Harga": 2100000, 
            "Gambar": get_local_image("katalog_4.jpeg"),
            "Spesifikasi": "**Bahan Rangka:** Besi Hollow Hitam Doff\n**Bahan Ambalan:** Multiplek 15mm Finishing HPL Motif Kayu Natural\n**Dimensi:** P 160cm x L 40cm x T 55cm\n**Kekuatan:** Mampu menahan beban TV LED hingga 65 inch dan perangkat sound system."
        },
        {
            "Nama": "Kabinet Sepatu Elegan", "Kategori": "Lemari Custom", "Harga": 1800000, 
            "Gambar": get_local_image("katalog_5.jpeg"),
            "Spesifikasi": "**Bahan:** Multiplek 15mm\n**Finishing:** HPL Motif Serat Kayu Gelap / Duco Putih\n**Kapasitas:** Mampu menampung 15 - 20 pasang sepatu/sandal.\n**Fitur Khusus:** Terdapat celah sirkulasi udara tersembunyi agar sepatu tidak bau/berjamur, dan rak miring untuk memudahkan pengambilan."
        },
        {
            "Nama": "Kitchen Island Marble", "Kategori": "Kitchen Set", "Harga": 5500000, 
            "Gambar": get_local_image("katalog_6.jpeg"),
            "Spesifikasi": "**Top Table:** Marmer Sintetis / Granit kualitas Premium\n**Bahan Kabinet:** Blockboard 18mm\n**Finishing:** Cat Duco Glossy / HPL Mewah\n**Dimensi:** P 150cm x L 80cm x T 85cm\n**Fungsi:** Sangat cocok untuk area potong makanan, mini bar, atau meja sarapan dadakan."
        },
        {
            "Nama": "Set Meja Makan Premium", "Kategori": "Meja & Kursi", "Harga": 4500000, 
            "Gambar": get_local_image("katalog_7.jpeg"),
            "Spesifikasi": "**Bahan Meja:** Kayu Mahoni/Jati finishing Natural Halus\n**Set Isi:** 1 Meja Makan + 4 Kursi Makan Nyaman\n**Bahan Kursi:** Rangka kayu kokoh dengan sandaran empuk dilapisi kain Fabric Premium / Oscar tahan air.\n**Dimensi Meja:** 140cm x 80cm."
        },
        {
            "Nama": "Backdrop TV HPL", "Kategori": "Lainnya", "Harga": 3200000, 
            "Gambar": get_local_image("katalog_8.jpeg"),
            "Spesifikasi": "**Bahan Panel Utama:** Multiplek 15mm lapis HPL Motif Marmer\n**Aksen:** Kisi-kisi kayu (Fluted Panel WPC)\n**Dimensi:** Menyesuaikan ukuran ruang TV (Harga start dari luasan 2x2 meter)\n**Fitur:** Bracket TV gantung tersembunyi, jalur kabel tak terlihat, dan efek lampu LED Strip Warm White."
        }
    ]
    return pd.DataFrame(data)

df_katalog = load_katalog()

# ==========================================
# 3. POP-UP DIALOG SPESIFIKASI (FITUR BARU)
# ==========================================
@st.dialog("📖 Detail Spesifikasi Produk")
def pop_up_spesifikasi(nama, kategori, harga, gambar, spesifikasi):
    # Desain Isi Pop-up
    st.markdown(f"<h3 style='color:#8B5E3C; margin-bottom:5px;'>{nama}</h3>", unsafe_allow_html=True)
    st.markdown(f"<p style='color:#888; font-size:14px; margin-top:-10px;'>Kategori: {kategori}</p>", unsafe_allow_html=True)
    
    if gambar:
        st.markdown(f'<img src="{gambar}" style="width:100%; border-radius:12px; margin-bottom:15px; border:1px solid #eee;">', unsafe_allow_html=True)
    else:
        st.info("Gambar lokal belum tersedia.")
        
    st.markdown("#### Detail Material:")
    st.markdown(spesifikasi)
    
    st.divider()
    st.markdown(f"**Estimasi Harga:** <span style='font-size:24px; color:#8B5E3C; font-weight:900;'>{format_rupiah(harga)}</span>", unsafe_allow_html=True)
    
    # Tombol WA di dalam Pop-up
    pesan = f"Halo Nayyara Design, saya sudah membaca spesifikasinya dan tertarik memesan *{nama}* seharga {format_rupiah(harga)}."
    link_wa = f"https://wa.me/6281380008637?text={urllib.parse.quote(pesan)}"
    st.link_button("✨ Pesan Langsung via WhatsApp", link_wa, use_container_width=True)

# ==========================================
# 4. MEGA CSS DENGAN ANIMASI LENGKAP & FIX LAYOUT
# ==========================================
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700;800&display=swap');
    
    * { font-family: 'Poppins', sans-serif; }
    .block-container { padding-top: 0rem !important; max-width: 100% !important; }
    .stApp { background-color: #FAFAFA; color: #3E362E; }

    /* ============ FLOATING ELEMENTS (Orb Animasi) ============ */
    .floating-element {
        position: fixed; width: 150px; height: 150px; border-radius: 50%;
        background: linear-gradient(135deg, rgba(139, 94, 60, 0.15), rgba(218, 165, 32, 0.1));
        filter: blur(40px); animation: float 8s ease-in-out infinite; pointer-events: none; z-index: 0;
    }
    @keyframes float { 0%, 100% { transform: translateY(0) rotate(0deg); } 50% { transform: translateY(-30px) rotate(180deg); } }

    /* ============ NAVBAR ============ */
    .nav-title { font-size: 32px; font-weight: 800; color: #8B5E3C; margin-top: 5px; text-shadow: 1px 1px 2px rgba(0,0,0,0.1); }
    
    /* Modifikasi Tombol Streamlit Native */
    .stButton>button, .stLinkButton>a {
        background: linear-gradient(135deg, #8B5E3C, #5C4033) !important;
        color: white !important; border-radius: 12px !important; border: none !important;
        padding: 10px 24px !important; font-weight: 700 !important;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;
        width: 100%; text-align: center; text-decoration: none;
    }
    .stButton>button:hover, .stLinkButton>a:hover {
        transform: translateY(-5px) scale(1.02) !important; box-shadow: 0 10px 20px rgba(139, 94, 60, 0.4) !important;
    }

    [data-testid="stLinkButton"] { display: flex !important; justify-content: center !important; }
    [data-testid="stLinkButton"] p { text-align: center !important; margin: auto !important; width: 100% !important; display: flex; justify-content: center; align-items: center; }

    /* ============ HERO BANNER ANIMASI ============ */
    .hero-section {
        background: linear-gradient(-45deg, #2D1A11, #4A2E1B, #8B5E3C, #5C4033);
        background-size: 400% 400%; animation: gradientShift 15s ease infinite;
        padding: 80px 20px; text-align: center; position: relative; overflow: hidden;
        border-radius: 16px; margin-top: 10px; box-shadow: 0 15px 35px rgba(0,0,0,0.2); z-index: 1;
    }
    @keyframes gradientShift { 0% { background-position: 0% 50%; } 50% { background-position: 100% 50%; } 100% { background-position: 0% 50%; } }
    
    .hero-section::before {
        content: ''; position: absolute; top: 0; left: 0; right: 0; bottom: 0;
        background-image: radial-gradient(2px 2px at 20px 30px, rgba(255,215,0,0.8), transparent), radial-gradient(2px 2px at 40px 70px, rgba(245,245,220,0.8), transparent), radial-gradient(2px 2px at 50px 160px, rgba(210,180,140,0.8), transparent), radial-gradient(3px 3px at 160px 120px, rgba(255,255,255,0.6), transparent);
        background-repeat: repeat; background-size: 200px 200px; animation: sparkle 15s linear infinite; opacity: 0.6;
    }
    @keyframes sparkle { 0% { transform: translateY(0); } 100% { transform: translateY(-200px); } }
    
    .hero-title {
        font-size: 60px !important; font-weight: 800; background: linear-gradient(90deg, #F5F5DC, #FFD700, #FFF8DC, #F5F5DC);
        background-size: 300% 300%; -webkit-background-clip: text; -webkit-text-fill-color: transparent; animation: textGlow 4s ease infinite; margin-bottom: 10px; position: relative; z-index: 2;
    }
    @keyframes textGlow { 0%, 100% { background-position: 0% 50%; filter: drop-shadow(0 0 15px rgba(255,215,0,0.3)); } 50% { background-position: 100% 50%; filter: drop-shadow(0 0 25px rgba(255,255,255,0.5)); } }
    
    .hero-subtitle { font-size: 20px; color: rgba(255,255,255,0.9); position: relative; z-index: 2; animation: fadeInUp 1s ease; }
    @keyframes fadeInUp { from { opacity: 0; transform: translateY(30px); } to { opacity: 1; transform: translateY(0); } }

    /* ============ SCROLLING HEADLINE ============ */
    .scrolling-container { width: 100%; overflow: hidden; background-color: #8B5E3C; color: white; padding: 12px 0; border-radius: 8px; margin-bottom: 30px; margin-top: 15px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); z-index: 1; position: relative; }
    .scrolling-text { display: inline-block; white-space: nowrap; animation: scroll-left 25s linear infinite; font-weight: 600; font-size: 15px; letter-spacing: 1px; }
    @keyframes scroll-left { 0% { transform: translateX(100%); } 100% { transform: translateX(-100%); } }

    /* ============ PRODUCT CARDS ANIMATION ============ */
    .anim-card { background: white; border-radius: 16px; overflow: hidden; transition: all 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275); box-shadow: 0 4px 15px rgba(0,0,0,0.05); border: 1px solid #EBEBEB; margin-bottom: 15px; height: 350px; display: flex; flex-direction: column; }
    .anim-card:hover { transform: translateY(-10px); box-shadow: 0 20px 40px rgba(139, 94, 60, 0.15); border-color: #8B5E3C; }
    .anim-img-box { width: 100%; height: 180px; min-height: 180px; background-color: #EBEBEB; overflow: hidden; position: relative; }
    .anim-img-box img { width: 100%; height: 100%; object-fit: cover; transition: transform 0.6s ease; }
    .anim-card:hover .anim-img-box img { transform: scale(1.1) rotate(2deg); }
    .anim-info { padding: 15px; text-align: center; display: flex; flex-direction: column; flex-grow: 1; justify-content: space-between; }
    .anim-title { font-size: 16px; font-weight: 700; color: #3E362E; margin-bottom: 5px; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden; }
    .anim-price { font-size: 20px; font-weight: 800; color: #8B5E3C; margin-top: auto; }

    /* Gambar Configurator Frame */
    .configurator-frame { border-radius: 16px; padding: 8px; background: linear-gradient(135deg, #EBEBEB, #FAFAFA); box-shadow: inset 0 2px 10px rgba(0,0,0,0.05), 0 10px 30px rgba(139, 94, 60, 0.2); overflow: hidden; }
    .configurator-frame img { border-radius: 12px; width: 100%; height: 500px; object-fit: cover; object-position: center; transition: opacity 0.3s ease-in-out; }

    #MainMenu, footer, header { visibility: hidden; }
    </style>
    
    <div class="floating-element" style="top: 20%; left: 5%;"></div>
    <div class="floating-element" style="top: 60%; right: 10%; animation-delay: -4s;"></div>
""", unsafe_allow_html=True)

# ==========================================
# 5. NAVIGATION BAR (Telah Dirapikan)
# ==========================================
# Kolom "Layanan Kami" dihapus, rasio diubah agar rapi
col_logo, col_space, col_kontak = st.columns([5, 2.5, 1.5])

with col_logo:
    st.markdown('<div class="nav-title">Nayyara Design</div>', unsafe_allow_html=True)

with col_space:
    st.empty() 

with col_kontak:
    pesan_halo = "Halo Nayyara Design, saya ingin konsultasi mengenai desain interior."
    link_wa_kontak = f"https://wa.me/6281380008637?text={urllib.parse.quote(pesan_halo)}"
    st.link_button("📞 Kontak Kami", link_wa_kontak, use_container_width=True)

# ==========================================
# 6. HERO BANNER ANIMASI & SCROLLING TEXT
# ==========================================
st.markdown("""
    <div class="hero-section">
        <h1 class="hero-title">Wujudkan Ruangan Impian.</h1>
        <p class="hero-subtitle">Spesialis Custom Lemari, Kitchen Set, dan Desain Interior Estetik.</p>
    </div>
""", unsafe_allow_html=True)

st.markdown("""
    <div class="scrolling-container">
        <div class="scrolling-text">
            ✨ PROMO SPESIAL: Gratis Biaya Survei dan Pengukuran untuk Area Bogor dan Sekitarnya! | 🛠️ Diskon 10% untuk Pemesanan Kitchen Set Custom Bulan Ini | 📱 Konsultasi Desain Interior Gratis via WhatsApp ✨
        </div>
    </div>
""", unsafe_allow_html=True)

# ==========================================
# 7. TABS APLIKASI
# ==========================================
tab_toko, tab_kalkulator, tab_customizer = st.tabs([
    "🛍️ Katalog Produk", 
    "🧮 Kalkulator Standar", 
    "🛠️ Customizer Furnitur 360"
])

# --- TAB 1: KATALOG PRODUK ---
with tab_toko:
    st.subheader("Koleksi Ready Stock & Inspirasi Desain")
    col_filter = st.columns(3)
    with col_filter[0]:
        kata_kunci = st.text_input("🔍 Cari produk...", placeholder="Misal: Lemari Minimalis")
    with col_filter[1]:
        pilihan_kategori = st.selectbox("Kategori", ["Semua Kategori", "Lemari Custom", "Kitchen Set", "Meja & Kursi", "Lainnya"])
    
    st.divider()
    
    df_tampil = df_katalog.copy()
    if kata_kunci:
        df_tampil = df_tampil[df_tampil['Nama'].str.contains(kata_kunci, case=False, na=False)]
    if pilihan_kategori != "Semua Kategori":
        df_tampil = df_tampil[df_tampil['Kategori'] == pilihan_kategori]
    
    if df_tampil.empty:
        st.warning("Produk tidak ditemukan.")
    else:
        kolom_produk = st.columns(4)
        for indeks, baris in df_tampil.reset_index().iterrows():
            with kolom_produk[indeks % 4]:
                img_src_html = f'<img src="{baris["Gambar"]}" alt="{baris["Nama"]}">' if baris["Gambar"] else '<div style="width:100%; height:100%; background-color:#ccc; display:flex; align-items:center; justify-content:center; color:#666;">No Image</div>'
                
                card_html = f"""
                <div class="anim-card">
                    <div class="anim-img-box">
                        {img_src_html}
                    </div>
                    <div class="anim-info">
                        <div>
                            <div class="anim-title">{baris['Nama']}</div>
                            <div style="font-size:12px; color:#888; margin-bottom:5px;">🏷️ {baris['Kategori']}</div>
                        </div>
                        <div class="anim-price">{format_rupiah(baris['Harga'])}</div>
                    </div>
                </div>
                """
                st.markdown(card_html, unsafe_allow_html=True)
                
                # TOMBOL POP-UP SPESIFIKASI
                if st.button("🔍 Lihat Spesifikasi", key=f"btn_spec_{indeks}", use_container_width=True):
                    pop_up_spesifikasi(baris['Nama'], baris['Kategori'], baris['Harga'], baris['Gambar'], baris['Spesifikasi'])
                
                # Tombol WA langsung (opsional, jika ingin double button)
                # pesan = f"Halo Nayyara Design, saya tertarik dengan produk {baris['Nama']} seharga {format_rupiah(baris['Harga'])} di katalog."
                # link_wa = f"https://wa.me/6281380008637?text={urllib.parse.quote(pesan)}"
                # st.link_button("🛒 Pesan", link_wa, use_container_width=True)

# --- TAB 2: KALKULATOR STANDAR ---
with tab_kalkulator:
    st.subheader("Hitung Cepat Biaya Furnitur")
    col_input, col_hasil = st.columns([1.5, 1])
    
    with col_input:
        col_p, col_t = st.columns(2)
        with col_p:
            panjang_std = st.number_input("Panjang (meter):", min_value=0.0, step=0.1, value=2.0)
        with col_t:
            tinggi_std = st.number_input("Tinggi (meter):", min_value=0.0, step=0.1, value=2.0)
            
        material_dasar_std = st.selectbox("Bahan Dasar:", ["Multiplek Premium - Rp 1.500.000/m²", "Blockboard - Rp 1.300.000/m²", "PVC Board - Rp 2.000.000/m²"])
        finishing_std = st.selectbox("Jenis Finishing:", ["HPL (Praktis) - Rp 500.000/m²", "Duco (Mewah) - Rp 1.200.000/m²", "Melamik (Serat Kayu) - Rp 800.000/m²"])

    with col_hasil:
        harga_dasar_std = int(material_dasar_std.split("Rp ")[1].replace(".", "").replace("/m²", ""))
        harga_finishing_std = int(finishing_std.split("Rp ")[1].replace(".", "").replace("/m²", ""))
        luas_std = panjang_std * tinggi_std
        total_harga_std = luas_std * (harga_dasar_std + harga_finishing_std)
        
        st.metric("Luas Total", f"{luas_std:.2f} m²")
        st.metric("Estimasi Biaya", format_rupiah(total_harga_std))
        
        pesan_wa_std = f"Halo Nayyara Design, saya minta estimasi furnitur {panjang_std}m x {tinggi_std}m bahan {material_dasar_std.split(' -')[0]} finishing {finishing_std.split(' -')[0]}. Estimasi: {format_rupiah(total_harga_std)}."
        st.link_button("📱 Ajukan Desain via WA", f"https://wa.me/6281380008637?text={urllib.parse.quote(pesan_wa_std)}", use_container_width=True)

# --- TAB 3: CUSTOMIZER FURNITUR 360 ---
with tab_customizer:
    st.subheader("🛠️ Bangun Furnitur Impianmu")
    st.write("Sesuaikan ukuran, material, dan warna untuk melihat bayangan desainnya secara langsung.")
    st.divider()

    col_vis1, col_vis2 = st.columns([1.2, 1.8], gap="large")

    with col_vis1:
        st.markdown("<h4 style='color:#8B5E3C;'>1. Spesifikasi Bentuk</h4>", unsafe_allow_html=True)
        vis_tipe = st.selectbox("Pilih Tipe Furnitur:", ["Lemari Pakaian", "Kitchen Set"])
        
        col_v1, col_v2, col_v3 = st.columns(3)
        with col_v1: vis_panjang = st.number_input("Panjang (m)", value=4.0, step=0.1)
        with col_v2: vis_tinggi = st.number_input("Tinggi (m)", value=2.0, step=0.1)
        with col_v3: vis_lebar = st.number_input("Kedalaman (m)", value=0.6, step=0.1)

        st.markdown("<h4 style='color:#8B5E3C; margin-top:20px;'>2. Material & Visual</h4>", unsafe_allow_html=True)
        vis_bahan = st.selectbox(
            "Finishing & Tekstur:", 
            ["HPL Solid (Halus Modern)", "HPL Woodgrain (Serat Kayu)", "Cat Duco (Glossy/Mewah)"]
        )
        
        vis_warna = st.radio(
            "Nuansa Warna Dominan:", 
            ["Putih Bersih / Cerah", "Abu-abu / Hitam Elegan", "Kayu Terang (Oak)", "Kayu Gelap (Walnut)"]
        )

    with col_vis2:
        img_url = ""
        
        if vis_tipe == "Lemari Pakaian":
            if "Putih" in vis_warna: img_url = get_local_image("lemari_putih.jpeg")
            elif "Abu-abu" in vis_warna: img_url = get_local_image("lemari_hitam.jpeg")
            elif "Terang" in vis_warna: img_url = get_local_image("lemari_oak.jpeg")
            else: img_url = get_local_image("lemari_walnut.jpeg")
                
        elif vis_tipe == "Kitchen Set":
            if "Putih" in vis_warna: img_url = get_local_image("kitchen_putih.jpeg")
            elif "Abu-abu" in vis_warna: img_url = get_local_image("kitchen_hitam.jpeg")
            elif "Terang" in vis_warna: img_url = get_local_image("kitchen_oak.jpeg")
            else: img_url = get_local_image("kitchen_walnut.jpeg")

        vis_img_html = f'<img src="{img_url}" alt="Visualisasi Furnitur">' if img_url else '<div style="width:100%; height:100%; background-color:#ccc; display:flex; align-items:center; justify-content:center; color:#666; font-size:18px;">Menunggu Gambar Lokal...</div>'

        st.markdown(f"""
        <div style="text-align:center; margin-bottom:10px; font-weight:600; color:#666;">
            Visualisasi: {vis_tipe} - {vis_warna}
        </div>
        <div class="configurator-frame">
            {vis_img_html}
        </div>
        """, unsafe_allow_html=True)
        
        harga_per_m2 = 1800000 if "Solid" in vis_bahan else 2000000 if "Woodgrain" in vis_bahan else 2500000
        luas_muka = vis_panjang * vis_tinggi
        estimasi_custom = luas_muka * harga_per_m2

        st.markdown("<br>", unsafe_allow_html=True)
        col_res1, col_res2 = st.columns(2)
        with col_res1:
            st.metric("Total Luas Muka", f"{luas_muka:.2f} m²")
        with col_res2:
            st.metric(f"Estimasi {vis_bahan}", format_rupiah(estimasi_custom))

        pesan_custom = f"Halo Nayyara Design, saya sudah cek Visualisator di Website.\n\nSaya ingin memesan:\n- Jenis: {vis_tipe}\n- Ukuran: P {vis_panjang}m x T {vis_tinggi}m x Kedalaman {vis_lebar}m\n- Material: {vis_bahan}\n- Warna: {vis_warna}\n\nEstimasi harga di web {format_rupiah(estimasi_custom)}. Tolong bantu survey ya!"
        wa_custom = f"https://wa.me/6281380008637?text={urllib.parse.quote(pesan_custom)}"
        st.link_button("✨ Pesan Desain Ini Sekarang", wa_custom, use_container_width=True)