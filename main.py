import sys, os, shutil, time, requests, math, psutil

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtGui

import design


def my_round(var, size):
    result = ((var * 100000) // (size * 100000)) * size
    if size >= 1:
        return math.floor(result)
    else:
        return math.floor(result * 100000) / 100000

class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    global CODE_FTXFutures
    global CODE_BinanceFutures

    def __init__(self):

        super().__init__()
        self.setupUi(self)

        self.setWindowIcon(QtGui.QIcon('icon.ico'))
        self.pushButton.clicked.connect(self.updateAmounts)
        self.pushButtonAbout.clicked.connect(self.showDialog)

        self.listWidget.addItem('ВНИМАНИЕ! Закройте CScalp перед выполнением.')

        self.comboBox.addItem('FTX: Бессрочные фьючерсы')
        self.comboBox.addItem('FTX: Спот')
        self.comboBox.addItem('Binance: Бессрочные фьючерсы')
        self.comboBox.addItem('Binance: Спот')

        if os.path.exists('config.ini'):
            with open('config.ini', "r") as f:
                data = f.read()
                self.CODE_FTXFutures = data.split('\n', 10)[0]
                self.CODE_BinanceFutures = data.split('\n', 10)[1]
                self.editLeverage.setText(data.split('\n', 10)[2])
                self.editPart1.setText(data.split('\n', 10)[3])
                self.editPart2.setText(data.split('\n', 10)[4])
                self.editPart3.setText(data.split('\n', 10)[5])
                self.editPart4.setText(data.split('\n', 10)[6])
                self.editPart5.setText(data.split('\n', 10)[7])
                self.editDepo.setText(data.split('\n', 10)[8])
        else:
            self.listWidget.addItem('Ошибка! Файл config.ini не найден')
            self.CODE_FTXFutures = ''
            self.CODE_BinanceFutures = ''
            self.editLeverage.setText('0')
            self.editPart1.setText('0')
            self.editPart2.setText('0')
            self.editPart3.setText('0')
            self.editPart4.setText('0')
            self.editPart5.setText('0')

        self.editCode.setText(self.CODE_FTXFutures)
        print(self.CODE_BinanceFutures)
        self.comboBox.currentIndexChanged.connect(self.comboBoxChanged)
        self.editCode.textChanged.connect(self.codeChanged)

    def codeChanged(self):
        if self.comboBox.currentIndex() == 0:
            self.CODE_FTXFutures = self.editCode.text()
        elif self.comboBox.currentIndex() == 2:
            self.CODE_BinanceFutures = self.editCode.text()

    def comboBoxChanged(self):
        self.listWidget.clear()

        if (self.comboBox.currentIndex() != 0) and (self.comboBox.currentIndex() != 2):
            self.listWidget.addItem('Режим [' + self.comboBox.currentText() + '] находится в разработке')
            self.pushButton.setEnabled(False)
        else:
            self.listWidget.addItem('Установлен режим [' + self.comboBox.currentText() + ']')
            self.pushButton.setEnabled(True)

        if self.comboBox.currentIndex() == 0:
            self.editCode.setText(self.CODE_FTXFutures)

        if self.comboBox.currentIndex() == 2:
            self.editCode.setText(self.CODE_BinanceFutures)

        if (self.comboBox.currentIndex() == 1) or (self.comboBox.currentIndex() == 3):
            self.editLeverage.setEnabled(False)
        else:
            self.editLeverage.setEnabled(True)

    def closeEvent(self, event):
        with open('config.ini', "w") as f:
            f.write(self.CODE_FTXFutures + '\n')
            f.write(self.CODE_BinanceFutures + '\n')
            f.write(self.editLeverage.text() + '\n')
            f.write(self.editPart1.text() + '\n')
            f.write(self.editPart2.text() + '\n')
            f.write(self.editPart3.text() + '\n')
            f.write(self.editPart4.text() + '\n')
            f.write(self.editPart5.text() + '\n')
            f.write(self.editDepo.text())

    def writeToFile(self, MVS_DIR, ACCOUNT_CODE, ex_prefix, ticker, depo, price, size, PART1, PART2, PART3, PART4, PART5):
        volume_max = float(depo) / float(price)
        size = float(size)
        Vol1 = my_round(volume_max * PART1 / 100, size)
        Vol2 = my_round(volume_max * PART2 / 100, size)
        Vol3 = my_round(volume_max * PART3 / 100, size)
        Vol4 = my_round(volume_max * PART4 / 100, size)
        Vol5 = my_round(volume_max * PART5 / 100, size)

        filename = ex_prefix + ticker + '_Settings_' + ACCOUNT_CODE + '.tmp'
        fullname = MVS_DIR + '\\' + filename
        if os.path.exists(fullname):

            with open(fullname, "r") as f, open('temp.txt', "w") as f2:
                lines = f.readlines()

                for line in lines:

                    st = str(line)

                    if (st.find('<First_WorkAmount Value=') != -1) and (PART1 != 0):
                        f2.write('    <First_WorkAmount Value="' + str(Vol1) + '" />\n')

                    elif (st.find('<Second_WorkAmount Value=') != -1) and (PART2 != 0):
                        f2.write('    <Second_WorkAmount Value="' + str(Vol2) + '" />\n')

                    elif (st.find('<Third_WorkAmount Value=') != -1) and (PART3 != 0):
                        f2.write('    <Third_WorkAmount Value="' + str(Vol3) + '" />\n')

                    elif (st.find('<Fourth_WorkAmount Value=') != -1) and (PART4 != 0):
                        f2.write('    <Fourth_WorkAmount Value="' + str(Vol4) + '" />\n')

                    elif (st.find('<Fifth_WorkAmount Value=') != -1) and (PART5 != 0):
                        f2.write('    <Fifth_WorkAmount Value="' + str(Vol5) + '" />\n')

                    # elif st.find('<SlimLevelsFactor Value=')  != -1:
                    #     f2.write('    <SlimLevelsFactor Value="'  + str(1*punkti) +'" />\n')
                    #
                    # elif st.find('<FatLevelsFactor Value=')  != -1:
                    #     f2.write('    <FatLevelsFactor Value="'  + str(10*punkti) +'" />\n')
                    #
                    # elif st.find('<SumTicks_Period Value=')  != -1:
                    #     f2.write('    <SumTicks_Period Value="50" />\n')
                    #
                    # elif st.find('<HideFilteredTicks Value=')  != -1:
                    #     f2.write('    <HideFilteredTicks Value="True" />\n')
                    #
                    # elif st.find('<PlaySoundOnTrade Value=')  != -1:
                    #     f2.write('    <PlaySoundOnTrade Value="True" />\n')

                    else:
                        f2.write(line)

            with open(fullname, "w") as f, open('temp.txt', "r") as f2:
                new_data = f2.read()
                f.write(new_data)

            f.close()
            f2.close()

            if PART1 == 0:
                Vol1 = 'X'

            if PART2 == 0:
                Vol2 = 'X'

            if PART3 == 0:
                Vol3 = 'X'

            if PART4 == 0:
                Vol4 = 'X'

            if PART5 == 0:
                Vol5 = 'X'

            round_st = ticker + ' ($' + str(price) + ') ' + str(Vol1) + ' ' + str(Vol2) + ' ' + str(
                Vol3) + ' ' + str(Vol4) + ' ' + str(Vol5)

            self.listWidget.addItem(round_st)

            return True

        else:
            self.listWidget.addItem('Файл с настройками для инструмента ' + ticker + ' не найден')
            return False


    def updateAmounts(self):
        self.listWidget.clear()

        thereIsError = False

        for proc in psutil.process_iter():
            name = proc.name()
            if name == "CryptoScalp.exe":
                self.listWidget.addItem('Ошибка! Запущен CScalp - выполнение невозможно.')
                thereIsError = True

        try:
            depo = float(self.editDepo.text())
        except ValueError:
            self.listWidget.addItem('Ошибка! Некорректное значение депозита')
            thereIsError = True

        LEVERAGE = 0
        if not self.editLeverage.text().isdigit():
            self.listWidget.addItem('Ошибка! Некорректное значение плеча')
            thereIsError = True
        else:
            LEVERAGE = float(self.editLeverage.text())

        try:
            PART1 = float(self.editPart1.text())
        except ValueError:
            self.listWidget.addItem('Ошибка! Некорректное значение объема 1')
            thereIsError = True

        try:
            PART2 = float(self.editPart2.text())
        except ValueError:
            self.listWidget.addItem('Ошибка! Некорректное значение объема 2')
            thereIsError = True

        try:
            PART3 = float(self.editPart3.text())
        except ValueError:
            self.listWidget.addItem('Ошибка! Некорректное значение объема 3')
            thereIsError = True

        try:
            PART4 = float(self.editPart4.text())
        except ValueError:
            self.listWidget.addItem('Ошибка! Некорректное значение объема 4')
            thereIsError = True

        try:
            PART5 = float(self.editPart5.text())
        except ValueError:
            self.listWidget.addItem('Ошибка! Некорректное значение объема 5')
            thereIsError = True

        if thereIsError:
            return

        MVS_DIR = os.getenv('APPDATA') + '\CScalp\Visualizer\mvs_cs'
        root_src_dir = MVS_DIR
        root_dst_dir = r'backup\backup ' + str(time.time())

        self.listWidget.addItem('Текущее UNIX-время: ' + str(time.time()))
        self.listWidget.addItem('Каталог с настройками: ' + root_src_dir)

        for src_dir, dirs, files in os.walk(root_src_dir):
            dst_dir = src_dir.replace(root_src_dir, root_dst_dir, 1)
            if not os.path.exists(dst_dir):
                os.makedirs(dst_dir)

            for file_ in files:
                src_file = os.path.join(src_dir, file_)
                dst_file = os.path.join(dst_dir, file_)
                if os.path.exists(dst_file):
                    os.remove(dst_file)
                shutil.copy(src_file, dst_dir)

        self.listWidget.addItem('Сформирована резервная копия настроек: ' + root_dst_dir)

        number_updated_files = 0
        number_skipped_tickers = 0

        #  FTX Futures
        if self.comboBox.currentIndex() == 0:
            ex_prefix = 'FTXD.FUT.'
            api_endpoint = "https://ftx.com/api/futures"
            json_data = requests.get(api_endpoint).json()
            depo = depo * LEVERAGE

            for item in json_data['result']:
                if (item['expiryDescription'] == 'Perpetual'):

                    ticker = item['name']
                    price = item['bid']
                    size = item['sizeIncrement']
                    priceIncrement = float(item['priceIncrement'])
                    PriceAggregationStep = 10
                    punkti = math.ceil((price * 0.0007) / (PriceAggregationStep * priceIncrement));

                    if self.writeToFile(MVS_DIR, self.CODE_FTXFutures, ex_prefix, ticker, depo, price, size, PART1, PART2, PART3, PART4, PART5):
                        number_updated_files += 1
                    else:
                        number_skipped_tickers += 1

        #  Binance Futures
        elif self.comboBox.currentIndex() == 2:
            ex_prefix = 'BINAD.CCUR_FUT.'
            api_endpoint_exchange = "https://binance.com/fapi/v1/exchangeInfo"
            api_endpoint_premiumIndex = "https://binance.com/fapi/v1/premiumIndex"
            json_data_exchange = requests.get(api_endpoint_exchange).json()
            json_data_premiumIndex = requests.get(api_endpoint_premiumIndex).json()
            depo = depo * LEVERAGE
            ACCOUNT_CODE = self.editCode.text()

            for item in json_data_exchange['symbols']:
                ticker = item['symbol']
                for filter in item['filters']:
                    if filter['filterType'] == 'LOT_SIZE':
                        size = filter['stepSize']
                for item in json_data_premiumIndex:
                    if item['symbol'] == ticker:
                        price = item['markPrice']

                        if self.writeToFile(MVS_DIR, self.CODE_BinanceFutures, ex_prefix, ticker, depo, price, size, PART1, PART2, PART3, PART4, PART5):
                            number_updated_files += 1
                        else:
                            number_skipped_tickers += 1

        self.listWidget.addItem(str(number_updated_files) + ' файлов обновлено')
        self.listWidget.addItem(str(number_skipped_tickers) + ' инструментов пропущено')

    def showDialog(self):
        QMessageBox.about(self, "О программе",
                          "UpdateCScalpAmounts v0.1.2\n\nПрограмма подключается к бирже\n"
                          "FTX (/api/futures)\n"
                          "Binance (/fapi/v1/exchangeInfo, /fapi/v1/premiumIndex),\n"
                          "где получает список инструментов и текущие цены лучшего бида.\n\nИсходя из цены инструмента, значений депозита, плеча и пропорций" +
                          " расcчитываются объемы.\n\nДалее перезаписываются настройки стаканов в папке C:\\Users\\ИМЯ_ПОЛЬЗОВАТЕЛЯ\\AppData\\Roaming\\CScalp\\Visualizer\\mvs_cs - заменяются значения параметров First|Second|Third|Fourth|Fifth_WorkAmount. Перед перезаписью настройки стаканов сохраняются в папку backup.\n\n" +
                          "В случае, если вы хотите оставить какие-то объемы нетронутыми, поставьте 0 в соответствующем поле.\n\nt.me/s1esarev\nL1FT@yandex.ru"
                          )


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()