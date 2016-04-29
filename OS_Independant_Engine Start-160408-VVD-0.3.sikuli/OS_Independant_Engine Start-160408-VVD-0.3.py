import logging; reload(logging)
FORMAT=("%(asctime) -8s %(message) s")
logging.basicConfig(format=FORMAT, filename="TestLog.txt", level=logging.DEBUG)

logging.info("[info] Check for Operating System...")

myVer = Settings.getOSVersion()

if Settings.isLinux():
    print "Linux detected! " + myVer
    logging.info("[info] Linux detected !" + myVer)
    find(Pattern("1459944594366.png").similar(0.89))
    doubleClick(Pattern("1459944608542.png").similar(0.84))
    doubleClick("1459944634342.png")
    click(Pattern("1459944716230.png").targetOffset(237,52))
    
elif Settings.isWindows():
    print "Windows detected! " + myVer
    logging.info("[info] Windows detected !" + myVer)
    doubleClick(Pattern("1460107790360.png").similar(0.80))
    
elif Settings.isMac():
    print "Mac OSX detected! " + myVer
    logging.info("[info] MAC OSX detected !" + myVer)
    click("1460107474940.png")
    click(Pattern("Screen Shot 2016-03-22 at 2.02.29 PM.png").targetOffset(59,11))
    doubleClick("1460109683894.png")
    #wait("1458652391503.png", 3)
    #click(Pattern("1458652391503.png").targetOffset(145,62))
    
else:
    print "Unsupported OS detected!"
    logging.error("[error] Unsupported OS detected!")
    exit(1)
    
if exists("1460109797811.png", 10) or exists("1460111982242.png", 10):
    print "[success] Engine started!" 
    logging.info("[success] Engine started!")
else:
    print "[error] Engine not started!"
    logging.error("[error] Engine not started!")
    exit(1)