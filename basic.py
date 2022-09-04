import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg

class MainWindows(qtw.QWidget):
    def __init__(self):
        super().__init__()
        # add a title
        self.setWindowTitle('PYQT5 Tutorial')
        
        # set vertical layout
        self.setLayout(qtw.QVBoxLayout())
        #self.setLayout(qtw.QHBoxLayout())

        # create a label
        my_label = qtw.QLabel('Whats your name')
        
        # change font
        my_label.setFont(qtg.QFont('Halvetica',34))

        self.layout().addWidget(my_label)
        

        # Entry Box
        my_entry = qtw.QLineEdit()
        my_entry.setObjectName('name_field')
        my_entry.setText('')
        self.layout().addWidget(my_entry)
        

        # create a button
        my_button = qtw.QPushButton('Press Me', clicked = lambda: press_it())
        self.layout().addWidget(my_button)
        
        self.show()

        def press_it():
            my_label.setText(f'Hello {my_entry.text()}')
            my_entry.setText('')
            
app = qtw.QApplication([])
mw = MainWindows()
app.exec_()