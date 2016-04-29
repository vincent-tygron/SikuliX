import logging; reload(logging)
FORMAT=("%(asctime) -8s %(message) s")
logging.basicConfig(format=FORMAT, filename="testLog.txt", level=logging.DEBUG)

logging.info("[info] Assigning clients to team...")

if Settings.isLinux() or Settings.isWindows():
    #Linux
    for x in range(0, 5):
        while exists("MainMenu-MultiPlayer-Tygron18-LinuxClient-160422-VVD-0.2.png", x):
            click()
            waitVanish("MainMenu-MultiPlayer-Tygron18-LinuxClient-160422-VVD-0.2.png", 1)
            break
    #Win8.1
    for x in range(0, 5):
        while exists("MainMenu-MultiPlayer-Mario3-Win8.1Client-160422-VVD-0.1.png", x):
            click()
            waitVanish("MainMenu-MultiPlayer-Mario3-Win8.1Client-160422-VVD-0.1.png", 1)
            break
    #Win10
    for x in range(0, 5):
        while exists("MainMenu-MultiPlayer-Tygron16-Win10Client-160422-VVD-0.1.png", x):
            click()
            waitVanish("MainMenu-MultiPlayer-Tygron16-Win10Client-160422-VVD-0.1.png", 1)
            break
    #MacOSX
    for x in range(0, 5):
        while exists("MainMenu-MultiPlayer-TygronsMacBook-MacOSXClient-160422-VVD-0.1.png", x):    
            click()
            waitVanish("MainMenu-MultiPlayer-TygronsMacBook-MacOSXClient-160422-VVD-0.1.png", 1)
            break

#########################################
# Check if all clients are connected... #
#########################################
    if exists("Admin-MultiPlayer-FourClientsConnected-160422-VVD-0.1.png", 30):
        print"[success] Clients were successfully invited and connected!"
        logging.info("[success] Clients were successfully invited and connected!")
    else:
        print"[error] Clients were not connected (in time)!"
        logging.error("[error] Clients were not connected (in time)!")
        exit(1)

else:
    exit(1) #OSX >>> Wip