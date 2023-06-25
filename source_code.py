from PIL import ImageGrab, Image
import numpy as np
import cv2 as cv
import pyautogui
import pydirectinput
import keyboard
import math
import time
import webbrowser

pyautogui.PAUSE = 0.0
previous_clicks = []
max_prev_clicks = 3

    #Functions
def distance(x1, y1, x2, y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

#Main Auto-Clicker
def autoclicker():
    global day, max_prev_clicks, previous_clicks
    game_window = [331, 214, 1210, 823]
    work_area = [331, 483, 1064, 823]

    while True:
        #Breaking the loop
        if(keyboard.is_pressed('p')):
            keyboard.wait('p')
        if(keyboard.is_pressed('esc')):
            break
        
        #In menu
        while(pyautogui.pixel(675, 789) == (255, 255, 255)):
            if(pyautogui.pixelMatchesColor(1051, 225, (75, 190, 66), tolerance = 5) != True):
                if(pyautogui.confirm('The House Health is not full. Do you want to buy it ?', buttons = ['Yes', 'No']) == 'Yes'):
                    pyautogui.click(x = 553, y = 344, clicks=5)
            if(pyautogui.confirm('Do you want to buy more ammo ?', buttons = ['Yes', 'No']) == 'Yes'):
                count = pyautogui.prompt('How many times do you want to click the ammo button ?')
                pyautogui.click(x = 419, y = 355, clicks= int(count))

            #Clicking on Done
            if(pyautogui.confirm('Do you want to go resume the game ?', buttons = ['Yes', 'No']) == 'Yes'):
                pyautogui.click(x = 675, y = 789)
                day = day + 1
                time.sleep(1)
            else:
                pyautogui.alert('Press OK to continue') 
                pyautogui.click(x = 675, y = 789)
                day = day + 1
                time.sleep(1)

        #Reload If empty
        if(pyautogui.pixelMatchesColor(345, 225, (202, 208, 72), tolerance = 5) != True):
            pydirectinput.press('space')

        #Gray for the finding the value
        img = np.array(ImageGrab.grab(bbox = work_area))
        gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)

        for i in range(0, len(gray), 20):
            flag = 0
            for j in range(0, len(gray[0]), 20):
                flag1 = 0
                for k in previous_clicks:
                    if distance(i, j, k[0], k[1]) < 30:
                        flag1 = 1
                        break
                if(flag1 == 1):
                    continue
                if(gray[i][j] <= 30):
                    pyautogui.click(x = (work_area[0] + j),y = (work_area[1] + i), clicks=2)
                    if(j < 545):
                        previous_clicks.append([i,j])
                    flag = 1
                    break
            if(flag == 1):
                break
        
        if(day == 12):
            max_prev_clicks = 1

        if len(previous_clicks) > max_prev_clicks:
            del previous_clicks[0]

#Code


webbrowser.open('https://www.crazygames.com/game/storm-the-house')

if __name__ == "__main__":
    global day
    day = 1
    pyautogui.alert('Press \n1.\'Right Ctrl\' to Start the Auto-Clicker \n2.\'P\' Key to Pause the Auto-Clicker \n2.\'Escape\' to Exit the Auto-Clicker')
    keyboard.wait('Ctrl')  

    autoclicker()

    print("Done on day ", day)