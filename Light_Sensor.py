#!/usr/bin/env python

import time

from grove.grove_light_sensor_v1_2 import GroveLightSensor

def main():

    # Grove - Light Sensor connected to port A0
    sensor = GroveLightSensor(0)

    while True:
        angle = sensor.light * 180 / 1000
        print('light value {}, turn to {} degree.'.format(sensor.light, angle))
        

        time.sleep(1)

if __name__ == '__main__':
    main()