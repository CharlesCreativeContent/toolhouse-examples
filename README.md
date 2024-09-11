# 💬 Toolhouse Playground

The Toolhouse Playground is an interactive environment that allows you to test [Toolhouse](https://toolhouse.ai) across various Language Models (LLMs) of your choice. It provides a user-friendly conversational interface to help you run and experiment with tools you add from the Tool Store.

- 🔄 Easily select and switch between different LLMs (across compatible providers) within the same conversation
- 🏷️ Conveniently set metadata to customize your experience
- 🧰 Quickly check your installed tools and their functionalities
- 🌊 Supports streaming responses by default for real-time interaction

## 🛠️ Configuration

1. Create a `.env` file by copying `.env.template`.
1. Add the relevant API Keys for any of the LLM providers you want to use.

You will need `TOOLHOUSE_API_KEY` and at least one other LLM API Key. If you don't provide an API key for a specific LLM provider, the Playground will throw an exception when you attempt to use it.

### 🚀 How to run it on your own machine


1. Install the required dependencies:

   ```
   $ pip install -r requirements.txt
   ```

2. Launch the app:

   ```
   $ streamlit run toolhouse_streamlit.py
   ```

## 🤝 Contributing

Toolhouse welcomes contributions from the developer community! If you'd like to contribute to the Toolhouse Playground, please consider the following:

- 🐛 Found a bug? Open an issue describing the problem and how to reproduce it.
- 💡 Have an idea for an improvement? Feel free to create an issue to discuss your suggestion.
- 🔧 Want to contribute code? Fork the repository, make your changes, and submit a pull request.

We appreciate all contributions and will review them as quickly as possible. Please ensure your code follows the project's coding standards and includes appropriate documentation.