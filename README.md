

# **IntelliSearch_CLI** 🚀  
_A Smart Context-Aware CLI Search Assistant using NLP and Machine Learning._

## **📌 Project Overview**  
IntelliSearch_CLI is an AI-powered command-line tool that provides **summarized search results** using Google Custom Search API. It applies **Natural Language Processing (NLP)** and **Machine Learning (ML)** to refine, rank, and present search results in a user-friendly way.  

---

## **🌟 Features**
✅ **Web Search Integration** – Uses Google Custom Search API to fetch relevant results.  
✅ **NLP Processing** – Extracts key insights from search results.  
✅ **Summarization** – Generates concise summaries of the search results.  
✅ **Machine Learning Ranking** – Ranks search results based on relevance.  
✅ **Command Line Interface (CLI)** – Simple, lightweight, and fast.  

---

## **🛠 Tech Stack**
🔹 **Python 3.x** – Programming language  
🔹 **Google Custom Search API** – Fetches web search results  
🔹 **spaCy** – NLP processing  
🔹 **NumPy & Scikit-learn** – Machine Learning ranking  
🔹 **dotenv** – Secure API key storage  
🔹 **Requests** – HTTP requests for API calls  

---

## **📂 Project Structure**
```
IntelliSearch_CLI/
│── .env                   # Stores API keys (DO NOT SHARE)
│── main.py                # Runs the CLI application
│── search_engine.py       # Handles web search
│── nlp_processing.py      # Processes search results using NLP
│── ml_model.py            # Machine learning ranking
│── requirements.txt       # Dependencies
│── README.md              # Project documentation
```

---

## **📥 Installation & Setup**

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/your-username/IntelliSearch_CLI.git
cd IntelliSearch_CLI
```

### **2️⃣ Create a Virtual Environment (Optional but Recommended)**
```bash
python -m venv venv
source venv/bin/activate  # On Mac/Linux
venv\Scripts\activate      # On Windows
```

### **3️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4️⃣ Set Up API Keys**
Create a `.env` file in the project directory and add your **Google API Key** & **Search Engine ID**:
```
API_KEY=your_google_api_key_here
CX_KEY=your_custom_search_engine_id_here
```

> **Get API Key & Search Engine ID:**  
> - [Google Cloud Console](https://console.cloud.google.com/) (API Key)  
> - [Google Custom Search Engine](https://programmablesearchengine.google.com/) (CX Key)

---

## **🚀 Usage**
Run the application:
```bash
python main.py
```

### **Example Interaction**
```bash
🔍 Enter search query (or type 'exit' to quit): AI in Healthcare

🔎 Searching, please wait...

1. How AI is Transforming Healthcare
   🔗 https://example.com/article1
   📄 AI in healthcare is revolutionizing diagnosis, treatment, and patient care...

2. The Future of AI in Medicine
   🔗 https://example.com/article2
   📄 Artificial Intelligence (AI) is rapidly changing the landscape of modern medicine...
```

To **exit**, type `exit`.

---

## **💡 How It Works**
1. **Takes a user input query** from the terminal.  
2. **Fetches web search results** from Google Custom Search API.  
3. **Processes the text** using NLP to extract key information.  
4. **Summarizes the results** to display concise insights.  
5. **Ranks the search results** using an ML model.  
6. **Displays output** in an easy-to-read format in the terminal.  

---

## **⚡ Future Improvements**
- [ ] Integrate **Gemini API** for enhanced AI-powered responses.  
- [ ] Implement **voice search** functionality.  
- [ ] Add **configurable search filters**.  
- [ ] Improve **ranking with deep learning**.  

---

## **📝 Contributing**
We welcome contributions!  
1. **Fork the repo**  
2. **Create a new branch** (`git checkout -b feature-name`)  
3. **Commit your changes** (`git commit -m "Add feature"`)  
4. **Push the branch** (`git push origin feature-name`)  
5. **Open a Pull Request** 🎉  

---


---

