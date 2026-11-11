import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

queries = [
    "What is the incidence of tuberculosis in Pakistan?",
    "What is the TB prevalence rate per 100,000 population in Pakistan?",
    "What is the multidrug-resistant TB situation in Pakistan?",
    "What percentage of TB cases in Pakistan are detected and notified?",
    "What is the prevalence of hepatitis C in Pakistan?",
    "What is the prevalence of hepatitis C in Punjab, Pakistan?",
    "What is the prevalence of hepatitis B in Pakistan?",
    "What are the main routes of hepatitis C transmission in Pakistan?",
]

for q in queries:
    print("="*60)
    print("Q:", q)
    resp = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": q}],
        temperature=0.2,
    )
    print("A:", resp.choices[0].message.content.strip())
    print()