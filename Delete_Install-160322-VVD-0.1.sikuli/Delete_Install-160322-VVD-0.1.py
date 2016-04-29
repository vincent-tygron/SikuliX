import logging;reload(logging)
FORMAT="%(asctime) -8s%(message)s"

logging.basicConfig(format=FORMAT, filename="Win10-test.log", level=logging.DEBUG)

logging.info("[info]Start Delete/ Install Test...")

find("1458638032195.png")
click("1458638040321.png")
find("1458638188162.png")
click("1458638207824.png")
find("1458638283547.png")
click("1458638303330.png")
find("1458638319324.png")
click("1458638327785.png")
wait(Pattern("1458638569014.png").targetOffset(19,69))
paste("1458638381685.png","Tygron Engine Test")
find("1458638660162.png")
click("1458638672136.png")
wait("1458638982008.png")
click("1458638997119.png")
wait("1458638828383.png")
click(Pattern("1458638842564.png").targetOffset(109,18))
click(Pattern("1458641667735.png").targetOffset(576,-453))
#waitVanish("1458809558926.png",10)
if not exists("1458809558926.png", 10):
    print("[success] Tygron Engine Test has been removed!")
    logging.info("[success] Tygron Engine Test has been removed!")
else:
    print("[error] Tygron Engine Test was not removed as expected!")
    logging.error("[error] Tygron Engine Test was not removed as expected!")
    exit(1)
import webbrowser
new = 2
url = "https://test.tygron.com"
webbrowser.open(url,new=new)
#App.open("C:\\Program Files (x86)\\Mozilla Firefox\\Firefox.exe")
#wait("1458639243393.png", 10)
#paste("1458639260527.png","https://test.tygron.com")
#type(Key.ENTER)
wait("1458639705634.png")
click()
wait("1458640884456.png")
click(Pattern("1458640896765.png").targetOffset(72,69))
wait("1458640942655.png")
click("1458640957062.png")
wait("1458641042840.png",30)
click("1458641042840.png")
wait("1458641092245.png")
click(Pattern("1458641104937.png").targetOffset(106,166))
wait("1458641162601.png",15)
click(Pattern("1458641179495.png").targetOffset(-61,110))
wait(Pattern("1458641218515.png").targetOffset(-76,-3))
click(Pattern("1458641277766.png").targetOffset(813,-493))
click(Pattern("1458641242061.png").targetOffset(102,168))
wait(Pattern("1458642790773.png").targetOffset(-1,61),10)
if not exists (Pattern("1458642790773.png").targetOffset(-1,61)):
    print("[error]Tygron Engine Test did not load as expected!")
    logging.error("[error]Tygron Engine Test did not load as expected!")
    exit(1)
else:
    print("[succes]Tygron Engine Test has been installed correctly, and loaded as expected!")
    logging.info("[succes]Tygron Engine Test has been installed correctly, and loaded as expected!")
click(Pattern("1458641361256.png").targetOffset(816,-491))
click("1458641994497.png")
wait(Pattern("1458642026903.png").similar(0.49), 10)
click(Pattern("1458642041048.png").targetOffset(1,66))
wait("1458642073958.png")
click(Pattern("1458642084829.png").targetOffset(187,-19))
click(Pattern("1458642118856.png").targetOffset(-183,-11))
if not exists("1458643037300-1.png"):
    click(Pattern("1459416911329.png").similar(0.58).targetOffset(76,23))
else:
    click(Pattern("1458643053152-1.png").targetOffset(73,92))
if exists("1459926872435.png"):
    print("[success] Installer(s) removed!")
    logging.info("[success] Installer(s) removed!")
else:
    print("[error] Not all downloads were cleared!")
    logging.error("[error] Not all downloads were cleared!")
click(Pattern("1458642203157.png").targetOffset(540,-301))
logging.info("[info]End Delete/ Install Test...")








