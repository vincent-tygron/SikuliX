if exists("Admin-MultiPlayer-FourClientsConnected-160422-VVD-0.1.png", 30):
    print"[success] Clients were successfully invited and connected!"
    logging.info("[success] Clients were successfully invited and connected!")
else:
    print"[error] Clients were not connected (in time)!"
    logging.error("[error] Clients were not connected (in time)!")
    exit(1)