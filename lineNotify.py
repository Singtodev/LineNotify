import requests
import os;
class LineNotify:
    
    def __init__(self):

        current_dir = os.path.dirname(os.path.abspath(__file__));

        file_path = current_dir + "/config.txt"

        try:
            with open(file_path, "r") as file:
                for line in file:
                    str = line.strip().split("=");
                    if str[0] == "line_token":
                        self.line_token = str[1];
                    elif str[0] == "line_api_url":
                        self.line_api_url = str[1];
        
        except FileNotFoundError:
            print(f"Error: File '{file_path}' not found.")

    def sendNotifyMessage(self , message):




        headers = {
            "Authorization": f"Bearer " + self.line_token,
        }

        data = {
            "message": message,
        }


        response = requests.post(self.line_api_url, headers=headers , data=data);

        if response.status_code == 200:
            print("Send Message Success!");
        else:
            print(F"Failed To send Message. Response : {response.status_code} , {response.text}");

    def sendNotifyStickerAndMessage(self , message , sticker_package_id , sticker_id):

        headers = {
            "Authorization": f"Bearer " + self.line_token,
        }

        data = {
            "message": message,
            "stickerPackageId": sticker_package_id,
            "stickerId": sticker_id,
        }

        response = requests.post(self.line_api_url, headers=headers , data=data);

        if response.status_code == 200:
            print("Send Message And Sticker Success!");
        else:
            print(F"Failed To send Sticker Line And Message. Response : {response.status_code} , {response.text}");






