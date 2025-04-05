# IntelliSearch

IntelliSearch is a powerful, interactive chatbot built using Streamlit that combines the capabilities of real-time web search and a local large language model (LLM) to deliver highly relevant, context-aware responses. This application leverages Google Custom Search and the DeepSeek-R1 model from Ollama to simulate an intelligent virtual assistant.



---

## 🚀 Features

- 🔍 **Web Search Integration** — Uses Google Custom Search API to gather up-to-date web content.
- 🧠 **Local LLM Integration** — Powered by Ollama’s DeepSeek-R1 model for accurate and context-rich responses.
- 🧮 **TF-IDF Ranking** — Ranks search results based on textual similarity to the query.
- 🧼 **Cleaned Output** — Removes unwanted tags and formats the output for clarity.
- 🌐 **Interactive Web Interface** — Built with Streamlit for ease of use and instant feedback.

---

## 📷 Demo

![screenshot](https://github.com/lebiraja/IntelliSearch/assets/demo.png) <!-- Add screenshot path if available -->

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit**
- **Ollama (DeepSeek-R1)**
- **Google Custom Search API**
- **Scikit-learn (TF-IDF + Cosine Similarity)**

---

## 🧑‍💻 How It Works

1. User inputs a query.
2. Google Custom Search API retrieves relevant links and snippets.
3. Snippets are ranked based on TF-IDF similarity to the original query.
4. The top snippets are embedded into a prompt and sent to the DeepSeek-R1 model via Ollama.
5. The model’s response is cleaned and displayed.

---

## ⚙️ Installation

### 1. Clone the Repository
```bash
git clone https://github.com/lebiraja/IntelliSearch.git
cd IntelliSearch
```

### 2. Set Up Environment
```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure API Keys
Create a `.env` file in the root directory:
```
GOOGLE_API_KEY=your_google_api_key
CX_SEARCH_ENGINE_ID=your_custom_search_engine_id
```

### 5. Run the App
```bash
streamlit run main.py
```

---

## 📂 Project Structure

```
IntelliSearch/
├── .env                    # API keys (not committed)
├── main.py                # Core Streamlit application
├── requirements.txt       # Python dependencies
└── README.md              # Project overview and setup
```

---

## ✅ To Do / Improvements

- [ ] Add support for more LLM models
- [ ] Store chat history locally or in a database
- [ ] Improve prompt generation for LLM
- [ ] Add unit and integration tests
- [ ] Deploy using Docker or Streamlit Cloud

---

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 🙌 Acknowledgements

- [Ollama](https://ollama.com/) — for LLM model hosting
- [Google Custom Search](https://programmablesearchengine.google.com/about/) — for search integration
- [Streamlit](https://streamlit.io/) — for UI

---

## **🤝 Contributing**  
Feel free to contribute by improving the model, dataset, or adding new features.  

Happy coding! 🚀  

---




