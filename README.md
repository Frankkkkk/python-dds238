# python-dds238
This library is very useful when reading the chinese DDS238 (and its variants: DDS238-2, ...)  power meter.

This library supposes that you're using an USB-to-RS485 dongle. It doesn't work yet for modbus-over-TCP
(though if you want to propose an MR, i'd accept it gladly !).

# Installation
To install the library, simply type:
```
$ pip3 install python-dds238
```


# Usage
I'ts very simple:
```python3
>>> from dds238 import DDS238
>>> meter = DDS238(modbus_device='/dev/ttyUSB0', meter_id=20)
>>> meter.voltage
215.4
>>> meter.power
1632
>>> meter.export_energy
1288.2
```

# DOC
```
 |  current
 |      Returns the current in Amperes
 |
 |  export_energy
 |      Returns the exported energy, in kWh
 |
 |  frequency
 |      Returns the frequency in Herz
 |
 |  import_energy
 |      Returns the imported energy, in kWh
 |
 |  power
 |      Returns the power in Watts. Positive is import. Negative power is exported
 |
 |  power_factor
 |      Returns the power factor (0-1 scalar)
 |
 |  reactive_power
 |      Return the reactive power in VAr
 |
 |  voltage
 |      Returns the voltage in Volts
 |
 |  ----------------------------------------------------------------------
 |
 |  change_address(self, address: int, baudrate=9600)
 |      Change the modbus address and the baudrate of the current device. USE AT YOUR OWN RISK !
```

# Baudrate reset
In the case that you fuckup the meter's baudrate, you can reset it to 9600 by going to the baudrate menu and holding down the select button. Once the display shows `- Clr -` you must cut off the power to the meter (while holding the button). The meter will reset to `9600` Bd.

You can reach a single meter on a bus by using id `0`.
