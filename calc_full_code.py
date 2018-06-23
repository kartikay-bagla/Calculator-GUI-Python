import sys, operator
from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

class Stack:
    """A simple stack class"""
    def __init__(self, l = []):
        """Initialize the stack, either with list l or empty list"""
        self.l = l
    def push(self, item):
        """push an item into the stack"""
        self.l.append(item)
    def pull(self):
        """pull or pop the topmost item from the stack"""
        try:
            return self.l.pop(-1)
        except:
            return None
    def peek(self):
        """returns thr topmost element of the stack without removing it"""
        try: return self.l[-1]
        except: return None

def preprocess(s):
    """adds spaces between numbers. 
    Input = "2*50/(300-100)"
    Output = "2 * 50 / ( 300 - 100 )" """
    infix_string = ""
    digits = " "
    i = 0
    inc = False
    while i < len(s):
        try:
            while s[i] in "1234567890.":
                digits += s[i]
                i += 1
                inc = True
        except:
            pass
        if digits != " ":
            digits += " "
            infix_string += digits
            digits = " "
        else:
            if s[i] == "*" and s[i+1] == "*":
                i += 1
                infix_string += "** "
            else:
                infix_string += s[i]
                infix_string += " "
        if not inc:
            i += 1
        else:
            inc = False
    return infix_string.split()

def infix_postfix(s):
    """Takes an equation formatted by preprocess func and converts it into postfix"""
    prec = {"**": 5, "%": 4, "*": 3, "/": 3,
            "+": 2, "-": 2, "(": 1}
    ops = Stack()
    post_fix = []
    for item in s:
        try:
             post_fix.append(float(item))
        except:
            if item == "(":
                ops.push(item)
            elif item == ")":
                top_op = ops.pull()
                while top_op != "(":
                    post_fix.append(top_op)
                    top_op = ops.pull()
            else:
                while len(ops.l) != 0 and (prec[ops.peek()] >= prec[item]):
                    post_fix.append(ops.pull())
                ops.push(item)
    while len(ops.l) != 0:
        post_fix.append(ops.pull())
    return post_fix

def calc(s):
    """takes a postfix equation in list form and return the sum in a single element list"""
    ops = {"+": operator.add,
           "-": operator.sub,
           "*": operator.mul,
           "/": operator.truediv,
           "%": operator.mod,
           "//": operator.floordiv,
           "**": operator.pow}
    i = 0
    while i < len(s):
        inc = True
        if type(s[i]) != float:
            ind = i - 2
            a = s.pop(ind)
            b = s.pop(ind)
            s.insert(ind, ops[s.pop(ind)](a, b))
            i = 0
            inc = False
        if inc:
            i+=1
    return s



class Window(QtGui.QMainWindow):
    def set_layout(self):
        """Creates the layout and initializes all the objects"""
        super(Window, self).__init__()
        self.setObjectName("MainWindow")
        self.resize(600, 400)
        self.centralwidget = QtGui.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.calc_win = QtGui.QLineEdit(self.centralwidget)
        self.calc_win.setMinimumSize(QtCore.QSize(500, 100))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.calc_win.setFont(font)
        self.calc_win.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.calc_win.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.calc_win.setReadOnly(True)
        self.calc_win.setObjectName("calc_win")
        self.verticalLayout.addWidget(self.calc_win)
        self.num_layout = QtGui.QGridLayout()
        self.num_layout.setSpacing(20)
        self.num_layout.setObjectName("num_layout")
        self.btn_7 = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_7.sizePolicy().hasHeightForWidth())
        self.btn_7.setSizePolicy(sizePolicy)
        self.btn_7.setObjectName(_fromUtf8("btn_7"))
        self.num_layout.addWidget(self.btn_7, 0, 0, 1, 1)
        self.btn_8 = QtGui.QPushButton(self.centralwidget)
        self.btn_8.setObjectName(_fromUtf8("btn_8"))
        self.num_layout.addWidget(self.btn_8, 0, 1, 1, 1)
        self.btn_9 = QtGui.QPushButton(self.centralwidget)
        self.btn_9.setObjectName(_fromUtf8("btn_9"))
        self.num_layout.addWidget(self.btn_9, 0, 2, 1, 1)
        self.btn_lp = QtGui.QPushButton(self.centralwidget)
        self.btn_lp.setObjectName(_fromUtf8("btn_lp"))
        self.num_layout.addWidget(self.btn_lp, 4, 0, 1, 1)
        self.btn_6 = QtGui.QPushButton(self.centralwidget)
        self.btn_6.setObjectName(_fromUtf8("btn_6"))
        self.num_layout.addWidget(self.btn_6, 1, 2, 1, 1)
        self.btn_0 = QtGui.QPushButton(self.centralwidget)
        self.btn_0.setObjectName(_fromUtf8("btn_0"))
        self.num_layout.addWidget(self.btn_0, 3, 1, 1, 1)
        self.btn_bksp = QtGui.QPushButton(self.centralwidget)
        self.btn_bksp.setObjectName(_fromUtf8("btn_bksp"))
        self.num_layout.addWidget(self.btn_bksp, 3, 0, 1, 1)
        self.btn_4 = QtGui.QPushButton(self.centralwidget)
        self.btn_4.setObjectName(_fromUtf8("btn_4"))
        self.num_layout.addWidget(self.btn_4, 1, 0, 1, 1)
        self.btn_5 = QtGui.QPushButton(self.centralwidget)
        self.btn_5.setObjectName(_fromUtf8("btn_5"))
        self.num_layout.addWidget(self.btn_5, 1, 1, 1, 1)
        self.btn_1 = QtGui.QPushButton(self.centralwidget)
        self.btn_1.setObjectName(_fromUtf8("btn_1"))
        self.num_layout.addWidget(self.btn_1, 2, 0, 1, 1)
        self.btn_2 = QtGui.QPushButton(self.centralwidget)
        self.btn_2.setObjectName(_fromUtf8("btn_2"))
        self.num_layout.addWidget(self.btn_2, 2, 1, 1, 1)
        self.btn_sub = QtGui.QPushButton(self.centralwidget)
        self.btn_sub.setObjectName(_fromUtf8("btn_sub"))
        self.num_layout.addWidget(self.btn_sub, 1, 3, 1, 1)
        self.btn_3 = QtGui.QPushButton(self.centralwidget)
        self.btn_3.setObjectName(_fromUtf8("btn_3"))
        self.num_layout.addWidget(self.btn_3, 2, 2, 1, 1)
        self.btn_dot = QtGui.QPushButton(self.centralwidget)
        self.btn_dot.setObjectName(_fromUtf8("btn_dot"))
        self.num_layout.addWidget(self.btn_dot, 3, 2, 1, 1)
        self.btn_div = QtGui.QPushButton(self.centralwidget)
        self.btn_div.setObjectName(_fromUtf8("btn_div"))
        self.num_layout.addWidget(self.btn_div, 3, 3, 1, 1)
        self.btn_add = QtGui.QPushButton(self.centralwidget)
        self.btn_add.setObjectName(_fromUtf8("btn_add"))
        self.num_layout.addWidget(self.btn_add, 0, 3, 1, 1)
        self.btn_mul = QtGui.QPushButton(self.centralwidget)
        self.btn_mul.setObjectName(_fromUtf8("btn_mul"))
        self.num_layout.addWidget(self.btn_mul, 2, 3, 1, 1)
        self.btn_mod = QtGui.QPushButton(self.centralwidget)
        self.btn_mod.setObjectName(_fromUtf8("btn_mod"))
        self.num_layout.addWidget(self.btn_mod, 4, 3, 1, 1)
        self.btn_eq = QtGui.QPushButton(self.centralwidget)
        self.btn_eq.setObjectName(_fromUtf8("btn_eq"))
        self.num_layout.addWidget(self.btn_eq, 4, 2, 1, 1)
        self.btn_rp = QtGui.QPushButton(self.centralwidget)
        self.btn_rp.setObjectName(_fromUtf8("btn_rp"))
        self.num_layout.addWidget(self.btn_rp, 4, 1, 1, 1)
        self.verticalLayout.addLayout(self.num_layout)
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 522, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(self)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        self.setStatusBar(self.statusbar)
        self.actionReset = QtGui.QAction(self)
        self.actionReset.setObjectName(_fromUtf8("actionReset"))
        self.actionQuit = QtGui.QAction(self)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.menuFile.addAction(self.actionReset)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menubar.addAction(self.menuFile.menuAction())

        #retranslateUI
        self.setWindowTitle("Calculator")
        self.calc_win.setText("0")
        self.btn_7.setText("7")
        self.btn_8.setText("8")
        self.btn_9.setText("9")
        self.btn_lp.setText("(")
        self.btn_6.setText("6")
        self.btn_0.setText("0")
        self.btn_bksp.setText("Backspace")
        self.btn_4.setText("4")
        self.btn_5.setText("5")
        self.btn_1.setText("1")
        self.btn_2.setText("2")
        self.btn_sub.setText("-")
        self.btn_3.setText("3")
        self.btn_dot.setText(".")
        self.btn_div.setText("/")
        self.btn_add.setText("+")
        self.btn_mul.setText("*")
        self.btn_mod.setText("%")
        self.btn_eq.setText("=")
        self.btn_rp.setText(")")
        self.menuFile.setTitle("File")
        self.actionReset.setText("Reset")
        self.actionQuit.setText("Quit")

    def __init__(self):
        """The initialization method, which intializes the actions of each button and shows the GUI"""
        self.screen_text = "" #Holds the current screen output
        self.set_layout()
        
        #Buttons to actions
        self.btn_0.clicked.connect(self.btn0_press)
        self.btn_1.clicked.connect(self.btn1_press)
        self.btn_2.clicked.connect(self.btn2_press)
        self.btn_3.clicked.connect(self.btn3_press)
        self.btn_4.clicked.connect(self.btn4_press)
        self.btn_5.clicked.connect(self.btn5_press)
        self.btn_6.clicked.connect(self.btn6_press)
        self.btn_7.clicked.connect(self.btn7_press)
        self.btn_8.clicked.connect(self.btn8_press)
        self.btn_9.clicked.connect(self.btn9_press)
        self.btn_lp.clicked.connect(self.btnlp_press)
        self.btn_rp.clicked.connect(self.btnrp_press)
        self.btn_bksp.clicked.connect(self.btnbksp_press)
        self.btn_add.clicked.connect(self.btnadd_press)
        self.btn_sub.clicked.connect(self.btnsub_press)
        self.btn_mul.clicked.connect(self.btnmul_press)
        self.btn_div.clicked.connect(self.btndiv_press)
        self.btn_mod.clicked.connect(self.btnmod_press)
        self.btn_dot.clicked.connect(self.btndot_press)
        self.btn_eq.clicked.connect(self.btneq_press)
        
        #Menu buttons to actions
        self.actionQuit.triggered.connect(self.quit_check)
        self.actionReset.triggered.connect(self.reset_app)
        self.show()

    def reset_app(self):
        """Resets the app"""
        self.screen_text = "0"
        self.calc_win.setText(self.screen_text)

    def quit_check(self):
        """Confirmation for quitting the app"""
        choice = QtGui.QMessageBox.question(self, "Quit?", "Are you sure you want to quit?", 
                                            QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if choice == QtGui.QMessageBox.Yes:
            sys.exit()
        else:
            pass
        
    def present_answer(self):
        """Takes the screen as input and returns the output"""
        try:
            s = self.screen_text
            s = str(calc(infix_postfix(preprocess(s)))[0]) #First spaces the input, converts to postfix and then solves
            self.calc_win.setText(s)
            self.screen_text = s
        except:
            QtGui.QMessageBox.information(self, "Invalid Input", "Invalid Input")
            return

    #Actions for button presses
    def btn0_press(self):
        self.screen_text += "0"
        self.calc_win.setText(self.screen_text)
    def btn1_press(self):
        self.screen_text += "1"
        self.calc_win.setText(self.screen_text)
    def btn2_press(self):
        self.screen_text += "2"
        self.calc_win.setText(self.screen_text)
    def btn3_press(self):
        self.screen_text += "3"
        self.calc_win.setText(self.screen_text)
    def btn4_press(self):
        self.screen_text += "4"
        self.calc_win.setText(self.screen_text)
    def btn5_press(self):
        self.screen_text += "5"
        self.calc_win.setText(self.screen_text)
    def btn6_press(self):
        self.screen_text += "6"
        self.calc_win.setText(self.screen_text)
    def btn7_press(self):
        self.screen_text += "7"
        self.calc_win.setText(self.screen_text)
    def btn8_press(self):
        self.screen_text += "8"
        self.calc_win.setText(self.screen_text)
    def btn9_press(self):
        self.screen_text += "9"
        self.calc_win.setText(self.screen_text)
    def btnlp_press(self):
        self.screen_text += "("
        self.calc_win.setText(self.screen_text)
    def btnrp_press(self):
        self.screen_text += ")"
        self.calc_win.setText(self.screen_text)
    def btnbksp_press(self):
        self.screen_text = self.screen_text[:-1]
        self.calc_win.setText(self.screen_text)
    def btnadd_press(self):
        self.screen_text += "+"
        self.calc_win.setText(self.screen_text)
    def btnsub_press(self):
        self.screen_text += "-"
        self.calc_win.setText(self.screen_text)
    def btnmul_press(self):
        self.screen_text += "*"
        self.calc_win.setText(self.screen_text)
    def btndiv_press(self):
        self.screen_text += "/"
        self.calc_win.setText(self.screen_text)
    def btnmod_press(self):
        self.screen_text += "%"
        self.calc_win.setText(self.screen_text)
    def btneq_press(self):
        self.present_answer()
    def btndot_press(self):
        if not self.screen_text[-1].isnumeric():
            self.screen_text += "0."
        else:
            self.screen_text += "."
        self.calc_win.setText(self.screen_text)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    MainWindow = Window()
    sys.exit(app.exec_())