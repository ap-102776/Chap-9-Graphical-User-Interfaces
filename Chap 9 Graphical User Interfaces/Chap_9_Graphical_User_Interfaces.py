# Anthony Perrine
# Dr. Giles
# Chap 9 Graphical User Interfaces

# This program creates a simple GUI for converting Celsius to Fahrenheit or vice versa. 

from breezypythongui import EasyFrame

class TemperatureConverter(EasyFrame):

# The constructor creates the GUI components.
    def __init__(self):
        EasyFrame.__init__(self, title = "Temperature Converter")
        self.addLabel(text = "Celsius", row = 0, column = 1)
        self.addLabel(text = "Fahrenheit", row = 0, column = 0)

        self.celsiusField = self.addFloatField(value = 0.0, row = 1, column = 1, precision = 2)
        self.fahrenheitField = self.addFloatField(value = 32.0, row = 1, column = 0, precision = 2)

        self.addButton(text = ">>>>", row = 2, column = 0, command = self.fahrToCelsius)
        self.addButton(text = "<<<<", row = 2, column = 1, command = self.celsiusToFahr)

# The event handling methods for the buttons are defined below.  
    def fahrToCelsius(self):
        fahr = self.fahrenheitField.getNumber()
        celsius = (fahr - 32) * 5 / 9
        self.celsiusField.setNumber(celsius)

    def celsiusToFahr(self):
        celsius = self.celsiusField.getNumber()
        fahrenheit = celsius * 9 / 5 + 32
        self.fahrenheitField.setNumber(fahrenheit)

# The main method creates an instance of the TemperatureConverter class and starts the GUI.
def main():
    TemperatureConverter().mainloop()
    
if __name__ == "__main__":
    main()