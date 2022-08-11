#!/usr/bin/env python
"""
Eastron SDM72D-Modbus V2 Smart Meter Three Phase Electrical System. The Python plugin for Domoticz
Original author: MFxMF
Modified by: bbossink (v1) and later by philip-s (v2)
Requirements: 
    1.python module minimalmodbus -> http://minimalmodbus.readthedocs.io/en/master/
        (pi@raspberrypi:~$ sudo pip3 install minimalmodbus)
    2.Communication module Modbus USB to RS485 converter module
"""
"""
<plugin key="SDM72D" name="Eastron SDM72D-Modbus v2" version="1.0.0" author="philip-s">
    <params>
        <param field="SerialPort" label="Modbus Port" width="200px" required="true" default="/dev/ttyUSB0" />
        <param field="Mode1" label="Baud rate" width="40px" required="true" default="9600"  />
        <param field="Mode2" label="Device ID" width="40px" required="true" default="1" />
        <param field="Mode3" label="Reading Interval min." width="40px" required="true" default="1" />
        <param field="Mode6" label="Debug" width="75px">
            <options>
                <option label="True" value="Debug"/>
                <option label="False" value="Normal"  default="true" />
            </options>
        </param>
    </params>
</plugin>

"""

import minimalmodbus
import serial
import Domoticz


class BasePlugin:
    def __init__(self):
        self.runInterval = 1
        self.rs485 = "" 
        return

    def onStart(self):
        self.rs485 = minimalmodbus.Instrument(Parameters["SerialPort"], int(Parameters["Mode2"]))
        self.rs485.serial.baudrate = Parameters["Mode1"]
        self.rs485.serial.bytesize = 8
        self.rs485.serial.parity = minimalmodbus.serial.PARITY_NONE
        self.rs485.serial.stopbits = 1
        self.rs485.serial.timeout = 1
        self.rs485.debug = False
                          

        self.rs485.mode = minimalmodbus.MODE_RTU
        devicecreated = []
        Domoticz.Log("Eastron SDM72D-M v2 Modbus plugin start")
        self.runInterval = int(Parameters["Mode3"]) * 1 
       
        if 1 not in Devices:
            Domoticz.Device(Name="L1 Volts", Unit=1,Type=0xF3,Subtype=0x8,Used=1).Create()
        Options = { "Custom" : "1;V"} 
        if 2 not in Devices:
            Domoticz.Device(Name="L2 Volts", Unit=2,Type=0xF3,Subtype=0x8,Used=1).Create()
        Options = { "Custom" : "1;V"} 
        if 3 not in Devices:
            Domoticz.Device(Name="L3 Volts", Unit=3,Type=0xF3,Subtype=0x8,Used=1).Create()
        Options = { "Custom" : "1;V"} 
        if 4 not in Devices:
            Domoticz.Device(Name="L1 Current", Unit=4,Type=0xF3,Subtype=0x17,Used=0).Create()
        Options = { "Custom" : "1;A"} 
        if 5 not in Devices:
            Domoticz.Device(Name="L2 Current", Unit=5,Type=0xF3,Subtype=0x17,Used=0).Create()
        Options = { "Custom" : "1;A"} 
        if 6 not in Devices:
            Domoticz.Device(Name="L3 Current", Unit=6,Type=0xF3,Subtype=0x17,Used=0).Create()
        Options = { "Custom" : "1;A"} 
        if 7 not in Devices:
            Domoticz.Device(Name="L1 Active Power", Unit=7,TypeName="Usage",Used=1).Create()
        Options = { "Custom" : "1;W"} 
        if 8 not in Devices:
            Domoticz.Device(Name="L2 Active Power", Unit=8,TypeName="Usage",Used=1).Create()
        Options = { "Custom" : "1;W"} 
        if 9 not in Devices:
            Domoticz.Device(Name="L3 Active Power", Unit=9,TypeName="Usage",Used=1).Create()
        Options = { "Custom" : "1;W"}
        if 10 not in Devices:
            Domoticz.Device(Name="L1 Apparent Power", Unit=10,TypeName="Usage",Used=0).Create()
        Options = { "Custom" : "1;W"} 
        if 11 not in Devices:
            Domoticz.Device(Name="L2 Apparent Power", Unit=11,TypeName="Usage",Used=0).Create()
        Options = { "Custom" : "1;W"} 
        if 12 not in Devices:
            Domoticz.Device(Name="L3 Apparent Power", Unit=12,TypeName="Usage",Used=0).Create()
        Options = { "Custom" : "1;W"}
        # if 13 not in Devices:
        #     Domoticz.Device(Name="L1 Reactive Power", Unit=13,TypeName="Custom",Used=0).Create()
        # Options = { "Custom" : "1;Var"} 
        # if 14 not in Devices:
        #     Domoticz.Device(Name="L2 Reactive Power", Unit=14,TypeName="Custom",Used=0).Create()
        # Options = { "Custom" : "1;Var"} 
        # if 15 not in Devices:
        #     Domoticz.Device(Name="L3 Reactive Power", Unit=15,TypeName="Custom",Used=0).Create()
        # Options = { "Custom" : "1;Var"}
        if 16 not in Devices:
            Domoticz.Device(Name="L1 Power Factor", Unit=16,TypeName="Custom",Used=0).Create()
        Options = { "Custom" : "1;"} 
        if 17 not in Devices:
            Domoticz.Device(Name="L2 Power Factor", Unit=17,TypeName="Custom",Used=0).Create()
        Options = { "Custom" : "1;"} 
        if 18 not in Devices:
            Domoticz.Device(Name="L3 Power Factor", Unit=18,TypeName="Custom",Used=0).Create()
        Options = { "Custom" : "1;"}
        # if 19 not in Devices:
        #     Domoticz.Device(Name="Average_line_to_neutral_volts", Unit=19,Type=0xF3,Subtype=0x8,Used=0).Create()
        # Options = { "Custom" : "1;V"} 
        # if 20 not in Devices:
        #     Domoticz.Device(Name="Average_line_current", Unit=20,Type=0xF3,Subtype=0x17,Used=0).Create()
        # Options = { "Custom" : "1;A"} 
        # if 21 not in Devices:
        #     Domoticz.Device(Name="Sum of line currents", Unit=21,Type=0xF3,Subtype=0x17,Used=0).Create()
        # Options = { "Custom" : "1;A"}
        # if 22 not in Devices:
        #     Domoticz.Device(Name="Total System Power", Unit=22,TypeName="Usage",Used=1).Create()
        # Options = { "Custom" : "1;Wh"} 
        # if 23 not in Devices:
        #     Domoticz.Device(Name="Total system volt amps", Unit=23,TypeName="Custom",Used=0).Create()
        # Options = { "Custom" : "1;VA"} 
        # if 24 not in Devices:
        #     Domoticz.Device(Name="Total system VAr", Unit=24,TypeName="Custom",Used=0).Create()
        # Options = { "Custom" : "1;VAr"} 
        # if 25 not in Devices:
        #     Domoticz.Device(Name="Total system power factor", Unit=25,TypeName="Custom",Used=0).Create()
        # Options = { "Custom" : "1;"} 
        # if 26 not in Devices:
        #     Domoticz.Device(Name="Frequency", Unit=26,TypeName="Custom",Used=0).Create()
        # Options = { "Custom" : "1;Hz"} 
        # if 27 not in Devices:
        #     Domoticz.Device(Name="Import Active Energy", Unit=27,Type=0x71,Subtype=0x0,Used=1).Create()
        # Options = { "Custom" : "1;kWh"}
        # if 28 not in Devices:
        #     Domoticz.Device(Name="Export Active Energy", Unit=28,Type=0x71,Subtype=0x0,Used=1).Create()
        # Options = { "Custom" : "1;kWh"} 
        # if 29 not in Devices:
        #     Domoticz.Device(Name="Line 1 to Line 2 volts", Unit=29,Type=0xF3,Subtype=0x8,Used=0).Create()
        # Options = { "Custom" : "1;V"} 
        # if 30 not in Devices:
        #     Domoticz.Device(Name="Line 2 to Line 3 volts", Unit=30,Type=0xF3,Subtype=0x8,Used=0).Create()
        # Options = { "Custom" : "1;V"} 
        # if 31 not in Devices:
        #     Domoticz.Device(Name="Line 3 to Line 1 volts", Unit=31,Type=0xF3,Subtype=0x8,Used=0).Create()
        # Options = { "Custom" : "1;V"} 
        # if 32 not in Devices:
        #     Domoticz.Device(Name="Average line to line volts", Unit=32,Type=0xF3,Subtype=0x8,Used=0).Create()
        # Options = { "Custom" : "1;V"} 
        # if 33 not in Devices:
        #     Domoticz.Device(Name="Neutral current", Unit=33,Type=0xF3,Subtype=0x17,Used=0).Create()
        # Options = { "Custom" : "1;A"}
        # if 34 not in Devices:
        #     Domoticz.Device(Name="Total Active Energy", Unit=34,Type=0x71,Subtype=0x0,Used=1).Create()
        # Options = { "Custom" : "1;kWh"} 
        # if 35 not in Devices:
        #     Domoticz.Device(Name="Total Reactive Energy", Unit=35,Type="Custom",Used=0).Create()
        # Options = { "Custom" : "1;kVArh"} 
        # if 36 not in Devices:
        #     Domoticz.Device(Name="Resettable total kWh", Unit=36,Type=0x71,Subtype=0x0,Used=0).Create()
        # Options = { "Custom" : "1;kWh"}
        # if 37 not in Devices:
        #     Domoticz.Device(Name="Resettable import kWh", Unit=37,Type=0x71,Subtype=0x0,Used=0).Create()
        # Options = { "Custom" : "1;kWh"}
        # if 38 not in Devices:
        #     Domoticz.Device(Name="Resettable export kWh", Unit=38,Type=0x71,Subtype=0x0,Used=0).Create()
        # Options = { "Custom" : "1;kWh"}
        # if 39 not in Devices:
        #     Domoticz.Device(Name="Net kWh(Import-Export)", Unit=39,Type=0x71,Subtype=0x0,Used=1).Create()
        # Options = { "Custom" : "1;kWh"} 
        # if 40 not in Devices:
        #     Domoticz.Device(Name="Total Import Active Power", Unit=40,TypeName="Usage",Used=1).Create()
        # Options = { "Custom" : "1;W"} 
        # if 41 not in Devices:
        #     Domoticz.Device(Name="Total Export Active Power", Unit=41,TypeName="Usage",Used=1).Create()
        # Options = { "Custom" : "1;W"} 
               
    def onStop(self):
        Domoticz.Log("Eastron SDM72D-M v2 Modbus plugin stop")

    def onHeartbeat(self):
        self.runInterval -=1;
        if self.runInterval <= 0:
            # Get data from SDM72D-M v2
            L1_Volts = self.rs485.read_float(0, functioncode=4, numberOfRegisters=2)
            L2_Volts = self.rs485.read_float(2, functioncode=4, numberOfRegisters=2)
            L3_Volts = self.rs485.read_float(4, functioncode=4, numberOfRegisters=2)
            L1_Current = self.rs485.read_float(6, functioncode=4, numberOfRegisters=2)
            L2_Current = self.rs485.read_float(8, functioncode=4, numberOfRegisters=2)
            L3_Current = self.rs485.read_float(10, functioncode=4, numberOfRegisters=2)
            L1_Active_Power = self.rs485.read_float(12, functioncode=4, numberOfRegisters=2)
            L2_Active_Power = self.rs485.read_float(14, functioncode=4, numberOfRegisters=2)
            L3_Active_Power = self.rs485.read_float(16, functioncode=4, numberOfRegisters=2)
            L1_Apparent_Power = self.rs485.read_float(18, functioncode=4, numberOfRegisters=2)
            L2_Apparent_Power = self.rs485.read_float(20, functioncode=4, numberOfRegisters=2)
            L3_Apparent_Power = self.rs485.read_float(22, functioncode=4, numberOfRegisters=2)
            # L1_Reactive_Power = self.rs485.read_float(24, functioncode=4, numberOfRegisters=2)
            # L2_Reactive_Power = self.rs485.read_float(26, functioncode=4, numberOfRegisters=2)
            # L3_Reactive_Power = self.rs485.read_float(28, functioncode=4, numberOfRegisters=2)
            L1_Power_Factor = self.rs485.read_float(30, functioncode=4, numberOfRegisters=2)
            L2_Power_Factor = self.rs485.read_float(32, functioncode=4, numberOfRegisters=2)
            L3_Power_Factor = self.rs485.read_float(34, functioncode=4, numberOfRegisters=2)
            # Average_line_to_neutral_volts = self.rs485.read_float(42, functioncode=4, numberOfRegisters=2)
            # Average_line_current = self.rs485.read_float(46, functioncode=4, numberOfRegisters=2)
            # Sum_of_line_currents = self.rs485.read_float(48, functioncode=4, numberOfRegisters=2)
            # Total_System_Power = self.rs485.read_float(52, functioncode=4, numberOfRegisters=2)
            # Total_System_Volt_amps = self.rs485.read_float(56, functioncode=4, numberOfRegisters=2)
            # Total_System_VAr = self.rs485.read_float(60, functioncode=4, numberOfRegisters=2)
            # Total_System_power_factor = self.rs485.read_float(62, functioncode=4, numberOfRegisters=2)
            # Frequency_of_supply_voltages = self.rs485.read_float(70, functioncode=4, numberOfRegisters=2)
            # Import_Wh_since_last_reset = self.rs485.read_float(72, functioncode=4, numberOfRegisters=2)
            # Export_Wh_since_last_reset = self.rs485.read_float(74, functioncode=4, numberOfRegisters=2)
            # Line_1_to_Line_2_volts = self.rs485.read_float(200, functioncode=4, numberOfRegisters=2)
            # Line_2_to_Line_3_volts = self.rs485.read_float(202, functioncode=4, numberOfRegisters=2)
            # Line_3_to_Line_1_volts = self.rs485.read_float(204, functioncode=4, numberOfRegisters=2)
            # Average_line_to_line_volts = self.rs485.read_float(206, functioncode=4, numberOfRegisters=2)
            # Neutral_current = self.rs485.read_float(224, functioncode=4, numberOfRegisters=2)
            # Total_active_energy_kWh = self.rs485.read_float(342, functioncode=4, numberOfRegisters=2)
            # Total_reactive_energy = self.rs485.read_float(344, functioncode=4, numberOfRegisters=2)
            # Resettable_total_kWh = self.rs485.read_float(384, functioncode=4, numberOfRegisters=2)
            # Resettable_import_kWh = self.rs485.read_float(388, functioncode=4, numberOfRegisters=2)
            # Resettable_export_kWh = self.rs485.read_float(390, functioncode=4, numberOfRegisters=2)
            # Net_kWh_Import_to_Export = self.rs485.read_float(396, functioncode=4, numberOfRegisters=2)
            # Import_power = self.rs485.read_float(1280, functioncode=4, numberOfRegisters=2)
            # Export_power = self.rs485.read_float(1282, functioncode=4, numberOfRegisters=2)
            
            #Update devices
            Devices[1].Update(0,str(L1_Volts))
            Devices[2].Update(0,str(L2_Volts))
            Devices[3].Update(0,str(L3_Volts))
            Devices[4].Update(0,str(L1_Current))
            Devices[5].Update(0,str(L2_Current))
            Devices[6].Update(0,str(L3_Current))
            Devices[7].Update(0,str(L1_Active_Power))
            Devices[8].Update(0,str(L2_Active_Power))
            Devices[9].Update(0,str(L3_Active_Power))
            Devices[10].Update(0,str(L1_Apparent_Power))
            Devices[11].Update(0,str(L2_Apparent_Power))
            Devices[12].Update(0,str(L3_Apparent_Power))
            # Devices[13].Update(0,str(L1_Reactive_Power))
            # Devices[14].Update(0,str(L2_Reactive_Power))
            # Devices[15].Update(0,str(L3_Reactive_Power))
            Devices[16].Update(0,str(L1_Power_Factor))
            Devices[17].Update(0,str(L2_Power_Factor))
            Devices[18].Update(0,str(L3_Power_Factor))
            # Devices[19].Update(0,str(Average_line_to_neutral_volts))
            # Devices[20].Update(0,str(Average_line_current))
            # Devices[21].Update(0,str(Sum_of_line_currents))
            # Devices[22].Update(0,str(Total_System_Power))
            # Devices[23].Update(0,str(Total_System_Volt_amps))
            # Devices[24].Update(0,str(Total_System_VAr))
            # Devices[25].Update(0,str(Total_System_power_factor))
            # Devices[26].Update(0,str(Frequency_of_supply_voltages))
            # Devices[27].Update(0,str(Import_Wh_since_last_reset*1000))
            # Devices[28].Update(0,str(Export_Wh_since_last_reset*1000))
            # Devices[29].Update(0,str(Line_1_to_Line_2_volts))
            # Devices[30].Update(0,str(Line_2_to_Line_3_volts))
            # Devices[31].Update(0,str(Line_3_to_Line_1_volts))
            # Devices[32].Update(0,str(Average_line_to_line_volts))
            # Devices[33].Update(0,str(Neutral_current))
            # Devices[34].Update(0,str(Total_active_energy_kWh))
            # Devices[35].Update(0,str(Total_reactive_energy))
            # Devices[36].Update(0,str(Resettable_total_kWh))
            # Devices[37].Update(0,str(Resettable_import_kWh))
            # Devices[38].Update(0,str(Resettable_export_kWh))
            # Devices[39].Update(0,str(Net_kWh_Import_to_Export))
            # Devices[40].Update(0,str(Import_power))
            # Devices[41].Update(0,str(Export_power))
            
            
            if Parameters["Mode6"] == 'Debug':
                Domoticz.Log("Eastron SDM72D-M v2 Modbus Data (not all)")
                # Domoticz.Log('Total system power: {0:.3f} W'.format(Total_System_Power))
                # Domoticz.Log('Import Wh since last reset: {0:.3f} kWh'.format(Import_Wh_since_last_reset))
                # Domoticz.Log('Export Wh since last reset: {0:.3f} kWh'.format(Export_Wh_since_last_reset))
                # Domoticz.Log('Total active energy kWh: {0:.3f} kWh'.format(Total_active_energy_kWh))
                # Domoticz.Log('Settable total kWh: {0:.3f} kWh'.format(Resettable_total_kWh))
                # Domoticz.Log('Settable import kWh: {0:.3f} kWh'.format(Resettable_import_kWh))
                # Domoticz.Log('Settable export kWh: {0:.3f} kWh'.format(Resettable_export_kWh))
                # Domoticz.Log('Import power: {0:.3f} kWh'.format(Import_power))
                # Domoticz.Log('Export power: {0:.3f} kWh'.format(Export_power))
               
            self.runInterval = int(Parameters["Mode3"]) * 6


global _plugin
_plugin = BasePlugin()


def onStart():
    global _plugin
    _plugin.onStart()


def onStop():
    global _plugin
    _plugin.onStop()


def onHeartbeat():
    global _plugin
    _plugin.onHeartbeat()

# Generic helper functions
def DumpConfigToLog():
    for x in Parameters:
        if Parameters[x] != "":
            Domoticz.Debug("'" + x + "':'" + str(Parameters[x]) + "'")
    Domoticz.Debug("Device count: " + str(len(Devices)))
    for x in Devices:
        Domoticz.Debug("Device:           " + str(x) + " - " + str(Devices[x]))
        Domoticz.Debug("Device ID:       '" + str(Devices[x].ID) + "'")
        Domoticz.Debug("Device Name:     '" + Devices[x].Name + "'")
        Domoticz.Debug("Device nValue:    " + str(Devices[x].nValue))
        Domoticz.Debug("Device sValue:   '" + Devices[x].sValue + "'")
        Domoticz.Debug("Device LastLevel: " + str(Devices[x].LastLevel))
    return
