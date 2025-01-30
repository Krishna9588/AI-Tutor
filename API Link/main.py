# import google.generativeai as genai
#
# genai.configure(api_key="Api Key")
# model = genai.GenerativeModel("gemini-1.5-flash")
# response = model.generate_content("Explain how AI works")
# print(response.text)

# Simpler Version


import google.generativeai as genai
import tkinter as tk  # For the pop-up
from tkinter import scrolledtext

genai.configure(api_key="API Key")  # Replace with your actual key
model = genai.GenerativeModel("gemini-1.5-flash")

def get_ai_response(question):
    prompt = f"{question}\n\nAnswer in 300 words or less."  # Word limit in prompt
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:  # Handle potential errors
        return f"Error: {e}"

def show_popup(answer):
    popup = tk.Toplevel(root)  # Create a new top-level window
    popup.title("AI Response")

    text_area = scrolledtext.ScrolledText(popup, wrap=tk.WORD) # Scrollable text
    text_area.insert(tk.END, answer)
    text_area.pack(fill=tk.BOTH, expand=True)  # Make text area expandable

root = tk.Tk()  # Create main window (not shown)
# root.withdraw()   # Hide the main window

while True:
    question = input("Enter your question (or type 'exit'): ")
    if question.lower() == 'exit':
        break

    ai_response = get_ai_response(question)
    show_popup(ai_response)
    root.update() # Keep the window active

root.destroy() # Clean up