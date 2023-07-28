import os
import json
import threading
import time
from classes.freelancer import FreelancerClient
from functions.find_replace import find_replace

def bot(configPath, botID):
    print("Bot "+ str(botID) + " running")
    clientBot = FreelancerClient(configPath=configPath)

    for times in range(1, 2):
        print(f"Contagem Total: {clientBot.getProjects()}")
        clientBot.bindAll()
        print("Enviando pedidos a 1/4 deles...")
        time.sleep(5)
    return

    while True:
        print("Bot "+ botID)
        time.sleep(5)
    pass

def main():
    files = os.listdir("./clients")
    for user in files:
        t = threading.Thread(target=bot,args=(f"./clients/{user}",files.index(user)), daemon=False)
        t.start()

if __name__ == "__main__":
    main()