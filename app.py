from flask import Flask, render_template, request
import pickle
import os

app = Flask(__name__)

MODEL_PATH = os.path.join("model", "academic_advisor_model.pkl")

def load_model():
    if not os.path.exists(MODEL_PATH):
        return None
    with open(MODEL_PATH, "rb") as f:
        return pickle.load(f)

@app.route("/", methods=["GET", "POST"])
def home():
    advice = None
    error = None

    if request.method == "POST":
        level = request.form.get("level", "").strip()
        interest = request.form.get("interest", "").strip()
        strongest_subject = request.form.get("subject", "").strip()
        study_goal = request.form.get("goal", "").strip()

        model = load_model()
        if model is None:
            error = "Model file not found. Train the model in Google Colab, then place academic_advisor_model.pkl inside the model folder."
        else:
            try:
                prediction = model.predict([[level, interest, strongest_subject, study_goal]])[0]
                advice = {
                    "track": prediction,
                    "summary": {
                        "Cybersecurity": "Build a foundation in networking, operating systems, secure coding, and security monitoring.",
                        "Software Development": "Focus on programming, data structures, databases, software engineering, and practical projects.",
                        "Data Science": "Strengthen Python, statistics, data analysis, machine learning, and data visualisation.",
                        "Networking": "Study computer networks, routing and switching, network services, troubleshooting, and network security."
                    }.get(prediction, "Discuss this recommendation with your academic adviser and compare it with your degree requirements."),
                    "next_steps": {
                        "Cybersecurity": ["Revise computer networking and operating systems.", "Practise Python and basic Linux commands.", "Complete a beginner defensive-security project."],
                        "Software Development": ["Practise Python programming and data structures.", "Build a small database-backed web application.", "Use Git and GitHub to document your projects."],
                        "Data Science": ["Practise Python with NumPy and pandas.", "Learn basic statistics and data cleaning.", "Build a small machine-learning project and explain its results."],
                        "Networking": ["Review OSI/TCP-IP concepts.", "Practise IP addressing and subnetting.", "Create a simple network diagram and troubleshoot sample faults."]
                    }.get(prediction, ["Review your course handbook.", "Speak with your academic adviser.", "Make a semester study plan."])
                }
            except Exception as exc:
                error = "Could not generate advice. Check that the model was trained with the expected four input fields. Details: " + str(exc)

    return render_template("index.html", advice=advice, error=error)

if __name__ == "__main__":
    app.run(debug=True)
