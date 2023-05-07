import os
import openai
import streamlit as st

openai.api_key = st.secrets["OPENAI_API_KEY"]

# Completion Version
def getNameCompletion(prompt):
  response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    temperature=0.7,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
  )
  return response

#Chat Completion Version

def getNameChat(messages): 
  response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=messages,
    temperature=0.7
  )
  return response 


st.title("Hedge Fund Name Generator")
st.divider()
user_prompt = st.text_input(label="Enter some keywords in the text box below to generate some names.")

# user_prompt = 'geographic features, (Global)'

prompt_template=f"""
You are a hedge name generator. Given a theme I want you to provide the top 3 names you can come up with. 
Make sure not to closely replicate existing hedge fund names. 

{user_prompt}

"""

messages = [{"role": "user", "content": prompt_template}]

response = getNameChat(messages=messages)
st.write ("Here are some ideas:")
st.write(response.choices[0].message.content)


