import sys

from PyQt6 import uic, QtCore, QtGui, QtWidgets
import datetime
import requests
from requests.exceptions import HTTPError
import json

class MainWindow(QtWidgets.QMainWindow):
    ServerAdress = "http://localhost:5000"
    MessageID = 0

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        uic.loadUi('messenger.ui', self)
        self.pushButton1.clicked.connect(self.pushButton1_clicked)

    def pushButton1_clicked(self):
        self.SendMessage()

    def SendMessage(self):
        UserName = self.lineEdit1.text()
        MessageText = self.lineEdit2.text()
        TimeStamp = str(datetime.datetime.today())
        msg = f"{{\"UserName\": \"{UserName}\", \"MessageText\": \"{MessageText}\", \"TimeStamp\": \"{TimeStamp}\"}}"
        # {"UserName": "RusAl", "MessageText": "Privet na sto let!!!", "TimeStamp": "2021-03-05T18:23:10.932973Z"}
        print("Отправлено сообщение: " + msg)
        url = self.ServerAdress + "/api/Messanger"
        data = json.loads(msg)  # string to json
        r = requests.post(url, json=data)
        # print(r.status_code, r.reason)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec())
