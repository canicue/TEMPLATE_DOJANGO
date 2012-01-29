#!/usr/bin/env python
import sys
from kdeui import KMainWindow, KApplication

class KMainWindow(KMainWindow):

  def __init__(self):
    KTMainWindow.__init__(self)

app = KApplication(sys.argv, "KDraw - Python")
window = KMainWindow()
window.show()
app.exec_loop()
