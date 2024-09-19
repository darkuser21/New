import streamlit as st
from groq import Groq

api = st.secrets["GROQ_API_KEY"]
client = Groq(api_key=api)

st.title("SASTA chatGPT💀 ")

def chatGPT():
    user_question = st.text_input("ESKE NICHE PUCH JO PUCHNA HAI: ", "")
    
    if st.button("MUZE TOUCH KAR", key="ask_button"):
        if user_question.strip() == "":
            st.write("JALDI PUCH BHAI .")
        else:
            message = {
                "content": user_question,
                "role": "user"
            }
            
            try:
                chat_completion = client.chat.completions.create(
                    messages=[message],
                    model="llama3-8b-8192",
                )
                
                if chat_completion.choices:
                    response = chat_completion.choices[0].message.content
                    st.text_area("YE LE ANPAD💀:", value=response, height=500)
                else:
                    st.write("ChatGPT: KUCH GADBAD HAI")
            
            except Exception as e:
                st.write(f"Error occurred: {e}")
chatGPT()
