import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Trợ lý AI - Lina", page_icon="🤖")
st.title("🤖 Trợ lý AI - Lina - Vi Tính Tấn Dân")

# Lấy API Key từ Streamlit Secrets hoặc ô nhập bên dưới
api_key = st.secrets.get("GEMINI_API_KEY", "")

if not api_key:
    api_key = st.sidebar.text_input("Nhập Google Gemini API Key:", type="password")
    st.sidebar.info("💡 Thầy có thể lấy API Key miễn phí tại [Google AI Studio](https://aistudio.google.com/)")

if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')

    if "chat_session" not in st.session_state:
        st.session_state.chat_session = model.start_chat(history=[])

    # Hiển thị lịch sử chat
    for message in st.session_state.chat_session.history:
        role = "user" if message.role == "user" else "assistant"
        with st.chat_message(role):
            st.markdown(message.parts[0].text)

    # Nhập tin nhắn
    if prompt := st.chat_input("Nhập tin nhắn trò chuyện với Lina..."):
        with st.chat_message("user"):
            st.markdown(prompt)
        with st.chat_message("assistant"):
            with st.spinner("Lina đang suy nghĩ..."):
                try:
                    response = st.session_state.chat_session.send_message(prompt)
                    st.markdown(response.text)
                except Exception as e:
                    st.error(f"Đã xảy ra lỗi: {e}")
else:
    st.warning("⚠️ Thầy vui lòng nhập Gemini API Key ở thanh bên trái để bắt đầu trò chuyện với Lina nhé!")
