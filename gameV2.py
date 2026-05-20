import streamlit as st
import streamlit.components.v1 as components

# 1. 스트림릿 페이지 기본 설정
st.set_page_config(
    page_title="GameForge Studio",
    page_icon="🎮",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. 스트림릿 자체 여백 및 상단 탑바 공간 완벽 제거 (짤림 방지)
st.markdown("""
    <style>
        /* 스트림릿 기본 상단 헤더 숨기기 */
        [data-testid="stHeader"] {
            display: none;
        }
        /* 메인 컨텐츠 영역의 마진과 패딩을 0으로 강제 초기화 */
        .main .block-container {
            padding-top: 0rem !important;
            padding-bottom: 0rem !important;
            padding-left: 0rem !important;
            padding-right: 0rem !important;
        }
        /* html 컴포넌트 테두리 제거 */
        iframe {
            border: none;
        }
    </style>
""", unsafe_allow_html=True)

# 3. game.html 파일을 직접 읽어와서 화면에 꽉 차게 띄우기
try:
    with open("game.html", "r", encoding="utf-8") as f:
        html_code = f.read()
    
    # HTML 컴포넌트 실행 (높이를 1000px로 넉넉하게 지정)
    components.html(html_code, height=1000, scrolling=True)

except FileNotFoundError:
    st.error("⚠️ 같은 폴더 안에 'game.html' 파일이 없습니다! 파일 이름을 확인해 주세요.")
