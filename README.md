# 📄 AI Resume Analyzer

A Streamlit-based web application that analyzes resumes against job descriptions using semantic similarity and skill matching.A lightweight AI-powered tool that helps job seekers evaluate resume-job fit and identify missing skills using semantic similarity.

## 🚀 Features

* Upload resume (PDF)
* Paste job description
* Semantic similarity scoring using Sentence Transformers
* Skill extraction and comparison
* Missing skill identification

## 🧠 How It Works

* Converts resume and job description into embeddings
* Uses cosine similarity to measure relevance
* Extracts key skills from both inputs
* Identifies missing skills in the resume

## 🛠️ Tech Stack

* Python
* Streamlit
* Sentence Transformers
* Scikit-learn
* PDFPlumber

## ▶️ Run Locally

```
pip install -r requirements.txt
streamlit run App.py
```

## 📸 Screenshot
[View Screenshot](Screenshot.png)

## 🎯 Example Output

- Match Score: 63.98%
- Skills Found: Python, SQL, Pandas
- Missing Skills: Tableau, Power BI

This helps users quickly understand how well their resume aligns with a specific job and what skills they need to improve.

## ⚠️ Limitations

* Rule-based skill extraction
* Does not measure experience depth

## 🔮 Future Improvements

* Skill importance weighting
* LLM-based suggestions
* Advanced NLP extraction
