from app_eda import show_column_description
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
    score_dict = {'매우안좋다': 1, '안좋다': 2, '보통이다': 3, '좋다': 4, '매우좋다': 5}
    return score_dict[score]

def run_ml():
    st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQJ2hDyjLKlxs6o6VuayarJJ7V133ht5yZTsQ&usqp=CAU.jpg',width=350)
    if st.button('데이터 보기') :
        st.dataframe(df)
        show_column_description()
        
    score = ['매우안좋다', '안좋다', '보통이다', '좋다', '매우좋다']
    feature_list = ['일반외관', '스피킹', '신체 조건', '정신적 경계', '자신감', '아이디어 제시 능력', '의사 소통 능력', '수행 평가']

    # feature_list와 score 리스트를 활용하여 라디오 버튼 생성
    new_data = []
    for feature in feature_list:
        score_selected = st.radio(f'본인의 {feature} 점수는 어떠합니까.', score)
        new_data.append(score_conversion(score_selected))

    new_data = np.array(new_data).reshape(1, -1)

    scaler_X2 = joblib.load('scaler_X2.pkl')
    classifier3 = joblib.load('classifier3.pkl')

    new_data = scaler_X2.transform(new_data)
    pred = classifier3.predict(new_data)

    if pred == 1:
        st.info('축하합니다. 고용 가능성이 매우 높습니다!')
    else:
        st.error('아쉽습니다. 고용 가능성이 낮습니다.')


