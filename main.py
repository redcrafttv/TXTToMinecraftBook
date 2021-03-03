import string
import pyautogui
import time
import pyperclip

fileInput = open('input.txt', 'r')


def main():
    time.sleep(5)
    for line in fileInput:
        print(line)
        pyperclip.copy(line)
        pyautogui.hotkey("ctrl", "v")
        pyautogui.hotkey("return")
        


#def main():
#    time.sleep(5)
#    #pyautogui.rightClick(x=500, y=500)
#    pages = []
#    current = ""
#    for line in fileInput:
#        modified = line + " "
#        for char in modified:
#           current += char
#            if len(current) == 10:
#                pages.append(current)
#                current = ""
#    i = 1  # Not started
#    j = 1  # Erstes buch in der Hotbar
#
#    for page in pages:
#        pyautogui.write(page)
#        print(i)
#        time.sleep(0.05)
#        if i == 99:
#            #pyautogui.moveTo(x=1071, y=437)
#            #pyautogui.leftClick(x=1071, y=437)
#            print("100 Reached")
#            time.sleep(0.1)
#            if j == 9:
#                j = 1
#                print("Hotbar Austauschen")
#                time.sleep(10)
#            print("Nächstes Buch")
#            time.sleep(1)
#
#            #pyautogui.rightClick(x=500, y=500)
#            j += 1
#            i = 1
#        else:
#            pass#pyautogui.click(x=1025, y=359)
#        i += 1  # Nächste Seite


if __name__ == '__main__':
    main()
