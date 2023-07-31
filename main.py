from lineNotify import *;


class Main ():

    def __init__(self):
        self.startProcess();

    def startProcess(self):

        ln = LineNotify()

        ## sticker package id 1 sticker_id 19 Angry Brown
        ## sticker package id 2 sticker_id 26 Coney Sleep
        
        ln.sendNotifyMessage("Hello World This is a first Message");
        ln.sendNotifyStickerAndMessage("Cony Go Sleep" , 2 , 26);

start = Main();
