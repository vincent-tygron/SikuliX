import logging; reload(logging)
FORMAT=("%(asctime) -8s %(message) s")
logging.basicConfig(format=FORMAT, filename="TestLog.txt", level=logging.DEBUG)

logging.info("[info Starting Multi Player client...")

#Win & Lin
if Settings.isWindows() or Settings.isLinux():
    dragDrop(Pattern("1460119963739.png").targetOffset(265,6), Pattern("1460119963739.png").targetOffset(-264,10))
    paste("qaautotest1@tygron.com")
    type(Key.TAB)
    paste("autotest1qa")
    click("1460120057083.png")
#Mac
elif Settings.isMac():
    dragDrop(Pattern("1460121516745.png").targetOffset(234,6), Pattern("1460121516745.png").targetOffset(-235,7))
    paste("qaautotest1@tygron.com")
    type(Key.TAB)
    paste("autotest1qa")
    click("1460121696234.png")
    
if exists("1460117970618.png", 5) or ("1460121828166.png", 5):
    print"[success] Client is started and ready!"
    logging.info("[success] Client is started and ready!")
else:
    print"[error] Client is not ready (yet)!"
    logging.error("[error] Client is not ready (yet)!")
    exit(1)
