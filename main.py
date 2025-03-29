#!/usr/bin/env python3
import sys
from f_cam import generate_front_camera_data
from sensor import generate_sensor_data
from resim import generate_resim

print("Processing...")
arguments = sys.argv
if len(arguments) == 1:
    camera_path = generate_front_camera_data()
    sensor_path = generate_sensor_data()
    resim_path = generate_resim()
    print(f"Camera data saved to: {camera_path}")
    print(f"Sensor data saved to: {sensor_path}")
    print(f"Resim data saved to: {resim_path}")
elif len(arguments) == 2:
    camera_path = generate_front_camera_data()
    sensor_path = generate_sensor_data()
    resim_path = generate_resim(output_path=arguments[1])
    print(f"Camera data saved to: {camera_path}")
    print(f"Sensor data saved to: {sensor_path}")
    print(f"Resim data saved to: {resim_path}")
else:
    print("INVALID NUMBER OF ARGUMENTS")
