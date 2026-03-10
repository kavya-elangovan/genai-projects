Built as part of my Generative AI Engineering portfolio.



\# AI ATS Resume Analyzer



An AI-powered resume analyzer that compares resumes with job descriptions and provides ATS match scores, strengths, missing skills, and improvement suggestions.



\## Features

\- Upload resume (PDF)

\- Paste job description

\- AI-powered analysis using Llama3

\- ATS-style resume evaluation



\## Tech Stack

\- Python

\- Streamlit

\- Ollama (Llama3)

\- pdfplumber

\- requests



\## Architecture



User uploads resume (PDF)

&nbsp;	|

&nbsp;	V

PDF text extraction (pdfplumber)

&nbsp;	|

&nbsp;	V

Prompt sent to Llama3 via Ollama API

&nbsp;	|

&nbsp;	V

AI evaluates resume vs job description

&nbsp;	|

&nbsp;	V

ATS-style feedback displayed



\## How to Run



1\. Install dependencies



pip install -r requirements.txt



2\. Start Ollama model



ollama run llama3



3\. Start the app



python -m streamlit run app.py



\## Application Screenshot



!\[AI ATS Resume Analyzer](screenshot.png)

