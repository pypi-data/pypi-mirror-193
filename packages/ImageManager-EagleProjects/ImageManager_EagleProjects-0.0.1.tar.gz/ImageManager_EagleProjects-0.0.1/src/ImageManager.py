import time
import pyautogui

class ImageManager:
    def waitLoading(self,path,timeout=240,loading=False):
        count= 0
        while count != 5:
            loading_image = pyautogui.locateCenterOnScreen(path)       
            if not loading:
                if loading_image == None:
                    time.sleep(timeout)
                    count+=1
            if loading_image != None:
                return loading_image
        return loading_image

    def switchClick(self,path_original,path_secondary):
        time.sleep(5)
        loading_image = pyautogui.locateCenterOnScreen(path_original)
        if loading_image != None:
            try:
                x_img, y_img = pyautogui.locateCenterOnScreen(path_original)
                pyautogui.moveTo(x_img,y_img)
                pyautogui.click()
            except TypeError:
                    print("Errore: non ho trovato l'elemento a schermo. Riprovare o cambiare immagine")       
        if loading_image == None:
            loading_image = pyautogui.locateCenterOnScreen(path_secondary)
            if loading_image != None:
                try:
                    x_img, y_img = pyautogui.locateCenterOnScreen(path_secondary)
                    pyautogui.moveTo(x_img,y_img)
                    pyautogui.click()
                except TypeError:
                    print("Errore: non ho trovato l'elemento a schermo. Riprovare o cambiare immagine")
        return loading_image

    def clickCustom(self,path,x=0,y=0,click_right=False,clicks_number=1):
        count = 0
        while count != 10:
            try:
                time.sleep(3)
                x_img, y_img = pyautogui.locateCenterOnScreen(path)
                pyautogui.moveTo(x_img+x,y_img+y,1)
                if not click_right:
                    if clicks_number > 1:
                        pyautogui.click(clicks=clicks_number)
                        break
                    else:
                        pyautogui.click()
                        break
                else:
                    pyautogui.click(button='right')
                    break       
            except:
                count+=1