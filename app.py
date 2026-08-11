import streamlit as st

# Website ka Title
st.title("🤖 My Personal AI Search Engine")
st.write("Aap is website par kuch bhi search kar sakte hain aur AI aapko uska jawab dega!")

# Search Box (Input)
user_query = st.text_input("Aap kya search karna chahte hain? Yahan type karein:")

# Jab user search box me kuch type karega
if user_query:
    st.write("---")
    st.subheader(f"🔍 Searching for: '{user_query}'")
    
    with st.spinner("AI aapke liye jawab dhoondh raha hai..."):
        # Smart automatic reply template
        simulated_answer = f"Hello Kalpana! Aapne search kiya hai '{user_query}'. Main ek AI assistant hoon aur aapka jawab jald hi yahan poori detail me dikhega."
        
    st.success("✨ Answer Found:")
    st.write(simulated_answer)
