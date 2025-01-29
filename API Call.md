### Hi everyone

Talking about API calls and integrating AI using API's in our Project.


##  Deepseek 
for more details visit the below link
```bash
https://api-docs.deepseek.com/
```

To integrate Deepseek into our project we can use this code with our "API keys"
```python
# Please install OpenAI SDK first: `pip3 install openai`

from openai import OpenAI

client = OpenAI(api_key="<DeepSeek API Key>", base_url="https://api.deepseek.com")

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "Hello"},
    ],
    stream=False
)

print(response.choices[0].message.content)
```

## Google Gemini AI

for more details visit the below link
```bash
https://ai.google.dev/gemini-api/docs/quickstart
```

To integrate Google's Gemini into our project we can use this code with our "API keys"
```python
import google.generativeai as genai

genai.configure(api_key="YOUR_API_KEY")
model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("Explain how AI works")
print(response.text)
```
