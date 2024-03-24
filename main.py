# Import necessary modules
import os  # For accessing environment variables
from langchain_openai import OpenAI  # For using OpenAI's API with Langchain
import streamlit as st  # For creating web apps
from langchain.prompts import PromptTemplate  # For creating prompt templates
from langchain.chains import LLMChain, SequentialChain  # For building language model chains
from langchain.memory import ConversationBufferMemory  # For storing conversation history

# Load OpenAI API key from environment variables
openai_key = os.environ["OPENAI_API_KEY"]

# Initialize the language model with OpenAI API key and set the temperature
llm = OpenAI(api_key=openai_key, temperature=0.8)

# Initialize the Streamlit interface with a title
st.title('Langchain Demo')

# Create a text input box in Streamlit for user input
input_text = st.text_input("Search for animals")

# Initialize memory buffers for different stages of the conversation
name_memory = ConversationBufferMemory(input_key='specie', memory_key='name_history')
weight_memory = ConversationBufferMemory(input_key='name', memory_key='weight_history')
others_memory = ConversationBufferMemory(input_key='weight', memory_key='others_history')

# Define the first prompt template for getting information about a species
my_prompt = PromptTemplate(
    input_variables=['specie'],
    template="tell me about {specie}"
)

# Create the first chain in the sequence to handle species information
chain = LLMChain(llm=llm, prompt=my_prompt, verbose=True, output_key='name', memory=name_memory)

# Define the second prompt template for getting the weight of an animal
my_prompt1 = PromptTemplate(
    input_variables=['name'],
    template="tell me only the approx weight of {name} without any text"
)

# Create the second chain in the sequence to handle animal weight information
chain1 = LLMChain(llm=llm, prompt=my_prompt1, verbose=True, output_key='weight', memory=weight_memory)

# Define the third prompt template for finding other animals with the same weight
my_prompt2 = PromptTemplate(
    input_variables=['weight'],
    template="mention five other animals that have the same {weight}"
)

# Create the third chain in the sequence to handle similar weight animal information
chain2 = LLMChain(llm=llm, prompt=my_prompt2, verbose=True, output_key='others', memory=others_memory)

# Combine the three chains into a sequential chain
Parent_chain = SequentialChain(chains=[chain, chain1, chain2], input_variables=['specie'], output_variables=['name', 'weight', 'others'], verbose=True)

# Execute the chain and display the results if the user has provided input
if input_text:
    st.write(Parent_chain({'specie': input_text}))

    # Display the animal name history in an expandable section
    with st.expander('Animal name'):
        st.info(name_memory.buffer)

    # Display the list of animals sharing the same weight in an expandable section
    with st.expander('other animals share weight'):
        st.info(others_memory.buffer)
