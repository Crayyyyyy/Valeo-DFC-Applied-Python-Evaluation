#!/usr/bin/env python
# coding: utf-8

# In[1]:


from random import uniform, randrange

from values import Value
import pandas as pd


# In[2]:


class Timestamp(Value):    
    def increment(self):
        temp = self.value + (27_700 + uniform(-50, 50))
        self.value = round(temp, 6)
        
class FrameID(Value):
    def increment(self):
        self.value += 1
        
class Speed(Value):
    def increment(self):
        if(self.value >= 120):
            self.value = round(120 + uniform(-0.05, 0.05), 2)
        else:
            self.value = round(self.value + 0.08, 2)

class YawRate(Value):
    def increment(self):
        self.value = uniform(-1,1)
 
class Signal1(Value):
    def increment(self, frameID: int):
        if frameID == 201:
            self.value = randrange(1,16, 1)

class Signal2(Value):
    def increment(self, signal1: int):
        if signal1 < 5:
            self.value = 0
        else:
            self.value = 80 + randrange(-10,10, 1)


# In[3]:


def generate_front_camera_data(output_file = "f_cam_out.csv", number_of_frames = 2000):
    timestamp = Timestamp(100_000_000, "μs")
    frameID = FrameID(100, "#")
    speed = Speed(60, "km/h")
    yawRate = YawRate(0, "deg/sec")
    signal1 = Signal1(0, "#")
    signal2 = Signal2(0, "#")

    pairs = {
        timestamp : [timestamp.value],
        frameID : [frameID.value],
        speed : [speed.value],
        yawRate : [yawRate.value],
        signal1 : [signal1.value],
        signal2 : [signal2.value]
    }
    for i in range(number_of_frames-1):
        for obj, arr in pairs.items():
            if isinstance(obj, Signal1):
                obj.increment(frameID.value)
            elif isinstance(obj, Signal2):
                obj.increment(signal1.value)
            else:
                obj.increment()
            arr.append(obj.value)

    df = pd.DataFrame({
        "Timestamp" : pairs[timestamp],
        "FrameID" : pairs[frameID],
        "Speed" : pairs[speed],
        "YawRate" : pairs[yawRate],
        "Signal1" : pairs[signal1],
        "Signal2" : pairs[signal2],
    })

    df.to_csv(output_file, index=False)


# In[4]:


dataFrame = generate_front_camera_data()

