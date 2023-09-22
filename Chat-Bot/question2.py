import json
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
nltk.download('punkt')
# Load NLTK stopwords (you might need to download them if not already installed)
nltk.download('stopwords')

# Load the JSON data from a file
with open('api/data/questions.json', 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)

# Function to extract keywords from text
def extract_keywords(text):
    # Tokenize the text
    words = word_tokenize(text)

    # Remove stopwords and punctuation
    stop_words = set(stopwords.words('english'))
    keywords = [word.lower() for word in words if word.isalnum() and word.lower() not in stop_words]

    return keywords

if __name__ == '__main__':
    while True:
        # Ask the user for keywords
        user_keywords = input("Enter keywords (space-separated): ").strip().split()

        # Check if the user wants to exit
        if not user_keywords:
            break

        matching_answers = []

        # Search for matching questions and their corresponding answers
        for item in data:
            item_question = item.get('question', '')
            item_keywords = extract_keywords(item_question)
            if any(keyword in item_keywords for keyword in user_keywords):
                matching_answers.append((item_question, item.get('answer', 'No answer found.')))

        if not matching_answers:
            print("No matching answers found.")
        else:
            print("Matching Answers:")
            for question, answer in matching_answers:
                # print("Question:", question)
                print("Answer:", answer)
                print()

    print("Goodbye!")
