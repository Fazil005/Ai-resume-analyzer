import streamlit as st
import pdfplumber
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# -------------------------------
# Load Model (only once)
# -------------------------------
@st.cache_resource
def load_model():
    return SentenceTransformer('all-MiniLM-L6-v2')

model = load_model()

# -------------------------------
# Extract Text from PDF
# -------------------------------
def extract_text_from_pdf(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text

# -------------------------------
# Clean Text
# -------------------------------
def clean_text(text):
    return " ".join(text.lower().split())

# -------------------------------
# Similarity Function
# -------------------------------
def get_similarity(resume_text, jd_text):
    embeddings = model.encode([resume_text, jd_text])
    score = cosine_similarity([embeddings[0]], [embeddings[1]])[0][0]
    return score

# -------------------------------
# Skill Database
# -------------------------------
SKILL_DB = [
    "python", "sql", "excel", "machine learning",
    "data analysis", "pandas", "numpy",
    "power bi", "tableau", "deep learning",
    "statistics", "data visualization", "etl",
    "data cleaning", "dashboard", "business intelligence",
    "reporting"
]

# -------------------------------
# Extract Skills
# -------------------------------
def extract_skills(text):
    found = []
    for skill in SKILL_DB:
        if skill in text:
            found.append(skill)
    return list(set(found))

# -------------------------------
# Missing Skills
# -------------------------------
def get_missing_skills(resume_skills, jd_skills):
    return list(set(jd_skills) - set(resume_skills))

# -------------------------------
# Streamlit UI
# -------------------------------
st.set_page_config(page_title="AI Resume Analyzer", layout="centered")

st.title("📄 AI Resume Analyzer")

# Inputs
resume_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])
jd_text_input = st.text_area("Paste Job Description Here")

# Button
analyze_btn = st.button("🔍 Analyze Resume")

# -------------------------------
# Main Logic
# -------------------------------
if analyze_btn:

    if resume_file and jd_text_input.strip():

        with st.spinner("Analyzing..."):

            # Extract text
            resume_text = extract_text_from_pdf(resume_file)

            # Clean text
            resume_text = clean_text(resume_text)
            jd_text = clean_text(jd_text_input)

            # Similarity score
            score = get_similarity(resume_text, jd_text)

            # Extract skills
            jd_skills = extract_skills(jd_text)
            resume_skills = extract_skills(resume_text)

            # Missing skills
            missing_skills = get_missing_skills(resume_skills, jd_skills)

        # -------------------------------
        # Output
        # -------------------------------
        st.subheader(f"📊 Match Score: {score * 100:.2f}%")

        st.write("### 📌 Skills Required (from JD):")
        st.write(", ".join(jd_skills) if jd_skills else "No key skills detected")

        st.write("### ✅ Skills Found in Resume:")
        st.write(", ".join(resume_skills) if resume_skills else "No relevant skills found")

        st.write("### ❌ Missing Skills:")
        if missing_skills:
            for skill in missing_skills:
                st.write(f"- {skill}")
        else:
            st.write("No major skills missing 🎉")

    else:
        st.warning("Please upload a resume and paste a job description.")