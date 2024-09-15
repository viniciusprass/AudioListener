import speech_recognition as sr
from openai import OpenAI

client = OpenAI(
    api_key='chave da api do gpt'
)

def listenAudio(audio_file):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio_data = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio_data, language='pt-BR')
            return text
        except sr.UnknownValueError:
            print("O áudio não pôde ser reconhecido")
            return None
        except sr.RequestError as e:
            print(f"Erro na solicitação: {e}")
            return None

def resumeAudio(text):
    if text:
        prompt = [{"role": "system", "content": f"Resuma este áudio: {text}"}]
        response = client.chat.completions.create(
            messages=prompt,
            model="gpt-4o-mini",
        )
        return response.choices[0].message.content
    else:
        return "Nenhum texto encontrado"

# Arquivo de áudio que será escutado e resumido
audio_file = "exemplo.wav"

text = listenAudio(audio_file)
feed = resumeAudio(text)
print(feed)
