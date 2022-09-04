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
        my_label = qtw.QLabel('Type Something here:')
        
        # change font
        my_label.setFont(qtg.QFont('Halvetica',34))

        self.layout().addWidget(my_label)
        

        # Combo Box
        my_text = qtw.QTextEdit(self,
                acceptRichText = True,  # for accepting color, bold, italiac text etc 
                lineWrapMode=qtw.QTextEdit.setFixedWidth,
                lineWrapColumnOrWidth=50, # number of columns in a line
                placeholderText = 'Hello World!', # default placeholder text, it disapper when we start typing
                #plainText = 'This is real text', # this is real default text
                #html = '<h1><em><center>Thi is Heading</center></em></h1>',
                readOnly = False) # can't type into text box if it is set to False
        
        # put combo on screen
        self.layout().addWidget(my_text)

        # create a button
        my_button = qtw.QPushButton('Press Me',clicked = lambda: press_it())
        self.layout().addWidget(my_button)
        
        self.show()
        
        def press_it():
            my_label.setText(f'You Picked {my_text.toPlainText()}')
            my_text.setPlainText('You Pressed the button')            

app = qtw.QApplication([])
mw = MainWindows()
app.exec_()