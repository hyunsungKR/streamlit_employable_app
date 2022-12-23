# 필리핀 학생들의 고용가능성과 Random forest를 이용한 고용가능성 예측 👀

## 📌 Project Explanation

* Jupyter Notebook에서 데이터 분석
* Visual Studio Code에서 Streamlit 라이브러리로 작업
* Nan데이터 값이 있으면 인공지능을 만들 때 에러가 발생하므로 Nan값 제거
* 인공지능 모델과 스케일러 모델은 pkl 파일화하여 진행하였습니다.
* AWS EC2를 이용하여 서버를 관리하였습니다.
* Github Actions를 이용한 CI/CD를 사용하였습니다.
* 유지보수작업을 수월하게 하기 위해서 다른 파일에서 함수를 만들고 그 함수를 import해서 작업을 하였습니다.
* MinMaxScaler 피쳐스케일링을 사용하여 좀 더 정교한 머신러닝 결과를 가져올 수 있도록 하였습니다.
* 정확도 89%의 Random Forest모델을 이용하여 결과를 예측하였습니다.



## 📌hyunsungKR
<a href="https://github.com/hyunsungKR/"><img src="https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=GitHub&logoColor=white"/></a> <a href="https://hyunsungstory.tistory.com/"><img src="https://img.shields.io/badge/Tistory-466BB0?style=flat-square&logo=Tistory&logoColor=white"/></a>

## 📌Languages
<img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=Python&logoColor=white"/>

## 📌 Library
<img src="https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=NumPy&logoColor=white"/> <img src="https://img.shields.io/badge/pandas-150458?style=flat-square&logo=pandas&logoColor=white"/> <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=flat-square&logo=Streamlit&logoColor=white"/> <img src="https://img.shields.io/badge/matplotlib.pyplot-40AEF0?style=flat-square&logo=&logoColor=white"/> 

<img src="https://img.shields.io/badge/Seaborn-006600?style=flat-square&logo=&logoColor=white"/> <img src="https://img.shields.io/badge/scikit-learn-F7931E?style=flat-square&logo=scikit-learn&logoColor=white"/> <img src="https://img.shields.io/badge/SciPy-8CAAE6?style=flat-square&logo=SciPy&logoColor=white"/>   

## 📌Tool
<img src="https://img.shields.io/badge/Visual Studio Code-007ACC?style=flat-square&logo=Visual Studio Code&logoColor=white"/> <img src="https://img.shields.io/badge/Anaconda-44A833?style=flat-square&logo=Anaconda&logoColor=white"/> <img src="https://img.shields.io/badge/Amazon AWS-232F3E?style=flat-square&logo=Amazon AWS&logoColor=white"/> 

## 📌Code block
```python
# 필요없는 컬럼 삭제 과정
df=df.drop('Name of Student',axis=1)
```
```python
# 고용 가능성 별로 유니크 값 확인
df.groupby('CLASS')['GENERAL APPEARANCE'].value_counts()
```
```python
# 능력별 합격자 분포 시각화
    col_list=df.columns
    selected_col=st.selectbox('컬럼을 선택하세요.',col_list)

    fig1=px.pie(df,selected_col,'CLASS',title='능력 별 합격자 분포')
    st.plotly_chart(fig1)
 ```
```python
# 주피터 노트북에서 개발하고 저장한 스케일러와 인공지능 불러오는 과정

scaler_X=joblib.load('scaler_X.pkl')
classifier = joblib.load('classifier2.pkl')
```
```python
# 고객에게 데이터를 입력받을 때 숫자 0~5로 받지않고, 문자로 받으면 숫자로 변환하는 조건문

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
 ```
 
 

## 📌 ML
* Using Model : from sklearn.ensemble import RandomForestClassifier
```python
# X와 y로 분리
X = df.iloc[:,:-1]
y = df['CLASS']
```
```python
# MinMaxScaler를 이용한 피쳐스케일링 과정
from sklearn.preprocessing import MinMaxScaler
scaler_X = MinMaxScaler()
X=scaler_X.fit_transform(X)
```
```python
# training / test 셋으로 분리
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.25,random_state=22)
```
```python
# 모델링 과정
from sklearn.ensemble import RandomForestClassifier
classifier3=RandomForestClassifier(n_estimators=100)
classifier3.fit(X_train,y_train)
y_pred = classifier3.predict(X_test)
```
```python
# 검증 과정 1
from sklearn.metrics import confusion_matrix,accuracy_score
cm=confusion_matrix(y_test,y_pred)
```
```python
# 검증 과정 2
accuracy_score(y_test,y_pred)
```
```python
# joblib 라이브러리를 이용하여 인공지능과, 피쳐스케일러 저장
# 저장 후 비주얼 스튜디오에 사용하기 위함
import joblib
joblib.dump(classifier3,'classifier3.pkl')
joblib.dump(scaler_X,'scaler_X2.pkl')
```
![image](https://user-images.githubusercontent.com/120348500/209256355-fc7430fc-15d9-4102-93a3-38df8a96a9cd.png)
* 검증 결과 정확도 89%의 Random forest의 모델 개발 완료



## 📌 URL
  - http://ec2-3-36-77-30.ap-northeast-2.compute.amazonaws.com:8504/

## 📌 Screen Shot
![image](https://user-images.githubusercontent.com/120348500/209257044-bf3d0454-8aec-4b7a-bda4-66d49be87569.png)
![image](https://user-images.githubusercontent.com/120348500/209257100-f75522f7-01ed-46af-aec1-c043955a6115.png)
![image](https://user-images.githubusercontent.com/120348500/209257149-0d464071-a79f-4c93-af1d-c6fadf5c2f78.png)
![image](https://user-images.githubusercontent.com/120348500/209257188-7d73f651-0542-4d01-96f1-402c1b40cc68.png)
![image](https://user-images.githubusercontent.com/120348500/209257217-63fa9654-d884-4987-8aea-82e9774d9b7e.png)


## 📌 Reference

* 필리핀 학생들의 고용가능성 데이터 : https://www.kaggle.com/datasets/anashamoutni/students-employability-dataset
