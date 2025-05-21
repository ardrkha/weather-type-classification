import pandas as pd
import joblib

# Load data test
X_test = pd.read_csv('data\X_test.csv')
y_test = pd.read_csv('data\y_test.csv').squeeze() 

# Load model
model_dict = joblib.load('model_dict.pkl')

# Ambil 1 data untuk prediksi
prediksi = X_test.iloc[:1].copy()
pred_dict = {'y_true': y_test.iloc[0]}

for name, model in model_dict.items():
    hasil_pred = model.predict(prediksi)
    pred_dict['prediksi_' + name] = hasil_pred[0] if hasil_pred.ndim == 1 else hasil_pred[0][0]

# Tampilkan hasil sebagai 1 baris DataFrame
print(pd.DataFrame([pred_dict]))
