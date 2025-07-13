# 🧠 Personality Prediction Model

This repository contains multiple machine learning models built to predict whether a person is an **Introvert or Extrovert** based on their social behaviour data.

---

## 📁 **Repository Structure**

```
Personality-Prediction-Model/
│
├── PersonalityPredictionLogReg/
│   ├── PersonalityPredictionLogReg.pkl
│   └── training_logreg.ipynb
│
├── PersonalityPredictionDT/
│   ├── PersonalityPredictionDT.pkl
│   └── training_dt.ipynb
│
├── PersonalityPredictionSVM/
│   ├── PersonalityPredictionSVM.pkl
│   └── training_svm.ipynb
│
├── PersonalityPredictionIntegrated/
│   ├── app.py
│   ├── PersonalityPredictionLogReg.pkl
│   ├── PersonalityPredictionDT.pkl
│   ├── PersonalityPredictionSVM.pkl
│   └── requirements.txt
│
└── README.md
```

---

## 💡 **Project Overview**

This project predicts personality type (Introvert or Extrovert) using features like:

- Time spent alone (hours per day)
- Stage fear (Yes/No)
- Social event attendance per month
- Going outside per week
- Feeling drained after socialising (Yes/No)
- Number of close friends
- Social media post frequency (per week)

---

## ⚙️ **Models Used**

✅ **Logistic Regression**  
✅ **Decision Tree**  
✅ **Support Vector Machine (SVM)**

Each model was trained and saved separately for comparison in the integrated Streamlit app.

---

## 🚀 **Integrated Streamlit App**

The `PersonalityPredictionIntegrated` folder contains:

- `app.py`: Streamlit app combining all models with:
  - Model selection dropdown  
  - Model accuracy table  
  - Model description section  
  - User-friendly UI with success animations
- Trained `.pkl` files for each model
- `requirements.txt` for deployment

---

## 🔧 **How to Run Locally**

1. Clone the repository:

```bash
git clone https://github.com/Weird-ragazzo/Personality-Prediction-Model.git
cd Personality-Prediction-Model/PersonalityPredictionIntegrated
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
streamlit run app_combined.py
```

---

## 🌐 **Deployment**

A modern UI version of this app is deployed on **Render** (see separate repo for the deployed version).

---

## ✨ **Future Improvements**

- Adding feature importance visualizations  
- Collecting real-world labelled data for model retraining  
- Implementing advanced models like Random Forest or XGBoost for further accuracy comparisons

---

## 👤 **Author**

- **Name:** Weird-ragazzo
- **GitHub:** [Weird-ragazzo](https://github.com/Weird-ragazzo)

---

## 📄 **License**

This project is for educational and portfolio purposes.

---

