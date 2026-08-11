import streamlit as st

# Page title aur layout configuration
st.set_page_config(page_title="Kalpana Data AI", page_icon="🤖")

st.title("🤖 Kalpana Data AI Chatbot")
st.write("Welcome! This is a multi-lingual personal AI assistant built by Kalpana Kumari.")

# 1. Computer ki memory me chat history initialize karna
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# 2. Puraani saari chat history screen par line se dikhana
for chat in st.session_state.chat_history:
    if chat["role"] == "user":
        st.markdown(f"**🧑‍💻 You:** {chat['text']}")
    else:
        st.markdown(f"**🤖 Kalpana AI:** {chat['text']}")
    st.write("---")

# 3. Form ka use karna taaki Button aur Enter dono ekdam sahi kaam karein
with st.form(key="chat_form", clear_on_submit=True):
    user_query = st.text_input("Aap kya search ya poochna chahte hain? Yahan type karein:")
    submit_button = st.form_submit_button(label="🔍 Search / Ask AI")

# 4. Jab user button par click karega ya Enter dabayega
if submit_button and user_query:
    # User ka sawaal memory me save karna
    st.session_state.chat_history.append({"role": "user", "text": user_query})
    
    with st.spinner("AI aapka jawaab aur language samajh raha hai..."):
        user_query_clean = user_query.lower()
        
        # Mix language (Hindi + English) handler
        if "hindi" in user_query_clean and "english" in user_query_clean or "dono" in user_query_clean:
            ai_reply = f"Hello Kalpana! Aapne '{user_query}' poocha hai. Iska jawab English aur Hindi dono me jald hi Google Gemini AI dhoondh kar layega. \n\n**[English]:** This system features multi-language explanation capability. \n\n**[Hindi]:** Yeh website aapko dono bhashaon me ek saath samjhane ke liye poori tarah ready hai!"
        
        # Hindi language handler
        elif any(word in user_query_clean for word in ["kaise", "kya", "btao", "hai", "namaste", "halo", "karo"]):
            ai_reply = f"नमस्ते कल्पना कुमारी! मैं आपकी पर्सनल एआई असिस्टेंट हूँ। आपके सवाल '{user_query}' का पूरा जवाब जल्द ही गूगल जेमिनी एआई इंटरनेट से ढूंढकर हिंदी में यहाँ दिखाएगा।"
        
        # Pure English language handler
        else:
            ai_reply = f"Hello! I am your personal AI assistant built by Kalpana Kumari. I have received your query: '{user_query}'. Soon, Google Gemini AI will fetch the complete and accurate answer in English for you!"
    
    # AI ka reply memory me save karna
    st.session_state.chat_history.append({"role": "bot", "text": ai_reply})
    
    # Page ko refresh karna taaki naya message list me turant dikhe
    st.rerun()
