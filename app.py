import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu
from app_home import run_home
from app_eda import run_eda
from app_ml import run_ml

st.set_page_config(page_title='employable')


def main() :
    st.header('필리핀 학생들의 고용 가능성과🛠')
    st.header('Random forest를 이용한 고용 가능성 예측🛠')
    with st.sidebar:
        st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQxYLO-VtGfw5urWoV9H3pqU1sBEuxqjPEw-w&usqp=CAU.jpg')
        menu = option_menu("App Menu", ["Home", "EDA", "ML"],
                            icons=['house', 'bar-chart', 'kanban'],
                            menu_icon="bi bi-menu-up", default_index=0,
                            styles={
            "container": {"padding": "5!important", "background-color": "#333333"},
            "icon": {"color": "white", "font-size": "25px"}, 
            "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#333333"},
            "nav-link-selected": {"background-color": "#ff99cc"}, })
    if menu == 'Home' :
        run_home()
    elif menu == 'EDA' :
        run_eda()
    elif menu == 'ML' :
        run_ml()

if __name__ == '__main__' :
    main()