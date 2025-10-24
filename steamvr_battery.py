import openvr

openvr.init(openvr.VRApplication_Background)
system = openvr.VRSystem()

print("=== SteamVR – devices status ===")
for i in range(openvr.k_unMaxTrackedDeviceCount):
    if system.isTrackedDeviceConnected(i):
        device_class = system.getTrackedDeviceClass(i)
        try:
            serial = system.getStringTrackedDeviceProperty(i, openvr.Prop_SerialNumber_String)
        except Exception:
            serial = "unknown"

        try:
            battery = system.getFloatTrackedDeviceProperty(i, openvr.Prop_DeviceBatteryPercentage_Float)
            print(f"{i}: {device_class} ({serial}) – battery: {battery*100:.0f}%")
        except openvr.error_code.TrackedProp_UnknownProperty:
            print(f"{i}: {device_class} ({serial}) – no data")
        except Exception as e:
            print(f"{i}: {device_class} ({serial}) – error: {e}")

openvr.shutdown()
input("Press Enter, aby close...")
