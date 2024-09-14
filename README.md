
# <img src="https://framerusercontent.com/images/xDisAjh26hdfRjOto5SnUUWvsEQ.svg?scale-down-to=64" width="50" style="position: relative; top: 10px">  Building an AI Clinic Agent using Toolhouse

<a href="https://www.canva.com/design/DAGQuHYK3pg/ADfxZiNf3ys84vHOvvU2Jw/watch?utm_content=DAGQuHYK3pg&utm_campaign=designshare&utm_medium=link&utm_source=editor"><img src="https://github.com/CharlesCreativeContent/myImages/blob/main/images/ToolhouseThumbnail.png?raw=true"></a>

Toolhouse is a platform that enables developers to integrate tools into their projects to build powerful AI agents effortlessly. With Toolhouse, you can leverage pre-built tools and create applications that perform a multitude of useful tasks with minimal code.

You can start this journey with only three lines of code!

This repository explores examples of how you can use our pre-built tools to create applications for various use cases, such as customer service, blog writing, pet care, and more. It also demonstrates how to build an API that integrates the Toolhouse SDK with OpenAI's GPT models.

Feel free to check out our [demo video](https://www.canva.com/design/DAGQuHYK3pg/ADfxZiNf3ys84vHOvvU2Jw/watch?utm_content=DAGQuHYK3pg&utm_campaign=designshare&utm_medium=link&utm_source=editor) to see Toolhouse in action.

## Getting Started
### Step 1: Clone the Repository
```bash
git clone https://github.com/CharlesCreativeContent/toolhouse-example.git
cd toolhouse-example
```

### Step 2: Set Up Environment Variables
- Create a .env file in the root directory of the project and add your Toolhouse and OpenAI API keys:
```bash
TOOLHOUSE_API_KEY=your_toolhouse_api_key
OPENAI_API_KEY=your_openai_api_key
```

### Step 3: Install Dependencies
- Install the required dependencies by running:
```bash
pip install -r requirements.txt
```

### Step 4: Run the Application
- Once all dependencies are installed, you can start the server with:
```bash
python app.py
```
The server will be running, and you can view the API documentation at http://127.0.0.1:8000/docs.

You can also open the demo.html file in your browser to see an example Veterinary Clinic application using the /pets endpoint.

### Step 5: Test the API
The FastAPI application includes a Swagger UI that allows you to test the various endpoints. The available endpoints are:

## Endpoint Description
| Endpoint  | Description                                                                                   |
|-----------|-----------------------------------------------------------------------------------------------|
| /pets     | Answers pet owners using an veterinary clinics documents and can tell if the clinic is open   |
| /blog     | Generates a first draft of a research blog post including embedded links.                     |
| /customer | Provides customer service answers, adapting to open and closing hours.                        |
| /twitter  | Returns details about Twitter users and sends emails using hunter.io API.                     |
| /test     | A test route to check the integration of the Toolhouse SDK.                                   |

### Project Structure
- **app.py**: The main file that sets up the FastAPI application and integrates Toolhouse with OpenAI's GPT models.
- **system_prompts.py**: Contains pre-configured system prompts that shape the behavior of each endpoint.
- **demo.html**: An example web page demonstrating the retrieval and generation (RAG) and search tools for a Veterinary Clinic.

## Understanding Toolhouse SDK
Toolhouse acts as an orchestration layer between GPT models and various tools. By integrating the Toolhouse SDK, you enable AI models to perform actions based on decisions made during interactions. For instance, the AI can send emails or retrieve customer support information by adding a tool in Toolhouse without the need to update your code.

### Why Use Toolhouse?
Building tools for AI agents can be time-consuming and complex. You need to:

- Define inputs and outputs.
- Implement robust error handling.
- Manage infrastructure to host the tools.
- Ensure effective communication with the model.
- Deal with different function-calling implementations across models.

Toolhouse simplifies this process by providing a platform where you can use tools written and maintained by developers like you. These tools work with any LLM that supports tool use. As most developers use more than one LLM provider in their deployments, Toolhouse helps you manage your functions across each model seamlessly.

### Key Benefits
- **Ease of Integration:** Start using powerful tools with minimal code changes.
- **Community-Driven:** Leverage tools developed by a community of developers.
- **Cross-Compatibility:** Works with multiple LLM providers and models.
- **Scalability:** Easily add or update tools without modifying your existing codebase.

## Join Our Community
Our growing community awaits you! We're looking forward to meeting you. While we focus on subjects relevant to Toolhouse, AI, or code, we're happy to chat about anything.

[Join us on Discord](https://discord.gg/xPvyBxhHtu)


