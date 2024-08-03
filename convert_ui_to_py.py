from PyQt5 import uic

with open('interface.py', 'w', encoding='utf-8') as fout:
    uic.compileUi('interface.ui', fout)
