#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
from values import Value
from random import randrange, uniform


# In[6]:


class Timestamp(Value):
    def increment(self):
        self.value += 200_000 + randrange(-10_000, 10_000, 1)
        self.value = round(self.value, 6)

class Speed(Value):
    def increment(self):
        if self.value >= 120.0:
            self.value = 120.0 + uniform(-0.1,0.1)
            self.value = round(self.value, 2)
        else:
            self.value += 0.56
            self.value = round(self.value, 2)


# In[7]:


def generate_sensor_data(output_file = "sensor_out.csv", number_of_frames = 2000):
    timestamp = Timestamp(100_000_000, "μs")
    speed = Speed(60, "km/h")

    pairs = {
        timestamp : [timestamp.value],
        speed : [speed.value]
    }
    while(timestamp.value <= 160_000_000):
        for obj, arr in pairs.items():
            obj.increment()
            arr.append(obj.value)

    df = pd.DataFrame({
        "Timestamp" : pairs[timestamp],
        "Speed" : pairs[speed],
    })

    df.to_csv(output_file, index=False)


# In[8]:


generate_sensor_data()

