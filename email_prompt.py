from setting import model
import pandas as pd
import time
from email.parser import Parser

def read_emails_from_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    emails = []
    raw_emails = content.strip().split('|')
    print(type(raw_emails))
    for raw_email in raw_emails:
        email_message = Parser().parsestr(raw_email.strip())
        email = {
            'From': email_message['From'],
            'To': email_message['To'],
            'Subject': email_message['Subject'],
            'Body': email_message.get_payload()
        }
        emails.append(email)

    return emails

file_path = 'C:/Users/ragar/Desktop/BridgeLabz_tasks/GenAI/GenAI/Emails.txt'
emails = read_emails_from_file(file_path)

processed_emails = []

for email in emails:
    print(f"Original Email:\n{email}\n")
    response = model.generate_content(f"Summarize the following email body:\n\n{email['Body']} it should cover all the information in the text ")
    summary = response.text
    transformed_response = model.generate_content(f"Transform the following summarized mail body to Spanish: \n\n{summary}")
    transformed_text = transformed_response.text
    print(f"Summary:\n{summary}\n")
    print(f"Transformed Text (Spanish):\n{transformed_text}\n")
    time.sleep(2)

    processed_emails.append({
        'From': email['From'],
        'To': email['To'],
        'Body': email['Body'],
        'Summary': summary,
        'Transformed Text': transformed_text
    })

df = pd.DataFrame(processed_emails)
output_file_path = 'C:/Users/ragar/Desktop/BridgeLabz_tasks/GenAI/GenAI/Emails_output.xlsx'
df.to_excel(output_file_path, index=False)

print(f"Processed emails have been saved to {output_file_path}")