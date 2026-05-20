import streamlit as st
import streamlit.components.v1 as components

# 1. 스트림릿 페이지 기본 설정 (가로로 꽉 차게)
st.set_page_config(
    page_title="GameForge Studio",
    page_icon="🎮",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. 스트림릿 자체 상단 탑바 및 내부 마진 원천 차단
st.markdown("""
    <style>
        /* 스트림릿 기본 헤더 및 푸터 완전 삭제 */
        [data-testid="stHeader"], footer {
            display: none !important;
        }
        /* 메인 콘텐츠 패딩을 0으로 만들어 꽉 채우기 */
        .main .block-container {
            padding-top: 0rem !important;
            padding-bottom: 0rem !important;
            padding-left: 0rem !important;
            padding-right: 0rem !important;
        }
        /* iframe 테두리 없애기 */
        iframe {
            border: none !important;
        }
    </style>
""", unsafe_allow_html=True)

# 3. game.html 파일을 읽어와서 마진 없이 렌더링
try:
    with open("game.html", "r", encoding="utf-8") as f:
        html_code = f.read()
    
    # 💡 scrolling=False로 설정하여 스트림릿이 만드는 바깥쪽 이중 스크롤바를 강제로 없앱니다.
    # 높이는 일반적인 모니터 해상도에 맞춰 900~950 선으로 핏을 맞춥니다.
    components.html(html_code, height=920, scrolling=False)

except FileNotFoundError:
    st.error("⚠️ 같은 폴더 안에 'game.html' 파일이 없습니다! 파일 이름을 확인해 주세요.")
