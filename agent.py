import os
from typing import List

from openai import OpenAI
from toolhouse import Toolhouse, Provider

# Load API keys from environment variables
TOOLHOUSE_API_KEY = os.getenv("TOOLHOUSE_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")# Initialize Anthropic and Toolhouse clients
client = OpenAI(api_key=OPENAI_API_KEY)
th = Toolhouse(access_token=TOOLHOUSE_API_KEY, provider=Provider.OPENAI)
MODEL = 'gpt-4o-mini'

# Set timezone for the AI Agent
th.set_metadata('timezone', '-7')

# Define system message for the AI agent
system_message = """
        IMPORTANT: Be extremely concise in all your answers. Keep it to 280 characters.
        You are a great customer support agent for a headphones company that is taked to help customers. Answer the question as faithfully as you can.
        You only reply to questions after 6:00AM PDT. 
        You need to find out what the time is. If a question is asked before 6:00AM PDT, you must reply saying: "Sorry, Can't answer right now, please try again later."
        Retrieve knowledge from any source you have and provide the best answer you can.
        Your main source of knowledge is this file which you can access by using a web scraper, but only scrape it once: https://gist.githubusercontent.com/orliesaurus/be34b6b36e79c154c7a3cb625c448ac3/raw/0bbda12501d866eb405263485d099ae4e1b2db76/faqs_headphones.txt
        Only respond with the details of the answer, like a real customer support agent would do.
        """

# Initialize message history
messages: List = [{"role": "system", "content": system_message }]
# Flag to check if it's the first question
first_question = True

def process_response(messages):
    global first_question
    
    # Prompt user for question (different for first and follow-up questions)
    if first_question:
        input_question = input("Hi I am a customer support bot. What is your question?")

        first_question = False
    else:
        input_question = input("Do you have a follow up question?")
    
    # Exit if user types '/quit' '/exit'
    if input_question.lower() in ["/quit", "/exit"]:
        exit()

    
    # Add user's question to message history
    messages.append({"role": "user", "content": f"{input_question}" })
    
    # Generate initial response using Anthropic model
    response = client.chat.completions.create(
                model=MODEL,
                max_tokens=1024,
                # Get the tools from toolhouse SDK to perform actions based on the request
                tools=th.get_tools(),
                messages=messages
            )
    
    # Run tools based on the response
    messages += th.run_tools(response)
    
    # Generate final response
    agent_setup = client.chat.completions.create(
    model=MODEL,
    max_tokens=1024,
    tools=th.get_tools(),
    messages=messages
    )
    agent_reply = agent_setup.choices[0].message.content
    # Print AI agent's response
    print("\033[33mSupport AI AGENT:\033[0m", agent_reply)
    
    # Add AI's response to message history
    messages.append({"role": "assistant", "content": f"{agent_reply}" })

# Main loop to continuously process responses
while True:
    process_response(messages)