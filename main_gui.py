from PyQt6.QtWidgets import QApplication, QMainWindow, QTextBrowser, QVBoxLayout, QPushButton, QWidget, QLineEdit, QLabel, QGraphicsView, QGraphicsScene, QGraphicsEllipseItem
from PyQt6.QtGui import QPalette, QColor, QFont, QBrush
from PyQt6.QtCore import Qt, QTimer, QPropertyAnimation, pyqtSlot
import sys
import speech_recognition as sr
import model  # Your query classification script
import Brain  # Your chatbot script
import Realtime_Info  # Your real-time info script
import text_to_speech  # Your TTS script


class SciFiChatbot(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("AI Assistant - Sci-Fi Edition")
        self.setGeometry(200, 200, 800, 500)

        # Set dark sci-fi theme
        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor("#000A24"))
        palette.setColor(QPalette.ColorRole.WindowText, QColor("#00CCFF"))
        self.setPalette(palette)

        # Layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        layout = QVBoxLayout()

        self.chat_display = QTextBrowser()
        self.chat_display.setFont(QFont("Courier", 12))
        self.chat_display.setStyleSheet("background-color: #001F3F; color: #00CCFF; border-radius: 10px; padding: 5px;")
        layout.addWidget(self.chat_display)

        self.input_box = QLineEdit()
        self.input_box.setFont(QFont("Courier", 12))
        self.input_box.setStyleSheet("background-color: #002B5C; color: #00CCFF; border-radius: 10px; padding: 5px;")
        self.input_box.returnPressed.connect(lambda: self.process_input())
        layout.addWidget(self.input_box)

        # AI Assistant Circle Animation
        self.circle_view = QGraphicsView(self)
        self.scene = QGraphicsScene(self)
        self.circle_view.setScene(self.scene)
        self.circle_view.setFixedSize(150, 150)  # Adjusted size

        self.circle = QGraphicsEllipseItem(0, 0, 100, 100)
        self.circle.setBrush(QBrush(QColor(0, 204, 255, 150)))  # Blue Glow
        self.circle.setPen(QColor(0, 204, 255))  # Outline
        self.scene.addItem(self.circle)

        layout.addWidget(self.circle_view)

        self.voice_button = QPushButton("🎤 Speak")
        self.voice_button.setFont(QFont("Courier", 12))
        self.voice_button.setStyleSheet("background-color: #333333; color: #00FF41;")
        self.voice_button.clicked.connect(self.start_voice_input)
        layout.addWidget(self.voice_button)

        self.central_widget.setLayout(layout)

        # Animation Setup
        self.timer = QTimer()
        self.timer.timeout.connect(self.rotate_circle)
        self.timer.start(50)  # Adjust speed of rotation

    def rotate_circle(self):
        """Rotates the circle continuously when idle."""
        self.circle.setRotation(self.circle.rotation() + 2)

    def expand_circle(self):
        """Expands the circle when bot speaks."""
        animation = QPropertyAnimation(self.circle_view, b"geometry")
        animation.setDuration(500)
        animation.setStartValue(self.circle_view.geometry())
        animation.setEndValue(self.circle_view.geometry().adjusted(-10, -10, 10, 10))
        animation.start()

    def shrink_circle(self):
        """Shrinks back to normal size after speaking."""
        animation = QPropertyAnimation(self.circle_view, b"geometry")
        animation.setDuration(500)
        animation.setStartValue(self.circle_view.geometry().adjusted(-10, -10, 10, 10))
        animation.setEndValue(self.circle_view.geometry())
        animation.start()

    def start_voice_input(self):
        self.expand_circle()  # Expand circle when speaking
        self.timer.stop()  # Stop rotation
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            self.chat_display.append("<b>Bot:</b> Listening...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)
            try:
                text = recognizer.recognize_google(audio)
                self.process_input(text)
            except sr.UnknownValueError:
                self.chat_display.append("<b>Bot:</b> Sorry, could not understand.")
            except sr.RequestError:
                self.chat_display.append("<b>Bot:</b> Connection error.")

        self.shrink_circle()  # Shrink back after response
        self.timer.start(50)  # Resume rotation

    @pyqtSlot(str)
    def process_input(self, user_input=None):
        if not user_input:  # Handles both voice and text input
            user_input = self.input_box.text().strip()
        
        if user_input == "":
            return  # Ignore empty input

        self.chat_display.append(f"<b>You:</b> {user_input}")
        self.input_box.clear()

        # Classify query
        query_type = model.FirstLayerDMM(user_input)
        print(query_type)

        if query_type[0].startswith("general"):
            response = Brain.ChatBot(user_input)
        elif query_type[0].startswith("realtime"):
            response = Realtime_Info.RealtimeSearchEngine(user_input)
        else:
            response = "I'm not sure how to handle that request."

        self.chat_display.append(f"<b>Bot:</b> {response}")
        text_to_speech.TextToSpeech(response)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    chatbot = SciFiChatbot()
    chatbot.show()
    sys.exit(app.exec())
