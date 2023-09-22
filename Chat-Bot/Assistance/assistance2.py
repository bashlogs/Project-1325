import json
from elevenlabs import generate, play, set_api_key

set_api_key("f4f77a690f86dd20de8549d749a31e69")

with open('api/data/ques.json', 'r', encoding='utf-8') as json_file:
    all_questions = json.load(json_file)

print("Please select your preferred language:")
for idx, language_set in enumerate(all_questions):
    print(f"{idx + 1}. {language_set['language']}")

selected_language_index = int(input("Enter the number corresponding to your preferred language: ")) - 1

if 0 <= selected_language_index < len(all_questions):
    selected_language = all_questions[selected_language_index]
    selected_questions = selected_language['questions']

    for question in selected_questions:
        audio = generate(
            text=question,
            voice="Sally",
            model="eleven_multilingual_v2",
            # language=selected_language['language']
        )
        play(audio)

else:
    print("Invalid language selection. Please choose a valid language.")
