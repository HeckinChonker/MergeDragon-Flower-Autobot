from imagesearch import * 

#Begin Game loop
while True:
    creaturematchloc = imagesearcharea("C:\\Python Projects\\MergeDragon-Flower-Autobot\\leftCreature.png", 0, 0, 3440, 1440, 0.65)
    if creaturematchloc[0] != -1:
            pyautogui.moveTo(creaturematchloc[0] + 10, creaturematchloc[1] + 10)
            pyautogui.dragTo(1720, 720, 0.5)
            time.sleep(7)
    else:
        creaturematchloc = imagesearcharea("C:\\Python Projects\\MergeDragon-Flower-Autobot\\rightcreature.png", 0, 0, 3440, 1440, 0.65)
        if creaturematchloc[0] != -1:
            pyautogui.moveTo(creaturematchloc[0] + 10, creaturematchloc[1] + 10)
            pyautogui.dragTo(1720, 720, 0.5)
            time.sleep(7)
    # leafMatchLoc = imagesearcharea("c:\\Users\\mritt\\Documents\\Python Projects\\MergeDragon-Flower-Autobot\\leaf.PNG", 0, 0, 3440, 1440, 0.85)
    # if leafMatchLoc[0] != -1:
    #     pyautogui.moveTo(leafMatchLoc[0] + 10, leafMatchLoc[1] + 10)
    #     pyautogui.click()
    #     time.sleep(1)