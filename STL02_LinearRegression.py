import requests
import pickle
import streamlit as st

# URL ของไฟล์ .pkl บน GitHub (แทนที่ด้วย URL ของคุณ)
model_url = 'https://raw.githubusercontent.com/anun311/py_code/refs/heads/main/mtcar_linear_reg_model.pkl'

def load_model_from_github(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # ตรวจสอบว่าดาวน์โหลดสำเร็จหรือไม่
        model = pickle.loads(response.content)
        return model
    except requests.exceptions.RequestException as e:
        st.error(f'เกิดข้อผิดพลาดในการดาวน์โหลดโมเดล: {e}')
        return None
    except pickle.UnpicklingError as e:
        st.error(f'เกิดข้อผิดพลาดในการโหลดโมเดลจากไฟล์: {e}')
        return None

# โหลดโมเดล
model = load_model_from_github(model_url)

# โหลดโมเดลจากไฟล์ .pkl
# with open('mtcar_linear_reg_model.pkl', 'rb') as f:
#     model = pickle.load(f)

inter_ = model.intercept_
hp_coef = model.coef_[0]
wt_coef = model.coef_[1]
am_coef = model.coef_[2]

var_hp = 200
var_wt = 3.5
var_am = 1
mpg_ = inter_ + (hp_coef * var_hp) + (wt_coef * var_wt) + (am_coef * var_am)

st.text(f"Intercept: {inter_}")
st.text(f"hp_coef: {hp_coef}")
st.text(f"wt_coef: {wt_coef}")
st.text(f"am_coef: {am_coef}")

st.text(f"var_hp: {var_hp}")
st.text(f"var_wt: {var_wt}")
st.text(f"var_am: {var_am}")
st.text(f"mpg_: {mpg_}")

# streamlit run STL02_LinearRegression.py
