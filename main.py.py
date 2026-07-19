
# SMART DEVICE MANAGEMENT SYSTEM
# EL 162 / 234 OOP MINI PROJECT
# Name:MENSAH REGINALD NHYIRABA
# Index Number:FOE.41.006.112.25

#PARENT CLASS
#-SmartDevices
class SmartDevice:
    def __init__(self, name, device_id):
        self.name = name
        self.__device_id = device_id
        self.__power_status = False

    # Getter for device ID
    def get_device_id(self):
        return self.__device_id

    # Setter for device ID
    def set_device_id(self, new_id):
        if new_id.strip() != "":
            self.__device_id = new_id
        else:
            print("Device ID cannot be empty.")

    # Getter for power status
    def get_power_status(self):
        return self.__power_status

    # Turn device on
    def turn_on(self):
        self.__power_status = True
        print(f"{self.name} is now ON.")

    # Turn device off
    def turn_off(self):
        self.__power_status = False
        print(f"{self.name} is now OFF.")

    # Display device information
    def display_info(self):
        print("\n------ DEVICE INFORMATION ------")
        print("Device Name :", self.name)
        print("Device ID   :", self.__device_id)
        print("Power Status:", "ON" if self.__power_status else "OFF")

#CHILD CLASSES
#-SecurityCamera
    class SecurityCamera(SmartDevices):               /
    def __init__(self, name, device_id):
        super().__init__(name, device_id)
        self.recording_status = False

    def start_recording(self):
        if self.get_power_status():
            self.recording_status = True
            print(f"{self.name} has started recording.")
        else:
            print("Please turn on the camera first.")

    def stop_recording(self):
        self.recording_status = False
        print(f"{self.name} has stopped recording.")

    def display_info(self):
        super().display_info()
        print("Recording Status:", "Recording" if self.recording_status else "Not Recording")

#SmartLight Class
           class SmartLight(SmartDevice):
    def __init__(self, name, device_id, brightness=50):
        super().__init__(name, device_id)
        self.brightness = brightness

    def increase_brightness(self):
        if self.brightness < 100:
            self.brightness += 10
            if self.brightness > 100:
                self.brightness = 100
            print(f"Brightness: {self.brightness}%")
        else:
            print("Brightness is already at maximum.")

    def decrease_brightness(self):
        if self.brightness > 0:
            self.brightness -= 10
            if self.brightness < 0:
                self.brightness = 0
            print(f"Brightness: {self.brightness}%")
        else:
            print("Brightness is already at minimum.")

    def display_info(self):
        super().display_info()
        print("Brightness:", self.brightness, "%").

#TemperatureSensor Class
    class TemperatureSensor(SmartDevice):
    def __init__(self, name, device_id, temperature=25):
        super().__init__(name, device_id)
        self.temperature = temperature

    def read_temperature(self):
        print(f"Current Temperature: {self.temperature}°C")

    def display_info(self):
        super().display_info()
        print("Temperature:", self.temperature, "°C")

 #Objects
  camera = #SecurityCamera("Front Door Camera", "CAM001")
light = #SmartLight("Living Room Light", "LGT001")
sensor = TemperatureSensor("Kitchen Sensor", "TMP001", 27)

 #Menu
 def menu():
    print(" SMART DEVICE MANAGEMENT SYSTEM ")
    print("1. Display Device Information")
    print("2. Turn Device On")
    print("3. Turn Device Off")
    print("4. Read Temperature")
    print("5. Adjust Brightness")
    print("6. Start/Stop Recording")
    print("7. Exit")

  while True:
    menu()

    choice = input("Enter your choice: ")

    if choice == "1":
        camera.display_info()
        light.display_info()
        sensor.display_info()

    elif choice == "2":
        camera.turn_on()
        light.turn_on()
        sensor.turn_on()

    elif choice == "3":
        camera.turn_off()
        light.turn_off()
        sensor.turn_off()

    elif choice == "4":
        sensor.read_temperature()

    elif choice == "5":
        print("\n1. Increase Brightness")
        print("2. Decrease Brightness")
        option = input("Choose option: ")

        if option == "1":
            light.increase_brightness()
        elif option == "2":
            light.decrease_brightness()
        else:
            print("Invalid option.")

    elif choice == "6":
        print("\n1. Start Recording")
        print("2. Stop Recording")
        option = input("Choose option: ")

        if option == "1":
            camera.start_recording()
        elif option == "2":
            camera.stop_recording()
        else:
            print("Invalid option.")

    elif choice == "7":
        print("Thank you for using the Smart Device Management System.")
        break

    else:
        print("Invalid choice. Please try again.")