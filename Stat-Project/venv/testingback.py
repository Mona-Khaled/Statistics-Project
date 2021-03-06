import sys
from PySide.QtCore import *
from PySide.QtGui import *

class Form(QMainWindow):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.setWindowFlags(Qt::Window | Qt::CustomizeWindowHint | Qt::WindowStaysOnTopHint)


if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)
    # Create and show the form
    form = Form()
    form.show()
    # Run the main Qt loop
    sys.exit(app.exec_())
