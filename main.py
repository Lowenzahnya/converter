import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from ui import Ui_MainWindow
from currency_converter import CurrencyConverter


class CurrencyConv(QtWidgets.QMainWindow):
	def __init__(self):
		super(CurrencyConv, self).__init__()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.init_UI()
	
	def init_UI(self):
		self.setWindowTitle('Конвертер')
		self.setWindowIcon(QIcon('exchanging.png'))

# Перепутал местами output_ currency и amount в Qt, поэтому все наоборот
		self.ui.input_currency.setPlaceholderText('Из валюты')
		self.ui.input_amount.setPlaceholderText('У меня есть')
		self.ui.output_currency.setPlaceholderText("Получаем")
		self.ui.output_amount.setPlaceholderText("Хочу приобрести")
		self.ui.pushButton.clicked.connect(self.converter)

	def converter(self):
		try:
			c = CurrencyConverter()
			input_currency = self.ui.input_currency.text().upper()
			output_amount = self.ui.output_amount.text().upper()
			input_amount = int(self.ui.input_amount.text())
			output_currency = round(c.convert(input_amount, input_currency, output_amount), 2)

			self.ui.output_currency.setText(str(output_currency))
		except:
			self.ui.output_currency.setText('Неверные данные')


app = QtWidgets.QApplication([])
application = CurrencyConv()
application.show()

sys.exit(app.exec())
