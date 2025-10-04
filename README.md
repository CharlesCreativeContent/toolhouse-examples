
# <img src="https://framerusercontent.com/images/xDisAjh26hdfRjOto5SnUUWvsEQ.svg?scale-down-to=64" width="50" style="position: relative; top: 10px">  Building an AI Clinic Agent using Toolhouse

<a href="https://shawncharles.com/toolhouse"><img src="https://github.com/CharlesCreativeContent/myImages/blob/main/images/PetGuru.png?raw=true"></a>

Toolhouse is a platform that enables developers to integrate tools into their projects to build powerful AI agents effortlessly. With Toolhouse, you can leverage pre-built tools and create applications that perform a multitude of useful tasks with minimal code.

Feel free to check out the [video](https://youtu.be/LwKPnH0198E) to see Toolhouse in action.

<a href="https://youtu.be/LwKPnH0198E"><img src="https://github.com/CharlesCreativeContent/myImages/blob/main/images/ToolhouseThumbnail.png?raw=true"></a>

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
The server will be running, and you can view the demo application at http://127.0.0.1:8000 and the API documentation at http://127.0.0.1:8000/docs

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
- **demo.html**: Web page demonstrating the retrieval augmented generation (RAG) and search tools for a veterinary clinic.

## Understanding Toolhouse SDK
Toolhouse acts as an orchestration layer between GPT models and various tools. By integrating the Toolhouse SDK, you enable AI models to perform actions based on decisions made during interactions. For instance, the AI can send emails or retrieve customer support information by adding a tool in Toolhouse without the need to update your code.

## More Projects

<table bordercolor="#66b2b2">
  
  <tr>
    <td width="33.3%"  style="align:center;" valign="top">
<a target="_blank" href="https://github.com/CharlesCreativeContent/runware-pokemon-generator">Runware Pokémon Generator</a>
        <br />
      <a target="_blank" href="https://github.com/CharlesCreativeContent/runware-pokemon-generator">
            <img src="https://github.com/CharlesCreativeContent/runware-pokemon-generator/raw/main/public/runware.gif?raw=true" width="100%"  alt="Runware Pokémon Generator"/>
        </a>
    </td>
    <td width="33.3%" valign="top">
<a target="_blank" href="https://github.com/CharlesCreativeContent/CoinGecko-Thesys-MCP">CoinGecko-Thesys-MCP</a>
      <br />
        <a target="_blank" href="https://github.com/CharlesCreativeContent/CoinGecko-Thesys-MCP">
          <img src="https://camo.githubusercontent.com/0dd2f60eb61954fb96f89c3c31fe17bdd70d5eede3adf617adca4db22e937638/68747470733a2f2f736861776e696d616765732e6e65746c6966792e6170702f696d616765732f436f696e4765636b6f2e676966" width="100%" alt="CoinGecko-Thesys-MCP"/>
        </a>
    </td>
    <td width="33.3%" valign="top">
<a target="_blank" href="https://github.com/CharlesCreativeContent/Demo-Day">Travel Web-Application</a>
        <br />
        <a target="_blank" href="https://github.com/CharlesCreativeContent/Demo-Day">
          <img src="https://github.com/CharlesCreativeContent/CharlesCreativeContent/raw/main/images/gif1.gif?raw=true" width="100%" alt="Portfolio"/>
        </a>
    </td>
  </tr>
</table>
