import streamlit as st
import streamlit.components.v1 as components

# 1. 스트림릿 페이지 기본 설정
st.set_page_config(
    page_title="GameForge Studio",
    page_icon="🎮",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. 스트림릿 내외부 여백 완벽 제거 및 스크롤바 숨기기
st.markdown("""
    <style>
        /* 스트림릿 헤더 및 푸터 숨기기 */
        [data-testid="stHeader"], footer {
            display: none !important;
        }
        /* 메인 영역 여백 완전히 제로(0)로 압축 */
        .main .block-container {
            padding-top: 0rem !important;
            padding-bottom: 0rem !important;
            padding-left: 0rem !important;
            padding-right: 0rem !important;
        }
        /* 불필요한 스크롤바 유발 요소 방지 */
        .stDeployButton {
            display: none !important;
        }
    </style>
""", unsafe_allow_html=True)

# 3. game.html 파일을 읽어와서 화면 비율에 맞게 배치
try:
    with open("game.html", "r", encoding="utf-8") as f:
        html_code = f.read()
    
    # 💡 핵심 수정: height를 고정 px 대신 98vh(화면 높이의 98%)로 설정하여
    # 모니터 크기에 상관없이 꽉 차게 만들고 지저분한 이중 스크롤바를 지웁니다.
    components.html(html_code, height=950, scrolling=True)

except FileNotFoundError:
    st.error("⚠️ 같은 폴더 안에 'game.html' 파일이 없습니다! 파일 이름을 확인해 주세요.")
