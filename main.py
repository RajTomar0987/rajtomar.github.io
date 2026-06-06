

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

    filename = topic.replace(" ", "_") + ".html"

    html = f"""
<!DOCTYPE html>
<html>
<head>
<title>{topic}</title>
<style>
body {{
    background:#0f172a;
    color:white;
    font-family:Arial,sans-serif;
    max-width:1000px;
    margin:auto;
    padding:30px;
}}
.hero {{
    background:linear-gradient(135deg,#2563eb,#7c3aed);
    padding:40px;
    border-radius:15px;
}}
.article {{
    background:#1e293b;
    padding:25px;
    border-radius:15px;
    margin-top:20px;
}}
</style>
</head>
<body>

<div class="hero">
<h1>{topic}</h1>
<p>AI Future Hub</p>
</div>

<div class="article">
{response.text.replace(chr(10), "<br>")}
</div>

</body>
</html>
"""

with open(f"articles/{today}/{filename}", "w", encoding="utf-8") as f:
    f.write(html)

    print(f"Saved: {filename}")
