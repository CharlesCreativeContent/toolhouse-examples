
# <img src="https://framerusercontent.com/images/xDisAjh26hdfRjOto5SnUUWvsEQ.svg?scale-down-to=64" width="50" style="position: relative; top: 10px">  Toolhouse Examples
Toolhouse is a platform that helps developers integrate tools in their projects, to build powerful AI agents. 

You can start this journey with only 3 lines of code.

In this repo we'll explore some examples of different ways you can leverage our pre-built tools and create applications that can perform many useful tasks. This project also demonstrates how to build an API that integrates Toolhouse SDK and OpenAI's GPT models to create various use cases. It provides endpoints for customer service, blog writing, pet care, and more.

Feel free to check out the [video](https://www.canva.com/design/DAGQlTTAn1U/EF1oa2jYMTZAl7F3N-djuQ/view?utm_content=DAGQlTTAn1U&utm_campaign=designshare&utm_medium=link&utm_source=editor) summarizing this repo.

## Step 1: Clone the Repository
```bash
git clone https://github.com/CharlesCreativeContent/toolhouse-example.git
cd toolhouse-example
```

## Step 2: Set Up Environment Variables
Create a .env file in the root directory of the project and add your Toolhouse and OpenAI API keys:
```bash
TOOLHOUSE_API_KEY=your_toolhouse_api_key
OPENAI_API_KEY=your_openai_api_key
```

## Step 3: Install Dependencies
Make sure to install the required dependencies by running:
```bash
pip install -r requirements.txt
```

## Step 4: Run the Application
Once all dependencies are installed, you can start the server with:

```bash
python app.py
```

The server will be running and you can view the API documentation at http://127.0.0.1:8000.

You can also also open the '**demo.html**' for an example Veterinary Clinic Application using the /pets Endpoint.

## Step 5: Test the API
The FastAPI application includes a Swagger UI that allows you to test the various endpoints. The following endpoints are available:

| Endpoint  | Description                                                                                   |
|-----------|-----------------------------------------------------------------------------------------------|
| /pets     | Answers Pet Owners using an Veterinary Clinics documents and can tell if the Clinic is open   |
| /blog     | Generates a first draft of a research blog post including embedded links.                     |
| /customer | Provides customer service answers, adapting to open and closing hours.                        |
| /twitter  | Returns details about Twitter users and sends emails using hunter.io API.                     |
| /test     | A test route to check the integration of the Toolhouse SDK.                                   |


## Understanding Toolhouse SDK
Toolhouse acts as an orchestration layer between the GPT model and various tools. The integration uses the Toolhouse SDK, which enables actions to be taken based on AI decisions. For instance, the AI can be able to send emails or retrieve customer support information by addding a tool in toolhouse instead of updating your code.

## Project Structure
**app.py**: This is the main file that sets up the FastAPI and integrates Toolhouse with OpenAI's GPT models.

**SystemPrompts.py:** This file contains pre-configured system prompts that are passed into the API to shape the behavior of each endpoint.

**demo.html:** This file contains an example of the rag and search tools on a web page, for a Veterinary Clinic

## How Toolhouse helps
Today's LLM technology doesn't need to run any code itself. Instead, you can run code externally. Get response with more context on what tools the LLM should use in your toolhouse,  a function to run those tools, and the LLM uses that to provide a more targeted generation, but also a long list of new capabilities.

Writing good tools is a long and time-consuming exercise which requires a lot of efforts. You have to write definitions of inputs and outputs, robust error handling, handle the infrastructure to host the tool and most importantly effective communication with the model. Every model implements function calling slightly differently. This causes challenges in schema design, logic implementation, and interaction management.

## ✨ Using Toolhouse -
You can use tools that have been written and maintained by developers like you. These tools work with any LLM that supports tool use. As most developers use more than one LLM provider in their deployments, Toolhouse is designed to help you manage your functions across each model.

## Get help
Our growing community awaits you: We're looking forward to meet you and while we focus on subjects relevant to Toolhouse, AI or code we're happy to chat about anything.

[Join us on Discord](https://discord.gg/xPvyBxhHtu)



