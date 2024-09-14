
import os
from dotenv import load_dotenv
from openai import OpenAI
from toolhouse import Toolhouse, Provider

# Load API keys from environment variables
load_dotenv()
TOOLHOUSE_API_KEY = os.getenv("TOOLHOUSE_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Initialize OpenAI and Toolhouse clients
client = OpenAI(api_key=OPENAI_API_KEY)
th = Toolhouse(access_token=TOOLHOUSE_API_KEY, provider=Provider.OPENAI)
MODEL = 'gpt-4o-mini'
# Set timezone for the Agent
th.set_metadata('timezone', '-7')

# A function that utilizes toolhouse integrated with OpenAI to make prompting very easy
def start_tool(messageList):
    # Creates the context to use the tools
    response = client.chat.completions.create(
        model=MODEL,
        max_tokens=1024,
        # Get the tools from toolhouse SDK to perform actions based on the request
        tools=th.get_tools(),
        messages=messageList
    )
    # Run tools based on the response
    messageList += th.run_tools(response)
    # Generate final response
    agent_setup = client.chat.completions.create(
    model=MODEL,
    max_tokens=1024,
    tools=th.get_tools(),
    messages=messageList
    )
    agent_reply = agent_setup.choices[0].message.content
    # Print AI agent's response
    print("\033[33mSupport AI AGENT:\033[0m", agent_reply)
    return agent_reply