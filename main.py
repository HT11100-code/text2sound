import pyttsx3

def read_text(text):
    engine = pyttsx3.init()
    
    rate = engine.getProperty('rate')
    #engine.setProperty('rate', rate - 50)
    #読み上げ速度の変更

    #voices = engine.getProperty('voices') 現在のボイスの取得
    #engine.setProperty('voice', voices[0].id)　ボイスの変更
    

    engine.say(text)
    engine.runAndWait()
    

if __name__ == "__main__":
    text = input("Enter the text to read: ")
    read_text(text)