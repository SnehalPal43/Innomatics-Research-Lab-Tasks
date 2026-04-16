# 🧠 AI Resume Screening System

This project is a simple AI-based Resume Screening System that evaluates candidate resumes based on a given job description.

It analyzes the skills mentioned in the resume, compares them with required job skills, and generates a score along with an explanation.

---

## 🚀 Features

* Extracts important skills from resumes
* Matches resume skills with job requirements
* Calculates a score (0–100)
* Provides explanation for the score
* Simple and modular pipeline using LangChain

---

## 🛠️ Technologies Used

* Python
* LangChain (PromptTemplate, Runnable)
* LangSmith (for tracing - optional)

---

## 📊 How It Works

1. A job description is defined with required skills
2. Candidate resumes are provided as input
3. The system compares resume skills with job requirements
4. A score is generated based on matching skills
5. An explanation is provided showing matched and missing skills

---

## 🧪 Sample Results

| Resume Type | Score   |
| ----------- | ------- |
| Strong      | 100/100 |
| Average     | 50/100  |
| Weak        | 0/100   |

---

## 📸 Output Example

The system produces output like:

Final Score: 100/100

Matched Skills: ['python', 'machine learning', 'nlp', 'sql']
Missing Skills: []

---

## 📂 Project Structure

AI-Resume-Screening-System/
│
├── resume_screening.ipynb
├── README.md
├── screenshots/

---

## ⚠️ Note

* This project uses a rule-based approach for simplicity
* API-based models (like OpenAI) can be integrated for advanced results
* API keys are not included for security reasons

---

## 🎯 Conclusion

This project demonstrates how a basic resume screening system can be built using Python and LangChain concepts.
It can be further enhanced using NLP models and real-world datasets.

---


