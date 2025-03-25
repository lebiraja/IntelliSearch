# **IntelliSearch** 🚀  
_A Smart Context-Aware Search Assistant using NLP and Machine Learning._

## **📌 Project Overview**  
IntelliSearch is an AI-powered search tool that provides **summarized search results** using Google Custom Search API. It applies **Natural Language Processing (NLP)** and **Machine Learning (ML)** to refine, rank, and present search results in a user-friendly way. The application now features a **Streamlit-based UI** for an enhanced user experience.

---

## **🌟 Features**
✅ **Web Search Integration** – Uses Google Custom Search API to fetch relevant results.  
✅ **NLP Processing** – Extracts key insights from search results.  
✅ **Summarization** – Generates concise summaries of the search results.  
✅ **Machine Learning Ranking** – Ranks search results based on relevance.  
✅ **User Interface (UI)** – A web-based UI built with **Streamlit** for ease of use.  

---

## **🛠 Tech Stack**
🔹 **Python 3.x** – Programming language  
🔹 **Google Custom Search API** – Fetches web search results  
🔹 **spaCy** – NLP processing  
🔹 **NumPy & Scikit-learn** – Machine Learning ranking  
🔹 **dotenv** – Secure API key storage  
🔹 **Requests** – HTTP requests for API calls  
🔹 **Streamlit** – Web-based UI framework  

---

## **📂 Project Structure**
```
IntelliSearch/
│── .env                   # Stores API keys (DO NOT SHARE)
│── app.py                # Runs the Streamlit UI application
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
git clone https://github.com/your-username/IntelliSearch.git
cd IntelliSearch
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
streamlit run app.py
```

### **Using the Web Interface**
1. Open the **Streamlit app** in your browser.
2. Enter your **search query** in the input field.
3. Click the **Search** button to retrieve summarized and ranked search results.
4. The results will be displayed in an interactive format with titles, links, and summaries.

---

## **💡 How It Works**
1. **Takes a user input query** from the UI.  
2. **Fetches web search results** from Google Custom Search API.  
3. **Processes the text** using NLP to extract key information.  
4. **Summarizes the results** to display concise insights.  
5. **Ranks the search results** using an ML model.  
6. **Displays output** in an interactive web-based UI.  

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

## **🤝 Contributing**  
Feel free to contribute by improving the model, dataset, or adding new features.  

Happy coding! 🚀
