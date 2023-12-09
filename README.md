# Denis' Silly Chatbot

This is a simple chatbot script that can answer questions using OpenAI's GPT-3.5 API.

## Usage

To use the denisbot:

1. Install the required packages: 

```
pip3 install openai
```

2. Export your OpenAI API key:

```
export OPENAI_API_KEY="YOUR_API_KEY" 
```

3. Run the denisbot script:

```
python3 denisbot.py
```

4. Ask the denisbot a question and it will attempt to respond using GPT-3.5.

```
# python3 denisbot.py
>>> Please tell me a dad joke

Why couldn't the bicycle stand up by itself? Because it was two-tired. 

>>> (...)
```

## Code Overview

The main logic is in \`denisbot.py\`. It does the following:

- Imports the OpenAI library
- Loads the API key from environment variable  
- Defines a \`get_response\` function that takes user input, sends it to GPT-3.5, and returns the response
- Runs an input loop to chat with the user

The key aspects are:

- Formatting the user prompt colorfully 
- Using the \`Completion.create\` method to generate text with GPT-3.5  
- Formatting the user prompt appropriately so GPT-3.5 can respond in a conversational way
- Handling API errors and retries
