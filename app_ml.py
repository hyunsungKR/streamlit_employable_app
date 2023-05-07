import streamlit as st
import numpy as np
import joblib
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix,accuracy_score
from PIL import Image

scaler_X=joblib.load('scaler_X.pkl')
classifier = joblib.load('classifier2.pkl')
df=pd.read_csv('Student-Employability-Datasets.csv')
# 필요없는 컬럼 제거
df=df.drop('Name of Student',axis=1)
# df의 CLASS 컬럼 변경
df = df.replace('LessEmployable', 0)
df = df.replace('Employable', 1)

def score_conversion(score):
    if score == '매우안좋다':
        return 1
    elif score == '안좋다':
        return 2
    elif score == '보통이다':
        return 3
    elif score == '좋다':
        return 4
    elif score == '매우좋다':
        return 5

def run_ml():
    st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQJ2hDyjLKlxs6o6VuayarJJ7V133ht5yZTsQ&usqp=CAU.jpg',width=350)
    if st.button('데이터 보기') :
        st.dataframe(df)
        with st.expander('데이터프레임 컬럼 상세 설명') :
            st.subheader('데이터프레임 컬럼 상세 설명')
            st.text('GENERAL APPEARANCE : 일반 외관')
            st.text('MANNER OF SPEAKING : 말하는 방식')
            st.text('PHYSICAL CONDITION : 신체 조건')
            st.text('MENTAL ALERTNESS : 정신적 경계')
            st.text('SELF-CONFIDENCE : 자신감')
            st.text('ABILITY TO PRESENT IDEAS : 아이디어 제시 능력')
            st.text('COMMUNICATION SKILLS : 의사 소통 능력')
            st.text('Student Performance Rating : 학생 수행 평가')
            st.text('CLASS  : 고용 가능 0은 불가능 1은 가능')
    score = ['매우안좋다','안좋다','보통이다','좋다','매우좋다']
    G_A=st.radio('본인의 일반외관 점수는 어떠합니까.',[score[0],score[1],score[2],score[3],score[4]])
    if G_A == score[0] :
        G_A = 1
    elif G_A == score[1] :
        G_A = 2
    elif G_A == score[2] :
        G_A = 3
    elif G_A == score[3] :
        G_A = 4
    elif G_A == score[4] :
        G_A = 5
    M_S=st.radio('본인의 스피킹 점수는 어떠합니까.',[score[0],score[1],score[2],score[3],score[4]])
    if M_S == score[0] :
        M_S = 1
    elif M_S == score[1] :
        M_S = 2
    elif M_S == score[2] :
        M_S = 3
    elif M_S == score[3] :
        M_S = 4
    elif M_S == score[4] :
        M_S = 5
    P_C=st.radio('본인의 신체 조건 점수는 어떠합니까.',[score[0],score[1],score[2],score[3],score[4]])
    if P_C == score[0] :
        P_C = 1
    elif P_C == score[1] :
        P_C = 2
    elif P_C == score[2] :
        P_C = 3
    elif P_C == score[3] :
        P_C = 4
    elif P_C == score[4] :
        P_C = 5
    M_A=st.radio('본인의 정신적 경계 점수는 어떠합니까.',[score[0],score[1],score[2],score[3],score[4]])
    if M_A == score[0] :
        M_A = 1
    elif M_A == score[1] :
        M_A = 2
    elif M_A == score[2] :
        M_A = 3
    elif M_A == score[3] :
        M_A = 4
    elif M_A == score[4] :
        M_A = 5
    S_C=st.radio('본인의 자신감 점수는 어떠합니까.',[score[0],score[1],score[2],score[3],score[4]])
    if S_C == score[0] :
        S_C = 1
    elif S_C == score[1] :
        S_C = 2
    elif S_C == score[2] :
        S_C = 3
    elif S_C == score[3] :
        S_C = 4
    elif S_C == score[4] :
        S_C = 5
    A_P=st.radio('본인의 아이디어 제시능력 점수는 어떠합니까.',[score[0],score[1],score[2],score[3],score[4]])
    if A_P == score[0] :
        A_P = 1
    elif A_P == score[1] :
        A_P = 2
    elif A_P == score[2] :
        A_P = 3
    elif A_P == score[3] :
        A_P = 4
    elif A_P == score[4] :
        A_P = 5
    C_S=st.radio('본인의 의사소통능력 점수는 어떠합니까.',[score[0],score[1],score[2],score[3],score[4]])
    if C_S == score[0] :
        C_S = 1
    elif C_S == score[1] :
        C_S = 2
    elif C_S == score[2] :
        C_S = 3
    elif C_S == score[3] :
        C_S = 4
    elif C_S == score[4] :
        C_S = 5
    S_P=st.radio('본인의 수행평가 점수는 어떠합니까.',[score[0],score[1],score[2],score[3],score[4]])
    if S_P == score[0] :
        S_P = 1
    elif S_P == score[1] :
        S_P = 2
    elif S_P == score[2] :
        S_P = 3
    elif S_P == score[3] :
        S_P = 4
    elif S_P == score[4] :
        S_P = 5

    new_data=np.array([G_A,M_S,P_C,M_A,S_C,A_P,C_S,S_P])

    new_data=new_data.reshape(1,8)

    scaler_X2=joblib.load('scaler_X2.pkl')

    classifier3 = joblib.load('classifier3.pkl')

    new_data = scaler_X2.transform(new_data)

    pred=classifier3.predict(new_data)

    if pred == 1 : 
        st.info('축하합니다. 고용 가능성이 매우 높습니다!')
    else :
        st.error('아쉽습니다. 고용 가능성이 낮습니다.')


