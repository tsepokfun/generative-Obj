import google.generativeai as genai
import time
import random
import google.api_core.exceptions

genai.configure(api_key="AIzaSyA6VkzaVBTxDLwX0JFrrQKgTCSI7L09XE4")  # Replace with your  API key

model = genai.GenerativeModel("gemini-1.5-flash")

chat = model.start_chat(
    history=[
        {"role": "user", "parts": "Hello"},
        {"role": "model", "parts": "Great to meet you. What would you like to know?"},
    ]
)

llm_cache = {} 

def get_response_with_backoff(prompt):
    wait_time = 1  
    while True:
        try:
            response = chat.send_message(prompt)
            return response.text
        except google.api_core.exceptions.ResourceExhausted:
            print(f"Rate limit exceeded. Waiting for {wait_time} seconds...")
            time.sleep(wait_time + random.uniform(0, 1)) 
            wait_time *= 2  
            if wait_time > 60:  
                raise Exception("Max retries exceeded")

def get_response_with_cache(prompt):
    if prompt in llm_cache:
        print("Using cached response")
        return llm_cache[prompt]
    else:
        response = get_response_with_backoff(prompt)
        llm_cache[prompt] = response
        return response

def gR(q):
    return get_response_with_cache(q) 