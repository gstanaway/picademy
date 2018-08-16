# ldr experiment trigger

### description 
A project from day two of Picademy Seattle 2018. Program waits for high light level, then displays sensehat data in shell, and also writes it to a `.csv` file.

### team
clare tally-foos, grant stanaway, jeannette milland vigio, kelly faber, scott mccomb

### what you'll need
* raspberry pi
* sense hat
* (mini black hat hack3r)[https://shop.pimoroni.com/products/mini-black-hat-hack3r] 
* LDR/photoresistor
* 1 uF electrolytic capacitor
* 4 female-to-male jumper wires

### additional resources
For detailed instructions on collecting and exporting data to .csv, see the [Sense HAT data logger](https://projects.raspberrypi.org/en/projects/sense-hat-data-logger) project at [projects.raspberrypi.org](projects.raspberripi.org).  

Help wiring the photoresistor came from [Raspberry Pi Light Sensor: A Simple LDR Tutorial](https://pimylifeup.com/raspberry-pi-light-sensor/) on [pimylifeup.com](pimylifeup.com), although the code used in this project is different.

### instructions
1. Assemble the physical components of the project (see `ldr_diagram.png` in this repository)  
>**Note:** in our example image, the purple wire is most important. One end is inserted into the breadboard between the photoresistor and capacitor; the other end runs to pin 4 on our hat hacker.
1. Download both python files from this repository to the same folder on your pi
1. Edit the `ldr` variable in `ldr_experiment_trigger.py` so that it corresponds to your wiring
1. Run `ldr_experiment_trigger.py`
1. Trigger data logging by shining a light onto the photo resister
1. Stop the program
1. Read your data in the newly-created file called `currentData.csv`
> You will be unable to open `currentData.csv` if the program is still running.
