"""Parser for Aicooker BLE advertisements.
This file is shamelessly copied from the following repository:
https://github.com/Bluetooth-Devices/govee-ble/blob/432223ada34def7bb58a1601afdfd6954cc3a152/src/govee_ble/parser.py

MIT License applies.
"""
from __future__ import annotations

import logging

from bluetooth_sensor_state_data import BluetoothData
from home_assistant_bluetooth import BluetoothServiceInfo
from sensor_state_data import SensorLibrary

_LOGGER = logging.getLogger(__name__)

MIN_TEMP = -17.7778
MAX_TEMP = 300
ERROR = "error"


class AicookingBluetoothDeviceData(BluetoothData):
    """Data for Aicooking BLE sensors."""

    def _start_update(self, service_info: BluetoothServiceInfo) -> None:
        """Update from BLE advertisement data."""
        _LOGGER.debug("Parsing Aicooking BLE advertisement data: %s", service_info)
        if not service_info.manufacturer_data:
            return

        self.set_device_manufacturer("Aicooking")
        self.set_device_name(service_info.name)
        self.set_device_type(service_info.name)

        changed_manufacturer_data = self.changed_manufacturer_data(service_info)
        if not changed_manufacturer_data or len(changed_manufacturer_data) > 1:
            # If len(changed_manufacturer_data) > 1 it means we switched
            # ble adapters so we do not know which data is the latest
            # and we need to wait for the next update.
            return

        for mfr_id, mfr_data in changed_manufacturer_data.items():
            self._process_mfr_data(
                service_info.address,
                service_info.name,
                mfr_id,
                mfr_data,
                service_info.service_uuids,
            )

    def _process_mfr_data(
        self,
        address: str,
        local_name: str,
        mgr_id: int,
        data: bytes,
        service_uuids: list[str],
    ) -> None:
        """Parser for Govee sensors."""
        msg_length = len(data)

        if msg_length == 4 and ("BBQ" in local_name or mgr_id == 0x55AA):
            self.set_device_type("CXL001-Y")
            temp = float(data)
            if temp >= MIN_TEMP and temp <= MAX_TEMP:
                self.update_predefined_sensor(SensorLibrary.TEMPERATURE__CELSIUS, temp)
            else:
                _LOGGER.debug("Ignoring invalid sensor values, temperature: %.1f", temp)
                self.update_predefined_sensor(SensorLibrary.TEMPERATURE__CELSIUS, ERROR)
