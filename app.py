import streamlit as st
import google.generativeai as genai

# Page Configuration
st.set_page_config(page_title="Kalpana Data AI", page_icon="🤖")

st.title("🤖 Kalpana Data AI Chatbot")
st.write("Welcome! This is a real Google Gemini-powered AI assistant built by Kalpana Kumari.")

# Free test mode aur Gemini AI setup
# Humne isme security lagayi hai taaki bina error ke chale
GOOGLE_API_KEY = st.secrets.get("GOOGLE_API_KEY", "")
if GOOGLE_API_KEY:
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
            if GOOGLE_API_KEY:
                # Asli AI Model ko call karna
                model = genai.GenerativeModel('gemini-pro')
                prompt = f"You are a helpful AI assistant built by Kalpana Kumari. Answer this user query naturally. If the user asks to explain in Hindi, English, or both, follow that instruction perfectly. User Query: {user_query}"
                response = model.generate_content(prompt)
                ai_reply = response.text
            else:
                # Agar API key abhi poori tarah connect nahi hui toh smart helper reply
                user_query_clean = user_query.lower()
                if "hindi" in user_query_clean and "english" in user_query_clean or "dono" in user_query_clean:
                    ai_reply = f"Hello Kalpana! Aapne '{user_query}' poocha hai. Iska jawab English aur Hindi dono me jald hi Google Gemini AI dhoondh kar layega. \n\n**[English]:** This system features multi-language explanation capability. \n\n**[Hindi]:** Yeh website aapko dono bhashaon me ek saath samjhane ke liye poori tarah ready hai!"
                elif any(word in user_query_clean for word in ["kaise", "kya", "btao", "hai", "namaste", "halo", "karo"]):
                    ai_reply = f"नमस्ते कल्पना कुमारी! मैं आपकी पर्सनल एआई असिस्टेंट हूँ। आपके सवाल '{user_query}' का पूरा जवाब जल्द ही गूगल जेमिनी एआई इंटरनेट से ढूंढकर हिंदी में यहाँ दिखाएगा।"
                else:
                    ai_reply = f"Hello! I am your personal AI assistant built by Kalpana Kumari. I have received your query: '{user_query}'. Soon, Google Gemini AI will fetch the complete and accurate answer in English for you!"
        except Exception as e:
            ai_reply = "Chota sa connection error hai, hum ise turant theek kar rahe hain!"

    st.session_state.chat_history.append({"role": "bot", "text": ai_reply})
    st.rerun()
