
# Laporan Proyek Machine Learning - Hardatama Rakha Ugraha




## Domain Proyek

**Latar Belakang :**

Cuaca memainkan peran penting dalam berbagai aspek kehidupan manusia, mulai dari perencanaan kegiatan harian hingga sektor industri seperti pertanian, transportasi, dan pariwisata. Kemampuan untuk memprediksi jenis cuaca secara akurat memungkinkan pengambilan keputusan yang lebih baik dan lebih efisien. Salah satu pendekatan yang umum digunakan untuk mendukung prediksi cuaca adalah melalui pemanfaatan algoritma machine learning.

\
**Mengapa dan Bagaimana Masalah Ini Harus Diselesaikan?**

Prediksi tipe cuaca yang akurat bisa menjadi komponen penting dalam sistem peringatan dini atau aplikasi mobil cuaca. Menyelesaikan masalah ini akan melibatkan beberapa tahap seperti eksplorasi data, pemilihan model, validasi, dan evaluasi dengan metrik yang tepat. Penyelesaian masalah ini juga menjadi sarana pembelajaran praktik terbaik dalam proyek machine learning nyata.

Menurut [Kowalski & Keeling, 2020], penggunaan machine learning untuk klasifikasi cuaca telah terbukti efektif dalam berbagai studi dan memungkinkan generalisasi yang lebih baik dibandingkan metode statistik tradisional.

> Referensi:
> Kowalski, J., & Keeling, R. (2020). Weather Classification with Machine Learning: A Review. International Journal of Climatology.
> DOI: https://doi.org/10.1002/joc.6510
## Business Understanding

**Problem Statements:**

1. Bagaimana cara mengklasifikasikan kondisi cuaca berdasarkan fitur-fitur seperti suhu, kelembaban, tekanan udara, dan lainnya?
2. Fitur apa saja yang berpengaruh dalam menentukan kondisi cuaca?

\
**Goals:**
1. Membangun model klasifikasi yang mampu memprediksi tipe cuaca (Rainy, Sunny, Cloudy, Snowy) berdasarkan input fitur cuaca.
2. Menerapkan teknik encoding lalu menggunakan correlation matrix untuk menilai seberapa berpengaruh fitur-fitur tersebut dengan fitur target.

\
**Solution Statements:**
1. Menggunakan beberapa algoritma machine learning untuk membandingkan performa klasifikasi, yaitu:
- K-Nearest Neighbors
- Decision Tree
- Random Forest
- AdaBoost
- Naive Bayes
2. Metrik evaluasi yang digunakan meliputi:
- Akurasi
- Presisi
- Recall
- F1-Score
- Confusion Matrix
## Data Understanding
Dataset yang digunakan bersifat sintetis dan tersedia dari platform Kaggle. Dataset terdiri dari 13200 baris yang mencakup berbagai fitur terkait cuaca dan mengkategorikan cuaca menjadi empat jenis: Rainy, Sunny, Cloudy, and Snowy.

Sumber dataset: https://www.kaggle.com/datasets/nikhil7280/weather-type-classification


**Fitur-fitur pada Dataset:**
| Fitur | Tipe | Deskripsi |
| ------ | ------ | ------ |
| Temperature | Numerik	| Suhu dalam °C (rentang luas: sangat dingin hingga sangat panas)|
|Humidity	| Numerik	|Kelembaban dalam % (termasuk >100% sebagai outlier)|
|Wind Speed	|Numerik|	Kecepatan angin dalam km/jam (mengandung nilai ekstrem/outlier)|
|Precipitation (%)|	Numerik|	Curah hujan dalam % (mengandung nilai ekstrem/outlier)|
|Cloud Cover	|Kategorikal	|Deskripsi tingkat tutupan awan (misal: clear, partly cloudy, overcast)|
|Atmospheric Pressure|	Numerik	|Tekanan udara dalam hPa (rentang luas)|
|UV Index	|Numerik|	Indeks radiasi UV|
|Season|	Kategorikal|	Musim saat data diambil (Spring, Summer, Autumn, Winter)|
|Visibility (km)	|Numerik|	Jarak pandang dalam km (bisa sangat rendah atau sangat tinggi)|
|Location	|Kategorikal|	Jenis lokasi (urban, rural, coastal, mountain, dll)|
|Weather Type	|Kategorikal|	Target klasifikasi: Rainy, Sunny, Cloudy, Snowy|

## Usage

1. Create Environment
```bash
python -m venv env
source env/bin/activate  # Linux/macOS
env\Scripts\activate     # Windows
```
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Open and run the notebook:
- Use Jupyter Notebook or JupyterLab to open the `notebook.ipynb` file.
- Run all cells to train the model.
## Contact

If you have any questions, feel free to reach out to us at hardatama27@gmail.com.

Developed by Hardatama Rakha Ugraha - 2025