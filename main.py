import pyttsx3

def read_text(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    text = input("Enter the text to read: ")
    read_text(text)