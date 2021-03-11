import time

def start():
    start_type = input("Type [M: Manual, R: Random] >> ")
    if start_type == "M":
        conditions = {}
        conditionstemperaturemode = input("Temperature Mode [F: Fahrenheit, C: Celsius] >> ")
        conditionstemperature = float(input("Temperature (Native mode) >> "))
        if conditionstemperaturemode == "C":
            conditionstemperature = round(((conditionstemperature*(9/5)) + 32)*100000)/100000
            print(conditionstemperature)

def 
