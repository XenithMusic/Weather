import time

conf2 = None

def start():
    global conf2
    start_type = input("Type [M: Manual, R: Random] >> ")
    if start_type == "M":
        conditions = {}
        conditionstemperaturemode = input("Temperature Mode [F: Fahrenheit, C: Celsius] >> ")
        conditionstemperature = float(input("Temperature (Native mode,7PM) >> "))
        conditionsdew = float(input("Dew Point (Native mode,7PM) >> "))
        conditionspressure = float(input("Air Pressure (Inches,7PM) >> "))
        aconditionstemperature = float(input("Temperature (Native mode,7AM) >> "))
        aconditionsdew = float(input("Dew Point (Native mode,7AM) >> "))
        aconditionspressure = float(input("Air Pressure (Inches,7AM) >> "))


        # AM


        if conditionstemperaturemode == "F":
            conditionscelsius = round(((conditionstemperature*(9/5)) + 32)*100000)/100000
            conditionsdewsius = round(((conditionsdew*(9/5)) + 32)*100000)/100000

        print(conditionscelsius)
        print(conditionsdewsius)

        satvp = 6.11*10*((7.5*conditionscelsius)/(237.3+conditionscelsius))
        actvp = 6.11*10*((7.5*conditionsdewsius)/(237.3+conditionsdewsius))
        print(satvp)
        print(actvp)
        rh = actvp/satvp
        rh = rh*100
        amhum = rh-((round(conditionspressure*100)**(0.90))/100)


        # PM


        if conditionstemperaturemode == "F":
            conditionscelsius = round(((aconditionstemperature*(9/5)) + 32)*100000)/100000
            conditionsdewsius = round(((aconditionsdew*(9/5)) + 32)*100000)/100000

        print(conditionscelsius)
        print(conditionsdewsius)

        satvp = 6.11*10*((7.5*conditionscelsius)/(237.3+conditionscelsius))
        actvp = 6.11*10*((7.5*conditionsdewsius)/(237.3+conditionsdewsius))
        print(satvp)
        print(actvp)
        rh = actvp/satvp
        rh = rh*100
        pmhum = rh-((round(conditionspressure*100)**(0.90))/100)


        # FIN


        conditionshumidity = (amhum+pmhum)/2

        print("Humidity at 9PM today: " + str(conditionshumidity))


        if conditionstemperaturemode == "C":
            conditionstemperature = round(((conditionstemperature*(9/5)) + 32)*100000)/100000
            print(conditionstemperature)

        conditions = {"temp":conditionstemperature,"tempmode":conditionstemperaturemode,"cloudcover":conditionshumidity,"humidity":conditionshumidity}

        return conditions

print(start())
time.sleep(5)
