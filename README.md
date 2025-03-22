Here's a **detailed and professional** `README.md` for your **Agentic Web App**, including **setup, environment variables, deployment, and usage instructions**.  

---

## **🌍 Agentic Web App**
🚀 **Autonomous Web Agent** using **LangChain, Groq, and Tavily** to **answer queries, perform web searches, and process files (PDF/CSV).**  

---

## **📌 Features**
✅ AI-powered responses using **Gemma-2 9B** (via **Groq API**)  
✅ Real-time **web search** using **Tavily API**  
✅ File upload support: **Extracts text from PDFs & displays CSV data**  
✅ **Streamlit-based UI** for interactive queries  
✅ **Dockerized deployment** for easy scaling  

---

## **🛠️ Setup & Installation**
### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/rahul0090392/agentic_app.git
cd agentic_app
```

### **2️⃣ Create & Activate a Virtual Environment**
```bash
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
```

### **3️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4️⃣ Set Up Environment Variables**
Create a `.env` file in the project root:
```bash
touch .env
```
Add the following variables:
```ini
GROQ_API_KEY=your_groq_api_key_here
TAVILY_API_KEY=your_tavily_api_key_here
```
🔹 **Where to get the keys?**  
- **Groq API Key** → [Groq Console](https://console.groq.com/)  
- **Tavily API Key** → [Tavily AI](https://tavily.com/)  

---

## **🚀 Running the App**
### **1️⃣ Local Development**
Run the Streamlit app:
```bash
streamlit run app.py --server.port=8501
```
Then open [http://localhost:8501](http://localhost:8501) in your browser.

---

## **📦 Docker Deployment**
### **1️⃣ Build the Docker Image**
```bash
docker build -t agentic_app .
```

### **2️⃣ Run the Container**
```bash
docker run -d -p 8501:8501 --env-file .env --name agentic_app agentic_app
```
Access it at **[http://localhost:8501](http://localhost:8501)**.

---

## **📜 Docker Compose Deployment**
Use **Docker Compose** for easier setup.
### **1️⃣ Start with Docker Compose**
```bash
docker-compose up -d
```

### **2️⃣ Stop the Containers**
```bash
docker-compose down
```

### **📂 `docker-compose.yml` (included in repo)**
```yaml
version: '3.8'

services:
  agentic_app:
    build: .
    container_name: agentic_app
    command: "streamlit run app.py --server.port=8501 --server.address=0.0.0.0"
    ports:
      - "8501:8501"
    env_file:
      - .env
    volumes:
      - .:/app  # Enables live code changes
    restart: unless-stopped
```

---

## **🌍 Cloud Deployment**
### **1️⃣ Deploy on AWS / GCP / Azure**
You can deploy using **Docker on EC2, GCP Compute Engine, or Azure App Service**.

### **2️⃣ Deploy on Render / Railway**
For **serverless deployment**, use:
- **Render** → [https://render.com/](https://render.com/)
- **Railway** → [https://railway.app/](https://railway.app/)

### **3️⃣ Deploy on Fly.io**
```bash
fly launch --name agentic-app
fly deploy
```

---

## **🔍 Usage Guide**
1️⃣ **Enter a query** to get AI-powered responses.  
2️⃣ **Upload a PDF or CSV** → Extracts text & displays data.  
3️⃣ **Web Search** → Uses Tavily API for real-time search.  

---

## **🛠️ Tech Stack**
- **LangChain** → AI agent framework  
- **Groq LLM** → AI model provider  
- **Tavily** → Web search API  
- **Streamlit** → Interactive UI  
- **Docker** → Containerized deployment  

---

## **📄 License**
This project is licensed under the **MIT License**.

---

## **🤝 Contributing**
1️⃣ Fork the repo  
2️⃣ Create a feature branch  
3️⃣ Commit your changes  
4️⃣ Open a **pull request** 🚀  

---
