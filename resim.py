import pandas as pd

def generate_resim(output_path = "resim.csv", camera_data_path = 'f_cam_out.csv', sensor_data_path = 'sensor_out.csv'):
    camera = pd.read_csv(camera_data_path)
    sensor = pd.read_csv(sensor_data_path)

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
        "Speed" : averages,
        "FrameID" : camera["FrameID"],
        "YawRate" : camera["YawRate"],
        "Signal1" : camera["Signal1"],
        "Signal2" : camera["Signal2"],
    })
    resim.to_csv(output_path, index=False)
    
    return output_path