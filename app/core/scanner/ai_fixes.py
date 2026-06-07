import os
# from openai import OpenAI
import google.generativeai as genai

# client = OpenAI(
#     api_key=os.getenv("OPENAI_API_KEY")
# )
from app.config import settings
print("Gemini Key Present:", bool(settings.gemini_api_key))
print(
    "Gemini Key Loaded:",
    settings.gemini_api_key[:8] + "..."
)
genai.configure(
    api_key=settings.gemini_api_key
)

def build_prompt(finding):
    return f"""
    You are a security expert.

    Security Finding:
    Type: {finding.type}
    Severity: {finding.severity}
    File: {finding.file}

    Description:
    {finding.message}

    Provide:
    1. Explanation
    2. Fix recommendation

    Keep response under 100 words.
    """

def generate_fix_suggestion(finding):
    try:
        prompt = build_prompt(finding)

        # response = client.chat.completions.create(
        #     model="gpt-4o-mini",
        #     messages=[
        #         {
        #             "role": "user",
        #             "content": prompt
        #         }
        #     ]
        # )

        # return response.choices[0].message.content
        model = genai.GenerativeModel(
        "gemini-2.5-flash"
            )
        
        response = model.generate_content(prompt)

        return response.text

    except Exception as e:
        print("AI Error:", e)

        return "Unable to generate suggestion."
    

def generate_ai_fixes(findings):
    fixes = {}

    for finding in findings:
        fixes[id(finding)] = generate_fix_suggestion(finding)

    return fixes    
