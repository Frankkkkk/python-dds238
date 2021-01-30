import minimalmodbus
import serial
import time



class DDS238:
    def __init__(self, modbus_device: str, meter_id: int = 1):
        self.modbus_device = modbus_device
        self.meter_id = meter_id
        self._configure_modbus()

    def _configure_modbus(self):
        instrument = minimalmodbus.Instrument(self.modbus_device, self.meter_id)
        time.sleep(.5)
        instrument.serial.baudrate = 9600
        instrument.serial.bytesize = 8
        instrument.serial.parity = serial.PARITY_NONE
        instrument.serial.stopbits = 1
        instrument.serial.timeout = 1 # seconds

        self._m = instrument


    @property
    def voltage(self) -> float:
        """ Returns the voltage in Volts """
        return self._m.read_register(0xC, 1)

    @property
    def current(self) -> float:
        """ Returns the current in Amperes """
        return self._m.read_register(0xD, 2)

    @property
    def frequency(self) -> float:
        """ Returns the frequency in Herz """
        return self._m.read_register(0x11, 2)

    @property
    def power(self) -> float:
        """ Returns the power in Watts. Positive is import. Negative power is exported """
        return self._m.read_register(0xE, 0, signed=True)


    @property
    def import_energy(self) -> float:
        """ Returns the imported energy, in kWh """
        return self._m.read_long(0xA)/100

    @property
    def export_energy(self) -> float:
        """ Returns the exported energy, in kWh """
        return self._m.read_long(0x8)/100


if __name__ == '__main__':
    d = DDS238('/dev/ttyUSB0', 1)
    print(f'Voltage: {d.voltage}')
    print(f'Current: {d.current}')
    print(f'Frequency: {d.frequency}')
    print(f'Power: {d.power}')
    print(f'Import energy: {d.import_energy}')
    print(f'Export energy: {d.export_energy}')

