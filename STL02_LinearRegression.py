import streamlit as st
import pickle
import pandas as pd
import requests

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

# streamlit run STL02_LinearRegression.py
st.header("Linear Regression is :blue[cool] :sunglasses:", divider=True)
with st.chat_message("assistant"):
    st.write(f"""สวัสดีครับ\n
    วันนี้เรามาลองใช้ฟังก์ชัน Linear Regression Model โดยการใช้ชุดข้อมูล mtcars
    ซึ่งผลการทดสอบตัวแปรและการวัดผลโมเดลมีรายละเอียด ดังนี้ ...
    - No. Observations: 32
    - R-squared: 0.840
    - Mean Squared Error: 5.6340959896827885
    - Root Mean Squared Error: 2.373625073528418
    จากผลการรันโมเดลสามารถเขียนสมการ Linear Regression ได้ดังนี้
    mpg = {inter_} + ({hp_coef} x hp) 
          + ({wt_coef} x wt) + ({am_coef} x am)
    """)

st.subheader("ระบุตัวเลือกเพื่อทำนาย")

col1, col2 = st.columns(2)
with col1:
    hp_number = st.number_input("Horse Power", min_value=50.0, max_value=400.0, step=5.0)
    st.write("กำลังแรงม้า (horsepower, hp):", hp_number)

    option = st.selectbox(
        "ระบบเกียร์ (Transmission)",
        ("0 = automatic", "1 = manual"),
        index=None,
        placeholder="Select contact method...",
    )
    st.write("ระบบเกียร์ (Transmission, am):", option)

with col2:
    wt_number = st.number_input("Weight (คูณ 1000 ปอนด์ (lbs.))", min_value=1.0, max_value=6.0, step=1.0)
    st.write("น้ำหนักรถ (weight, wt):", wt_number, "ปอนด์", round((float(wt_number)*1000*0.453592)/1000,2), "ตัน")

    var_hp = float(hp_number)
    var_wt = float(wt_number)
    display_wt = round(var_wt * 1000, 2)
    display_wt2 = round((var_wt * 0.453592)/1000, 2)

    if option == "0 = automatic":
        var_am = 0
    elif option == "1 = manual":
        var_am = 1
    else:
        var_am = None

if st.button("Predicted"):

    display_wt = round(var_wt * 1000, 2)
    display_wt2 = round((var_wt*1000*0.453592)/1000, 2)

    mpg_ = inter_ + (hp_coef * var_hp) + (wt_coef * var_wt) + (am_coef * var_am)
    display_mpg = round(mpg_, 2)
    st.write(f"""เมื่อรถยนต์มีคุณสมบัติ:\n - กำลังเครื่องยนต์ เท่ากับ {var_hp} แรงม้า
    \n - น้ำหนักรถ เท่ากับ {display_wt} ปอนด์ หรือ {display_wt2} ตัน
    \n - และระบบเกียร์เป็น {option} 
    \n จะทำให้รถยนต์สามารถวิ่งได้ไกล {display_mpg} ไมล์ ต่อน้ำมัน 1 แกนลอน""")
