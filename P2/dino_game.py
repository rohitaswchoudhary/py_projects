import pyautogui
import time
from PIL import Image, ImageGrab

def hit(key):
    pyautogui.keyDown(key)


def is_collide(data):

    for i in range(300,415):
        for j in range(410,560):
            if data[i,j]<40:
                hit("down")
                return True

    for i in range(300,415):
        for j in range(563,650):
            if data [i,j]<40:
                hit('up')
                return True

    return False

if __name__ == "__main__":
    time.sleep(10)
    hit('up')

    while True:
        image= ImageGrab.grab().convert('L')
        data = image.load()
        is_collide(data)


        # print(asarray(image))


        for i in range (300,415):
            for j in range(410,563):
                data[i,j] = 171

        image.show()
        break