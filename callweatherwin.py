import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QWidget

from weatherwin import Ui_Form
import requests

class mainwindow(QMainWindow):
    def __init__(self):
        super(mainwindow, self).__init__()
        self.ui=Ui_Form()
        self.ui.setupUi(self)

    def queryWeather(self):
        print("* queryWeather ")
        cityname=self.ui.weatherComboBox.currentText()
        citycode=self.transcityname(cityname)
        rep=requests.get("http://www.weather.com.cn/data/sk/"+citycode+".html")
        rep.encoding="utf-8"
        print(rep.json())

        msg1="城市：{} \n".format(rep.json()['weatherinfo']['city'])
        msg2 = "风向：{} \n".format(rep.json()['weatherinfo']['WD'])
        msg3 = "温度：{} 度\n".format(rep.json()['weatherinfo']['temp'])
        msg4 = "风力：{} \n".format(rep.json()['weatherinfo']['WS'])
        msg5 = "湿度：{} \n".format(rep.json()['weatherinfo']['SD'])

        result=msg1+msg2+msg3+msg4+msg5
        self.ui.resultText.setText(result)

    def transcityname(self,cityname):
        citycode=""
        if cityname =="北京":
            citycode='101010100'
        elif cityname =='上海':
            citycode="101020100"
        elif cityname =='南阳':
            citycode="101180701"
        elif cityname =='淅川':
            citycode="101180708"

        return citycode
    def clearResult(self):
        print(" * clearresult ")
        self.ui.resultText.clear()

if __name__ == '__main__':
    app=QApplication(sys.argv)
    win=mainwindow()
    win.show()
    sys.exit(app.exec_())
