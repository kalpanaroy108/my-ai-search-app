import streamlit as st
import google.generativeai as genai

# Page Configuration
st.set_page_config(page_title="Kalpana Data AI", page_icon="🤖")

st.title("🤖 Kalpana Data AI Chatbot")
st.write("Welcome! This is a real Google Gemini-powered AI assistant built by Kalpana Kumari.")

# Direct Password / API Key Setup (Ab kisi settings ki zaroorat nahi)
GOOGLE_API_KEY = "AIzaSyD-7n7X9Wc4b2R5V1m8K0z3Q6p9L_Real"
genai.configure(api_key=GOOGLE_API_KEY)

# Chat history memory setup
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Purani chats screen par dikhana
for chat in st.session_state.chat_history:
    if chat["role"] == "user":
        st.markdown(f"**🧑‍💻 You:** {chat['text']}")
    else:
        st.markdown(f"**🤖 Kalpana AI:** {chat['text']}")
    st.write("---")

# User form for input
with st.form(key="chat_form", clear_on_submit=True):
    user_query = st.text_input("Aap kya search ya poochna chahte hain? Yahan type karein:")
    submit_button = st.form_submit_button(label="🔍 Search / Ask AI")

if submit_button and user_query:
    st.session_state.chat_history.append({"role": "user", "text": user_query})
    
    with st.spinner("Google Gemini AI aapke liye jawab dhoondh raha hai..."):
        try:
            model = genai.GenerativeModel('gemini-pro')
            prompt = f"You are a helpful AI assistant built by Kalpana Kumari. Answer this user query naturally. If the user asks to explain in Hindi, English, or both, follow that instruction perfectly. User Query: {user_query}"
            response = model.generate_content(prompt)
            ai_reply = response.text
        except Exception as e:
            ai_reply = "Chota sa connection error hai, hum ise turant theek kar rahe hain!"

    st.session_state.chat_history.append({"role": "bot", "text": ai_reply})
    st.rerun()
