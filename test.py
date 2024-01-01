import google.generativeai as genai
import textwrap


G_API_KEY="AIzaSyCQLhzQ9hkE-YM4dTLhU5vQwjEWwCLlsZI"
genai.configure(api_key=G_API_KEY)

model = genai.GenerativeModel('gemini-pro')

response = model.generate_content("What is the meaning of life?")


print(response.text)