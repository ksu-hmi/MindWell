import streamlit as st
from textblob import TextBlob
from datetime import datetime
import pandas as pd
import os

st.set_page_config(page_title="MindWell: Your Mental Health Companion", layout="centered")

# --- Header Section ---
st.title("🧠 MindWell")
st.subheader("Your AI-Powered Mental Health Companion")
st.markdown("Track your mood, journal your thoughts, and gain emotional insights.")

# Initialize data storage
data_file = "mindwell_data.csv"
if not os.path.exists(data_file):
    df = pd.DataFrame(columns=["Date", "Mood", "Journal", "Sentiment", "Summary", "Suggestions"])
    df.to_csv(data_file, index=False)

# --- Mood Tracker and Journal Entry ---
with st.form(key="journal_form"):
    st.markdown("### 📝 How are you feeling today?")
    mood = st.selectbox("Select your mood", ["Very Happy", "Happy", "Neutral", "Sad", "Very Sad"])
    journal_entry = st.text_area("Write about your day", height=200)
    submit = st.form_submit_button("Analyze Entry")

def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0.3:
        return "Positive", "You're expressing positive emotions. Keep it up! Consider noting what contributed to this feeling."
    elif polarity < -0.3:
        return "Negative", "It seems like you're going through something tough. Consider talking to a friend or trying a breathing exercise."
    else:
        return "Neutral", "You're feeling balanced. Mindfulness meditation or a walk might help maintain clarity."

def summarize_entry(text):
    blob = TextBlob(text)
    summary = " ".join(blob.sentences[:2])  # Simple summary (could use more advanced models)
    return summary

if submit and journal_entry.strip() != "":
    sentiment, suggestion = analyze_sentiment(journal_entry)
    summary = summarize_entry(journal_entry)
    today = datetime.now().strftime("%Y-%m-%d")

    # Save entry
    new_data = pd.DataFrame([{
        "Date": today,
        "Mood": mood,
        "Journal": journal_entry,
        "Sentiment": sentiment,
        "Summary": summary,
        "Suggestions": suggestion
    }])
    new_data.to_csv(data_file, mode='a', header=False, index=False)

    # Show feedback
    st.success("✅ Entry Analyzed")
    st.markdown(f"**Sentiment:** {sentiment}")
    st.markdown(f"**Summary:** {summary}")
    st.markdown(f"**AI Suggestion:** {suggestion}")

    # Optionally display calendar/trend in future

# --- Mood History ---
st.markdown("### 📅 Your Mood Journal")
if os.path.exists(data_file):
    df = pd.read_csv(data_file)
    if not df.empty:
        st.dataframe(df.tail(7))  # show last 7 entries
    else:
        st.info("No entries found. Start journaling to see your history here.")
      


