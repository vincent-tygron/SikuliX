import logging;reload(logging)
FORMAT="%(asctime) -8s%(message)s"

logging.basicConfig(format=FORMAT, filename="Win10-test.log", level=logging.DEBUG)

logging.info("[info] >>>>>>>>>> Start Win 10 - TestsuiteA <<<<<<<<<<")

runScript("C:\Users\Tygron\Documents\SikuliX\Delete_Install-160322-VVD-0.1.sikuli")
runScript("C:\Users\Tygron\Documents\SikuliX\SkipGPUWarning-WipeCache-160411-VVD-0.2.sikuli")

logging.info("[info]<<<<<<<<<< End Win 10 - TestsuiteA >>>>>>>>>>")