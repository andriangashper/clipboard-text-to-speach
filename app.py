import time
import threading
import pyttsx3
import pyperclip
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtCore import pyqtSlot

class TextToSpeechApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.init_ui()
        self.monitoring_thread = None
        self.monitoring = False
        self.closeEvent = self.closeEvent


    def init_ui(self):
        self.setGeometry(100, 100, 400, 200)
        self.setWindowTitle("Text to Speech App")

        self.monitor_clipboard_btn = QPushButton("Monitor Clipboard", self)
        self.monitor_clipboard_btn.setGeometry(50, 50, 150, 50)  

        self.stop_monitoring_btn = QPushButton("Stop Monitoring", self)
        self.stop_monitoring_btn.setGeometry(200, 50, 150, 50)  

        self.monitor_clipboard_btn.clicked.connect(self.start_monitoring)
        self.stop_monitoring_btn.clicked.connect(self.stop_monitoring)


    def start_monitoring(self):
        if not self.monitoring:
            self.monitoring = True
            self.monitoring_thread = threading.Thread(target=self.monitor_clipboard)
            self.monitoring_thread.start()


    def stop_monitoring(self):
        if self.monitoring:
            self.monitoring = False
            self.monitoring_thread.join()


    def monitor_clipboard(self):
        self.previous_clipboard_text = ""
        while self.monitoring:
            current_clipboard_text = pyperclip.paste()

            if current_clipboard_text != self.previous_clipboard_text:
                self.text_to_speech(current_clipboard_text)
                self.previous_clipboard_text = current_clipboard_text

            time.sleep(1)  # Check the clipboard every second


    def text_to_speech(self, text):
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()


    @pyqtSlot()
    def closeEvent(self, event):
        if self.monitoring_thread and self.monitoring_thread.is_alive():
            self.stop_monitoring()
        event.accept()



if __name__ == '__main__':
    app = QApplication([])
    window = TextToSpeechApp()
    window.show()
    app.exec_()