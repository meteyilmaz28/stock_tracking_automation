# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1637, 897)
        self.lblurunaciklamasi = QtWidgets.QLabel(Dialog)
        self.lblurunaciklamasi.setGeometry(QtCore.QRect(70, 450, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lblurunaciklamasi.setFont(font)
        self.lblurunaciklamasi.setObjectName("lblurunaciklamasi")
        self.cmburunmarkasi = QtWidgets.QComboBox(Dialog)
        self.cmburunmarkasi.setGeometry(QtCore.QRect(370, 170, 131, 31))
        self.cmburunmarkasi.setObjectName("cmburunmarkasi")
        self.cmburunkategori = QtWidgets.QComboBox(Dialog)
        self.cmburunkategori.setGeometry(QtCore.QRect(540, 170, 131, 31))
        self.cmburunkategori.setObjectName("cmburunkategori")
        self.lblurunmarkasi = QtWidgets.QLabel(Dialog)
        self.lblurunmarkasi.setGeometry(QtCore.QRect(370, 120, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lblurunmarkasi.setFont(font)
        self.lblurunmarkasi.setObjectName("lblurunmarkasi")
        self.lblurunkategori = QtWidgets.QLabel(Dialog)
        self.lblurunkategori.setGeometry(QtCore.QRect(540, 120, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lblurunkategori.setFont(font)
        self.lblurunkategori.setObjectName("lblurunkategori")
        self.lneurunaciklamasi = QtWidgets.QLineEdit(Dialog)
        self.lneurunaciklamasi.setGeometry(QtCore.QRect(70, 490, 741, 91))
        self.lneurunaciklamasi.setObjectName("lneurunaciklamasi")
        self.tblListele = QtWidgets.QTableWidget(Dialog)
        self.tblListele.setGeometry(QtCore.QRect(870, 80, 751, 631))
        self.tblListele.setRowCount(30)
        self.tblListele.setColumnCount(7)
        self.tblListele.setObjectName("tblListele")
        self.btnurunekle = QtWidgets.QPushButton(Dialog)
        self.btnurunekle.setGeometry(QtCore.QRect(70, 750, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btnurunekle.setFont(font)
        self.btnurunekle.setObjectName("btnurunekle")
        self.btnurunsilme = QtWidgets.QPushButton(Dialog)
        self.btnurunsilme.setGeometry(QtCore.QRect(240, 750, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btnurunsilme.setFont(font)
        self.btnurunsilme.setObjectName("btnurunsilme")
        self.btnurunguncelleme = QtWidgets.QPushButton(Dialog)
        self.btnurunguncelleme.setGeometry(QtCore.QRect(410, 750, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btnurunguncelleme.setFont(font)
        self.btnurunguncelleme.setObjectName("btnurunguncelleme")
        self.btnurunlistele = QtWidgets.QPushButton(Dialog)
        self.btnurunlistele.setGeometry(QtCore.QRect(610, 750, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btnurunlistele.setFont(font)
        self.btnurunlistele.setObjectName("btnurunlistele")
        self.btnurunmarkasiolustur = QtWidgets.QPushButton(Dialog)
        self.btnurunmarkasiolustur.setGeometry(QtCore.QRect(70, 600, 331, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btnurunmarkasiolustur.setFont(font)
        self.btnurunmarkasiolustur.setObjectName("btnurunmarkasiolustur")
        self.btnurun_kategori_olustur = QtWidgets.QPushButton(Dialog)
        self.btnurun_kategori_olustur.setGeometry(QtCore.QRect(460, 600, 351, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btnurun_kategori_olustur.setFont(font)
        self.btnurun_kategori_olustur.setObjectName("btnurun_kategori_olustur")
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(370, 230, 118, 161))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lblurunkodu = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lblurunkodu.setFont(font)
        self.lblurunkodu.setObjectName("lblurunkodu")
        self.verticalLayout.addWidget(self.lblurunkodu)
        self.urunkodu = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.urunkodu.setFont(font)
        self.urunkodu.setObjectName("urunkodu")
        self.verticalLayout.addWidget(self.urunkodu)
        self.birimfiyati = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.birimfiyati.setFont(font)
        self.birimfiyati.setObjectName("birimfiyati")
        self.verticalLayout.addWidget(self.birimfiyati)
        self.stokmiktari = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.stokmiktari.setFont(font)
        self.stokmiktari.setObjectName("stokmiktari")
        self.verticalLayout.addWidget(self.stokmiktari)
        self.logo = QtWidgets.QGraphicsView(Dialog)
        self.logo.setGeometry(QtCore.QRect(90, 130, 256, 271))
        self.logo.setObjectName("logo")
        self.lneurunadi = QtWidgets.QLineEdit(Dialog)
        self.lneurunadi.setGeometry(QtCore.QRect(500, 270, 221, 31))
        self.lneurunadi.setObjectName("lneurunadi")
        self.lnestokmiktari = QtWidgets.QLineEdit(Dialog)
        self.lnestokmiktari.setGeometry(QtCore.QRect(502, 351, 221, 31))
        self.lnestokmiktari.setObjectName("lnestokmiktari")
        self.lneurunkodu = QtWidgets.QLineEdit(Dialog)
        self.lneurunkodu.setGeometry(QtCore.QRect(500, 230, 221, 31))
        self.lneurunkodu.setText("")
        self.lneurunkodu.setObjectName("lneurunkodu")
        self.lnebirimfiyati = QtWidgets.QLineEdit(Dialog)
        self.lnebirimfiyati.setGeometry(QtCore.QRect(500, 310, 221, 31))
        self.lnebirimfiyati.setObjectName("lnebirimfiyati")
        self.btnurunara = QtWidgets.QPushButton(Dialog)
        self.btnurunara.setGeometry(QtCore.QRect(1510, 30, 81, 31))
        self.btnurunara.setObjectName("btnurunara")
        self.btnurunkategorisil = QtWidgets.QPushButton(Dialog)
        self.btnurunkategorisil.setGeometry(QtCore.QRect(460, 670, 351, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btnurunkategorisil.setFont(font)
        self.btnurunkategorisil.setObjectName("btnurunkategorisil")
        self.btnurunmarkasisil = QtWidgets.QPushButton(Dialog)
        self.btnurunmarkasisil.setGeometry(QtCore.QRect(70, 670, 331, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btnurunmarkasisil.setFont(font)
        self.btnurunmarkasisil.setObjectName("btnurunmarkasisil")
        self.cmbkategoriyegorelistele = QtWidgets.QComboBox(Dialog)
        self.cmbkategoriyegorelistele.setGeometry(QtCore.QRect(880, 30, 101, 31))
        self.cmbkategoriyegorelistele.setObjectName("cmbkategoriyegorelistele")
        self.btnkategoriyegorelistele = QtWidgets.QPushButton(Dialog)
        self.btnkategoriyegorelistele.setGeometry(QtCore.QRect(1000, 30, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btnkategoriyegorelistele.setFont(font)
        self.btnkategoriyegorelistele.setObjectName("btnkategoriyegorelistele")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.lblurunaciklamasi.setText(_translate("Dialog", "Ürün Açıklaması"))
        self.lblurunmarkasi.setText(_translate("Dialog", "Ürün Markası"))
        self.lblurunkategori.setText(_translate("Dialog", "Ürün kategori"))
        self.btnurunekle.setText(_translate("Dialog", "Ürün Ekle"))
        self.btnurunsilme.setText(_translate("Dialog", "Ürün Silme"))
        self.btnurunguncelleme.setText(_translate("Dialog", "Ürün Güncelleme"))
        self.btnurunlistele.setText(_translate("Dialog", "Ürün Listeleme"))
        self.btnurunmarkasiolustur.setText(_translate("Dialog", "Ürün Markası Oluştur"))
        self.btnurun_kategori_olustur.setText(_translate("Dialog", "Ürün Kategori Oluştur"))
        self.lblurunkodu.setText(_translate("Dialog", "Ürün kodu"))
        self.urunkodu.setText(_translate("Dialog", "Ürün adı"))
        self.birimfiyati.setText(_translate("Dialog", "Birim Fiyatı"))
        self.stokmiktari.setText(_translate("Dialog", "Stok Miktarı"))
        self.btnurunara.setText(_translate("Dialog", "Ürün Kodu Ara"))
        self.btnurunkategorisil.setText(_translate("Dialog", "Ürün Kategori Sil"))
        self.btnurunmarkasisil.setText(_translate("Dialog", "Ürün Markası Sil"))
        self.btnkategoriyegorelistele.setText(_translate("Dialog", "Kategoriye Göre Listele"))
