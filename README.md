# A Mental Health Companion App Using AI-Powered Journaling and Mood Tracking

Mental health is increasingly recognized as a critical aspect of overall well-being, yet access to mental health services remains limited, especially for young adults, students, and people in rural areas. MindWell is a mobile-first application designed to help users manage their mental health daily through AI-supported journaling, personalized mood tracking, and emotional insight generation. The app is designed to be both a therapeutic companion and a data-driven tool to help users understand emotional patterns over time.

## Features
- Daily AI-Powered Journaling: Users write journal entries in natural language. The AI summarizes key emotional themes, classifies mood, and highlights stress or positivity indicators
- Mood Tracking Dashboard: Users can select their mood each day, which is tracked on a calendar and shown in weekly or monthly views for trends.
- Emotion Analysis: Based on user input, the AI can suggest helpful coping strategies, mindfulness exercises, or just encouraging messages.
- Privacy-Focused: All data will be stored locally or encrypted, giving the user control over their mental health data.
- Optional Reminders and Prompts: Daily check-ins and writing prompts to encourage consistent self-care.


## Prerequisites

Ensure you have the following installed:
- Python 3.7+
- `streamlit`
- `pandas`
- `scikit-learn`
- `requests`
- `Pillow` (for image processing)

Install all the necessary dependencies using the following command:

```bash
pip install -r requirements.txt
```

## Installation & Setup

1. **Clone the repository**:

```bash
git clone https://github.com/aaarif796/AI-Powered-Preventive-Healthcare-System.git
cd AI-Powered-Preventive-Healthcare-System
```

2. **Download or Place Model Files**:

Make sure to have the pre-trained model files:
- `label_encoders.pkl`
- `lr_dt.pkl` (Logistic Regression model for academic and social pressures)
- `lr_ht.pkl` (Logistic Regression model for understanding emotions)
- `lr_ob.pkl` (Logistic Regression model for self-reflection and wellness tracking)

Place these files inside the `model` folder.

3. **Add Images**:

Place relevant images in the `images` folder for visual representation.

4. **CSS Styling**:

The application uses a custom CSS file for styling. Ensure you have the `style.css` file in the `style` folder.

## Usage

1. **Run the Application**:

Use Streamlit to launch the app with the following command:

```bash
streamlit run app.py
```

2. **Input Data**:

Fill out the form with your general mental health and lifestyle details (e.g., age, stressors, coping habits, mental health history, etc.).

3. **Receive Feedback**:

MindWell will be open-source and customizable, aiming to bridge the gap between wellness and accessible tech.


## Folder Structure

```
├── images
│   ├── MH1pic.jpeg
├── model
│   ├── label_encoders.pkl
│   ├── lr_dt.pkl
│   ├── lr_ht.pkl
│   ├── lr_ob.pkl
├── style
│   ├── style.css
├── app.py
├── README.md
├── requirements.txt
```

## Model Details

- **label_encoders.pkl**: Used to encode categorical data.
- **lr_dt.pkl**: Logistic Regression model for predicting the risk of academic and social pressures.
- **lr_ht.pkl**: Logistic Regression model for better understanding of emotions.
- **lr_ob.pkl**: Logistic Regression model for self-reflection and wellness tracking.

## Acknowledgments

This application was developed as part of the **TechXcelerate 2024** challenge, focusing on developing a predictive healthcare system using machine learning and AI.

_will be adding two models, XGBoost and Naive Bayes, to the analysis of the diabetes dataset( diabetes data.csv) or enhanced predictive modeling._
>Sprint 2
focusing on developing a predictive healthcare system using machine learning and AI.
>Sprint 2
In this update to the Jupyter Notebook, the heart disease dataset analysis, I integrated two new models, the Gradient Boosting Classifier and the XGBoost Classifier, to enhance the dataset's predictive analysis. These models were trained on the resampled and scaled data, followed by evaluation metrics to compare their performance against previously implemented classifiers.
The app is designed to be both a therapeutic companion and a data-driven tool to help users understand emotional patterns over time.
