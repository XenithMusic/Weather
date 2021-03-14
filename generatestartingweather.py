import time

def start():
    start_type = input("Type [M: Manual, R: Random] >> ")
    if start_type == "M":
        conditions = {}
        conditionstemperaturemode = input("Temperature Mode [F: Fahrenheit, C: Celsius] >> ")
        conditionstemperature = float(input("Temperature (Native mode) >> "))
        conditionspressure = float(input("Air Pressure (Inches) >> "))
        conditionscelsius = round(((conditionstemperature*(9/5)) + 32)*100000)/100000
        savp = 6.11*10*((7.5*conditionstemperature)/(237.3+conditionstemperature))
        avp = savp/1.9476
        conditionshumidity = (avp/savp)*100

        confidence = conditionstemperature-20
        confidence2 = conditionstemperature-40
        confidence2 = confidence2*5
        if confidence <= 0:
            confidence = 0
        elif confidence2 >= 100:
            confidence2 = 100
            confidence = confidence2
        else:
            if confidence2 <= 0:
                print(confidence)
                print(confidence2)
                trueconf = (confidence+0)/2
            else:
                print(confidence)
                print(confidence2)
                trueconf = (confidence+confidence2)/2

        conditionsrainchance = (trueconf/100)*conditionshumidity

        if conditionstemperaturemode == "C":
            conditionstemperature = round(((conditionstemperature*(9/5)) + 32)*100000)/100000
            print(conditionstemperature)

        conditions = {"temp":conditionstemperature,"tempmode":conditionstemperaturemode,"humid":conditionshumidity,"rainchance":conditionsrainchance,"rainchanceconf":trueconf}
        return conditions

print(start())
time.sleep(5)
