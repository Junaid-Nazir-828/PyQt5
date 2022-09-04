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
        my_label = qtw.QLabel('Hello World!')
        
        # change font
        my_label.setFont(qtg.QFont('Halvetica',34))

        self.layout().addWidget(my_label)
        

        # Combo Box
        my_combo = qtw.QComboBox(self) # can also work without passing self        
        # adding items
        my_combo.addItem('apples','something')
        my_combo.addItem('banana',2)
        my_combo.addItem('mango')
        my_combo.addItems(['one','two','three'])
        my_combo.insertItem(2,'an item')
        # put combo on screen
        self.layout().addWidget(my_combo)


        # create a button
        my_button = qtw.QPushButton('Press Me',clicked = lambda: press_it())
        self.layout().addWidget(my_button)
        
        self.show()
        
        def press_it():
            my_label.setText(f'You Picked {my_combo.currentText()}')
            #my_label.setText(f'You Picked {my_combo.currentData()}')
            #my_label.setText(f'You Picked {my_combo.currentIndex()}')

app = qtw.QApplication([])
mw = MainWindows()
app.exec_()