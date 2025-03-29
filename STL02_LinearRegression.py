import streamlit as st
import pickle
import pandas as pd
import requests

st.header("Python 🐍 Project Model")
st.write("Created by Feasible")

tab1, tab2 = st.tabs(["mtcars", "diabetes"])
with tab1:

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

    inter_ = model.intercept_
    hp_coef = model.coef_[0]
    wt_coef = model.coef_[1]
    am_coef = model.coef_[2]

    # streamlit run STL02_LinearRegression.py
    st.header("Linear Regression is :blue[cool] :sunglasses:", divider=True)
    with st.chat_message("assistant"):
        st.write(f"""สวัสดีครับ\n
        วันนี้เรามาลองใช้ฟังก์ชัน Linear Regression Model โดยการใช้ชุดข้อมูล mtcars
    เพื่อทำนาย MPG: Miles per Gallon ระยะทางที่รถยนต์สามารถขับเคลื่อนได้โดยใช้น้ำมัน 1 แกนลอน 
    ซึ่งตัวแปรที่ใช้งานมาจากการวิเคราะห์ตัวแปรต้น (x) ที่ส่งผลต่อการทำนายตัวแปรตาม (y) ได้แก่
        1) กำลังแรงม้า 2) น้ำหนักตัวรถยนต์ และ 3) ระบบเกียร์
    ซึ่งผลการทดสอบตัวแปรและการวัดผลโมเดลมีรายละเอียด ดังนี้ ...
        - Observations: 32
        - R-squared: 0.840
        - Mean Squared Error: 5.634
        - Root Mean Squared Error: 2.374
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
            placeholder="กรุณาเลือก ระบบเกียร์",
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
        if var_am == None:
            st.error('กรุณาระบุตัวเลือกครับ', icon="🚨")
        else:
            display_wt = round(var_wt * 1000, 2)
            display_wt2 = round((var_wt*1000*0.453592)/1000, 2)

            mpg_ = inter_ + (hp_coef * var_hp) + (wt_coef * var_wt) + (am_coef * var_am)
            display_mpg = round(mpg_, 2)
            display_mpg2 = round(mpg_*1.609344, 2)

            with st.chat_message("assistant"):
                st.write(f""".\n
    เมื่อรถยนต์มีคุณสมบัติ:
    - กำลังเครื่องยนต์ เท่ากับ {var_hp} แรงม้า
    - น้ำหนักรถ เท่ากับ {display_wt} ปอนด์ หรือ {display_wt2} ตัน
    - และระบบเกียร์เป็น {option} 
    จะทำให้รถยนต์สามารถวิ่งได้ไกล {display_mpg} ไมล์ ต่อน้ำมัน 1 แกนลอน
    หรือ {display_mpg2} กิโลเมตร ต่อน้ำมัน 3.785 ลิตร """)

with tab2:

    # URL ของไฟล์ .pkl บน GitHub (แทนที่ด้วย URL ของคุณ)
    model_log_url = 'https://raw.githubusercontent.com/anun311/py_code/refs/heads/main/diabetes_logistic_reg_model.pkl'

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
    model_lg = load_model_from_github(model_log_url)

    lg_inter_ = model_lg.intercept_[0]
    coef_pregnancies = model_lg.coef_[0][0]
    coef_glucose = model_lg.coef_[0][1]
    coef_bp = model_lg.coef_[0][2]
    coef_bmi = model_lg.coef_[0][3]
    coef_dmpedfunc = model_lg.coef_[0][4]
    
    st.header("Logistic Regression is also :blue[cool] :stars:", divider=True)
    with st.chat_message("assistant"):
        st.write(f"""สวัสดีครับ\n
    ครั้งนี้เราจะมาใช้งาน Logistic Regression Model โดยการใช้ชุดข้อมูล diabetes 
    เป็นข้อมูลผู้ป่วยหญิงชาว Pima Indians ที่มีโอกาสเป็นโรคเบาหวานได้
    เพื่อทำนาย Outcome: 0=ไม่เป็น DM, 1=เป็น DM ซึ่งมีตัวแปรที่ใช้งาน
    มาจากการวิเคราะห์ตัวแปรต้น (x) ได้แก่
        1) จำนวนครั้งที่ตั้งครรภ์ 2) ระดับน้ำตาลกลูโคสในเลือด  3) ค่าความดันโลหิตตัวล่าง 
        4) ดัชนีมวลกาย (BMI) และ 5) ฟังก์ชันประวัติโรคเบาหวาน
    ซึ่งผลการทดสอบตัวแปรและการวัดผลโมเดลมีรายละเอียด ดังนี้ ...
        - Observations: 154
        - Accuracy: 0.79
        - Precision: 0.63
        - Recall: 0.66
        - F1 Score: 0.64
    จากผลการรันโมเดลสามารถเขียนสมการ Linear Regression ได้ดังนี้
    Outcome = {lg_inter_} + ({coef_pregnancies} x pregnancies) 
        + ({coef_glucose} x glucose) + ({coef_bp} x bp) 
        + ({coef_bmi} x bmi) + ({coef_dmpedfunc} x diabetespedigreefunction)""")
        url = "https://feasibleth.com/"
        st.write("""คุณผู้อ่านสามารถอ่านรายละเอียด mini project นี้ ได้ที่: %s """% url)
    
    st.subheader("ระบุตัวเลือกเพื่อทำนาย")

    col1, col2 = st.columns(2)
    with col1:
        pregnancies_number = st.number_input("จำนวนครั้งที่ตั้งครรภ์", min_value=0.0, max_value=20.0, step=1.0, value=6.0)
        st.write( "Pregnancies:", pregnancies_number)

        bp_number = st.number_input("ค่าความดันโลหิตตัวล่าง", min_value=60.0, max_value=125.0, step=5.0, value=62.0)
        st.write( "Blood pressure:", bp_number)

        dmpedfunc_number = st.number_input("ฟังก์ชันประวัติโรคเบาหวาน", min_value=0.005, max_value=3.000, step=1.000, value=0.178)
        st.write( "Diabetes pedigree function:", round(dmpedfunc_number, 4))

    with col2:
        glucose_number = st.number_input("ระดับน้ำตาลกลูโคสในเลือด", min_value=50.0, max_value=220.0, step=1.0, value=162.0)
        st.write("Glucose:", glucose_number)

        bmi_number = st.number_input("ดัชนีมวลกาย (BMI)", min_value=10.0, max_value=70.0, step=1.0, value=24.3)
        st.write("BMI:", bmi_number)

        var_pregnancies = float(pregnancies_number)
        var_glucose = float(glucose_number)
        var_bp = float(bp_number)
        var_bmi = float(bmi_number)
        var_dmpedfunc = float(dmpedfunc_number)

    if st.button("ทำนายค่า"):
        if var_pregnancies == None:
            st.error('กรุณาระบุตัวเลือกครับ', icon="🚨")
        else:
            outcome = lg_inter_ + (coef_pregnancies * var_pregnancies) + (coef_glucose * var_glucose) + (coef_bp * var_bp) + (coef_bmi * var_bmi) + (coef_dmpedfunc * var_dmpedfunc)
            # Sigmoid prob
            pred_prop = math.exp(outcome)/(1+math.exp(outcome))
            
            thershold = 0.5
            if pred_prop >= thershold: 
                pred_outcome_name = 'เป็นเบาหวาน'
            else:
                pred_outcome_name = 'ไม่เป็นเบาหวาน'

            with st.chat_message("assistant"):
                st.write(f""".\n
    เมื่อมีคุณสมบัติ:
        - จำนวนครั้งที่ตั้งครรภ์ เท่ากับ {int(pregnancies_number)} ครั้ง
        - ระดับน้ำตาลกลูโคสในเลือด เท่ากับ {int(glucose_number)} mg/dL
        - ค่าความดันโลหิตตัวล่าง เท่ากับ {int(bp_number)} mmHg
        - ดัชนีมวลกาย (BMI) เท่ากับ {var_bmi}
        - ฟังก์ชันประวัติโรคเบาหวาน เท่ากับ {round(dmpedfunc_number, 4)} mg/dL
    จะทำให้คำนวนค่า z ของ Linear Regression เท่ากับ {round(outcome, 4)} 
    คิดเป็น Sigmoid probability เท่ากับ {round(pred_prop, 4)} 
    โมเดล Logistic Regression ทำนายว่า {pred_outcome_name}
    """)
