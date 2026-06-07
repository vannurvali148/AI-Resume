import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

TECHNICAL_SKILLS = [
    "python", "java", "sql", "machine learning", "data analysis",
    "deep learning", "html", "css", "javascript", "react",
    "node.js", "flask", "django", "streamlit", "numpy",
    "pandas", "mongodb", "mysql", "git", "aws",
    "docker", "kubernetes", "api", "nlp"
]

SOFT_SKILLS = [
    "communication",
    "teamwork",
    "leadership",
    "problem solving",
    "time management",
    "critical thinking",
    "adaptability",
    "collaboration",
    "creativity",
    "decision making"
]

EXPERIENCE_TERMS = [
    "internship",
    "intern",
    "project",
    "projects",
    "experience",
    "worked",
    "developed",
    "built",
    "implemented",
    "designed",
    "created",
    "handled",
    "led"
]

EDUCATION_TERMS = [
    "b.e",
    "be",
    "btech",
    "b.tech",
    "mca",
    "bca",
    "degree",
    "cgpa",
    "gpa",
    "university",
    "college",
    "school",
    "graduated",
    "education",
    "diploma"
]


def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-zA-Z0-9\s\.\+#-]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def phrase_present(text, phrase):
    pattern = r"\b" + re.escape(phrase.lower()) + r"\b"
    return re.search(pattern, text.lower()) is not None


def extract_items(text, item_list):
    found = []
    text = text.lower()

    for item in item_list:
        if phrase_present(text, item) and item not in found:
            found.append(item)

    return found


def analyze_resume(resume_text, job_text):
    resume_clean = clean_text(resume_text)
    job_clean = clean_text(job_text)

    if not resume_clean.strip() or not job_clean.strip():
        return {
            "final_score": 0.0,
            "text_score": 0.0,
            "skill_score": 0.0,
            "soft_skill_score": 0.0,
            "experience_score": 0.0,
            "education_score": 0.0,
            "resume_skills": [],
            "job_skills": [],
            "matched_skills": [],
            "missing_skills": [],
            "resume_soft_skills": [],
            "job_soft_skills": [],
            "matched_soft_skills": [],
            "missing_soft_skills": [],
            "resume_experience": [],
            "job_experience": [],
            "matched_experience": [],
            "missing_experience": [],
            "resume_education": [],
            "job_education": [],
            "matched_education": [],
            "missing_education": [],
            "suggestions": ["Failed to analyze: One or both files contained no readable text."]
        }

    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([resume_clean, job_clean])
    text_score = cosine_similarity(vectors[0], vectors[1])[0][0]

    # Technical skills
    resume_skills = extract_items(resume_clean, TECHNICAL_SKILLS)
    job_skills = extract_items(job_clean, TECHNICAL_SKILLS)
    matched_skills = list(set(resume_skills) & set(job_skills))
    missing_skills = list(set(job_skills) - set(resume_skills))

    # Soft skills
    resume_soft_skills = extract_items(resume_clean, SOFT_SKILLS)
    job_soft_skills = extract_items(job_clean, SOFT_SKILLS)
    matched_soft_skills = list(set(resume_soft_skills) & set(job_soft_skills))
    missing_soft_skills = list(set(job_soft_skills) - set(resume_soft_skills))

    # Experience
    resume_experience = extract_items(resume_clean, EXPERIENCE_TERMS)
    job_experience = extract_items(job_clean, EXPERIENCE_TERMS)
    matched_experience = list(set(resume_experience) & set(job_experience))
    missing_experience = list(set(job_experience) - set(resume_experience))

    # Education
    resume_education = extract_items(resume_clean, EDUCATION_TERMS)
    job_education = extract_items(job_clean, EDUCATION_TERMS)
    matched_education = list(set(resume_education) & set(job_education))
    missing_education = list(set(job_education) - set(resume_education))

    # Scores
    skill_score = len(matched_skills) / len(job_skills) if job_skills else 0
    soft_skill_score = len(matched_soft_skills) / len(job_soft_skills) if job_soft_skills else 0
    experience_score = len(matched_experience) / len(job_experience) if job_experience else 0
    education_score = len(matched_education) / len(job_education) if job_education else 0

    final_score = (
        0.45 * skill_score +
        0.20 * soft_skill_score +
        0.20 * experience_score +
        0.10 * education_score +
        0.05 * text_score
    )

    suggestions = []

    if missing_skills:
        suggestions.append("Add missing technical skills: " + ", ".join(missing_skills))

    if missing_soft_skills:
        suggestions.append("Add missing soft skills: " + ", ".join(missing_soft_skills))

    if missing_experience:
        suggestions.append("Improve experience section with: " + ", ".join(missing_experience))

    if missing_education:
        suggestions.append("Add education-related keywords: " + ", ".join(missing_education))

    if "project" not in resume_clean and "projects" not in resume_clean:
        suggestions.append("Add a projects section to strengthen your resume.")

    if "certification" not in resume_clean and "certifications" not in resume_clean:
        suggestions.append("Add certifications to improve selection chances.")

    if not suggestions:
        suggestions.append("Your resume is a strong match for this job role.")

    return {
        "final_score": final_score,
        "text_score": text_score,
        "skill_score": skill_score,
        "soft_skill_score": soft_skill_score,
        "experience_score": experience_score,
        "education_score": education_score,
        "resume_skills": resume_skills,
        "job_skills": job_skills,
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "resume_soft_skills": resume_soft_skills,
        "job_soft_skills": job_soft_skills,
        "matched_soft_skills": matched_soft_skills,
        "missing_soft_skills": missing_soft_skills,
        "resume_experience": resume_experience,
        "job_experience": job_experience,
        "matched_experience": matched_experience,
        "missing_experience": missing_experience,
        "resume_education": resume_education,
        "job_education": job_education,
        "matched_education": matched_education,
        "missing_education": missing_education,
        "suggestions": suggestions
    }