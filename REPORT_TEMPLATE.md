# Academic Procedure Report: PS8 AI Product Description Writer

**Project Title:** AI Product Description Writer (PS8)  
**Domain:** Applied Artificial Intelligence / Natural Language Generation  
**Course:** Final Year Mini Project Laboratory  
**Academic Year:** 2025–2026  

---

## 1. Problem Statement & Motivation
E-commerce sellers and small businesses frequently face challenges drafting engaging marketing copy for product listings. Human copywriting can be time-consuming and inconsistent. 

**Objective:** Develop a lightweight, free-to-use web application that ingests product names, technical specifications, and intended audience profiles, and generates:
1. One catchy, marketing-ready product title.
2. Exactly three concrete customer benefits.
3. A focused product description of approximately 60 words.

The system must operate strictly within free, open-source constraints and never fabricate unmentioned features or specifications.

---

## 2. System Architecture & Technical Specifications

```
+-------------------------------------------------------------+
|               Streamlit Front-End Web Client                |
|  [Inputs: Product Name, Features, Target Audience, Tone]    |
+------------------------------+------------------------------+
                               |
                               | (Secure HTTP POST via Requests)
                               v
+-------------------------------------------------------------+
|                  OpenRouter API Gateway                     |
|         Header: Bearer Auth Token (.env sourced)            |
+------------------------------+------------------------------+
                               |
                               | (Zero-Cost Inference)
                               v
+-------------------------------------------------------------+
|           google/gemma-4-26b-a4b-it:free (Apache 2.0)       |
|      Enforced JSON Schema with Negative Grounding Rules     |
+------------------------------+------------------------------+
                               |
                               | (Validated JSON Response)
                               v
+-------------------------------------------------------------+
|            Result Parsing, Formatting & UI Render           |
|   - Title Card       - 3 Benefit Badges   - 60-Word Card   |
+-------------------------------------------------------------+
```

### Component Details
- **User Interface (Streamlit):** Reactive web framework providing form inputs, quick-sample triggers, state caching, and responsive rendering.
- **Security & Config (python-dotenv):** Loads keys from isolated local `.env` files, excluding credentials from source repositories.
- **Inference Pipeline (Requests + OpenRouter):** Dispatches asynchronous HTTP calls to the free `google/gemma-4-26b-a4b-it:free` model.
- **Output Sanitation Engine:** Custom regex and parser verifying JSON validity and enforcing the strict 3-benefit constraint.

---

## 3. Algorithm & Implementation Procedure

### Step-by-Step Procedure:
1. **User Input Collection:** Collects `Product Name`, `Features`, `Target Audience`, and `Tone` (Professional, Friendly, Luxury, Casual).
2. **Pre-Flight Input Validation:** Asserts that input strings are non-empty and verifies API key readiness.
3. **Prompt Construction with Guardrails:**
   - Injects a system instruction specifying the role of marketing copywriter.
   - Enforces strict anti-hallucination rules (zero invented specs, zero fake warranties/discounts).
   - Constrains output schema strictly to `{ "title": "...", "benefits": ["...", "...", "..."], "description": "..." }`.
4. **API Communication:** Transmits payload to OpenRouter endpoint with a 45-second timeout.
5. **Exception Handling:** Catches HTTP 401 (auth), HTTP 429 (rate quota), HTTP 503 (server maintenance), and connectivity failures.
6. **Data Extraction & Rendering:** Parses output into JSON, validates key presence, computes description word count, and displays formatted markdown and raw export blocks.

---

## 4. Experimental Results & Verification Summary

| Test Case | Product Input | Selected Tone | Observed Output Status | Word Count |
|:---|:---|:---|:---|:---:|
| TC-01 | AeroGlide Backpack | Professional | Valid JSON, 3 Benefits, Clear Title | 58 words |
| TC-02 | TerraPods Earbuds | Friendly | Valid JSON, 3 Benefits, Clear Title | 61 words |
| TC-03 | Lumina Desk Lamp | Luxury | Valid JSON, 3 Benefits, Clear Title | 64 words |
| TC-04 | HydroPure Steel Flask | Casual | Valid JSON, 3 Benefits, Clear Title | 56 words |
| TC-05 | PulseFit Smart Tracker | Professional | Valid JSON, 3 Benefits, Clear Title | 60 words |

---

## 5. Conclusion & Future Enhancements
The mini project successfully satisfies all design requirements:
- Zero financial cost utilizing the free Gemma model tier.
- Adherence to anti-hallucination marketing constraints.
- Clean user experience with quick-load presets, copy tools, and input validation.

**Future Scope:**
1. Multi-language output translation support.
2. Batch CSV export for multi-product retail catalogs.
3. SEO keyword density optimizer.
