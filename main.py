

from datetime import datetime
import os
today = datetime.now().strftime("%Y-%m-%d")

os.makedirs(f"articles/{today}", exist_ok=True)

from google import genai



client = genai.Client(
    api_key=os.environ["GEMINI_API_KEY"]
)   


topics = [
    "ChatGPT",
    "Google Gemini",
    "AI Tools",
    "Artificial Intelligence",
    "Machine Learning"
]

for topic in topics:
    print(topic)

    prompt = f"""
Write a detailed SEO article.

Title: {topic}

Requirements:
- 1000+ words
- H1, H2, H3 headings
- FAQ section
- Conclusion
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    filename = topic.replace(" ", "_") + ".txt"

    with open(f"articles/{today}/{filename}", "w", encoding="utf-8") as f:
        f.write(response.text)

    print(f"Saved: {filename}")
