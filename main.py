import streamlit as st
from utils import generate_script

st.markdown(
    """
<style>
div.stButton > button:first-child {
    background-color: #0099ff;
    color:#ffffff;
}
div.stButton > button:hover {
    background-color: #00ff00;
    color: #FFFF00;
}
</style>
    """, unsafe_allow_html=True
)

if 'API_KEY' not in st.session_state:
    st.session_state["API_KEY"]=''


st.title("❤️ YouTube Script Writing Tool")

st.sidebar.title("😎🗝️")
st.session_state["API_KEY"]=st.sidebar.text_input("What's your API key?", type="password")
st.sidebar.image("./youtube_logo.png", width=300, use_column_width=True)

# capture User Input

prompt = st.text_input("Please provide the topic of Video.", key="prompt")
video_length = st.text_input("Expected Video Length 🕒 (in Minutes)", key="video_length")
creativity = st.slider("Creativity Level - (0 Low || 1 High)", 0.0, 1.0, 0.2, step=0.1)

submit = st.button("Generate Script for me")

if submit:

    if st.session_state["API_KEY"]:
        search_result, title, script = generate_script(prompt=prompt, 
                                                       video_length=video_length,
                                                       creativity=creativity, 
                                                       api_key=st.session_state["API_KEY"])
        st.success("Hope you like the script.❤️")
        st.write("Max Token Length is 2,000")

        st.subheader("Title 🔥 : ")
        st.write(title)

        st.subheader("Your Video Script 📄 : ")
        st.write(script)

        st.subheader("Check Out - DuckDuckGo Search 🔍")
        with st.expander("Show me 👀"):
            st.info(search_result)
    else:
        st.error("Oooopsssss! Please provide API Key...")
