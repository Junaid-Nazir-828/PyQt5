import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg

class MainWindows(qtw.QWidget):
    def __init__(self):
        super().__init__()
        
        # add a title
        self.setWindowTitle('PYQT5 Tutorial')
        
        # set QForm layout
        form_layout = qtw.QFormLayout()
        self.setLayout(form_layout)

        # add widgets
        label_1 = qtw.QLabel('This is Cool Label Row')
        label_1.setFont(qtg.QFont('Helvetica',24))

        f_name = qtw.QLineEdit(self)
        l_name = qtw.QLineEdit(self)
        
        # add rows to App
        form_layout.addRow(label_1)
        form_layout.addRow('First Name:',f_name)
        form_layout.addRow('Last Name:',l_name)
        form_layout.addRow(qtw.QPushButton('Press Me',clicked = lambda: press_it()))

        def press_it():
            label_1.setText(f'Your Text: {f_name.text()} {l_name.text()}')
        # show the app
        self.show()
        
            
app = qtw.QApplication([])
mw = MainWindows()
app.exec_()