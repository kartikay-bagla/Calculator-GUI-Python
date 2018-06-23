import sys
import operator
from PyQt4 import QtCore, QtGui

class Window(QtGui.QMainWindow):
    """The main class for the GUI"""
    
    #Class variable ops which has the {symbols: functions}
    #relationship for calculations
    ops = {"+": operator.add,
           "-": operator.sub,
           "*": operator.mul,
           "/": operator.truediv,
           "%": operator.mod,
           "//": operator.floordiv,
           "**": operator.pow}
    def __init__(self):
        """Initializes and shows the GUI"""
        #set up everything
        self.set_layout() 
        #objects connected to actions
        self.calculate.clicked.connect(self.calculate_output)
        #Show the GUI after initialization
        self.show()


    def set_layout(self):
        """Creates the layout and initializes everything"""
        super(Window, self).__init__()
        self.setWindowTitle("Calculator")
        self.resize(800, 200)
        self.centralwidget = QtGui.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_inp1 = QtGui.QLabel(self.centralwidget)
        self.label_inp1.setObjectName("label_inp1")
        self.gridLayout.addWidget(self.label_inp1, 0, 0, 1, 1)
        self.label_inp2 = QtGui.QLabel(self.centralwidget)
        self.label_inp2.setObjectName("label_inp2")
        self.gridLayout.addWidget(self.label_inp2, 0, 2, 1, 1)
        self.inp1 = QtGui.QLineEdit(self.centralwidget)
        self.inp1.setObjectName("inp1")
        self.gridLayout.addWidget(self.inp1, 1, 0, 1, 1)
        self.operators = QtGui.QComboBox(self.centralwidget)
        self.operators.setObjectName("operators")
        self.gridLayout.addWidget(self.operators, 1, 1, 1, 1)
        self.label_equals = QtGui.QLabel(self.centralwidget)
        self.label_equals.setObjectName("label_equals")
        self.gridLayout.addWidget(self.label_equals, 1, 3, 1, 1)
        self.output = QtGui.QLineEdit(self.centralwidget)
        self.output.setObjectName("output")
        self.gridLayout.addWidget(self.output, 1, 4, 1, 1)
        self.label_output = QtGui.QLabel(self.centralwidget)
        self.label_output.setObjectName("label_output")
        self.gridLayout.addWidget(self.label_output, 0, 4, 1, 1)
        self.inp2 = QtGui.QLineEdit(self.centralwidget)
        self.inp2.setObjectName("inp2")
        self.gridLayout.addWidget(self.inp2, 1, 2, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.calculate = QtGui.QPushButton(self.centralwidget)
        self.calculate.setObjectName("calculate")
        self.gridLayout_2.addWidget(self.calculate, 1, 0, 1, 1)
        self.output.raise_()
        self.label_inp1.raise_()
        self.label_inp2.raise_()
        self.label_output.raise_()
        self.label_equals.raise_()
        self.inp1.raise_()
        self.operators.raise_()
        self.inp2.raise_()
        self.calculate.raise_()
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 803, 26))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.setWindowTitle("Calculator")
        self.label_inp1.setText("Input 1")
        self.label_inp2.setText("Input 2")
        self.operators.addItems(list(Window.ops.keys()))
        self.label_equals.setText("=")
        self.output.setReadOnly(True)
        self.label_output.setText("Output")
        self.calculate.setText("Calculate")
    
    def calculate_output(self):
        """Gets the value in the input fields, calculates and 
        prints the output in the output text field"""

        #Getting the text from the input fields
        val1 = self.inp1.text() 
        val2 = self.inp2.text()
        self.output.setText("")

        #Checking if numbers
        try:
            val1 = float(val1)
            val2 = float(val2)

        #A pop up if not number
        except:
            QtGui.QMessageBox.information(self, "Invalid Input", "The entered input is not a number!")
            return

        #Getting the operator
        op = self.operators.currentText()
        #Getting the corresponding function
        op_func = Window.ops[op]
        #Calculating the Result
        result = op_func(val1, val2)
        #Printing the result
        self.output.setText(str(result))
        return

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv) #Initializing the App
    MainWindow = Window() #Creating instance of Window
    sys.exit(app.exec_()) #Exit procedure