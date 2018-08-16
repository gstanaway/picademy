# picademy seattle group A project "Pi-lot Safety"
# description: waits for high light level, then displays sensehat data in shell, writes it to .csv
# team: clare tally-foos, grant stanaway, jeannette milland vigio, kelly faber, scott mccomb,  
# resources: raspberry pi, sense hat, LDR/photoresistor, 1 uF electrolytic capacitor, resistor
# for detailed instructions on collecting and exporting data to .csv, see "Sense HAT data logger" at projects.raspberrypi.org

# import libraries:
from gpiozero import LightSensor
from time import sleep
from sense_hat import SenseHat
from datetime import datetime, date, time
from csv import writer

# define light sensor
ldr = LightSensor(4) # replace "4" with whichever pin corresponds to your wiring

# define sensehat
sense = SenseHat()
red = (255, 0, 0)
green = (0, 255, 0)

# define function for getting sensehat data together
def get_sense_data():
    sense_data = [] #empty list
        #Collect these
    sense_data.append(datetime.now())
    sense_data.append('Light: ')
    sense_data.append(ldr.value)
    sense_data.append('Temp: ')
    sense_data.append(sense.get_temperature())
    sense_data.append('Pressure')
    sense_data.append(sense.get_pressure())
    sense_data.append('Humidity')
    sense_data.append(sense.get_humidity())
    
    acc = sense.get_accelerometer_raw()
    sense_data.append(acc["x"])
    sense_data.append(acc["y"])
    sense_data.append(acc["z"])

    return sense_data # display the above data in shell

# logic for when to write / display data according to light level, refers to external file named "writer.py"

with open('currentData.csv', 'w', newline='') as f:
    data_writer = writer(f)
    while True:
        sleep(1)
        if ldr.value > 0.90: # write / display sense hat data only during high light level
            print("High Light", ldr.value)
            data = get_sense_data() # collect data
            print(data) # show data in shell
            data_writer.writerow(data) # write data to csv
            sense.clear(red) # show red on sensehat when writing data
        else:
            print("Low Light", ldr.value)
            sense.clear(green) # show green when not writing data
            
