# Import the required modules
import pyautogui as gui
import pytesseract as pyt
from PIL import Image
from time import sleep

pyt.pytesseract.tesseract_cmd = r'C:\Users\GANESH\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'


def Image_text():
    '''Getting text from an image'''

    img = Image.open(r'Images\testImage1.jpg')
    # img.show('images')

    text = pyt.image_to_string(img)
    # print(text)

    def Notepad_text(text):
        '''Writing text on notepad'''

        sleep(3)
        gui.write(text,interval=0.25)

    Notepad_text(text)

    

if __name__ == "__main__":

    Image_text()

    print("Code Completed 🔥")