# Import the necessary module
import os
from dotenv import load_dotenv
from typing import List
from pydantic import BaseModel
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware

# Importing System Prompts to command Toolhouse SDK
from SystemPrompts import *
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
# Set timezone for the AI Agent
th.set_metadata('timezone', '-7')

# Create FastAPI instance
app = FastAPI(title="Toolhouse Example Applications", description="This API routes queries using toolhouse to create multiple different usecases.", version="1.0.0")
# Allow all origins, methods, and headers
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

# The app will automatically serve the Swagger UI at /docs
# Root route redirects to the Swagger UI (/docs)
@app.get("/", include_in_schema=False)  # Exclude this route from appearing in Swagger UI
async def redirect_to_docs():
    return RedirectResponse(url="/docs")

# Create request schema
class UserInput(BaseModel):
    message: str
# Example Pet_Care endpoint to demonstrate the API functionality
@app.post("/pets", summary="Get a custom message", description="Returns a custom message string.")
async def get_pet_advice(request: UserInput): 
    system_message = pet_care_prompt.format(input = request.message)
    messages: List = [{"role": "system", "content": system_message}]
    return { "received_messages": start_tool(messages) }

# Example Route to Test the Toolhouse SDK
@app.post("/test", summary="Test the Toolhouse SDK", description="Returns a test response from the integrated tools.") 
async def run_test(request: UserInput): 
    system_message = test_prompt.format(input=request.message)
    messages: List = [{"role": "system", "content": system_message }]
    return { "received_messages": start_tool(messages) }

# Example Blog Endpoint to mark a first draft of research blog posts
@app.post("/blog", summary="Blog Draft Maker", description="Returns a blog post about your given topic including 3 embedded links")
async def get_blog(request: UserInput):
    system_message = blog_prompt.format(input = request.message)
    messages: List = [{"role": "system", "content": system_message }]
    return { "received_messages": start_tool(messages) }

# Example Customer Service endpoint to answer customer service questions during open hours
@app.post("/customer", summary="Customer Service Agent", description="Returns a response from the customer service model that has RAG functionality based on your docs and can change request based on open and closing hours.")
async def answer_customer_question(request: UserInput):
    system_message = customer_agent_prompt
    messages: List = [{"role": "system", "content": system_message + request.message }]
    return { "received_messages": start_tool(messages) }

# Example Twitter endpoint to find ideal customers
@app.post("/twitter", summary="Twitter Audience Finder", description="Returns the First and Last Name of a Twitter User and we use this with the hunter.io API to get valid emails and Toolhouse can send the email")
async def get_email(request: UserInput):
    system_message = twitter_emailer_prompt.format(input = request.message)
    messages: List = [{"role": "system", "content": system_message }]
    return { "received_messages": start_tool(messages) }



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

# Run the app using Uvicorn
if __name__ == "__main__":
    import uvicorn
    print("\033[33mSupport AI AGENT:\033[0m", "You can try the app by opening the 'demo.html' file")
    uvicorn.run(app)