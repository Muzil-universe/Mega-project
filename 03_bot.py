import pyautogui
import time
import pyperclip
from openai import OpenAI

# Initialize OpenAI client
client = OpenAI(
    api_key="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",
    base_url="https://openrouter.ai/api/v1"
)

# Function to check if last message is from a specific sender
def is_last_message_from_sender(chat_log, sender_name="Sistorolgy"):
    last_line = chat_log.strip().split('\n')[-1]
    return sender_name in last_line

# Click on the Chrome icon to activate the window
pyautogui.click(3470, 1321)
time.sleep(1)

while True:
    time.sleep(5)

    # Select chat area
    pyautogui.moveTo(3320, 309)
    pyautogui.dragTo(4525, 1165, duration=1, button='left')
    time.sleep(0.5)

    # Copy selected text
    pyautogui.hotkey('ctrl', 'c')
    pyautogui.click(3335, 804)
    time.sleep(0.5)

    # Get copied text
    chat_history = pyperclip.paste()
    print("Captured text:")
    print(chat_history)

    # Check if last message is from Sahar
    if is_last_message_from_sender(chat_history):
        # Send chat to model
        chat = client.chat.completions.create(
            model="deepseek/deepseek-chat",
            messages=[
                {
                    "role": "system",
                    "content": "You are a person named Muzamil who speaks Urdu and English. "
        "You are from Lahore, Pakistan — a coder and a student. "
        "You respond casually and sometimes formally, depending on context. "
        "You often use humor and emojis (😂😜🙃), and keep replies short and natural, like a human. and use emoji if needed not not used and also add emoji in your system that once send by sender   "
        "You mostly write in Urdu, but switch to English if the other person does. "
        "You sometimes give help, sometimes ask for help, and sometimes just chat casually. "
        "Analyze the chat and respond exactly like Muzamil would and shorter size reply equal to sender mostly in one line."
                },
                {
                    "role": "user",
                    "content": chat_history
                }
            ]
        )

        # Extract and copy response
        response = chat.choices[0].message.content
        pyperclip.copy(response)

        # Paste and send response
        pyautogui.click(x=3830, y=1226)
        time.sleep(0.5)
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(0.5)
        pyautogui.press('enter')
