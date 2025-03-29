#!/usr/bin/env python3
import pandas as pd
import sys

def generate_resim(output_path = "resim.csv", camera_data_path = 'f_cam_out.csv', sensor_data_path = 'sensor_out.csv'):
    try:
        camera = pd.read_csv(camera_data_path)
        sensor = pd.read_csv(sensor_data_path)
    except:    
        return
    
    cameraSpeed = []
    sensorSpeed = []

    for indexC, rowC in camera.iterrows():
        for indexS, rowS in sensor.iterrows():
            if rowC["Timestamp"] <= rowS["Timestamp"]: 
                cameraSpeed.append(rowC["Speed"])
                sensorSpeed.append(rowS["Speed"])
                break
                

    averages = ((pd.Series(cameraSpeed) + pd.Series(sensorSpeed))/2).tolist()

    resim = pd.DataFrame({
        "Timestamp" : camera["Timestamp"],
        "FrameID" : camera["FrameID"],
        "Speed" : averages,
        "YawRate" : camera["YawRate"],
        "Signal1" : camera["Signal1"],
        "Signal2" : camera["Signal2"],
    })
    resim.to_csv(output_path, index=False)
    
    return output_path

arguments = sys.argv
if len(arguments) == 1:
    generate_resim()
elif len(arguments) == 2:
    generate_resim(output_path=arguments[1])
elif len(arguments) == 4:
    generate_resim(output_path=arguments[1], camera_data_path=arguments[1], sensor_data_path=arguments[2])
else:
    print("INVALID NUMBER OF ARGUMENTS")
    
    