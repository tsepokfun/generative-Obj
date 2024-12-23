import google.generativeai as genai

genai.configure(api_key="AIzaSyA6VkzaVBTxDLwX0JFrrQKgTCSI7L09XE4")  # Replace with your  API key

model = genai.GenerativeModel("gemini-1.5-flash")

chat = model.start_chat(
    history=[
        {"role": "user", "parts": "Hello"},
        {"role": "model", "parts": "Great to meet you. What would you like to know?"},
    ]
)

def gR(q):
    response = chat.send_message(q)
    return response.text