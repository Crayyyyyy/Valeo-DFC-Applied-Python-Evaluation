#!/usr/bin/env python3
import sys
from f_cam import generate_front_camera_data
from sensor import generate_sensor_data
from resim import generate_resim

if len(sys.argv) == 1:
    generate_front_camera_data()
    generate_sensor_data()
    generate_resim()
