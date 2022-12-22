import streamlit as st
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
import numpy as np

# plotly 라이브러리
import plotly.express as px
# altair 라이브러리
import altair as alt

# 각 운영체제에 따른 한글 출력
# 리눅스의 경우 해당 글꼴이 설치되어있어야 합니다.
import platform
from matplotlib import font_manager, rc
plt.rcParams['axes.unicode_minus'] = False
if platform.system() == 'Darwin':
    rc('font', family='AppleGothic')
elif platform.system() == 'Windows':
    path = 'c:/windows/Fonts/malgun.ttf'
    font_name = font_manager.FontProperties(fname=path).get_name()
    rc('font', family=font_name)
elif platform.system() == 'Linux':
    rc('font', family='NanumGothic')
else:
    print('Unknown system... sorry~~~~')

df=pd.read_csv('Student-Employability-Datasets.csv')
# 필요없는 컬럼 제거
df=df.drop('Name of Student',axis=1)
# df의 CLASS 컬럼 변경
df = df.replace('LessEmployable', 0)
df = df.replace('Employable', 1)



def run_eda() :
    st.subheader('데이터 분석🛠')
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
    st.subheader('차트 분석🛠')
    st.info('능력 별 합격자 분포(pie chart)')
    col_list=df.columns
    selected_col=st.selectbox('컬럼을 선택하세요.',col_list)

    fig1=px.pie(df,selected_col,'CLASS',title='능력 별 합격자 분포')
    st.plotly_chart(fig1)
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

    st.info('능력별 점수 분포')
    selected_col2=st.selectbox('컬럼을 선택하세요',col_list)
    fig2 = plt.figure()
    df[selected_col2].value_counts().plot(kind='bar')
    st.pyplot(fig2)
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


    

    if st.button('상관계수 차트 보기') :
        st.subheader('상관 관계 분석')
        st.text('상관 계수란? 상관관계 분석에서 두 변수 간에 선형 관계의 정도를 수량화하는 측도입니다.')
        fig3=plt.figure()
        df_corr=df[col_list].corr()
        sb.heatmap(data=df_corr,cmap='coolwarm',annot=True,fmt='.1f',linewidths=0.8,vmin=-1,vmax=1)
        st.pyplot(fig3)
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

    