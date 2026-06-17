# AI Fashion

An intelligent fashion application powered by Google's Gemini AI API and Streamlit.

## Overview

AI Fashion is a web-based application that leverages Google's Gemini 2.5 Flash model to provide AI-driven fashion insights, recommendations, and analysis. Users can upload images and interact with the AI to get fashion-related information and suggestions.

## Features

- 🖼️ **Image Upload**: Upload fashion images for analysis
- 🤖 **AI-Powered Analysis**: Utilize Google Gemini AI for intelligent fashion insights
- 💬 **Interactive Interface**: User-friendly Streamlit web interface
- 🎨 **Image Processing**: Built-in image handling with Pillow

## Requirements

- Python 3.8+
- Google Gemini API Key

## Installation

1. Clone or download this project
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your Gemini API key:
   - Get your API key from [Google AI Studio](https://aistudio.google.com/app/apikey)
   - Open `AI-Fashion.py` and replace `YOUR_GEMINI_API_KEY_HERE` with your actual API key

## Usage

Run the application with:
```bash
streamlit run AI-Fashion.py
```

The app will launch in your default browser at `http://localhost:8501`

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

## Support

For issues or questions, please refer to:
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Google Gemini API Documentation](https://ai.google.dev/docs)
