from openai import OpenAI

# Define the user's command or chat message
command = '''
.muzil: achaa us na rt kha tha ussay bta dena ka attendance lgwie thi ussana
[1:25 PM, 5/1/2025] .muzil: 😜😂
[1:26 PM, 5/1/2025] .muzil: saiii kheta hon
[1:26 PM, 5/1/2025] Alisha: Ge okkk
[1:26 PM, 5/1/2025] Alisha: Acha ge
[3:04 PM, 5/1/2025] Alisha: Bhai wo assignment theek hai?
[3:04 PM, 5/1/2025] Alisha: 2nd wali
[3:04 PM, 5/1/2025] Alisha: Main likh lun wohi?
'''

# Connect to OpenRouter
client = OpenAI(
    api_key="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",
    base_url="https://openrouter.ai/api/v1"
)

# Create the chat
chat = client.chat.completions.create(
    model="deepseek/deepseek-chat",
    messages=[
        {
            "role": "system",
            "content": "You are a person named Muzamil who speaks Urdu and English. He is from Lahore, Pakistan, a coder and a student. Analyze the chat and respond like Muzamil."
        },
        {
            "role": "user",
            "content": command
        }
    ]
)

# Print the response
print(chat.choices[0].message.content)
