import streamlit as st

def run_home() :
    st.write('📝 이 앱은 필리핀 학생들의 고용가능성을 분석하여 예측 및 차트로 보여주는 앱입니다.')
    st.write('📝 EDA를 눌러보시면 데이터별로 분석된 차트를 확인하실 수 있습니다.')
    st.write('📝 ML은 인공지능이 학습하여 결과를 예측한 값을 확인하실 수 있습니다.')

    st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQfl1ugkHpb5edtGyxcBCCmbSPmU1AHsl2PhQ&usqp=CAU.png',width=550)