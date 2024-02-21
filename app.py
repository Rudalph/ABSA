import streamlit as st
import openai
import time

# Set your OpenAI API key
openai.api_key = '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'

# Define your input prompt
prompt = "Given a review, analyze the sentiment for specific aspects:"

# List of aspects to analyze
aspects_keywords_list = [
    "Whitening", "Plaque removal", "Cavity prevention", "Freshness/breath", "Tartar control", "Sensitivity relief",
    "Convenience", "Application", "Packaging", "Accessibility", "Instructions",
    "Minty", "Sweet", "Refreshing", "Bitter", "Strong", "Artificial",
    "Gentle on gums", "Non-irritating", "Soft bristles/texture", "Smooth application",
    "Affordable", "Cost-effective", "Expensive", "Worth the price", "Budget-friendly",
    "Lasting freshness", "Long-lasting effects", "Durable packaging", "Staying power",
    "Natural ingredients", "Chemical-free", "Artificial additives", "Alcohol-free", "Fluoride-free",
    "Creamy", "Foamy", "Gel-like", "Thick", "Thin", "Grainy",
    "Fresh", "Strong scent", "Overpowering", "Unpleasant odor",
    "Design", "Size", "Portability", "Environmental friendliness"
]

delay_between_requests = 30

# Title
st.title("Aspect-Based Sentiment Analysis")


# Sidebar
st.sidebar.title("Navigation")
st.sidebar.markdown("""
- Home
- About
""")

# Home
st.header("Home")
st.write("Welcome to the Aspect-Based Sentiment Analysis App. Please enter a review to analyze.")

# Take review as input
review = st.text_input("Enter the review you want to analyze: ")

if review:
    # Perform aspect-based sentiment analysis for each aspect
    for aspect in aspects_keywords_list:
        response = openai.Completion.create(
            engine="gpt-3.5-turbo-instruct",
            prompt=f"{prompt}\nReview: {review}\nAspect: {aspect}\nSentiment:",
            max_tokens=150
        )
        sentiment = response['choices'][0]['text'].strip()
        st.write(f"\nReview: {review}")
        st.write(f"Aspect: {aspect}")
        st.write(f"Sentiment: {sentiment}")
        time.sleep(delay_between_requests)

    # Print the final aspect
    st.write("\nAspect Analyzed: All Aspects from the provided list.")

# About
st.header("About")
st.write("This app uses OpenAI's GPT-3 model to perform aspect-based sentiment analysis on user-provided reviews.")
