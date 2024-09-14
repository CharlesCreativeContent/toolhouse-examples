# Import the necessary module
from typing import List
from pydantic import BaseModel
from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware

# Importing System Prompts to command Toolhouse SDK
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

# Importing System Prompts to command Toolhouse SDK
from system_prompts import *
from start_tool import *

# Create FastAPI instance
app = FastAPI(title="Toolhouse Example Applications", description="This API routes queries using toolhouse to create multiple different usecases.", version="1.0.0")
# Allow all origins, methods, and headers - FOR TESTING! CHANGE IN PRODUCTION!
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

# Serves the Swagger UI at /docs so developers can quickly get into the tool
# Root route redirects to the Swagger UI (/docs)


# Initialize HTML templates
templates = Jinja2Templates(directory="./")

@app.get("/", response_class=HTMLResponse, include_in_schema=False)
async def read_root(request: Request):
    return templates.TemplateResponse("demo.html", {"request": request, "app_name": "Pet Guru App"})

# Create request schema
class UserInput(BaseModel):
    message: str
# Example Pet_Care endpoint to demonstrate the API functionality
@app.post("/pets", summary="Talk to a Veterinarian", description="Answers Pet Owners using an animal hospitals documents and can even tell if the Clinic is open in your area.")
async def get_pet_advice(request: UserInput): 
    chatHistory: List = [{"role": "system",
        "content": pet_care_prompt.format(input = request.message)
        }]
    return { "received_messages": start_tool(chatHistory) }

# Example Route to Test the Toolhouse SDK
@app.post("/test", summary="You can test the Toolhouse SDK", description="Returns a test response from the integrated tools.") 
async def run_test(request: UserInput): 
    chatHistory: List = [{"role": "system",
        "content": test_prompt.format(input = request.message)
        }]
    return { "received_messages": start_tool(chatHistory) }

# Example Blog Endpoint to mark a first draft of research blog posts
@app.post("/blog", summary="Blog Draft Maker", description="Returns a blog post about your given topic including 3 embedded links")
async def get_blog(request: UserInput):
    chatHistory: List = [{"role": "system",
        "content": blog_prompt.format(input = request.message)
        }]
    return { "received_messages": start_tool(chatHistory) }

# Example Customer Service endpoint to answer customer service questions during open hours
@app.post("/customer", summary="Customer Service Agent", description="Returns a response from the customer service model that has RAG functionality based on your docs and can change request based on open and closing hours.")
async def answer_customer_question(request: UserInput):
    chatHistory: List = [{"role": "system",
        "content": customer_agent_prompt + request.message
        }]
    return { "received_messages": start_tool(chatHistory) }

# Example Twitter endpoint to find ideal customers
@app.post("/twitter", summary="Twitter Audience Finder", description="Returns the First and Last Name of a Twitter User and we use this with the hunter.io API to get valid emails and Toolhouse can send the email")
async def get_email(request: UserInput):
    chatHistory: List = [{"role": "system",
        "content": twitter_email_prompt.format(input = request.message)
        }]
    return { "received_messages": start_tool(chatHistory) }


# Run the app using Uvicorn
if __name__ == "__main__":
    import uvicorn
    print("\033[33mSupport AI AGENT:\033[0m", "You can try the app by opening the 'demo.html' file")
    uvicorn.run(app)