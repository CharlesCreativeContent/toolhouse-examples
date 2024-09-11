from typing import List
from pydantic import BaseModel
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from useTool import startTool

# Create FastAPI instance
app = FastAPI(title="Toolhouse Example Applications", description="This API routes queries using toolhouse to create multiple different usecases.", version="1.0.0")

# The app will automatically serve the Swagger UI at /docs
# Root route redirects to the Swagger UI (/docs)
@app.get("/", include_in_schema=False)  # Exclude this route from appearing in Swagger UI
async def redirect_to_docs():
    return RedirectResponse(url="/docs")

# Create request schema
class UserInput(BaseModel):
    message: str

# Example endpoint to demonstrate the API functionality
@app.post("/message", summary="Get a custom message", description="Returns a custom message string.")
async def get_message(request: UserInput): # Extract the message from the request

    system_message = """
        IMPORTANT: Be extremely concise in all your answers. Keep it to 280 characters.
        You are a great customer support agent for a headphones company that is taked to help customers. Answer the question as faithfully as you can.
        You only reply to questions after 6:00AM PDT. 
        You need to find out what the time is. If a question is asked before 6:00AM PDT, you must reply saying: "Sorry, Can't answer right now, please try again later."
        Retrieve knowledge from any source you have and provide the best answer you can.
        Your main source of knowledge is this file which you can access by using a web scraper, but only scrape it once: https://gist.githubusercontent.com/orliesaurus/be34b6b36e79c154c7a3cb625c448ac3/raw/0bbda12501d866eb405263485d099ae4e1b2db76/faqs_headphones.txt
        Only respond with the details of the answer, like a real customer support agent would do.
        """
    
    messages: List = [{"role": "system", "content": system_message + request.message }]

    
    return {
        "received_messages": startTool(messages),
        }

# Run the app using Uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)