# Langchain Demo

This project demonstrates the integration of Langchain with OpenAI's GPT models to create a simple web application using Streamlit. The application takes a user's query about animals, finds information about the specified animal, retrieves its approximate weight, and then lists other animals with a similar weight.

## Features

- **Search for Animals**: Enter the name of an animal to retrieve detailed information, its approximate weight, and other animals with similar weights.
- **Conversation Memory**: Utilizes conversation memory to keep track of the search history and related information.
- **Streamlit Interface**: A simple and user-friendly web interface for interacting with the application.
- ## How It Works
The application is built using several key components from the Langchain and Streamlit libraries:

1. **OpenAI Integration**: Utilizes the OpenAI API to process natural language queries and generate responses.
2. **Streamlit App**: Creates an interactive web interface where users can input queries and view responses.
3. **Langchain Chains and Prompts**: Implements a sequence of language model chains to handle different stages of information retrieval.

### Code Structure

- **Environment Setup**: Retrieves the OpenAI API key from the environment variables.
- **Streamlit Interface**: Initializes the web app's title and input field.
- **Memory Buffers**: Sets up memory buffers to store the conversation history for different stages of the query process.
- **Prompt Templates**: Defines templates for the queries to be sent to the language model.
- **LLM Chains**: Each chain handles a specific part of the conversation, fetching and processing the required information.
- **Sequential Chain**: Combines individual chains into a single process, orchestrating the flow of information retrieval and response generation.

### Execution Flow

1. The user enters a search query related to animals.
2. The first chain fetches general information about the specified animal.
3. The second chain obtains the approximate weight of the animal.
4. The third chain finds other animals with a similar weight.
5. The results are displayed in the Streamlit app, with details available in expandable sections.

## Running the Application
To run this application, you will need Python installed on your system, along with the required packages: `streamlit`, `langchain_openai`, and `langchain`.

1. Clone this repository to your local machine.
2. Navigate to the project directory in your terminal.
3. Run the command `streamlit run app.py` (replace `app.py` with the filename of this script).
4. The Streamlit interface will open in your default web browser, where you can interact with the application.

## Dependencies
- Python 3.8+
- streamlit
- langchain_openai
- langchain

Ensure you have the OpenAI API key set as an environment variable `OPENAI_API_KEY` before running the application.

## Future Enhancements
- Expand the range of topics beyond animals to include plants, geography, etc.
- Implement additional memory and context management features for more complex conversations.
- Enhance the user interface with advanced features like visual representations of data.


## Installation

To run this project, you need to have Python installed on your system. If you do not have Python installed, you can download it from [python.org](https://www.python.org/downloads/).

1. **Clone the Repository**

   ```bash
   git clone https://github.com/gapilongo/langchain.git
   cd langchain-demo
