# Import the required modules
import pyautogui as gui
import pytesseract as pyt
from PIL import Image

pyt.pytesseract.tesseract_cmd = r'C:\Users\GANESH\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'


def Image_text():
    '''Getting text from an image'''

    img = Image.open(r'Images\testImage1.jpg')
    # img.show('images')

    text = pyt.image_to_string(img)
    # print(text)


if __name__ == "__main__":

    Image_text()

    print("Code Completed 🔥")