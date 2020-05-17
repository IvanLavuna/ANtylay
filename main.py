import speech_recognition as sr
import pyttsx3

badWords = []


''' 
this function fills badWords array with bad words
'''
def fillBadWordsWithWords(file):
    f = open(file, "r")
    f1 = f.readlines()
    for i in f1:
        badWords.append(i)

'''
this function says not to swear
'''
def sayNotToCurse():
    engine = pyttsx3.init("espeak")
    engine.setProperty('rate', 150)
    engine.say('''D'not swear Julian !''')
    engine.runAndWait()


''' 
3 values as parameters
checking a given word for how much it is similar 
as given bad word from a list of Bad words  
'''


def similar(curWord, badWord, percent):
    matrix = [[0 for i in range(len(curWord) + 1)] for i in range(len(badWord) + 1)]
    biggestSubString = 0

    for i in range(len(badWord)):
        for j in range(len(curWord)):
            if badWord[i] == curWord[j]:
                matrix[i + 1][j + 1] = matrix[i][j] + 1
                biggestSubString = max(biggestSubString, matrix[i + 1][j + 1])
            else:
                matrix[i + 1][j + 1] = max(matrix[i + 1][j], matrix[i][j + 1])
                biggestSubString = max(biggestSubString, matrix[i + 1][j + 1])

    maxLen = max(len(badWord), len(curWord))

    if maxLen == 0:
        return False

    return biggestSubString / maxLen >= percent


'''
This is a function for checking if current word is a bad word
'''


def inBadWords(curWord):
    for badWord in badWords:
        if similar(curWord, badWord, 0.6) or '*' in curWord:
            return True
    return False


def main():
    r = sr.Recognizer()
    m = sr.Microphone()
    try:
        with m as source:
            r.adjust_for_ambient_noise(source)
        print("Set minimum energy threshold to {}".format(r.energy_threshold))

        while True:
            with m as source:
                audio = r.listen(source)
            try:
                # recognize speech using Google Speech Recognition
                value = r.recognize_google(audio, language="uk-UA")

                print(value)
                value = value.split()

                for val in value:
                    if inBadWords(val):
                        print("is recognised")
                        sayNotToCurse()


            except sr.UnknownValueError:
                pass
            except sr.RequestError as e:
                print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    fillBadWordsWithWords("погані_слова.txt")
    main()
