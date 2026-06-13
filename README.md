# 🏏 Cricket FAQ Chatbot

An AI-powered FAQ chatbot built for the **CodeAlpha Artificial Intelligence Internship (Task 2)**. The bot uses NLP techniques to understand user questions about cricket and respond with the most relevant answer from a curated FAQ knowledge base.

## Overview

Instead of relying on exact keyword matches, this chatbot:

- Cleans and tokenizes user input using **NLTK** (lowercasing, punctuation removal, tokenization, custom stopword filtering tuned for cricket terminology).
- Converts both the FAQ dataset and user queries into **TF-IDF vectors**.
- Computes **cosine similarity** between the user's question and every FAQ entry, with additional scoring bonuses for exact matches and keyword overlap.
- Returns the best-matching answer if the confidence score is above a set threshold, or a helpful fallback message if not.

The result is a chatbot that can understand paraphrased or loosely-worded questions, not just exact copies of the stored FAQs.

## Features

- 📚 Large, structured FAQ dataset covering cricket rules, formats, IPL, players, records, bowling, batting, and DRS.
- 🧠 NLP preprocessing pipeline (tokenization, normalization, stopword filtering) via NLTK.
- 🔍 TF-IDF + cosine similarity matching with custom relevance scoring.
- 💬 Interactive chat interface built with Streamlit.
- 🎯 Confidence score shown alongside each matched answer.
- 💡 Sidebar with clickable "suggested questions" for quick exploration.
- 🔄 "Clear conversation" option to reset the chat.

## Tech Stack

- **Python**
- **Streamlit** – web-based chat interface
- **NLTK** – text preprocessing and tokenization
- **scikit-learn** – TF-IDF vectorization and cosine similarity

## Project Structure

```
CodeAlpha_FAQChatbot/
├── app.py            # Streamlit UI and chat logic
├── faq_engine.py     # NLP preprocessing and FAQ matching engine
├── faqs.py           # FAQ dataset (questions, answers, aliases, suggestions)
├── requirements.txt  # Project dependencies
└── README.md
```

## Setup & Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/flame-112/CodeAlpha_FAQChatbot.git
   cd CodeAlpha_FAQChatbot
   ```

2. (Optional) Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the app:
   ```bash
   streamlit run app.py
   ```

5. Open the local URL shown in the terminal (usually `http://localhost:8501`) in your browser.

## Usage

- Type a cricket-related question into the chat input (e.g., "What is DRS?" or "How many overs in an ODI?").
- The bot will match your question against its FAQ database and return the closest answer along with a confidence score.
- Use the sidebar's suggested questions for quick examples, or click "Clear conversation" to start fresh.

## How It Works (Under the Hood)

1. **Preprocessing**: User input and FAQ questions are lowercased, stripped of punctuation, tokenized, and filtered against a custom stopword list (preserving cricket-specific terms).
2. **Vectorization**: All FAQ entries (including aliases) are converted into TF-IDF vectors during initialization.
3. **Matching**: The user's processed query is vectorized and compared against all FAQ vectors using cosine similarity.
4. **Scoring**: Additional bonuses are applied for exact question matches and high keyword overlap, refining the ranked results.
5. **Response**: If the best score exceeds a threshold, the corresponding answer is returned; otherwise, a fallback message is shown.

## Acknowledgements

This project was built as part of the **CodeAlpha AI Internship Program** (Task 2: Chatbot for FAQs).
