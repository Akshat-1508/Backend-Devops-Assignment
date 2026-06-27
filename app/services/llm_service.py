import google.generativeai as genai

from app.core.config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-1.5-flash")


def generate_summary(df):

    sample = df.head(30).to_string(index=False)

    prompt = f"""
You are a financial analyst.

Analyze these transactions.

{sample}

Generate:

1. Spending overview
2. Suspicious transactions
3. Largest expenses
4. Spending recommendations

Limit to 200 words.
"""

    response = model.generate_content(prompt)

    return response.text