import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


# KONFIGURASI HALAMAN

st.set_page_config(
    page_title="Bike Sharing Dashboard",
    page_icon="🚲",
    layout="wide"
)


# LOAD DATA


@st.cache_data
def load_data():
    return pd.read_csv("data/day.csv")


df = load_data()


# SIDEBAR FILTER

st.sidebar.title("⚙️ Filter Data")

year_option = st.sidebar.selectbox(
    "Pilih Tahun",
    options=df["yr"].unique(),
    format_func=lambda x: "2011" if x == 0 else "2012"
)

season_option = st.sidebar.multiselect(
    "Pilih Musim",
    options=df["season"].unique(),
    default=df["season"].unique()
)

workingday_option = st.sidebar.radio(
    "Jenis Hari",
    options=["Semua", "Hari Kerja", "Hari Libur"]
)


# FILTER DATA

filtered_df = df[
    (df["yr"] == year_option) &
    (df["season"].isin(season_option))
]

if workingday_option == "Hari Kerja":
    filtered_df = filtered_df[filtered_df["workingday"] == 1]
elif workingday_option == "Hari Libur":
    filtered_df = filtered_df[filtered_df["workingday"] == 0]


# HEADER

st.title("🚲 Bike Sharing Dashboard")
st.caption("Dashboard analisis peminjaman sepeda")


# KPI METRICS

st.subheader("📊 Key Performance Indicators")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Peminjaman", f"{filtered_df['cnt'].sum():,}")

with col2:
    st.metric("Rata-rata Harian", f"{int(filtered_df['cnt'].mean()):,}")

with col3:
    st.metric("Hari Tertinggi", f"{filtered_df['cnt'].max():,}")

# VISUALISASI  - CUACA
st.subheader("🌦️ Pengaruh Cuaca")

weather_avg = filtered_df.groupby("weathersit")["cnt"].mean()

fig1, ax1 = plt.subplots()
weather_avg.plot(kind="bar", ax=ax1)
ax1.set_xlabel("Kondisi Cuaca")
ax1.set_ylabel("Rata-rata Peminjaman")
ax1.set_title("Rata-rata Peminjaman berdasarkan Cuaca")

st.pyplot(fig1)


# SUHU & KELEMBAPAN
st.subheader("🌡️ Suhu & 💧 Kelembapan")

col1, col2 = st.columns(2)

with col1:
    avg_temp = filtered_df["temp"].mean()
    st.metric(
        "Rata-rata Suhu",
        f"{avg_temp * 41:.1f} °C"
    )

with col2:
    avg_hum = filtered_df["hum"].mean()
    st.metric(
        "Rata-rata Kelembapan",
        f"{avg_hum * 100:.1f} %"
    )


# VISUALISASI HUBUNGAN

st.subheader("📈 Hubungan Suhu & Kelembapan dengan Peminjaman")

fig3, ax3 = plt.subplots()
ax3.scatter(filtered_df["temp"], filtered_df["cnt"], alpha=0.5, label="Suhu")
ax3.scatter(filtered_df["hum"], filtered_df["cnt"],
            alpha=0.5, label="Kelembapan")
ax3.set_xlabel("Nilai Normalisasi")
ax3.set_ylabel("Jumlah Peminjaman")
ax3.set_title("Pengaruh Suhu & Kelembapan terhadap Peminjaman")
ax3.legend()

st.pyplot(fig3)

# INSIGHT TAMBAHAN

st.info(
    "📌 **Insight:** Peminjaman sepeda cenderung meningkat pada suhu yang lebih hangat, "
    "namun kelembapan tinggi dapat menurunkan minat pengguna."
)


# VISUALISASI  - HARI KERJA VS LIBUR

st.subheader("🏢 Hari Kerja vs Hari Libur")

workday_avg = filtered_df.groupby("workingday")["cnt"].mean()
workday_avg.index = ["Hari Libur", "Hari Kerja"]

fig2, ax2 = plt.subplots()
workday_avg.plot(kind="bar", ax=ax2)
ax2.set_xlabel("Jenis Hari")
ax2.set_ylabel("Rata-rata Peminjaman")
ax2.set_title("Perbandingan Peminjaman")

st.pyplot(fig2)


# INSIGHT
st.subheader("💡 Insight Otomatis")

if weather_avg.idxmax() == 1:
    st.success("Peminjaman tertinggi terjadi saat cuaca cerah.")
else:
    st.info("Cuaca sangat memengaruhi tingkat peminjaman sepeda.")

if workday_avg.idxmax() == 1:
    st.success("Hari kerja mendominasi peminjaman sepeda.")
else:
    st.info("Hari libur menunjukkan pola peminjaman yang berbeda.")


# DATA PREVIEW

with st.expander("🔍 Lihat Data"):
    st.dataframe(filtered_df)
