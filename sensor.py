#!/usr/bin/env python3

import pandas as pd
import sys

from values import Value
from random import randrange, uniform


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

def generate_sensor_data(output_path = "sensor_out.csv", timestamp_trashold = 160_000_000):
    timestamp = Timestamp(100_000_000, "μs")
    speed = Speed(60, "km/h")

    pairs = {
        timestamp : [timestamp.value],
        speed : [speed.value]
    }
    while(timestamp.value <= timestamp_trashold):
        for obj, arr in pairs.items():
            obj.increment()
            arr.append(obj.value)

    df = pd.DataFrame({
        "Timestamp" : pairs[timestamp],
        "Speed" : pairs[speed],
    })

    df.to_csv(output_path, index=False)
    return output_path

arguments = sys.argv
if len(arguments) == 1:
    generate_sensor_data()
elif len(arguments) == 2:
    generate_sensor_data(output_path=arguments[1])
else:
    print("INVALID NUMBER OF ARGUMENTS")
    
    