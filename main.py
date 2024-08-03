import sys
import json
import warnings
import pandas as pd
from PyQt5.QtWidgets import QApplication, QDialog, QTableWidgetItem, QMessageBox, QInputDialog, QAbstractItemView
from PyQt5.QtGui import QColor
from interface import Ui_Dialog

warnings.filterwarnings("ignore", category=DeprecationWarning)

class InventoryApp(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.products = []  # Ürünleri saklamak için bir liste
        self.colors = {}  # Markalara ve kategorilere göre renkleri saklamak için bir sözlük
        self.brands = []  # Markalar listesi
        self.categories = []  # Kategoriler listesi
        
        self.setup_connections()
        self.setup_table()
        self.load_from_excel()  # Excel dosyasından ürünleri yükle
        self.load_brands_and_categories()  # Markalar ve kategorileri yükle

    def setup_connections(self):
        self.ui.btnurunekle.clicked.connect(self.add_product)
        self.ui.btnurunsilme.clicked.connect(self.delete_product)
        self.ui.btnurunguncelleme.clicked.connect(self.update_product)
        self.ui.btnurunlistele.clicked.connect(self.list_products)
        self.ui.btnurunmarkasiolustur.clicked.connect(self.create_brand)
        self.ui.btnurun_kategori_olustur.clicked.connect(self.create_category)
        self.ui.btnkategoriyegorelistele.clicked.connect(self.list_by_category)
        self.ui.btnurunara.clicked.connect(self.search_product)
        self.ui.btnurunmarkasisil.clicked.connect(self.delete_brand)
        self.ui.btnurunkategorisil.clicked.connect(self.delete_category)

    def setup_table(self):
        self.ui.tblListele.setColumnCount(7)
        self.ui.tblListele.setHorizontalHeaderLabels(["Ürün Kodu", "Marka", "Kategori", "Ürün Adı", "Stok Miktarı", "Birim Fiyatı", "Ürün Açıklaması"])
        self.ui.tblListele.setEditTriggers(QAbstractItemView.NoEditTriggers)  # Hücrelerin düzenlenmesini engeller

    def add_product(self):
        barkod = self.ui.lneurunkodu.text()
        marka = self.ui.cmburunmarkasi.currentText()
        kategori = self.ui.cmburunkategori.currentText()
        urun_adi = self.ui.lneurunadi.text()
        stok_miktari = self.ui.lnestokmiktari.text()
        birim_fiyati = self.ui.lnebirimfiyati.text()
        urun_aciklamasi = self.ui.lneurunaciklamasi.text()

        if not barkod or not urun_adi:
            QMessageBox.warning(self, "Uyarı", "Ürün Kodu ve Ürün Adı alanları boş olamaz!")
            return

        if any(product[0] == barkod for product in self.products):
            QMessageBox.warning(self, "Uyarı", "Bu ürün kodu zaten mevcut!")
            return

        product = [barkod, marka, kategori, urun_adi, stok_miktari, birim_fiyati, urun_aciklamasi]
        self.products.append(product)
        
        self.clear_fields()
        self.list_products()
        self.save_to_excel()

    def delete_product(self):
        current_row = self.ui.tblListele.currentRow()
        if current_row >= 0:
            del self.products[current_row]
            self.list_products()
            self.save_to_excel()
        else:
            QMessageBox.warning(self, "Uyarı", "Silmek için bir ürün seçin!")
            
    def update_product(self):
        current_row = self.ui.tblListele.currentRow()
        if current_row >= 0:
            barkod = self.ui.lneurunkodu.text()
            marka = self.ui.cmburunmarkasi.currentText()
            kategori = self.ui.cmburunkategori.currentText()
            urun_adi = self.ui.lneurunadi.text()
            stok_miktari = self.ui.lnestokmiktari.text()
            birim_fiyati = self.ui.lnebirimfiyati.text()
            urun_aciklamasi = self.ui.lneurunaciklamasi.text()
            
            if any(product[0] == barkod and idx != current_row for idx, product in enumerate(self.products)):
                QMessageBox.warning(self, "Uyarı", "Bu ürün kodu zaten mevcut!")
                return

            self.products[current_row] = [barkod, marka, kategori, urun_adi, stok_miktari, birim_fiyati, urun_aciklamasi]
            
            self.list_products()
            self.save_to_excel()
        else:
            QMessageBox.warning(self, "Uyarı", "Güncellemek için bir ürün seçin!")
            
    def list_products(self):
        self.ui.tblListele.setRowCount(0)
        for product in self.products:
            row_position = self.ui.tblListele.rowCount()
            self.ui.tblListele.insertRow(row_position)
            for column, item in enumerate(product):
                item_str = str(item)  # Ürün bilgilerini olduğu gibi ekleyin
                self.ui.tblListele.setItem(row_position, column, QTableWidgetItem(item_str))
                
            marka = product[1].upper()  # Marka adını büyük harfe çevir
            kategori = product[2].upper()  # Kategori adını büyük harfe çevir
            key = (marka, kategori)
            
            if key not in self.colors:
                self.colors[key] = self.generate_color()
            
            color = self.colors[key]
            
            self.ui.tblListele.item(row_position, 1).setBackground(color)
            self.ui.tblListele.item(row_position, 2).setBackground(color)

            stok_miktari = product[4]
            if stok_miktari.isdigit() and int(stok_miktari) < 10000:
                self.highlight_low_stock(row_position)  # Stok miktarı düşükse satırı kırmızı yap

    def list_by_category(self):
        selected_category = self.ui.cmbkategoriyegorelistele.currentText().upper()  # Seçilen kategoriyi büyük harfe çevir
        self.ui.tblListele.setRowCount(0)  # Tabloyu temizle

        for product in self.products:
            product_category = product[2].upper()  # Ürün kategorisini büyük harfe çevir

            if selected_category == "TÜMÜ" or product_category == selected_category:
                row_position = self.ui.tblListele.rowCount()
                self.ui.tblListele.insertRow(row_position)
                for column, item in enumerate(product):
                    item_str = str(item)  # item'ı str türüne dönüştür
                    self.ui.tblListele.setItem(row_position, column, QTableWidgetItem(item_str))

                marka = product[1].upper()
                kategori = product[2].upper()
                key = (marka, kategori)

                if key not in self.colors:
                    self.colors[key] = self.generate_color()

                color = self.colors[key]

                self.ui.tblListele.item(row_position, 1).setBackground(color)
                self.ui.tblListele.item(row_position, 2).setBackground(color)

                stok_miktari = product[4]
                if stok_miktari.isdigit() and int(stok_miktari) < 10000:
                    self.highlight_low_stock(row_position)

        if self.ui.tblListele.rowCount() == 0:
            QMessageBox.information(self, "Bilgi", f"Seçilen kategori '{selected_category}' için ürün bulunamadı!")

        
    def create_brand(self):
        text, ok = QInputDialog.getText(self, "Yeni Marka", "Yeni marka adı girin:")
        if ok and text:
            text = text.upper()
            self.ui.cmburunmarkasi.addItem(text)
            self.brands.append(text)
            self.save_brands_and_categories()  # Markaları ve kategorileri kaydet

    def create_category(self):
        text, ok = QInputDialog.getText(self, "Yeni Kategori", "Yeni kategori adı girin:")
        if ok and text:
            # Yeni kategoriyi sadece cmburunkategori'ye ekle
            text = text.upper()
            self.ui.cmburunkategori.addItem(text)
            self.categories.append(text)
            self.save_brands_and_categories()  # Markaları ve kategorileri kaydet
    
    def delete_brand(self):
        brand, ok = QInputDialog.getItem(self, "Marka Sil", "Silinecek markayı seçin:", self.get_brand_list(), 0, False)
        if ok and brand:
            self.ui.cmburunmarkasi.removeItem(self.ui.cmburunmarkasi.findText(brand))
            self.brands.remove(brand)
            self.products = [product for product in self.products if product[1] != brand]
            self.list_products()
            self.save_to_excel()
            self.save_brands_and_categories()  # Markaları ve kategorileri kaydet
        
    def delete_category(self):
        category, ok = QInputDialog.getItem(self, "Kategori Sil", "Silinecek kategoriyi seçin:", self.get_category_list(), 0, False)
        if ok and category:
            self.ui.cmburunkategori.removeItem(self.ui.cmburunkategori.findText(category))
            self.ui.cmbkategoriListele.removeItem(self.ui.cmbkategoriListele.findText(category))
            self.categories.remove(category)
            self.products = [product for product in self.products if product[2] != category]
            self.list_products()
            self.save_to_excel()
            self.save_brands_and_categories()  # Markaları ve kategorileri kaydet
            
    def clear_fields(self):
        self.ui.lneurunkodu.clear()
        self.ui.cmburunmarkasi.setCurrentIndex(0)
        self.ui.cmburunkategori.setCurrentIndex(0)
        self.ui.lneurunadi.clear()
        self.ui.lnestokmiktari.clear()
        self.ui.lnebirimfiyati.clear()
        self.ui.lneurunaciklamasi.clear()
        
    def generate_color(self):
        import random
        base_color = QColor(random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))
        return base_color

    def highlight_low_stock(self, row_position):
        for column in range(self.ui.tblListele.columnCount()):
            self.ui.tblListele.item(row_position, column).setBackground(QColor("lightcoral"))

    def save_to_excel(self):
        df = pd.DataFrame(self.products, columns=["Ürün Kodu", "Marka", "Kategori", "Ürün Adı", "Stok Miktarı", "Birim Fiyatı", "Ürün Açıklaması"])
        df.to_excel("inventory.xlsx", index=False)

    def load_from_excel(self):
        try:
            df = pd.read_excel("inventory.xlsx")
            self.products = df.values.tolist()
            self.list_products()
        except FileNotFoundError:
            pass
    
    def save_brands_and_categories(self):
        data = {
            "brands": self.brands,
            "categories": self.categories
        }
        with open("brands_and_categories.json", "w") as f:
            json.dump(data, f)
    
    def load_brands_and_categories(self):
        try:
            with open("brands_and_categories.json", "r") as f:
                data = json.load(f)
                self.brands = [brand.upper() for brand in data.get("brands", [])]  # Büyük harfe çevir
                self.categories = [category.upper() for category in data.get("categories", [])]  # Büyük harfe çevir
                self.ui.cmburunmarkasi.addItems(self.brands)
                self.ui.cmburunkategori.addItems(self.categories)
                self.ui.cmbkategoriyegorelistele.addItems(self.categories)
        except FileNotFoundError:
            pass
    
    def get_brand_list(self):
        return self.brands
    
    def get_category_list(self):
        return self.categories

    def search_product(self):
        search_code, ok_code = QInputDialog.getText(self, "Ürün Kodu ile Ara", "Ürün kodunu girin (boş bırakabilirsiniz):")
        search_brand, ok_brand = QInputDialog.getText(self, "Marka ile Ara", "Marka girin (boş bırakabilirsiniz):")
        search_category, ok_category = QInputDialog.getText(self, "Kategori ile Ara", "Kategori girin (boş bırakabilirsiniz):")
        search_stock, ok_stock = QInputDialog.getText(self, "Stok Miktarı ile Ara", "Stok miktarı girin (boş bırakabilirsiniz):")

        if ok_code is None or ok_brand is None or ok_category is None or ok_stock is None:
            return

    # Arama kriterlerini küçük harfe çevirin
        search_code = search_code.lower()
        search_brand = search_brand.lower()
        search_category = search_category.lower()
        search_stock = search_stock.lower()

        self.ui.tblListele.setRowCount(0)
        for product in self.products:
            row_position = self.ui.tblListele.rowCount()
            self.ui.tblListele.insertRow(row_position)
            for column, item in enumerate(product):
                if column == 1:  # Marka sütunu
                    item_str = str(item).upper()  # Marka adını büyük harf yap
                elif column == 2:  # Kategori sütunu
                    item_str = str(item).upper()  # Kategori adını büyük harf yap
                else:
                    item_str = str(item)
                self.ui.tblListele.setItem(row_position, column, QTableWidgetItem(item_str))
                
            marka = product[1].upper()  # Marka adını büyük harfe çevir
            kategori = product[2].upper()  # Kategori adını büyük harfe çevir
            key = (marka, kategori)
            
            if key not in self.colors:
                self.colors[key] = self.generate_color()
            
            color = self.colors[key]
            
            self.ui.tblListele.item(row_position, 1).setBackground(color)
            self.ui.tblListele.item(row_position, 2).setBackground(color)

            stok_miktari = product[4]
            if stok_miktari.isdigit() and int(stok_miktari) < 10000:
                self.highlight_low_stock(row_position)  # Stok miktarı düşükse satırı kırmızı yap


            if self.ui.tblListele.rowCount() == 0:
                QMessageBox.information(self, "Bilgi", "Kriterlere uyan ürün bulunamadı!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = InventoryApp()
    window.show()
    sys.exit(app.exec_())
