import pyttsx3  #library for text-to-speech conversion.
if __name__ == '__main__':
    print("Welcome to Robo Speaker!!")
    text_to_speech = pyttsx3.init()
    while(True):
        word = input("Enter what you want me to speak or 'q' to quit: ")
        if(word == 'q'):
            break
        text_to_speech.say(word)
        text_to_speech.runAndWait()







