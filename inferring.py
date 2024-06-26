import time
from settings import model

input_file_path = "C:\\Users\\ragar\\Desktop\\BridgeLabz_tasks\\GenAI\\GenAI\\Reviews.txt"
output_file_path = "C:\\Users\\ragar\\Desktop\\BridgeLabz_tasks\\GenAI\\GenAI\\Sentiment_Analysis.txt"


def read_file(file_path):
    with open(file_path, 'r', encoding="utf-8") as file:
        content = file.read()
    reviews = content.strip().split('|')
    return reviews

def process_reviews(reviews):
    responses = []
    for review in reviews:
        response = model.generate_content(f"""{review} Given the user's comment, generate a response that categorizes the comment into Positive, Neutral, or Negative based on its sentiment. Your response should include the following information formatted as a dictionary:
                                              - original_review: [the original review],
                                              - brand: [mention the brand if available, else 'unknown'],
                                              - product: [mention the product if available, else 'unknown'],
                                              - sentiment: [positive, negative, or neutral]""")
        responses.append(response.text)
        print(response.text)
        time.sleep(2)
    return responses

def save_responses(file_path, responses):
    with open(file_path, "w", encoding="utf-8") as file:
        for response in responses:
            file.write(response + '\n')

reviews = read_file(input_file_path)
responses = process_reviews(reviews)
save_responses(output_file_path, responses)
print(f"Responses saved to {output_file_path}")