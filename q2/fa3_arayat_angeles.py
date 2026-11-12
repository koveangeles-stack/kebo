from abc import ABC, abstractmethod

class Sensor(ABC):
    @abstractmethod
    def get_reading(self):
        pass


class TempSensor(Sensor):
    def get_reading(self):
        return "24.5°C"
    def __str__(self):
        return "24.5°C"

class PHSensor(Sensor):
    def get_reading(self):
        return "7.2 pH (Neutral)"
    def __str__(self):
        return "7.2 pH (Neutral)"



tempSensor = TempSensor()
pHSensor = PHSensor()
print("--- Lab Inventory System ---")

print(f"[pH Sensor] Reading: {pHSensor}")
print(f"[Temperature Sensor] Reading: {tempSensor}")

print("\n-------------------------------")
