# python-dds238
This library is very useful when reading the chinese DDS238 (and its variants: DDS238-2, ...)  power meter.

This library supposes that you're using an USB-to-RS485 dongle. It doesn't work yet for modbus-over-TCP
(though if you want to propose an MR, i'd accept it gladly !).


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
