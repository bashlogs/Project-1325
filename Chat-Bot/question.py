import json
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

nltk.download('stopwords')
nltk.download('punkt')

with open('api/data/questions.json', 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)

def extract_keywords(text):
    words = word_tokenize(text)

    stop_words = set(stopwords.words('english'))
    keywords = [word.lower() for word in words if word.isalnum() and word.lower() not in stop_words]

    return keywords

def search_answers_by_keywords(keywords):
    matching_answers = []
    for item in data:
        item_keywords = extract_keywords(item['question'])
        if any(keyword in item_keywords for keyword in keywords):
            matching_answers.append(item)

    return matching_answers

if __name__ == '__main__':
    while True:
        user_question = input("Ask a question (or 'exit' to quit): ").strip()

        if user_question.lower() == 'exit':
            break

        user_keywords = extract_keywords(user_question)

        matching_answers = search_answers_by_keywords(user_keywords)

        if not matching_answers:
            print("No matching answers found.")
        else:
            print("Matching Answers:")
            for answer in matching_answers:
                print("Question:", answer['question'])
                print("Answer:", answer['answer'])
                print("Answer Author:", answer['answer_author'])
                print("URL:", answer['url'])
                print()

    print("Goodbye!")
