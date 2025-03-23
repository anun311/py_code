import streamlit as st
import pickle
import pandas as pd

# โหลดโมเดลจากไฟล์ .pkl
ss = "https://github.com/anun311/py_code/blob/9b596cb84aa702d0f0a333d54b13b4e710af111d/mtcar_linear_reg_model.pkl"
with open(ss, 'rb') as f:
    model = pickle.load(f)

print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)


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

# streamlit run STL02_LinearRegression.py
