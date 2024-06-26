import time
import json
from settings import model

input_file_path = "C:\\Users\\ragar\\Desktop\\BridgeLabz_tasks\\GenAI\\GenAI\\Reviews.txt"
output_file_path = "C:\\Users\\ragar\\Desktop\\BridgeLabz_tasks\\GenAI\\GenAI\\Sentiment_Analysis.json"

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
        response_text = response.text.strip().strip('```')

        print(f"Response Text: {response_text}")
        
        try:
            response_json = json.loads(response_text)
            responses.append(response_json)
            print(response_json)
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
            print(f"Response was: {response_text}")
        
        time.sleep(2)
    return responses

def save_responses(file_path, responses):
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(responses, file, ensure_ascii=False, indent=4)

reviews = read_file(input_file_path)
responses = process_reviews(reviews)
save_responses(output_file_path, responses)
print(f"Responses saved to {output_file_path}")
