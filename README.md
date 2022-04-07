# This repository is the workstation in RaspberryPi1 of the Collision Avoidance System #

- advmotor.py > is the script that runs the car and processes the distance sensor, communication with another car and decide on different scenarios
- transmit.sh > transmits a file to a user in the same network
- Transmit.py > runs scripts in a loop and continously sending a file to a user using transmit.sh
- ultrasonic.py > distance sensor script

*Every sensor script exports the data to a txt file which will be imported to the advmotor.py for the buildup scenarios*

