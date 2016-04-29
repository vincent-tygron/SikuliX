import logging;reload(logging)
FORMAT="%(asctime) -8s%(message)s"

logging.basicConfig(format=FORMAT, filename="Win10-test.log", level=logging.DEBUG)

wait(1)
openApp("C:\Users\Tygron\AppData\Local\Tygron Engine Test\Tygron Engine Test.exe")
wait("1458723954770.png",10)
dragDrop(Pattern("1459934558117.png").targetOffset(262,-127), Pattern("1459934563949.png").targetOffset(-289,-120))
type(Key.BACKSPACE)
paste(Pattern("1458723997314-1.png").targetOffset(2,-119),"qaautotest1@tygron.com")
paste(Pattern("1458723997314-1.png").targetOffset(2,-62),"autotest1qa")
click(Pattern("1458724253575.png").targetOffset(-1,47))
if not exists("1460553626153.png", 3):
    print("[warning]ATI FirePro is finally recognized, or something is off?")
    logging.info("[warning]ATI FirePro is finally recognized, or something is off?")
    print("[message]Please check, and update test if needed!")
    logging.debug("[message]Please check, and update test if needed!")
    #exit(1)
else:
    print("[success]ATI FirePro is correctly flagged!")
    logging.info("[success]ATI FirePro is correctly flagged!")
    click(Pattern("1460553626153.png").targetOffset(-81,141))
    click(Pattern("1460553626153.png").targetOffset(-90,185))
wait("1460631665598.png", 30)
click()
wait("1460640845593.png")
click()
wait("1458724590165.png")
click("1460536225935.png")
waitVanish(Pattern("1458724481310.png").targetOffset(70,-96),10)
openApp("C:\Users\Tygron\AppData\Local\Tygron Engine Test\Tygron Engine Test.exe")
if not exists("1458724821987.png", 30):
    print("[error]Cache NOT deleted!")
    logging.error("[error]Cache NOT deleted!")
    exit(1)
else:
    print("[succes]Cache was deleted!")
    logging.info("[succes]Cache was deleted!")
click(Pattern("1458724821987.png").targetOffset(-168,244))
wait("1458724866547.png",5)
click(Pattern("1458724882027.png").targetOffset(-1,286))
wait("1458723954770.png",10)
paste(Pattern("1458723997314-2.png").targetOffset(2,-119),"qaautotest1@tygron.com")
paste(Pattern("1458723997314-2.png").targetOffset(2,-62),"autotest1qa")
click(Pattern("1458724253575.png").targetOffset(-1,47))
#wait("1460553626153.png", 5)
if not exists("1460553626153.png"):
    print("[warning]ATI FirePro is finally recognized, or something is off?")
    logging.info("[warning]ATI FirePro is finally recognized, or something is off?")
    print("[message]Please check, and update test if needed!")
    logging.debug("[message]Please check, and update test if needed!")
    exit(1)
else:
    print("[success]ATI FirePro is correctly flagged!")
    logging.info("[success]ATI FirePro is correctly flagged!")
click(Pattern("1460553626153.png").targetOffset(-81,141))
click(Pattern("1460553626153.png").targetOffset(-90,185))
wait("1460631813213.png",10)
click()
wait("1458725104634.png",5)
paste("1458725139720.png","WWWWWWWWWWtestWWWWWWW")
click(Pattern("1458725384175.png").targetOffset(233,11))
wait("1458726098136.png",5)
if not exists("1458726098136.png"):
    print("[error]Project name too long, but not flagged!")
    logging.error("[error]Project name too long, but not flagged!")
    exit(1)
else:
    print("[success]Correctly refused project name that was too long!")
    logging.info("[success]Correctly refused project name that was too long!")
click(Pattern("1458726124601.png").targetOffset(219,311))
wait("1460631813213.png",10)
click()
wait("1458725104634.png",5)
paste("1458725139720.png","SikuliX-test-W10-ATI")
click(Pattern("1458725384175.png").targetOffset(233,11))
wait("1458726352431.png")
paste(Pattern("1458726375991.png").targetOffset(-183,-154),"Baarn")
type(Key.ENTER)
#wait("1458726456887.png",10)
if not exists("1458726456887.png", 10):
    print("[error]The search function did not find Baarn!")
    logging.error("[error]The search function did not find Baarn!")
    exit(1)
else:
    print("[success]The search function navigated to the desired location Baarn!")
    logging.info("[success]The search function navigated to the desired location Baarn!")
dragDrop(Pattern("1458726494637.png").targetOffset(-73,-1), Pattern("1458726536957.png").targetOffset(18,-2))
wait("1458726625932.png",10)
click(Pattern("1458726645205.png").targetOffset(418,297))

waittime = 1
for x in range(0, 360):
    if exists("1458727002793.png", waittime):
        print("[success]The wizard has finished creating a 3kmx3km map of rural Baarn in %d seconds!" % (x*waittime))
        logging.info("[success]The wizard has finished creating a 3kmx3km map of rural Baarn in %d seconds!" % (x*waittime))
        break

if not exists("1458727002793.png", waittime):
    print("[error]The wizard process was not finished (in %d seconds)!" % (x*waittime))
    logging.error("[error]The wizard process was not finished (in %d seconds)!" % (x*waittime))
    exit(1)

click(Pattern("1458727031225.png").targetOffset(-111,-174))
wait("1458727053769.png",5)
click(Pattern("1458727053769.png").targetOffset(-19,91))
wait("1458727121384.png",5)
click(Pattern("1458727121384.png").targetOffset(49,60))
waitVanish("1458727053769.png",5)
openApp("C:\Users\Tygron\AppData\Local\Tygron Engine Test\Tygron Engine Test.exe")
wait("1458723954770.png",10)
#paste(Pattern("1458723997314-3.png").targetOffset(2,-119),"qaautotest1@tygron.com")
paste(Pattern("1458723997314-3.png").targetOffset(2,-62),"autotest1qa")
click(Pattern("1458724253575.png").targetOffset(-1,47))
if exists("1460553626153.png"):
    click(Pattern("1460553626153.png").targetOffset(-81,141))
    click(Pattern("1460553626153.png").targetOffset(-90,185))
wait("1460538469559.png",30)
click()
wait("1458727294464.png")
click(Pattern("1458727307210.png").targetOffset(812,-495))
