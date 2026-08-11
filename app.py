import streamlit as st

# Page configuration
st.set_page_config(page_title="Kalpana Data AI", page_icon="🤖")

st.title("🤖 Kalpana Data AI Chatbot")
st.write("Welcome! This is a multi-lingual personal AI assistant built by Kalpana Kumari.")

# 1. Chat memory initialize karna
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# 2. Purani saari chat history screen par line se dikhana
for chat in st.session_state.chat_history:
    if chat["role"] == "user":
        st.markdown(f"**🧑‍💻 You:** {chat['text']}")
    else:
        st.markdown(f"**🤖 Kalpana AI:** {chat['text']}")
    st.write("---")

# 3. User se sawaal lena
user_query = st.text_input("Aap kya search ya poochna chahte hain? Yahan type karein:", key="user_input")

# Jab user message send karega
if user_query:
    # User ka sawaal memory me save karna
    st.session_state.chat_history.append({"role": "user", "text": user_query})
    
    with st.spinner("AI aapka jawaab aur language samajh raha hai..."):
        # Humne AI ke dimaag ko train kar diya hai ki woh user ki language ke hisab se jawab de
        # Agle step me hum isme asli Google Gemini API connect karenge
        
        user_query_clean = user_query.lower()
        
        # Agar user mix bhasha ya dono me chahta hai
        if "hindi" in user_query_clean and "english" in user_query_clean or "dono" in user_query_clean:
            ai_reply = f"Hello Kalpana! Aapne '{user_query}' poocha hai. Iska jawab English aur Hindi dono me jald hi Google Gemini AI dhoondh kar layega. [English]: This features multi-language explanation capability. [Hindi]: Yeh website aapko dono bhashaon me ek saath samjhane ke liye poori tarah ready hai!"
        
        # Agar user sirf Hindi me baat kar raha hai
        elif any(word in user_query_clean for word in ["kaise", "kya", "btao", "hai", "namaste", "halo"]):
            ai_reply = f"नमस्ते कल्पना कुमारी! मैं आपकी पर्सनल एआई असिस्टेंट हूँ। आपके सवाल '{user_query}' का पूरा जवाब जल्द ही गूगल जेमिनी एआई इंटरनेट से ढूंढकर हिंदी में यहाँ दिखाएगा।"
        
        # Agar user pure English me baat kar raha hai
        else:
            ai_reply = f"Hello! I am your personal AI assistant built by Kalpana Kumari. I have received your query: '{user_query}'. Soon, Google Gemini AI will fetch the complete and accurate answer in English for you!"
    
    # AI ka reply memory me save karna
    st.session_state.chat_history.append({"role": "bot", "text": ai_reply})
    
    # Page ko refresh karna taaki naya message screen par dikhne lage
    st.rerun()
