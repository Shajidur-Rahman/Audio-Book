import pyttsx3
import PyPDF2

book = open('my.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)
speaker = pyttsx3.init()
speaker.say("Hello World! I am Python")
speaker.runAndWait()  # sudo apt install libespeak1

# 8:39
