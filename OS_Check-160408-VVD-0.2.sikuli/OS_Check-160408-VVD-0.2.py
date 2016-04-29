import logging; reload(logging)
FORMAT=("%(asctime) -8s %(message) s")
logging.basicConfig(format=FORMAT, filename="LinuxTestLog.txt", level=logging.DEBUG)

logging.info("[info] Check for Operating System...")

myVer = Settings.getOSVersion()
if Settings.isLinux():
    print "Linux detected! " + myVer
    logging.info("[info] Linux detected !" + myVer)
elif Settings.isWindows():
    print "Windows detected! " + myVer
    logging.info("[info] Windows detected !" + myVer)
elif Settings.isMac():
    print "Mac OSX detected! " + myVer
    logging.info("[info] MAC OSX detected !" + myVer)
else:
    print "Unsupported OS detected!"
    logging.error("[error] Unsupported OS detected!")
    exit(1)