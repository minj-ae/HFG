from pick import pick
import os
import win32api
import art
import time

def main():
    drives = win32api.GetLogicalDriveStrings()
    title = ''
    des = ''
    options = ''
    option = ''
    index = ''
    foldername = ''
    folderdir = ''
    checkex = False

    title=art.text2art("HFG")
    des = "Hidden Folder Generator for Windows\n EMAIL: munji@munji.kr\n\n\n\n"
    options = ['PRESS ENTER TO START']
    option, index = pick(options, title, des) 
    if index == 0:
        title = 'Select Folder Type'
        options = ['Create fake system folder']
        option, index = pick(options, title) 
        if index == 0:
            title = 'Select Hardware Device'
            options = drives.split('\000')[:-1]
            option, index = pick(options, title)
            foldername = input("Folder Name: ")
            folderdir = (option+foldername)
            checkex = os.path.isdir(folderdir)
            if checkex is True:
                print("Sorry, folder already exists.")
                time.sleep(3)
                main()
            else:
                os.system('cls')
                os.mkdir(folderdir)
                os.system('attrib +s +h '+ folderdir)
                print("Done! You can now access to "+ folderdir)
                time.sleep(5)

if __name__ == "__main__":
    main()