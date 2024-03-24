import os
from langchain_openai import OpenAI
import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from langchain.memory import ConversationBufferMemory
import inspect

openai_key = os.environ["OPENAI_API_KEY"]
llm = OpenAI(api_key=openai_key, temperature=0.8)
# sig = inspect.signature(OpenAI)
# print(sig.parameters)

st.title('Langchain Demo')
input_text = st.text_input("Search for animals")

name_memory = ConversationBufferMemory(input_key='specie', memory_key='name_history')
weight_memory = ConversationBufferMemory(input_key='name', memory_key='weight_history')
others_memory = ConversationBufferMemory(input_key='weight', memory_key='others_history')

my_prompt = PromptTemplate(
    input_variables=['specie'],
    template="tell me about {specie}"
)

chain = LLMChain(llm=llm,prompt=my_prompt,verbose=True, output_key='name', memory=name_memory)

my_prompt1 = PromptTemplate(
    input_variables=['name'],
    template="tell me only the approx weight of {name} without any text"
)

chain1 = LLMChain(llm=llm,prompt=my_prompt1 ,verbose=True, output_key='weight', memory=weight_memory)

my_prompt2 = PromptTemplate(
    input_variables=['weight'],
    template="menetion five other animals that have same {weight}"
)

chain2 = LLMChain(llm=llm,prompt=my_prompt2 ,verbose=True, output_key='others',memory=others_memory)

Parent_chain = SequentialChain(chains=[chain,chain1,chain2],input_variables=['specie'],output_variables=['name', 'weight', 'others'], verbose=True)

if input_text:
    st.write(Parent_chain({'specie':input_text}))

    with st.expander('Animal name'):
        st.info(name_memory.buffer)

    with st.expander('other animals share weight'):
        st.info(others_memory.buffer)