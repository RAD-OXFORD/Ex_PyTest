"""
File: Register.py
Scope: Implements the City Registration app as per the requirement
Static text - welcomeMessage - “Welcome to Registration”
Static text - enterCity - “Enter city name”
Static text - cityError - “Please enter city”
Static text - confirmation - “Thanks”
Text field - city
Button - registerButton - “Register”

Revision: 1.0
Comment: Implemented requirements for City register App

"""

import sys
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout

class CityRegApp(QWidget):
    
    def __init__(self):
        super().__init__()
        # Create static text for welcomeMessage
        self.welcomeMessage = QLabel()
        self.welcomeMessage.setText("Welcome to Registration")
        self.welcomeMessage.setFont(QFont('Arial', 20))
        
        #Create static text for display message
        self.enterCity = QLabel()
        self.enterCity.setText("Enter City name")
        self.enterCity.setFont(QFont('Arial', 10))
        
        #Create text box for Entering City Name
        self.city = QLineEdit()
        self.city.move(20,20)
        self.city.resize(280,40)
        
        #Create Push Button
        self.registerButton = QPushButton("Register")
        self.registerButton.setFont(QFont('Arial', 14))
        
        #Create a Static text box for Displaying Error Message
        self.cityError = QLabel()
        self.cityError.setText("")
        self.cityError.setFont(QFont('Arial',10))
        
        #Create a Static text box for Displaying Thank you Message
        self.confirmation = QLabel()
        self.confirmation.setText("")
        self.confirmation.setFont(QFont('Arial',10))
        
        #Create a function on button click for next steps
        self.registerButton.clicked.connect(lambda: self.CheckCity())
        
        # set UI size
        self.setGeometry(50, 50, 300, 200)
        # Set UI Name
        self.setWindowTitle("Register")
        
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.welcomeMessage) # Add Welcome Message to Layout
        self.layout.addWidget(self.enterCity)      # Add Enter City Name to Layout
        self.layout.addWidget(self.city)               # Add Text box to Layout 
        self.layout.addWidget(self.registerButton)     # Add Register button to Layout
        self.layout.addWidget(self.cityError)          # Add Static Text for cityError (Default is empty)
        self.layout.addWidget(self.confirmation)       # Add Static Text for CityConfirmation (Default is empty) 
        self.setLayout(self.layout)            
    
    def CheckCity(self):
        cityname = self.city.text()        # Read City name entered by user 
        self.cityError.clear()             # Clear the old entries if any from the cityError field
        self.confirmation.clear()          # Clear the old entries if any from the confirmation field
        if len(cityname)>0:                 # Checking if the name entered, should not be empty
            self.confirmation.setText("Thank you") # if not empty display Thank you
        else:
            self.cityError.setText("Enter City name") # if empty display Enter City name
         
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CityRegApp()
    ex.show()
    sys.exit(app.exec_())