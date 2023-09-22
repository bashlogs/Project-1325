from elevenlabs import generate, play, set_api_key

set_api_key("f4f77a690f86dd20de8549d749a31e69")
audio = generate(
  text="Hello! 你好! Hola! नमस्ते! Bonjour! こんにちは! مرحبا! 안녕하세요! Ciao! Cześć! Привіт! வணக்கம்!",
  voice="Bella",
  model="eleven_multilingual_v2"
)

play(audio)