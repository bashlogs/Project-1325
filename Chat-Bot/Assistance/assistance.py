from elevenlabs import generate, play, set_api_key

# Set your API key
set_api_key("f4f77a690f86dd20de8549d749a31e69")

# Define the list of questions
questions = [
    "In which language are you most comfortable communicating?",
    "Is this another appointment or a follow-up from a previous one?",
    "How would you describe your pain or discomfort?",
    "Can you provide some details about your medical history?",
    "Are you currently taking any medications?",
    "Could you please share your health records with us?",
    "Is there anything else you want to convey to the doctor?"
]

# Iterate through the questions and generate audio responses
for question in questions:
    audio = generate(
        text=question,
        voice="Sally",
        model="eleven_multilingual_v2"
    )

    # Play the audio response
    play(audio)
