# AI Fashion Design Generator

A comprehensive AI-powered fashion design application built with Streamlit and Google's Gemini AI.

## Overview

AI Fashion Design Generator is an intelligent web application that leverages Google's Gemini 2.5 Flash model to help users create, analyze, and discover fashion designs. The app includes a design generator, outfit analyzer, product finder, and trend insights engine. Perfect for fashion enthusiasts, designers, and shoppers looking for AI-powered fashion inspiration and analysis.

## Features

- 🎨 **Fashion Designer**: Generate detailed fashion designs based on preferences and descriptions
- 📸 **Outfit Analyzer**: Upload and analyze clothing images with AI insights
- 🛍️ **Product Suggestions**: Find affordable similar products from online stores (Amazon, Flipkart, Myntra, etc.)
- 📈 **Trend Insights**: Analyze current fashion trends and market demand
- ⚙️ **Fashion Preferences**: Save and customize your style profile (gender, category, style, colors, fabric)
- 💬 **AI-Powered Responses**: Detailed fashion recommendations powered by Gemini AI

## Requirements

- Python 3.8+
- Google Gemini API Key

## Installation

1. Clone or download this project
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Setup & Configuration

### Get Your Gemini API Key

1. Visit [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Sign in with your Google account
3. Click **"Create API key"** button
4. Copy the generated API key

### Configure API Key with Streamlit Secrets

The application uses Streamlit's secrets management for secure API key storage.

**Option 1: Local Development**

1. Create a `.streamlit` folder in your project root:
   ```bash
   mkdir .streamlit
   ```
2. Create a `secrets.toml` file inside `.streamlit/`:
   ```bash
   touch .streamlit/secrets.toml
   ```
3. Add your API key to `secrets.toml`:
   ```toml
   GEMINI_API_KEY = "your-api-key-here"
   ```
4. **Important**: Add `.streamlit/secrets.toml` to your `.gitignore` to prevent committing secrets!

**Option 2: Streamlit Cloud Deployment**

1. Push your code to GitHub (without secrets.toml)
2. Deploy on [Streamlit Cloud](https://streamlit.io/cloud)
3. In the app settings, go to **Secrets** tab
4. Add your secret:
   ```toml
   GEMINI_API_KEY = "your-api-key-here"
   ```

## Usage

1. Ensure your API key is configured in `.streamlit/secrets.toml`
2. Run the application:
   ```bash
   streamlit run AI-Fashion.py
   ```
3. The app will launch in your default browser at `http://localhost:8501`

### Using the App

**Fashion Designer Tab** 🎨
- Set your fashion preferences in the sidebar (gender, clothing type, style, colors, fabric)
- Describe your fashion idea in the text area
- Click "Generate Fashion Design" to create detailed designs
- Download the design as a text file

**Outfit Analyzer Tab** 📸
- Upload a fashion image (JPG, JPEG, or PNG)
- Click "Analyze Outfit" to get AI insights on colors, style, occasion, and pricing

**Product Suggestions Tab** 🛍️
- Click "Find Similar Products" to get affordable product recommendations
- Suggestions include brand, price, and online store links

**Trend Insights Tab** 📈
- Enter a fashion category (e.g., "Streetwear", "Formal Wear")
- Click "Analyze Trends" to see trending colors, fabrics, and future predictions

### First Run Checklist

- [ ] `.streamlit/secrets.toml` file created with `GEMINI_API_KEY`
- [ ] All dependencies installed: `pip install -r requirements.txt`
- [ ] Internet connection available (required for API calls)
- [ ] Application loads without errors at `http://localhost:8501`

## Dependencies

- **streamlit**: Web application framework
- **google-generativeai**: Google Gemini API client
- **pillow**: Image processing library

## Project Structure

```
AI Fashion/
├── AI-Fashion.py       # Main application file
├── requirements.txt    # Project dependencies
└── README.md          # This file
```

## License

MIT License

## Troubleshooting

### "Error: Secret key not found"
- Ensure `.streamlit/secrets.toml` exists in your project root
- Verify the file contains: `GEMINI_API_KEY = "your-key"`
- Restart Streamlit: `Ctrl+C` and run `streamlit run AI-Fashion.py` again

### "Error: Invalid API key"
- Check that your API key in `secrets.toml` is correct and active
- Visit [Google AI Studio](https://aistudio.google.com/app/apikey) to verify your key
- Ensure there are no extra spaces around the key value

### "ModuleNotFoundError"
- Install all dependencies: `pip install -r requirements.txt`
- Verify you're using the correct Python environment

### Application won't start
- Check that port 8501 is not in use
- Run with debug mode: `streamlit run AI-Fashion.py --logger.level=debug`
- Ensure `.streamlit/secrets.toml` is properly configured

## Support

For issues or questions, please refer to:
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Google Gemini API Documentation](https://ai.google.dev/docs)
