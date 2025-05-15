Email-Classifier-fastapi
==============================

Email classifier in fastapi following 12 factor app principles

Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------


## 🚀 Run Locally

### ✅ Prerequisites

- Python 3.10 or 3.11
- `pip` or `conda`
- `git` (optional)

---

### 🔧 Setup Instructions

#### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/Email-Classifier-fastapi.git
cd Email-Classifier-fastapi
<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>

# Using venv
python3 -m venv env
source env/bin/activate      # Windows: .\env\Scripts\activate

## 3. Install Required Packages
pip install -r requirements.txt

#  Create a .env File
MODEL_PATH=app/models/email_classifier.pkl
ENV=development

# Run the FastAPI Server
uvicorn app.main:app --reload

Once the server is running:
	•	Swagger UI → http://127.0.0.1:8000/docs

 Example API Usage

 Endpoint

POST /api/v1/predict    

 Sample Request
 {
  "text": "Congratulations! You have won a free ticket!"
}
Sample Response
{
  "prediction": "spam"
}

Run Pytest with PYTHONPATH Set

This ensures the app module is correctly discovered.
bash
PYTHONPATH=. pytest tests/test_predict.py

🐳 Docker Support

🏗️ Build Docker Image
bash
docker build -t email-classifier-fastapi .

🚀 Run the Docker Container
bash
docker run -d -p 8000:8000 --env-file .env email-classifier-fastapi


⸻

🔁 CI/CD – GitHub Actions

This repo includes a CI workflow that:
	•	Installs Python 3.12
	•	Installs dependencies
	•	Runs tests with pytest

✅ Workflow File

.github/workflows/test.yml

To Trigger CI/CD

Every time you push or create a pull request:
bash 
git add .
git commit -m "Trigger CI test"
git push origin main
✅ CI passes if tests succeed
❌ CI fails if tests break

You can check the status under the Actions tab in your GitHub repository.

⸻


## ✅ 12-Factor App Compliance

| # | Factor                     | Status        | Notes |
|---|----------------------------|---------------|-------|
| 1️⃣ | **Codebase**               | ✅ Followed    | Single Git-tracked codebase |
| 2️⃣ | **Dependencies**           | ✅ Followed    | Declared in `requirements.txt` |
| 3️⃣ | **Config**                 | ✅ Followed    | `.env` file + `dotenv` loaded |
| 4️⃣ | **Backing Services**       | ✅ Followed    | Model/vectorizer loaded externally |
| 5️⃣ | **Build, Release, Run**    | ⚠️ Partial     | Docker used, but release phase isn't clearly separated |
| 6️⃣ | **Processes**              | ✅ Followed    | Stateless FastAPI endpoints |
| 7️⃣ | **Port Binding**           | ✅ Followed    | Binds using `uvicorn` |
| 8️⃣ | **Concurrency**            | ⚠️ Partial     | Not yet configured for multi-worker scalability |
| 9️⃣ | **Disposability**          | ✅ Followed    | Fast start/stop, no persistent state |
| 🔟 | **Dev/Prod Parity**        | ⚠️ Partial     | Docker helps, but no prod deployment setup yet |
| 1️⃣1️⃣ | **Logs**                   | ⚠️ Partial     | Logs to console, but no centralized logging |
| 1️⃣2️⃣ | **Admin Processes**        | ✅ Followed    | Pytest and Makefile for admin/testing |