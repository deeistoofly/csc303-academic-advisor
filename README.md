# CSC 303 — Academic Advisor System

A beginner-friendly Flask web application that uses a scikit-learn model trained in Google Colab to suggest a study/career track.

## Project structure

- `app.py` — Flask backend / web routes
- `templates/index.html` — web form and results page
- `requirements.txt` — Python dependencies
- `colab_training.py` — model-training code to run in Google Colab
- `data/` — place any additional dataset here
- `model/` — place the downloaded `.pkl` model here

## 1. Install tools

Install Python, Git, and Visual Studio Code. In VS Code, install the official Python extension. Create a GitHub account and a repository named `csc303-academic-advisor`.

## 2. Open the project in VS Code

Extract this ZIP, then open the `CSC303_Academic_Advisor` folder in VS Code.

Open the terminal in VS Code and run:

### Windows PowerShell

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

If PowerShell blocks activation, run this in the current terminal, if permitted:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

## 3. Train the model in Google Colab

1. Open Google Colab and create a new notebook.
2. Copy the contents of `colab_training.py` into a cell and run it.
3. It creates `academic_advisor_model.pkl`.
4. In a new cell, run:

```python
from google.colab import files
files.download("academic_advisor_model.pkl")
```

5. In VS Code, create a folder named `model` in the project folder.
6. Put the downloaded file at `model/academic_advisor_model.pkl`.

The provided dataset is only a demonstration dataset. Explain this limitation in your report and use a larger, reviewed dataset for real academic advising.

## 4. Run the web app

In the activated VS Code terminal:

```powershell
python app.py
```

Open the local address shown in the terminal (normally `http://127.0.0.1:5000`) in your browser. Submit the form and check that the model returns a recommendation.

## 5. Git and GitHub

Create a repository on GitHub named `csc303-academic-advisor`. Do not initialise it with a README if you plan to push this existing folder.

In the VS Code terminal, run:

```bash
git init
git add .
git commit -m "Initial academic advisor system"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/csc303-academic-advisor.git
git push -u origin main
```

Replace `YOUR-USERNAME` with your GitHub username. If Git asks you to identify yourself, run:

```bash
git config --global user.name "Your Name"
git config --global user.email "your-email@example.com"
```

Then repeat the commit/push commands as needed.

## 6. Add a `.gitignore`

Create a file named `.gitignore` with:

```text
.venv/
__pycache__/
*.pyc
.env
```

You may commit the `.pkl` file for this school demo if its size is small and your lecturer expects it. Otherwise, document how to obtain it.

## 7. What to explain in the assignment

- **Software engineering:** requirements, folder structure, reusable modules, dependency management, version control, testing, and a web interface.
- **AI technique:** supervised machine learning classification with a Random Forest model.
- **Data processing:** categorical features are converted with `OneHotEncoder`.
- **Deployment:** Flask loads the saved `.pkl` model and calls `predict()` when a user submits the form.
- **Testing:** test several combinations of interests, subjects, and goals; verify that the page handles missing model files; note that the toy dataset is too small for real-world conclusions.
- **Ethics/limitations:** the output is guidance only. It must not replace official academic counselling, and recommendations depend on dataset quality.

## Important

The `.pkl` model is created by running the training code in Colab. The app will display an error until you put that file in the `model` folder.
