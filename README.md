# 🚲 Bike Sharing Data Analysis & Dashboard

## 📌 Deskripsi Proyek

Proyek ini bertujuan untuk melakukan **analisis data peminjaman sepeda (Bike Sharing Dataset)** dan menyajikan hasil analisis tersebut dalam bentuk **dashboard interaktif menggunakan Streamlit**.
Dashboard digunakan sebagai media penyampaian insight agar hasil analisis lebih mudah dipahami dan eksploratif.

---

## 📂 Dataset

Dataset yang digunakan adalah **Bike Sharing Dataset (day.csv dan hour.csv)** yang berisi data peminjaman sepeda harian dan perjam dengan berbagai variabel, antara lain:

	- instant: record index
	- dteday : date
	- season : season (1:springer, 2:summer, 3:fall, 4:winter)
	- yr : year (0: 2011, 1:2012)
	- mnth : month ( 1 to 12)
	- hr : hour (0 to 23)
	- holiday : weather day is holiday or not (extracted from http://dchr.dc.gov/page/holiday-schedule)
	- weekday : day of the week
	- workingday : if day is neither weekend nor holiday is 1, otherwise is 0.
	+ weathersit : 
		- 1: Clear, Few clouds, Partly cloudy, Partly cloudy
		- 2: Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist
		- 3: Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds
		- 4: Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog
	- temp : Normalized temperature in Celsius. The values are divided to 41 (max)
	- atemp: Normalized feeling temperature in Celsius. The values are divided to 50 (max)
	- hum: Normalized humidity. The values are divided to 100 (max)
	- windspeed: Normalized wind speed. The values are divided to 67 (max)
	- casual: count of casual users
	- registered: count of registered users
	- cnt: count of total rental bikes including both casual and registered
  
Dataset disimpan pada folder:

```
data/day.csv dan data/hour.csv
```

---

## ▶️ Cara Menjalankan Proyek

### 1️⃣ Menjalankan Notebook

Notebook digunakan untuk proses:

* data understanding
* data cleaning
* exploratory data analysis (EDA)
* penarikan insight

Langkah:

```bash
pip install pandas matplotlib
```

Lalu buka notebook:

```
ML_[Muhammad Zacky Alan Fernando].ipynb
```

menggunakan Jupyter Notebook atau JupyterLab.

---

### 2️⃣ Menjalankan Dashboard Streamlit

Dashboard digunakan untuk menyajikan hasil analisis secara interaktif.
### Melalui Local Environment

#### Install dependencies:

```bash
pip install -r requirements.txt
```

#### Jalankan dashboard:

```bash
streamlit run app.py
```

Dashboard akan terbuka otomatis di browser pada:

```
http://localhost:8501
```

---

## Akses secara Online
```
https://bike-sharing-6yicciravmyumqfdjg6drn.streamlit.app/
```


## 📊 Ringkasan Insight Hasil Analisis

Beberapa insight utama yang diperoleh dari analisis data antara lain:

* **Cuaca memiliki pengaruh signifikan** terhadap jumlah peminjaman sepeda, di mana peminjaman tertinggi terjadi saat kondisi cuaca cerah.
* **Hari kerja memiliki rata-rata peminjaman lebih tinggi** dibandingkan hari libur, menunjukkan sepeda digunakan sebagai sarana transportasi rutin.
* **Suhu yang lebih hangat cenderung meningkatkan peminjaman**, namun kelembapan yang terlalu tinggi dapat menurunkan minat pengguna.
* Pola peminjaman menunjukkan tren yang relatif stabil pada kondisi cuaca dan hari tertentu.

---

## 🛠️ Teknologi yang Digunakan

* Python
* Pandas
* Matplotlib
* Streamlit
* GitHub

---

## 👤 Author

**Muhammad Zacky Alan Fernando**
Project ini dibuat sebagai bagian dari tugas analisis data dan pengembangan dashboard interaktif.

---


Tinggal bilang mau versi yang mana 😄
