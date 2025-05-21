#pip install gttsをする必要あり（requirements.txtに追加してない）
from gtts import gTTS

def read_text(text):
    tts = gTTS(text=text, lang='en')
    tts.save("output_file.mp3")

if __name__ == "__main__":
    text = input("Enter the text to read: ")
    read_text(text)


