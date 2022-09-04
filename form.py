import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg

class MainWindows(qtw.QWidget):
    def __init__(self):
        super().__init__()
        
        # add a title
        self.setWindowTitle('PYQT5 Tutorial')
        
        
            
app = qtw.QApplication([])
mw = MainWindows()
app.exec_()