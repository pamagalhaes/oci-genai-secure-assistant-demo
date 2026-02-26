# Secure vs Insecure AI Assistant (Oracle GenAI)

![Demo screenshot](assets/demo.png)

A side-by-side demonstration of secure vs insecure LLM interaction using Oracle Generative AI (OCI).

This project shows how prompt injection, data exfiltration attempts, and PII exposure can affect real-world AI applications — and how basic guardrails and logging mechanisms can mitigate these risks.

---

## Objective

Large Language Models (LLMs) are powerful, but unsafe usage can introduce serious risks:

- Prompt injection
- Jailbreak attempts
- Sensitive data leakage
- Lack of auditability

This demo compares two execution paths:

**Insecure Mode** – User input is sent directly to the LLM without validation  
**Secure Mode** – Input is validated, suspicious prompts are blocked, and PII is masked before output  

---

## Architecture Overview

User Input  
→ Guardrails (prompt inspection)  
→ OCI Generative AI (Cohere Command-R model)  
→ Optional PII masking  
→ Structured JSON logging  

The secure flow applies:

- Basic prompt injection detection (keyword-based)
- PII masking on model output
- Structured audit logs (JSONL)

All calls are made using Oracle OCI Generative AI SDK.

---

## Features

- Side-by-side comparison (Secure vs Insecure)
- Prompt injection detection
- Basic jailbreak detection
- PII masking
- Structured audit logging (JSONL format)
- Interactive attack scenarios (buttons)
- Built using Streamlit + OCI SDK

---

## Attack Scenarios Included

- Prompt Injection
- Jailbreak attempts
- Data exfiltration attempts
- PII repetition
- Safe, legitimate prompts

This allows clear visualization of how secure patterns change LLM behavior.

---

## Technologies Used

- Oracle Generative AI (OCI)
- Cohere Command-R model
- Python 3.9+
- Streamlit
- OCI Python SDK

---

## How to Run

Clone the repository:

```bash
git clone https://github.com/pamagalhaes/oci-genai-secure-assistant-demo.git
cd oci-genai-secure-assistant-demo
```
Create a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```
Install dependencies:

```bash
pip install oci streamlit python-dotenv
```
Make sure your OCI config file is properly set:

```bash
~/.oci/config
```
Then run:

```bash
streamlit run app.py
```

---

## Logging

All interactions are recorded in:

```bash
logs.jsonl
```
Each entry includes:
- Mode (secure/insecure)
- Action (allow/block)
- Reason
- Prompt preview
- Model used
- Region
- This simulates enterprise-grade auditability.

---

## Security Disclaimer

This project demonstrates basic guardrails for educational purposes.
It does NOT represent a full production-ready AI security architecture.
In production environments, additional layers such as:
- Context isolation
- Retrieval validation
- LLM output moderation
- Advanced policy engines
- Role-based access controls

should be implemented.

## Next Steps (Future Enhancements)

- RAG with document ingestion
- Vector search integration
- Policy-based guardrails
- Risk scoring instead of keyword detection
- Observability dashboards

## Author
Paulo Magalhaes
linkedin: https://www.linkedin.com/in/paulomagalhaes82/

Built as a hands-on demonstration of AI security patterns using Oracle Cloud Infrastructure (OCI).






