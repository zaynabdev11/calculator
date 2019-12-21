from PyQt5.uic.properties import QtGui , QtCore





def on_key(key):
    # test for a specific key
    if key == QtCore.Qt.Key_Return:
        print('return key pressed')
    else:
        print('key pressed: %i' % key)