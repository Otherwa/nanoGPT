import re
import os

input_file = os.path.join(os.path.dirname(__file__), 'chats.txt')
output_file = os.path.join(os.path.dirname(__file__), 'cleanchats.txt')


def remove_timestamp(message):
    pattern = r'^\d{1,2}/\d{1,2}/\d{2}, \d{2}:\d{2} - '
    cleaned_message = re.sub(pattern, '', message)
    return cleaned_message.strip()

def remove_emojis(message):
    emoji_pattern = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F700-\U0001F77F"  # alchemical symbols
        u"\U0001F780-\U0001F7FF"  # Geometric Shapes Extended
        u"\U0001F800-\U0001F8FF"  # Supplemental Arrows-C
        u"\U0001F900-\U0001F9FF"  # Supplemental Symbols and Pictographs
        u"\U0001FA00-\U0001FA6F"  # Chess Symbols
        u"\U0001FA70-\U0001FAFF"  # Symbols and Pictographs Extended-A
        u"\U00002702-\U000027B0"  # Dingbats
        u"\U000024C2-\U0001F251" 
        "]+", flags=re.UNICODE)
    cleaned_message = re.sub(emoji_pattern, '', message)
    return cleaned_message

def format_messages(messages):
    formatted_messages = []
    
    for message in messages:
        message = remove_timestamp(message)
        message = remove_emojis(message)
        if message:
            if ":" in message:
                parts = message.split(":", 1)
                formatted_message = f"{parts[0]}:\n{parts[1]}"
                formatted_messages.append(formatted_message)
            else:
                formatted_messages.append(message)
    
    return "\n\n".join(formatted_messages)

with open(input_file, 'r', encoding='utf-8') as f:
    chat_messages = f.readlines()

formatted_chat = format_messages(chat_messages)

with open(output_file, 'w', encoding='utf-8') as f:
    f.write(formatted_chat)

print(f"Formatted chat saved to {output_file}")