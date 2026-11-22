# PS8 – AI Product Description Writer

An enterprise-grade, lightweight web application built for final-year college mini-project submissions. It automatically generates an attractive product title, exactly three customer benefits, and an approximately 60-word marketing description from raw product specifications and target audience details using free-tier models on OpenRouter.

---

## 📌 Project Overview
- **Project Code:** PS8
- **Core Functionality:** Transforms product name, features, and target audience into conversion-oriented marketing assets.
- **Strict Grounding:** Prohibits hallucinated specifications, fake certifications, fabricated warranties, or false discounts.
- **Structured Output:** Strictly outputs 1 attractive title, exactly 3 distinct benefits, and a concise ~60-word description.
- **Automated Fallback Architecture:** Automatically handles rate limits (HTTP 429) and upstream maintenance (HTTP 502/503) by seamlessly switching to free backup models.

---

## 🛠️ Technology Stack
- **Programming Language:** Python 3.10+
- **Web Framework:** Streamlit
- **HTTP Client:** Requests
- **Environment Management:** python-dotenv
- **Inference Gateway:** OpenRouter API
- **AI Models (100% Free Tier):**
  - **Primary Model:** `baidu/ernie-5.5-flash-preview:free` (configurable via `OPENROUTER_MODEL` in `.env`)
  - **Fallback Model 1:** `nvidia/nemotron-3-ultra-550b-a55b:free`
  - **Fallback Model 2:** `inclusionai/ling-3.2-flash:free`

---

## 📁 Repository Structure
```text
Genai_AI_product_description_writer/
│
├── app.py                 # Streamlit web application & multi-model fallback engine
├── test_app.py            # Unit tests for JSON extraction, markdown unwrapping & schema
├── requirements.txt       # Project dependencies
├── .env.example           # Environment template (keys & primary model)
├── .gitignore             # Exclusion rules for secrets, virtual environments & cache
├── LICENSE                # Open-source MIT license
├── README.md              # Project documentation & setup instructions
├── REPORT_TEMPLATE.md     # Two-page college mini-project procedure report
└── TESTING.md             # Detailed test matrix, edge cases & 5 sample product cases
```

---

## ⚡ Quick Setup Guide (Windows)

### 1. Prerequisites
Ensure Python is installed on your computer:
```cmd
python --version
```

### 2. Create and Activate Virtual Environment
Open Command Prompt or PowerShell in the project directory:
```cmd
cd /d E:\Genai
python -m venv venv
venv\Scripts\activate
```

### 3. Install Required Dependencies
```cmd
pip install -r requirements.txt
```

### 4. Configure Environment Variables
1. Get a free API key from [OpenRouter](https://openrouter.ai/).
2. Copy `.env.example` to create your local `.env`:
   ```cmd
   copy .env.example .env
   ```
3. Set your API key and primary model in `.env`:
   ```env
   OPENROUTER_API_KEY=sk-or-v1-xxxxxxxxxxxxxxxxxxxx
   OPENROUTER_MODEL=baidu/ernie-5.5-flash-preview:free
   ```

### 5. Launch the Web Application
```cmd
streamlit run app.py
```
The application will open automatically in your browser at:
`http://localhost:8501`

---

## ✨ Features
1. **Modern Responsive UI:** Polished interface with hero header, clean cards, and responsive equal-height benefit containers.
2. **Preset Sample Loader:** Collapsible drawer to quickly test products (e.g., Smart Backpack, Eco Earbuds).
3. **Four Tone Options:** Professional, Friendly, Luxury, and Casual.
4. **Three Equal-Height Benefit Cards:** Dynamically styled equal-length cards (`BENEFIT 01`, `BENEFIT 02`, `BENEFIT 03`).
5. **Concise Description (~60 Words):** Accurately sized marketing copy grounded strictly in user features.
6. **1-Click Copy Box:** Clean markdown block containing the complete marketing kit without raw JSON clutter.
7. **Instant `.txt` Download:** A download button exporting `[Product_Name]_Marketing_Kit.txt` ready for college project submission.
8. **Live Terminal Logging:** Detailed request and response logs printed directly in the terminal for debugging.
9. **Automatic Free-Tier Fallback:** Respects `Retry-After` headers and switches between free models on rate limits.

---

## 🔒 Security & Policy Compliance
- **Zero Paid Model Guarantee:** The app programmatically enforces that every candidate model ends with `:free`.
- **Credential Protection:** The `.env` file is excluded via `.gitignore` and is never exposed in the UI or committed to GitHub.
- **No Local Model Weights:** Uses zero local disk space for AI weights; all inference occurs via the free API.

---

<img width="1917" height="865" alt="image" src="https://github.com/user-attachments/assets/708fcc03-16db-4939-b7dd-aa18135be053" />
<img width="1917" height="870" alt="image" src="https://github.com/user-attachments/assets/c3525198-f588-4948-aa9a-e1a31dc1d1ca" />
<img width="1917" height="867" alt="image" src="https://github.com/user-attachments/assets/b623df47-f99f-45bb-b056-1c175c9b445e" />
<img width="1917" height="867" alt="image" src="https://github.com/user-attachments/assets/733bfee3-9721-42c6-a80b-6bb5fbeb32ca" />





---

## 🌐 GitHub Repository
Official repository link:
[https://github.com/ritisha12345/Genai_AI_product_description_writer.git](https://github.com/ritisha12345/Genai_AI_product_description_writer.git)
