import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QLabel
from qtpy.QtCore import Qt

class FactorialCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    
    def init_ui(self):
        # Set up the window
        self.setWindowTitle('Factorial Calculator')
        self.setGeometry(300, 300, 300, 200)
        
        # Create layout
        layout = QVBoxLayout()

        # Create and add widgets
        self.input_label = QLabel('Enter a number:')
        layout.addWidget(self.input_label)
        
        self.input_field = QLineEdit()
        self.input_field.setStyleSheet("color: white; background-color: black;")  # Set text color to white and background to black
        layout.addWidget(self.input_field)
        
        self.calculate_button = QPushButton('Calculate Factorial')
        self.calculate_button.clicked.connect(self.calculate_factorial)
        layout.addWidget(self.calculate_button)
        
        self.result_label = QLabel('')
        layout.addWidget(self.result_label)
        
        self.setLayout(layout)

    def calculate_factorial(self):
        try:
            num = int(self.input_field.text())
            if num < 0:
                self.result_label.setText('Error: Factorial of a negative number doesn\'t exist.')
            else:
                result = self.factorial(num)
                self.result_label.setText(f'Factorial of {num} is: {result}')
        except ValueError:
            self.result_label.setText('Error: Please enter a valid integer.')
    
    def factorial(self, n):
        if n == 0 or n == 1:
            return 1
        else:
            return n * self.factorial(n - 1)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = FactorialCalculator()
    window.show()
    sys.exit(app.exec())
