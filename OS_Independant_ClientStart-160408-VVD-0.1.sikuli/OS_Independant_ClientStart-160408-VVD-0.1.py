import logging; reload(logging)
FORMAT=("%(asctime) -8s %(message) s")
logging.basicConfig(format=FORMAT, filename="TestLog.txt", level=logging.DEBUG)

logging.info("[info Starting Multi Player client...")

dragDrop(Pattern("1460117725818.png").similar(0.74).targetOffset(266,8), Pattern("1460117725818.png").similar(0.74).targetOffset(-264,11))
paste("qaautotest1@tygron.com")
type(Key.TAB)
paste("autotest1qa")
click("1460117908066.png")
if exists("1460117970618.png", 30):
    print"[success] Client is started and ready!"
    logging.info("[success] Client is started and ready!")
else:
    print"[error] Client is not ready (yet)!"
    logging.error("[error] Client is not ready (yet)!")
    exit(1)