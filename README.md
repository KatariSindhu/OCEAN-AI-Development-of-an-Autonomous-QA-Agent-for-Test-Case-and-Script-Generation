# OceanAI: Autonomous QA Agent 🌊

## 🚀 Overview
OceanAI is an intelligent, autonomous QA system designed to revolutionize software testing. It acts as a "Testing Brain" that ingests project documentation, understands web structures, and autonomously generates:

1.  **Test Plans:** Comprehensive positive/negative test cases grounded in documentation.
2.  **Automation Scripts:** Self-healing Selenium (Python) scripts mapped to real HTML selectors.

## 🛠️ Tech Stack
* **Frontend:** Streamlit (Reactive UI)
* **Backend:** FastAPI (High-performance API)
* **AI Engine:** Google Gemini 1.5 Flash (via Direct REST API for network resilience)
* **Memory:** ChromaDB + HuggingFace Embeddings (Local Vector Store)
* **Resilience:** Implements **Circuit Breaker Pattern** (Stability Mode) to ensure system uptime during API outages.

## ⚙️ Setup Instructions

### 1. Prerequisites
* Python 3.9+
* Google API Key (configured in `.env`)

### 2. Installation
1.  Clone the repository or download the source code.
2.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3.  Create a `.env` file in the root directory:
    ```env
    GOOGLE_API_KEY=your_api_key_here
    ```



### 3. Running the System
**Step 1: Start the Intelligence Backend**
Open a terminal and run:
```bash
python -m uvicorn backend:app --reload
```
**Step 2: Launch the UI Open a new terminal and run:**

```bash
streamlit run frontend.py
```



### 🧠 Key Features (Novelty)
**1. Direct API Layer:** Bypasses standard library wrappers to use raw HTTP/REST for enterprise-grade connectivity and to resolve gRPC conflicts.

**2.Circuit Breaker Pattern:** Includes a fallback "Stability Mode". If the external AI provider experiences downtime or safety blocks, the system automatically switches to a backup logic engine, ensuring the QA team can continue working without interruption.

**3.Strict Grounding:** The RAG (Retrieval-Augmented Generation) pipeline ensures test cases are generated strictly from the uploaded product_specs.md, preventing AI hallucinations.



### Project Structure
**1.backend.py:** The FastAPI server containing the AI logic and Circuit Breaker.

**2.frontend.py:** The Streamlit interface for uploading docs and generating scripts.

**3.checkout.html:** The target web application being tested.

**4.product_specs.md:** The requirement rules for the AI to learn.


