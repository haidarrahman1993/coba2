import pickle
import pandas as pd
import streamlit as st
from Interface import dept_con
from Interface import work_acc
from Interface import promote

model = pickle.load(open('model_ds.pkl', 'rb'))

st.title('PREDIKSI GAJI KARYAWAN')

# input data baru
divisi = st.selectbox('Divisi Karyawan?',
                          ('sales','accounting','hr','technical','support','management','IT','product_mng','marketing','RandD'))
promosi = st.selectbox('Apakah Karyawan Sudah Di Promosikan Dalam Waktu Lima Tahun Terakhir?',
                                     ('yes','no'))
sl = st.slider('Seberapa Senang Karyawan Tersebut Di Perusahaan Ini?',
                               0,100,1,1)
satisfaction_level = (sl - 0) / (100 - 0) * 100 # normalisasi 0-100 menjadi 0-1
le = st.slider('Kinerja Karyawan Tersebut Di Perusahaan Ini?',
                               0,100,1,1)
last_evaluation = (le - 0) / (100 - 0) * 100
number_project = st.number_input('Jumlah Proyek Yang Sudah Pernah Dikerjakan:',min_value=0,max_value=100,value=0,step=1)
average_montly_hours = st.number_input('Jam Kerja Dalam Sebulan:',min_value=0,max_value=200,value=0,step=1)
time_spend_company = st.number_input('Sudah Berapa Tahun Karyawan Tersebut Bekerja Di Perusahaan?',min_value=0,max_value=100,value=0,step=1)
kecelakaan = st.selectbox('Apakah Karyawan Tersebut Pernah Mengalami Kecelakaan Kerja?',
                             ('yes','no'))


Department = dept_con(divisi)
promotion_last_5years = promote(promosi)
Work_accident = work_acc(kecelakaan)

# initialize list of lists
data = [[Department,satisfaction_level,last_evaluation,number_project,average_montly_hours,time_spend_company,Work_accident,promotion_last_5years]]
  
# Create the pandas DataFrame
New_Data = pd.DataFrame(data, columns=['Department','satisfaction_level','last_evaluation','number_project','average_montly_hours','time_spend_company','Work_accident','promotion_last_5years'])

if st.button('Prediksi Gaji Karyawan:'):
  Prediction = model.predict(New_Data)
  pred = Prediction
  rec_str = pred.item()[:]

  # hasil prediksi
  if rec_str == 'low':
    st.write('Karyawan tersebut diprediksi mendapatkan gaji Rendah')
  elif rec_str == 'medium':
    st.write('Karyawan tersebut diprediksi mendapatkan gaji Cukup')
  elif rec_str == 'high':
    st.write('Karyawan tersebut diprediksi mendapatkan gaji Tinggi')