import pytest
from PyQt5 import QtCore
import Register



@pytest.fixture
def app(qtbot):
    test_Register_app = Register.CityRegApp()
    qtbot.addWidget(test_Register_app)
    return test_Register_app


def test_1_display(app):
    #Testcase 1 : Test that all elements are displayed on screen, with the exception of 
    #             cityError and confirmation. Include in test that cityError is NOT displayed.
    assert app.welcomeMessage.text() == "Welcome to Registration", print("Static text: 'Welcome to Registration displayed' does not match expected output")
    assert app.enterCity.text() == "Enter City name", print("Static text: 'Enter City name' does not match expected output")
    assert app.city.text() == "", print("Text field: is not empty when app is launched")
    assert app.registerButton.text() == "Register", print("Button: Register is not displayed")
    assert app.cityError.text() == "", print("Static text:'City Error' Field shall not be displayed ")
    assert app.confirmation.text() == "", print("Static text: 'Confirmation' shall not displayed")
    
def test_2_display(app, qtbot):
    
    #Testcase 2 : Test that Thank you message is displayed once a city name is entered 
    #             and Register button is tapped
    app.city.setText("Chippenham") # Enter City name in EditField
    qtbot.mouseClick(app.registerButton, QtCore.Qt.LeftButton)
    assert app.confirmation.text() == "Thank you", print("Static text:'City name' is not entered")
    assert app.cityError.text() == "", print("Static text:'' Field is not displayed ")
    

def test_3_display(app, qtbot):
    #Testcase 3 : Test that "Enter City name" is displayed when register button is tapped  
    #             with no entry in the Editbox
    qtbot.mouseClick(app.registerButton, QtCore.Qt.LeftButton)
    assert app.confirmation.text() == "", print("Static text:'confirmation' Field is not empty")
    assert app.cityError.text() == "Enter City name", print("Static text:'Enter City name' Field is not displayed ")
    
