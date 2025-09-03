from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    data = {
        "overview": "Software Engineer specializing in Python, Flask, and Machine Learning, with hands-on experience in full-stack development and data analytics.",

        "projects": [
            {"name": "Portfolio Website", "desc": "Personal portfolio ", "link": "https://profile-1ojf.onrender.com/"},
            {"name": "Machine Learning Project", "desc": "Mobile Price Range Prediction Model ", "link": "https://github.com/yourgithub/ml-project"},
            {"name": "Portfolio Website", "desc": "Basic visitor entry system", "link": "https://github.com/Bhakti-Goyal/visitor-entry-system"},
            {"name": "Portfolio Website", "desc": "Food Traceability System", "link": "https://food-traceability-1.onrender.com"},
        ],

        "education": [
            {"degree": "B.Tech in Computer Science", "school": "Mody University of Science and Technology, Rajasthan", "year": "2022 – 2026", "score": "CGPA: 7.97"},
            {"degree": "Intermediate (CBSE)", "school": "Sir Padampat Singhania School, Kota", "year": "2021 – 2022", "score": "81.66%"},
            {"degree": "High School (CBSE)", "school": "Sir Padampat Singhania School, Kota", "year": "2019 – 2020", "score": "81.70%"},
        ],

        "trainings": [
            {"title": "Machine Learning with python", "provider": "SkillForge", "duration": "15th June 2024 – 15th July 2025", "desc": "Completed hands-on training in Python programming, data analysis, and machine learning basics."},

        ]
       ,


        "internships": [
            {"role": "Intern", "company": "Nobel Dehydrates", "duration": "June 2025 – August 2025", "desc": "Developed a website for Food traceability and deployed it at biggner level and they can update it according to their needs."},
        ],

        "certificates": [
            {"title": "Inetrnship Certification", "issuer": "Nobel Dehydrates", "img": "images/cert1.jpg"},
            {"title": "Inetrnship Certification", "issuer": "SkillForge", "img": "images/cert2.jpg"},
        ],

        "cocurricular": [
            {"activity": "Article Writing for College Magazine 'ENGINIUM' ", "desc": "The Role of Artificial Intelligence in Predictive Maintenance and System Renewal", "file": "pdfs/article1.pdf"},
            {"activity": "Article Writing for College Magazine 'ENGINIUM' ", "desc": "AI and EVs: Tackling Seasonal Extremes for Peak Performance", "file": "pdfs/article2.pdf"},
            {"activity": "Article Writing for College Magazine 'ENGINIUM' ", "desc": "Cloud Seeding", "file": "pdfs/article3.pdf"},
        
        ],

        "contact": {
            "name": "Bhakti Goyal",
            "email": "bbhaktigoyal@gmail.com",
            "linkedin": "https://www.linkedin.com/in/bhakti-goyal-33921b26b/",
            "github": "https://github.com/Bhakti-Goyal"
        }
    }
    return render_template("index.html", data=data)

if __name__ == "__main__":
    app.run(debug=True)
