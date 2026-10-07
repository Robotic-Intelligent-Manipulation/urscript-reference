# Module Interfaces (I/O, TCP/IP Sockets, RTDE & Fieldbuses)

> **Reference Module**: URScript Specification (Chapter 17)
> **Total Functions**: 75 functions
> **Target Controllers**: Universal Robots e-Series, UR20, UR30, CB-Series (SW 5.16+)

## Overview

Low-level hardware and peripheral communication interfaces. Includes digital and analog I/O lines for the controller and tool flange, TCP/IP client sockets (bridging vision systems and external PCs), Real-Time Data Exchange (RTDE) register synchronizers, industrial Modbus RTU/TCP fieldbuses, XML-RPC client factories, and teach pendant popup dialogs.

## Function Index (75 Functions)

- [`enable_external_ft_sensor(enable, sensor_mass=0.0, sensor_measuring_offset=[0.0, 0.0, 0.0], sensor_cog=[0.0, 0.0, 0.0])`](#enable_external_ft_sensor)
- [`ft_rtde_input_enable(enable, sensor_mass=0.0, sensor_ measuring_offset=[0.0, 0.0, 0.0], sensor_cog=[0.0, 0.0, 0.0])`](#ft_rtde_input_enable)
- [`get_analog_in(n)`](#get_analog_in)
- [`get_analog_out(n)`](#get_analog_out)
- [`get_configurable_digital_in(n)`](#get_configurable_digital_in)
- [`get_configurable_digital_out(n)`](#get_configurable_digital_out)
- [`get_digital_in(n)`](#get_digital_in)
- [`get_digital_out(n)`](#get_digital_out)
- [`get_flag(n)`](#get_flag)
- [`get_standard_analog_in(n)`](#get_standard_analog_in)
- [`get_standard_analog_out(n)`](#get_standard_analog_out)
- [`get_standard_digital_in(n)`](#get_standard_digital_in)
- [`get_standard_digital_out(n)`](#get_standard_digital_out)
- [`get_tool_analog_in(n)`](#get_tool_analog_in)
- [`get_tool_digital_in(n)`](#get_tool_digital_in)
- [`get_tool_digital_out(n)`](#get_tool_digital_out)
- [`modbus_add_signal(IP, slave_number, signal_address, signal_type, signal_name, sequential_mode=False, register_ count=1)`](#modbus_add_signal)
- [`modbus_add_rw_signal(IP, slave_number, read_address, read_register_count, write_address, write_register_count, signal_ name, sequential_mode=False)`](#modbus_add_rw_signal)
- [`modbus_delete_signal(signal_name)`](#modbus_delete_signal)
- [`modbus_get_signal_status(signal_name, is_secondary_ program=False)`](#modbus_get_signal_status)
- [`modbus_send_custom_command(IP, slave_number, function_code, data)`](#modbus_send_custom_command)
- [`modbus_set_digital_input_action(signal_name, action)`](#modbus_set_digital_input_action)
- [`modbus_set_output_register(signal_name, register_value, is_secondary_program=False)`](#modbus_set_output_register)
- [`modbus_set_output_signal(signal_name, digital_value, is_ secondary_program, False)`](#modbus_set_output_signal)
- [`modbus_set_signal_update_frequency(signal_name, update_frequency)`](#modbus_set_signal_update_frequency)
- [`modbus_get_error(signal_name)`](#modbus_get_error)
- [`modbus_get_time_since_signal_invalid(signal_name)`](#modbus_get_time_since_signal_invalid)
- [`modbus_request_update_signal_value(signal_name)`](#modbus_request_update_signal_value)
- [`modbus_reset_connection(connection_id, is_ blocking=True)`](#modbus_reset_connection)
- [`modbus_set_signal_watchdog(signal_name, new_timeout_ in_sec)`](#modbus_set_signal_watchdog)
- [`read_input_boolean_register(address)`](#read_input_boolean_register)
- [`read_input_float_register(address)`](#read_input_float_register)
- [`read_input_integer_register(address)`](#read_input_integer_register)
- [`read_output_boolean_register(address)`](#read_output_boolean_register)
- [`read_output_float_register(address)`](#read_output_float_register)
- [`read_output_integer_register(address)`](#read_output_integer_register)
- [`read_port_bit(address)`](#read_port_bit)
- [`read_port_register(address)`](#read_port_register)
- [`rpc_factory(type, url)`](#rpc_factory)
- [`rtde_set_watchdog(variable_name, min_frequency, action=’pause’)`](#rtde_set_watchdog)
- [`set_analog_inputrange(port, range)`](#set_analog_inputrange)
- [`set_analog_out(n, f )`](#set_analog_out)
- [`set_configurable_digital_out(n, b)`](#set_configurable_digital_out)
- [`set_digital_out(n, b)`](#set_digital_out)
- [`set_flag(n, b)`](#set_flag)
- [`set_standard_analog_out(n, f)`](#set_standard_analog_out)
- [`set_standard_digital_out(n, b)`](#set_standard_digital_out)
- [`set_tool_digital_out(n, b)`](#set_tool_digital_out)
- [`set_tool_communication(enabled, baud_rate, parity, stop_ bits, This function will activate or deactivate the ’Tool Communication Interface’ (TCI). The TCI will enable communication with a external tool via the robots analog inputs hereby avoiding external wiring. >>> set_tool_communication(True, 115200, 1, 2, 1.0, 3.5)  enabled: Boolean to enable or disable the TCI (string). Valid values: True (enable), False (disable) baud_rate: The used baud rate (int). Valid values: 9600, 19200, 38400, 57600, 115200, 1000000, 2000000, 5000000. parity: The used parity (int). Valid values: 0 (none), 1 (odd), 2 (even). stop_bits: The number of stop bits (int). Valid values: 1, 2. rx_idle_chars: Amount of chars the RX unit in the tool should wait before marking a message as over / sending it to the PC (float). Valid values: min=1.0 max=40.0. tx_idle_chars: Amount of chars the TX unit in the tool should wait before starting a new transmission since last activity on bus (float). Valid values: min=0.0 max=40.0. Return Value None Note: Enabling this feature will disable the robot tool analog inputs. Example command: set_tool_communication(True, 115200, 1, 2, 1.0, 3.5) • Example Parameters: • enabled = True • baud rate = 115200 • parity = ODD • stop bits = 2 • rx idle time = 1.0 • tx idle time = 3.5      Parameters`](#set_tool_communication)
- [`set_tool_digital_output_mode (n, mode)`](#set_tool_digital_output_mode)
- [`set_tool_output_mode (mode)`](#set_tool_output_mode)
- [`set_tool_voltage(voltage)`](#set_tool_voltage)
- [`socket_close(socket_name=’socket_0’)`](#socket_close)
- [`socket_get_var(name, socket_name=’socket_0’)`](#socket_get_var)
- [`socket_open(address, port, socket_name=’socket_0’)`](#socket_open)
- [`socket_read_ascii_float(number, socket_name=’socket_0’, timeout=2)`](#socket_read_ascii_float)
- [`socket_read_binary_integer(number, socket_ name=’socket_0’, timeout=2)`](#socket_read_binary_integer)
- [`socket_read_byte_list(number, socket_name=’socket_0’, timeout=2)`](#socket_read_byte_list)
- [`socket_read_line(socket_name=’socket_0’, timeout=2)`](#socket_read_line)
- [`socket_read_string(socket_name=’socket_0’, prefix =’’, suffix =’’, interpret_escape=’False’, timeout=2)`](#socket_read_string)
- [`socket_send_byte(value, socket_name=’socket_0’)`](#socket_send_byte)
- [`socket_send_int(value, socket_name=’socket_0’)`](#socket_send_int)
- [`socket_send_line(str, socket_name=’socket_0’)`](#socket_send_line)
- [`socket_send_string(str, socket_name=’socket_0’)`](#socket_send_string)
- [`socket_set_var(name, value, socket_name=’socket_0’)`](#socket_set_var)
- [`write_output_boolean_register(address, value)`](#write_output_boolean_register)
- [`write_output_float_register(address, value)`](#write_output_float_register)
- [`write_output_integer_register(address, value)`](#write_output_integer_register)
- [`write_port_bit(address, value)`](#write_port_bit)
- [`write_port_register(address, value)`](#write_port_register)
- [`zero_ftsensor()`](#zero_ftsensor)
- [`request_boolean_from_primary_client(message)`](#request_boolean_from_primary_client)
- [`request_float_from_primary_client(message)`](#request_float_from_primary_client)
- [`request_integer_from_primary_client(message)`](#request_integer_from_primary_client)
- [`request_string_from_primary_client(message)`](#request_string_from_primary_client)

---

## API Documentation

<a id="enable_external_ft_sensor"></a>
### `enable_external_ft_sensor(enable, sensor_mass=0.0, sensor_measuring_offset=[0.0, 0.0, 0.0], sensor_cog=[0.0, 0.0, 0.0])`
**Section**: URScript 17.1.1

**Description**:
Deprecated:
This function is used for enabling and disabling the use of external F/T measurements in the controller. Be
aware that the following function is impacted:
• force_mode
• freedrive_mode
The RTDE interface shall be used for feeding F/T measurements into the real-time control loop of the
robot using input variable external_force_torque of type VECTOR6D. If no other RTDE watchdog
has been configured (using script function rtde_set_watchdog), a default watchdog will be set to a
10Hz minimum update frequency when the external F/T sensor functionality is enabled. If the update
frequency is not met the robot program will pause.

**Parameters**:
- **`enable`**: enable or disable feature (bool)
- **`sensor_mass`**: mass of the sensor in kilograms (float)
- **`sensor_measuring_offset`**: [x, y, z] measuring offset of the sensor in meters relative to the tool flange frame
- **`sensor_cog`**: [x, y, z] center of gravity of the sensor in meters relative to the tool flange frame Deprecated When using this function, the sensor position is applied such that the resulting torques are computed with opposite sign. New programs should use ft_rtde_input_enable in place of this.
- **`Notes`**: • The TCP Configuration in the installation must also include the weight and offset contribution of the sensor. • Only the enable parameter is required, sensor mass, offset and center of gravity are optional (zero if not provided).

**Return Value**: `None`

**Example**:
Example command: Please refer to ft_rtde_input_enable for some examples of usage
• screw_driving

---

<a id="ft_rtde_input_enable"></a>
### `ft_rtde_input_enable(enable, sensor_mass=0.0, sensor_ measuring_offset=[0.0, 0.0, 0.0], sensor_cog=[0.0, 0.0, 0.0])`
**Section**: URScript 17.1.2

**Description**:
This function is used for enabling and disabling the use of external F/T measurements in the controller. Be
aware that the following function is impacted:
• force_mode
• screw_driving
• freedrive_mode
The RTDE interface shall be used for feeding F/T measurements into the real-time control loop of the
robot using input variable external_force_torque of type VECTOR6D. If no other RTDE watchdog
has been configured (using script function rtde_set_watchdog), a default watchdog will be set to a
10Hz minimum update frequency when the external F/T sensor functionality is enabled. If the update
frequency is not met the robot program will pause.

**Parameters**:
- **`enable`**: enable or disable feature (bool)
- **`sensor_mass`**: mass of the sensor in kilograms (float)
- **`sensor_measuring_offset`**: [x, y, z] measuring offset of the sensor in meters relative to the tool flange frame
- **`sensor_cog`**: [x, y, z] center of gravity of the sensor in meters relative to the tool flange frame
- **`Notes`**: This function replaces the deprecated enable_external_ft_sensor. The TCP Configuration in the installation must also include the weight and offset contribution of the sensor. Only the enable parameter is required; sensor mass, offset and center of gravity are optional (zero if not provided).

**Return Value**: `None`

**Example**:
```urscript
Example command: ft_rtde_input_enable(True, 1.0, [0.1, 0.0, 0.0], [0.2, 0.1,
0.5])
• Example Parameters:
• enable -> Enabling the feed of an external F/T measurements in the controller.
• sensor_mass -> mass of F/T sensor is set to 1.0 Kg.
• sensor_measuring_offset -> sensor measuring offset is set to [0.1, 0.0, 0.0] m from
the tool flange in tool flange frame coordinates.
• sensor_cog -> Center of Gravity of the sensor is set to x=200 mm, y=100 mm, z=500
mm from the center of the tool flange in tool flange frame coordinates.
• ft_rtde_input_enable(True, 0.5)
• Example Parameters:
• enable S{​​rarr}​​ Enabling the feed of an external F/T measurements in the
controller.
• sensor_mass S{​​rarr}​​ mass of F/T sensor is set to 0.5 Kg.
• Both sensor measuring offset and sensor's center of gravity are zero.
• @example:
• C{​​ft_rtde_input_enable(False)}​​
• Disable the feed of external F/T measurements in the controller (no other
parameters required)
```

---

<a id="get_analog_in"></a>
### `get_analog_in(n)`
**Section**: URScript 17.1.3

**Description**:
Deprecated: Get analog input signal level

**Parameters**:
- **`n`**: The number (id) of the input, integer: [0:3]

**Return Value**:
Deprecated: The get_standard_analog_in and get_tool_analog_in replace this function. Ports
2-3 should be changed to 0-1 for the latter function. This function might be removed in the next major
release.

> [!NOTE]
> Note: For backwards compatibility n:2-3 go to the tool analog inputs.

**Example**:
```urscript
Example command: get_analog_in(1)
• Example Parameters:
• n is analog input 1
• Returns value of analog output #1
```

---

<a id="get_analog_out"></a>
### `get_analog_out(n)`
**Section**: URScript 17.1.4

**Description**:
Deprecated: Get analog output signal level

**Parameters**:
- **`n`**: The number (id) of the output, integer: [0:1]

**Return Value**:
float, The signal level in Amperes, or Volts
Deprecated: The get_standard_analog_out replaces this function. This function might be removed
in the next major release.

**Example**:
```urscript
Example command: get_analog_out(1)
• Example Parameters:
• n is analog output 1
• Returns value of analog output #1
float, The signal level in Amperes, or Volts
```

---

<a id="get_configurable_digital_in"></a>
### `get_configurable_digital_in(n)`
**Section**: URScript 17.1.5

**Description**:
Get configurable digital input signal level
See also get_standard_digital_in and get_tool_digital_in.

**Parameters**:
- **`n`**: The number (id) of the input, integer: [0:7]

**Return Value**:
boolean, The signal level.

**Example**:
```urscript
Example command: get_configurable_digital_in(1)
• Example Parameters:
• n is configurable digital input 1
• Returns True or False
```

---

<a id="get_configurable_digital_out"></a>
### `get_configurable_digital_out(n)`
**Section**: URScript 17.1.6

**Description**:
Get configurable digital output signal level
See also get_standard_digital_outand get_tool_digital_out.

**Parameters**:
- **`n`**: The number (id) of the output, integer: [0:7]

**Return Value**:
boolean, The signal level.

**Example**:
```urscript
Example command: get_configurable_digital_out(1)
• Example Parameters:
• n is configurable digital output 1
• R'eturns True or False
```

---

<a id="get_digital_in"></a>
### `get_digital_in(n)`
**Section**: URScript 17.1.7

**Description**:
Deprecated: Get digital input signal level

**Parameters**:
- **`n`**: The number (id) of the input, integer: [0:9]

**Return Value**:
boolean, The signal level.
Deprecated: The get_standard_digital_in and get_tool_digital_in replace this function.
Ports 8-9 should be changed to 0-1 for the latter function. This function might be removed in the next major
release.

> [!NOTE]
> Note: For backwards compatibility n:8-9 go to the tool digital inputs.

**Example**:
```urscript
Example command: get_digital_in(1)
• Example Parameters:
• n is digital input 1
• Returns True or False
```

---

<a id="get_digital_out"></a>
### `get_digital_out(n)`
**Section**: URScript 17.1.8

**Description**:
Deprecated: Get digital output signal level

**Parameters**:
- *None / No arguments required.*

**Return Value**:
boolean, The signal level.
Deprecated: The get_standard_digital_out and get_tool_digital_out replace this function.
Ports 8-9 should be changed to 0-1 for the latter function. This function might be removed in the next major
release.

> [!NOTE]
> Note: For backwards compatibility n:8-9 go to the tool digital outputs.

**Example**:
```urscript
Example command: get_digital_out(1)
• Example Parameters:
• n is digital output 1
• Returns True or False
```

---

<a id="get_flag"></a>
### `get_flag(n)`
**Section**: URScript 17.1.9

**Description**:
Flags behave like internal digital outputs. They keep information between program runs.

**Parameters**:
- **`n`**: The number (id) of the flag, integer: [0:31]

**Return Value**:
Boolean, The stored bit.

**Example**:
```urscript
Example command: get_flag(1)
• Example Parameters:
• n is flag number 1
• Returns True or False
n: The number (id) of the output, integer: [0:9]
```

---

<a id="get_standard_analog_in"></a>
### `get_standard_analog_in(n)`
**Section**: URScript 17.1.10

**Description**:
Get standard analog input signal level
See also get_tool_analog_in.

**Parameters**:
- **`n`**: The number (id) of the input, integer: [0:1]

**Return Value**:
float, The signal level in Amperes, or Volts

**Example**:
```urscript
Example command: get_standard_analog_in(1)
• Example Parameters:
• n is standard analog input 1
• Returns value of standard analog input #1
```

---

<a id="get_standard_analog_out"></a>
### `get_standard_analog_out(n)`
**Section**: URScript 17.1.11

**Description**:
Get standard analog output signal level

**Parameters**:
- **`n`**: The number (id) of the output, integer: [0:1]

**Return Value**:
float, The signal level in Amperes, or Volts

**Example**:
```urscript
Example command: get_standard_analog_out(1)
• Example Parameters:
• n is standard analog output 1
• Returns value of standard analog output #1
```

---

<a id="get_standard_digital_in"></a>
### `get_standard_digital_in(n)`
**Section**: URScript 17.1.12

**Description**:
Get standard digital input signal level
See also get_configurable_digital_in and get_tool_digital_in.

**Parameters**:
- **`n`**: The number (id) of the input, integer: [0:7]

**Return Value**:
boolean, The signal level.

**Example**:
```urscript
Example command: get_standard_digital_in(1)
• Example Parameters:
• n is standard digital input 1
• Returns True or False
```

---

<a id="get_standard_digital_out"></a>
### `get_standard_digital_out(n)`
**Section**: URScript 17.1.13

**Description**:
Get standard digital output signal level
See also get_configurable_digital_out and get_tool_digital_out.

**Parameters**:
- **`n`**: The number (id) of the output, integer: [0:7]

**Return Value**:
boolean, The signal level.

**Example**:
```urscript
Example command: get_standard_digital_out(1)
• Example Parameters:
• n is standard digital output 1
• Returns True or False
```

---

<a id="get_tool_analog_in"></a>
### `get_tool_analog_in(n)`
**Section**: URScript 17.1.14

**Description**:
Get tool analog input signal level
See also get_standard_analog_in.

**Parameters**:
- **`n`**: The number (id) of the input, integer: [0:1]

**Return Value**:
float, The signal level in Amperes, or Volts

**Example**:
```urscript
Example command: get_tool_analog_in(1)
• Example Parameters:
• n is tool analog input 1
• Returns value of tool analog input #1
```

---

<a id="get_tool_digital_in"></a>
### `get_tool_digital_in(n)`
**Section**: URScript 17.1.15

**Description**:
Get tool digital input signal level
See also get_configurable_digital_in and get_standard_digital_in.

**Parameters**:
- **`n`**: The number (id) of the input, integer: [0:1]

**Return Value**:
boolean, The signal level.

**Example**:
```urscript
Example command: get_tool_digital_in(1)
• Example Parameters:
• n is tool digital input 1
• Returns True or False
```

---

<a id="get_tool_digital_out"></a>
### `get_tool_digital_out(n)`
**Section**: URScript 17.1.16

**Description**:
Get tool digital output signal level
See also get_standard_digital_out and get_configurable_digital_out.

**Parameters**:
- **`n`**: The number (id) of the output, integer: [0:1]

**Return Value**:
boolean, The signal level.

**Example**:
```urscript
Example command: get_tool_digital_out(1)
Example Parameters:
n is tool digital out 1
Returns True or False
```

---

<a id="modbus_add_signal"></a>
### `modbus_add_signal(IP, slave_number, signal_address, signal_type, signal_name, sequential_mode=False, register_ count=1)`
**Section**: URScript 17.1.17

**Description**:
Adds a new modbus signal for the controller to supervise. Expects no response. If the signal is an output
type, then until the first set_output_signal/register() command the function code will be 2/3, after the call it
will switch to 15/16.
Matrix of function codes used for accessing coils or discrete inputs:
Read
Write
Signal type
Single Coil Multiple
Coils
Single Coil Multiple Coils
0 = Digital input
-
-
1 = Digital output
15 = Multiple digital
outputs
Matrix of function codes used for accessing coils or discrete inputs:
Read
Write
Signal type
Single
register
Multiple
registers
Single
register
Multiple
registers
2 = Register input
-
-
3 = Register output
16 = Multiple register
outputs

**Parameters**:
- *None / No arguments required.*

**Return Value**: `None`

> [!NOTE]
> Note: Numerical IP addresses are recommended. DNS name resolution may lead to unexpected program
> stops.
> slave_number: An integer normally not used and set to 255, but is a free choice between 0 and 255.
> signal_address: An integer specifying the address of the either the coil or the register that this new
> signal should reflect. Consult the configuration of the modbus unit for this information. The value must be
> greater or equal to 0.
> signal_type: An integer specifying the type of signal to add. 0 = digital input, 1 = digital output, 2 =
> register input, 3 = register output, 15 = multiple digital output, 16 = multiple register output. Note: this
> function does not accept 23 = multiple read-write signal type.
> signal_name: A string uniquely identifying the signal. If a string is supplied which is equal to an already
> added signal, the new signal will replace the old one. The length of the string can not exceed 20
> characters. The signal name cannot be empty.
> sequential_mode: Setting to True forces the modbus client to wait for a response before sending the
> next request. This mode is required by some fieldbus units (Optional).
> register_count: Number of registers/coils accessed by the signal [1-123] (Optional, the default value
> is 1).
> Example command 1: modbus_add_signal("172.140.17.11", 255, 5, 1, "output1")
> • Example Parameters:
> • IP address = 172.140.17.11
> • Slave number = 255
> • Signal address = 5
> • Signal type = 1 digital output
> • Signal name = output 1
> Example command 2: modbus_add_signal("172.140.17.11", 255, 5, 16, "output2",
> False, 10)
> IP: A string specifying the IP address of the modbus unit to which the modbus signal is connected. The
> IP can not be empty.
> • Example Parameters:
> • IP address = 172.140.17.11
> • Slave number = 255
> • Signal address = 5
> • Signal type = 16 multiple register output
> • Signal name = output 2
> • sequential_mode = False
> • register_count = 10

**Example**:
```urscript
modbus_add_signal("172.140.17.11", 255, 5, 1, "output1")
```

---

<a id="modbus_add_rw_signal"></a>
### `modbus_add_rw_signal(IP, slave_number, read_address, read_register_count, write_address, write_register_count, signal_ name, sequential_mode=False)`
**Section**: URScript 17.1.18

**Description**:
Adds a new modbus signal for the controller to supervise. This function will use the function code 23. The
read and write addresses can overlap. Until the first set_output_register() command the function code will
be 3, after the call it will switch to 23.

**Parameters**:
- **`IP`**: A string specifying the IP address of the modbus unit to which the modbus signal is connected. The IP can not be empty.
- **`slave_number`**: An integer normally not used and set to 255, but is a free choice between 0 and 255.
- **`read_address`**: An integer specifying the address of the first register that this new signal should read from.
- **`read_register_count`**: Number of registers to read [1-123].
- **`write_address`**: An integer specifying the address of the first register that this new signal should write to.
- **`write_register_count`**: Number of registers to write [1-123].
- **`signal_name`**: A string uniquely identifying the signal. If a string is supplied which is equal to an already added signal, the new signal will replace the old one. The length of the string can not exceed 20 characters. The signal name cannot be empty.
- **`sequential_mode`**: Setting to True forces the modbus client to wait for a response before sending the next request. This mode is required by some fieldbus units (Optional).

**Return Value**: `None`

**Example**:
```urscript
modbus_add_rw_signal("172.140.17.11", 255, 5, 10, 15, 10, "output1")
Example command: modbus_add_rw_signal("172.140.17.11", 255, 5, 10, 15, 10
"output1")
This example will create a signal that cyclically reads 10 registers from addresses 5-14, an writes 10
registers to addresses 10-19 Signal will use Function Code 3 to read register until first time modbus_set_
register_output(...) is called. Afterwards Function Code 23 will be used to both read and write registers in
remote device.
• Example Parameters:
• IP address = 172.140.17.11
• Slave number = 255
• Signal read address = 5
• Signal read register count = 10
• Signal write address = 15
• Signal write register count = 10
• Signal name = output 1
```

---

<a id="modbus_delete_signal"></a>
### `modbus_delete_signal(signal_name)`
**Section**: URScript 17.1.19

**Description**: *Executes built-in URScript operation.*

**Parameters**:
- **`signal_name`**: A string equal to the name of the signal that should be deleted. The signal name can not be empty.

**Return Value**: `None`

**Example**:
```urscript
modbus_delete_signal("output1")
Example command: modbus_delete_signal("output1")
• Example Parameters:
• Signal name = output1
```

---

<a id="modbus_get_signal_status"></a>
### `modbus_get_signal_status(signal_name, is_secondary_ program=False)`
**Section**: URScript 17.1.20

**Description**:
Reads the current value(s) of a specific signal. If the modbus watchdog is active, this will return the last
valid value(s). No error will be thrown within the watchdog time. If needed, the modus_get_error() or the
modbus_get_time_since_signal_invalid() can be used to detected that the signal is in an error state before
the watchdog expires.

**Parameters**:
- **`signal_name`**: A string equal to the name of the signal for which the value should be gotten. Can not be empty.
- **`is_secondary_program`**: A boolean for internal use only. Must be set to False. (Optional, default is False)

**Return Value**:
An integer or a boolean. For digital signals: True or False. For register signals: The register value
expressed as an unsigned integer. If the signal was declared to have access for multiple registers/coild,
then the return value will be an array of unsigned integers / booleans. The length of the returned array is
equal to the register_count of the signal.
Deletes the signal identified by the supplied signal name.

**Example**:
```urscript
modbus_get_signal_status("output1",False)
Example command: modbus_get_signal_status("output1")
Example Parameters:
• Signal name = output 1
• Is_secondary_program = False by default
```

---

<a id="modbus_send_custom_command"></a>
### `modbus_send_custom_command(IP, slave_number, function_code, data)`
**Section**: URScript 17.1.21

**Description**:
Sends a command specified by the user to the modbus unit located on the specified IP address. Cannot
be used to request data, since the response will not be received. The user is responsible for supplying
data which is meaningful to the supplied function code. The builtin function takes care of constructing the
modbus frame, so the user should not be concerned with the length of the command.

**Parameters**:
- **`IP`**: A string specifying the IP address locating the modbus unit to which the custom command should be send. Can not be empty.
- **`slave_number`**: An integer specifying the slave number to use for the custom command. Must be between [0-255].
- **`function_code`**: An integer specifying the function code for the custom command.
- **`data`**: An array of integers in which each entry must be a valid byte (0-255) value.

**Return Value**: `None`

**Example**:
```urscript
modbus_send_custom_command("172.140.17.11",103,6,

[17,32,2,88])
The above example sets the watchdog timeout on a Beckhoff BK9050 to 600 ms. That is done using the
modbus function code 6 (preset single register) and then supplying the register address in the first two
bytes of the data array ([17,32] = [0x1120]) and the desired register content in the last two bytes ([2,88] =
[0x0258] = dec 600).
Example command: modbus_send_custom_command("172.140.17.11", 103, 6,
[17,32,2,88])
• Example Parameters:
• IP address = 172.140.17.11
• Slave number = 103
• Function code = 6
• Data = [17,32,2,88]
• Function code and data are specified by the manufacturer of the slave Modbus device
connected to the UR controller
```

---

<a id="modbus_set_digital_input_action"></a>
### `modbus_set_digital_input_action(signal_name, action)`
**Section**: URScript 17.1.22

**Description**:
Sets the selected digital input signal to either a "default" or "freedrive" action.

**Parameters**:
- **`signal_name`**: A string identifying a digital input signal that was previously added. Can not be empty.
- **`action`**: The type of action. The action can either be "default" or "freedrive". Can not be empty. (string)

**Return Value**: `None`

**Example**:
```urscript
modbus_set_digital_input_action("input1", "freedrive")
Example command: modbus_set_digital_input_action("input1", "freedrive")
• Example Parameters:
• Signal name = "input1"
```

---

<a id="modbus_set_output_register"></a>
### `modbus_set_output_register(signal_name, register_value, is_secondary_program=False)`
**Section**: URScript 17.1.23

**Description**:
Sets the output register(s) signal identified by the given name to the given value.

**Parameters**:
- **`signal_name`**: A string identifying an output register signal that in advance has been added. Can not be empty.
- **`register_value`**: An integer which must be a valid word (0-65535) value or a list of integer values. The list can not be empty. The size of the list must be less than 123 and must be equal or less to the signal's declared register count. Note: if a shorter list is given as an input, then registers with greater indexes will keep previous value
- **`is_secondary_program`**: A boolean for internal use only. Must be set to False. (Optional, false by default) Example command 1: modbus_set_output_register("output1", 300, False) • Example Parameters: • Signal name = output1 • Register value = 300 • Is_secondary_program = False (Note: must be set to False) Example command 2: modbus_add_signal("127.0.0.1", 255, 0, 16, "output2", False, 10)
- **`list_var`**: =[10,9,8,7,6,5,4,3,2,1] modbus_set_output_register("output2", list_var) • Action = "freedrive" • Example Parameters: • Signal name = output2 • Register values = 10,9,8,7,6,5,4,3,2,1 • Is_secondary_program = False by default

**Return Value**: `None`

**Example**:
```urscript
modbus_set_output_register("output1",300,False)
```

---

<a id="modbus_set_output_signal"></a>
### `modbus_set_output_signal(signal_name, digital_value, is_ secondary_program, False)`
**Section**: URScript 17.1.24

**Description**:
Sets the output digital signal(s) identified by the given name to the given value.

**Parameters**:
- **`signal_name`**: A string identifying an output digital signal that in advance has been added. Can not be empty.
- **`digital_value`**: A boolean to which value the signal will be set or a list of boolean values. The list can not be empty. The size of the list must be less than 123 and must be equal or less to the signal's declared register count. Note: if a shorter list is given as an input, then coils with greater indexes will keep previous value
- **`is_secondary_program`**: A boolean for internal use only. Must be set to False. Example command 1: modbus_set_output_signal("output1", True, False) • Example Parameters: • Signal name = output1 • Digital value = True • Is_secondary_program = False (Note: must be set to False) Example command 2: modbus_add_signal("127.0.0.1", 255, 0, 15, "output2", False, 5)
- **`list_var`**: =[True, False, True, False, True] modbus_set_output_signal("output2", list_var) • Example Parameters: • Signal name = output2 • Digital values = True, False, True, False, True • Is_secondary_program = False by default.

**Return Value**: `None`

**Example**:
```urscript
modbus_set_output_signal("output2",True,False)
```

---

<a id="modbus_set_signal_update_frequency"></a>
### `modbus_set_signal_update_frequency(signal_name, update_frequency)`
**Section**: URScript 17.1.25

**Description**:
Sets the frequency with which the robot will send requests to the Modbus controller to either read or write
the signal value.

**Parameters**:
- **`signal_name`**: A string identifying an output digital signal that in advance has been added. Can not be empty.
- **`update_frequency`**: An integer in the range 0-500 specifying the update frequency in Hz.

**Return Value**: `None`

> [!NOTE]
> Note: The function accepts -1 and 0 as a valid input as a special value to create acyclic signals.
> Note: If the input is 0 the signal will be acyclic.

**Example**:
```urscript
modbus_set_signal_update_frequency("output2",20)
Example command: modbus_set_signal_update_frequency("output2", 20)
• Example Parameters:
• Signal name = output2
• Signal update frequency = 20 Hz
```

---

<a id="modbus_get_error"></a>
### `modbus_get_error(signal_name)`
**Section**: URScript 17.1.26

**Description**:
Returns the current error state of the signal.

**Parameters**:
- **`signal_name`**: A string equal to the name of the signal. The signal name can not be empty.
- **`error_source`**: Selects the type of the returned error. Integer, 0 = combined, 1 = device error, 2 = connection error (Optional, default is 0 = combined)

**Return Value**:
32 bit integer
0 = No error, Device errors
1 = Device error - illegal function code
2 = Device error - illegal data access
3 = Device error - illegal data value
4 = Device error - server failure
5 = Device error - acknowledge exception
6 = Device error - server busy
10 = Device error - gateway problem
11 = Device error - gateway target failure
Connection errors
Values from 1-113, see details in https://en.wikipedia.org/wiki/Errno.h and
https://www.ibm.com/docs/en/db2/11.5?topic=message-tcpip-errors
NOTICE
If combined errors are requested, then the returned value's upper 2 bytes will store the
connection error, the lower 2 bytes will store the device errors. Example returned value:
0xFFFE0004 (dec:-131068) -> upper 0xFFFE = -2 Disconnected ; lower 0x0004 =
Device error - server failure

**Example**:
```urscript
modbus_get_error("output1")
Example command: modbus_get_error("output1")
• Example Parameters:
• Signal name = output1
```

---

<a id="modbus_get_time_since_signal_invalid"></a>
### `modbus_get_time_since_signal_invalid(signal_name)`
**Section**: URScript 17.1.27

**Description**:
Returns the time in seconds since the signal is invalid (has communication or device error).For input
signals function tells how long ago was last time when signal value was successfully read from remote
device. For output signals function tells how long ago was last time when signal value was successfully
written to remote device.

**Parameters**:
- **`signal_name`**: A string equal to the name of the signal. The signal name can not be empty.

**Return Value**:
A float number representing the time in seconds since the signal is in a communication or device error.

**Example**:
```urscript
modbus_get_time_since_signal_invalid("output1")
Example command: modbus_get_time_since_signal_invalid("output1")
• Example Parameters:
• Signal name = output1
```

---

<a id="modbus_request_update_signal_value"></a>
### `modbus_request_update_signal_value(signal_name)`
**Section**: URScript 17.1.28

**Description**:
Request an update of the signal regardless of the used frequency.

**Parameters**:
- **`signal_name`**: A string equal to the name of the signal. The signal name can not be empty.

**Return Value**: `None`

**Example**:
```urscript
modbus_request_update_signal_value("output1")
Example command: modbus_request_update_signal_value("output1")
• Example Parameters:
• Signal name = output1
```

---

<a id="modbus_reset_connection"></a>
### `modbus_reset_connection(connection_id, is_ blocking=True)`
**Section**: URScript 17.1.29

**Description**:
Tear down, and reconnect all signals to remote device. By default it will block as long as there are errors in
the connection.

**Parameters**:
- **`connection_id`**: A string specifying the IP address of the modbus unit to which the modbus signal is connected. The IP can not be empty.

**Return Value**: `None`

**Example**:
```urscript
modbus_reset_connection("172.140.17.11")
Example command: modbus_reset_connection("172.140.17.11")
Example Parameters:
• connection_id = 172.140.17.11
```

---

<a id="modbus_set_signal_watchdog"></a>
### `modbus_set_signal_watchdog(signal_name, new_timeout_ in_sec)`
**Section**: URScript 17.1.30

**Description**:
Set tolerance for modbus errors (both communication, and device exceptions) as minimum time between
valid device responses. No error will be thrown within the watchdog time. If needed, the modus_get_error
() or the modbus_get_time_since_signal_invalid() can be used to detected that the signal is in an error
state before the watchdog expires.Default signal timeout is 2 seconds.

**Parameters**:
- **`signal_name`**: A string identifying an output digital signal that in advance has been added. Can not be empty.
- **`new_timeout_in_sec`**: A number in range 0-300 representing seconds.

**Return Value**: `None`

**Example**:
```urscript
modbus_set_signal_watchdog("signal1", 5)
Example command: modbus_set_signal_watchdog("signal1", 10.5)
Example Parameters:
• signal_name = signal1
• new_timeout_in_sec = 10.5 seconds
```

---

<a id="read_input_boolean_register"></a>
### `read_input_boolean_register(address)`
**Section**: URScript 17.1.31

**Description**:
Reads the boolean from one of the input registers, which can also be accessed by a Field bus. Note, uses
it’s own memory space.

**Parameters**:
- **`address`**: Address of the register (0:127)

**Return Value**:
• is_blocking = True
The boolean value held by the register (True, False)

> [!NOTE]
> Note: The lower range of the boolean input registers [0:63] is reserved for FieldBus/PLC interface usage.
> The upper range [64:127] cannot be accessed by FieldBus/PLC interfaces, since it is reserved for external
> RTDE clients.

**Example**:
```urscript
bool_val = read_input_boolean_register(3)
Example command: read_input_boolean_register(3)
• Example Parameters:
• Address = input boolean register 3
```

---

<a id="read_input_float_register"></a>
### `read_input_float_register(address)`
**Section**: URScript 17.1.32

**Description**:
Reads the float from one of the input registers, which can also be accessed by a Field bus. Note, uses it’s
own memory space.

**Parameters**:
- **`address`**: Address of the register (0:47)

**Return Value**:
The value held by the register (float)

> [!NOTE]
> Note: The lower range of the float input registers [0:23] is reserved for FieldBus/PLC interface usage. The
> upper range [24:47] cannot be accessed by FieldBus/PLC interfaces, since it is reserved for external
> RTDE clients.

**Example**:
```urscript
float_val = read_input_float_register(3)
Example command: read_input_float_register(3)
• Example Parameters:
• Address = input float register 3
```

---

<a id="read_input_integer_register"></a>
### `read_input_integer_register(address)`
**Section**: URScript 17.1.33

**Description**:
Reads the integer from one of the input registers, which can also be accessed by a Field bus. Note, uses
it’s own memory space.

**Parameters**:
- **`address`**: Address of the register (0:47)

**Return Value**:
The value held by the register [-2,147,483,648 : 2,147,483,647]

> [!NOTE]
> Note: The lower range of the integer input registers [0:23] is reserved for FieldBus/PLC interface usage.
> The upper range [24:47] cannot be accessed by FieldBus/PLC interfaces, since it is reserved for external
> RTDE clients.

**Example**:
```urscript
int_val = read_input_integer_register(3)
Example command: read_input_integer_register(3)
• Example Parameters:
• Address = input integer register 3
```

---

<a id="read_output_boolean_register"></a>
### `read_output_boolean_register(address)`
**Section**: URScript 17.1.34

**Description**:
Reads the boolean from one of the output registers, which can also be accessed by a Field bus. Note,
uses it’s own memory space.

**Parameters**:
- **`address`**: Address of the register (0:127)

**Return Value**: `None`

> [!NOTE]
> Note: The lower range of the boolean output registers [0:63] is reserved for FieldBus/PLC interface usage.
> The upper range [64:127] cannot be accessed by FieldBus/PLC interfaces, since it is reserved for external
> RTDE clients.

**Example**:
```urscript
bool_val = read_output_boolean_register(3)
Example command: read_output_boolean_register(3)
• Example Parameters:
• Address = output boolean register 3
```

---

<a id="read_output_float_register"></a>
### `read_output_float_register(address)`
**Section**: URScript 17.1.35

**Description**:
Reads the float from one of the output registers, which can also be accessed by a Field bus. Note, uses it’s
own memory space.

**Parameters**:
- **`address`**: Address of the register (0:47)

**Return Value**:
The value held by the register (float)

> [!NOTE]
> Note: The lower range of the float output registers [0:23] is reserved for FieldBus/PLC interface usage.
> The upper range [24:47] cannot be accessed by FieldBus/PLC interfaces, since it is reserved for external
> RTDE clients.

**Example**:
```urscript
float_val = read_output_float_register(3)
Example command: read_output_float_register(3)
• Example Parameters:
• Address = output float register 3
The boolean value held by the register (True, False)
```

---

<a id="read_output_integer_register"></a>
### `read_output_integer_register(address)`
**Section**: URScript 17.1.36

**Description**:
Reads the integer from one of the output registers, which can also be accessed by a Field bus. Note, uses
it’s own memory space.

**Parameters**:
- **`address`**: Address of the register (0:47)

**Return Value**:
The int value held by the register [-2,147,483,648 : 2,147,483,647]

> [!NOTE]
> Note: The lower range of the integer output registers [0:23] is reserved for FieldBus/PLC interface usage.
> The upper range [24:47] cannot be accessed by FieldBus/PLC interfaces, since it is reserved for external
> RTDE clients.

**Example**:
```urscript
int_val = read_output_integer_register(3)
Example command: read_output_integer_register(3)
• Example Parameters:
• Address = output integer register 3
```

---

<a id="read_port_bit"></a>
### `read_port_bit(address)`
**Section**: URScript 17.1.37

**Description**:
Reads one of the ports, which can also be accessed by Modbus clients

**Parameters**:
- **`address`**: Address of the port (See port map on Support site, page "Modbus Server" )

**Return Value**:
The value held by the port (True, False)

**Example**:
```urscript
boolval = read_port_bit(3)
Example command: read_port_bit(3)
• Example Parameters:
• Address = port bit 3
```

---

<a id="read_port_register"></a>
### `read_port_register(address)`
**Section**: URScript 17.1.38

**Description**:
Reads one of the ports, which can also be accessed by Modbus clients

**Parameters**:
- **`address`**: Address of the port (See port map on Support site, page "Modbus Server" )

**Return Value**:
The signed integer value held by the port (-32768 : 32767)

**Example**:
```urscript
intval = read_port_register(3)
Example command: read_port_register(3)
Example Parameters:
Address = port register 3
```

---

<a id="rpc_factory"></a>
### `rpc_factory(type, url)`
**Section**: URScript 17.1.39

**Description**:
Creates a new Remote Procedure Call (RPC) handle. Please read the subsection ef{Remote Procedure
Call (RPC)} for a more detailed description of RPCs.

**Parameters**:
- **`url`**: The URL to the RPC server. Currently two protocols are supported: pstream and http. The pstream URL looks like "<ip-address>:<port>", for instance "127.0.0.1:8080" to make a local connection on port 8080. A http URL generally looks like "http://<ip-address>:<port>/<path>", whereby the <path> depends on the setup of the http server. In the example given above a connection to a local Python webserver on port 8080 is made, which expects XMLRPC calls to come in on the path "RPC2".

**Return Value**:
A RPC handle with a connection to the specified server using the designated RPC backend. If the server is
not available the function and program will fail. Any function that is made available on the server can be
called using this instance. For example "bool isTargetAvailable(int number, ...)" would be
"proxy.isTargetAvailable(var_1, ...)", whereby any number of arguments are supported (denoted by the
...).

> [!NOTE]
> Note: Giving the RPC instance a good name makes programs much more readable (i.e. "proxy" is not a
> very good name).

**Example**:
```urscript

proxy
=
rpc_factory("xmlrpc",
"http://127.0.0.1:8080/RPC2")
Example command: rpc_factory("xmlrpc", "http://127.0.0.1:8080/RPC2")
• Example Parameters:
• type = xmlrpc
• url = http://127.0.0.1:8080/RPC2
```

---

<a id="rtde_set_watchdog"></a>
### `rtde_set_watchdog(variable_name, min_frequency, action=’pause’)`
**Section**: URScript 17.1.40

**Description**:
This function will activate a watchdog for a particular input variable to the RTDE. When the watchdog did
not receive an input update for the specified variable in the time period specified by min_frequency (Hz),
the corresponding action will be taken. All watchdogs are removed on program stop.

**Parameters**:
- **`variable_name`**: Input variable name (string), as specified by the RTDE interface
- **`min_frequency`**: The minimum frequency (float) an input update is expected to arrive.
- **`type`**: The type of RPC backed to use. Currently only the "xmlrpc" protocol is available.
- **`action`**: Optional: Either "ignore", "pause" or "stop" the program on a violation of the minimum frequency. The default action is "pause".

**Return Value**:
None

> [!NOTE]
> Note: Only one watchdog is necessary per RTDE input package to guarantee the specified action on
> missing updates.

**Example**:
```urscript
rtde_set_watchdog("input_int_register_0", 10, "stop")
Example command: rtde set watchdog( "input int register 0" , 10, "stop" )
• Example Parameters:
• variable name = input int register 0
• min frequency = 10 hz
• action = stop the program
```

---

<a id="set_analog_inputrange"></a>
### `set_analog_inputrange(port, range)`
**Section**: URScript 17.1.41

**Description**:
Deprecated: Set range of analog inputs
Port 0 and 1 is in the controller box, 2 and 3 is in the tool connector.

**Parameters**:
- **`port`**: analog input port number, 0,1 = controller, 2,3 = tool
- **`range`**: Controller analog input range 0: 0-5V (maps automatically onto range 2) and range 2: 0-10V.
- **`range`**: Tool analog input range 0: 0-5V (maps automatically onto range 1), 1: 0-10V and 2: 4-20mA.
- **`Deprecated`**: The set_standard_analog_input_domain and set_tool_analog_input_domain replace this function. Ports 2-3 should be changed to 0-1 for the latter function. This function might be removed in the next major release.

**Return Value**: `None`

> [!NOTE]
> Note: For Controller inputs ranges 1: -5-5V and 3: -10-10V are no longer supported and will show an
> exception in the GUI.

---

<a id="set_analog_out"></a>
### `set_analog_out(n, f )`
**Section**: URScript 17.1.42

**Description**:
Deprecated: Set analog output signal level

**Parameters**:
- **`n`**: The number (id) of the output, integer: [0:1]
- **`f`**: The relative signal level [0;1] (float)
- **`Deprecated`**: The set_standard_analog_out replaces this function. This function might be removed in the next major release.

**Return Value**: `None`

**Example**:
```urscript
Example command: set_analog_out(1,0.5)
• Example Parameters:
• n is standard analog output port 1
• f = 0.5, that corresponds to 5V (or 12mA depending on domain setting) on the output port
```

---

<a id="set_configurable_digital_out"></a>
### `set_configurable_digital_out(n, b)`
**Section**: URScript 17.1.43

**Description**:
Set configurable digital output signal level
See also set_standard_digital_out and set_tool_digital_out.

**Parameters**:
- **`n`**: The number (id) of the output, integer: [0:7]

**Return Value**: `None`

**Example**:
```urscript
Example command: set_configurable_digital_out(1,True)
• Example Parameters:
• n is configurable digital output 1
• b = True
```

---

<a id="set_digital_out"></a>
### `set_digital_out(n, b)`
**Section**: URScript 17.1.44

**Description**:
Deprecated: Set digital output signal level

**Parameters**:
- **`n`**: The number (id) of the output, integer: [0:9]
- **`b`**: The signal level. (boolean)
- **`Deprecated`**: The set_standard_digital_out and set_tool_digital_out replace this function. Ports 8-9 should be changed to 0-1 for the latter function. This function might be removed in the next major release.

**Return Value**: `None`

**Example**:
```urscript
Example command: set_digital_out(1,True)
• Example Parameters:
• n is digital output 1
• b = True
```

---

<a id="set_flag"></a>
### `set_flag(n, b)`
**Section**: URScript 17.1.45

**Description**:
Flags behave like internal digital outputs. They keep information between program runs.

**Parameters**:
- **`n`**: The number (id) of the flag, integer: [0:31]
- **`b`**: The stored bit. (boolean)
- **`b`**: The signal level. (boolean)

**Return Value**: `None`

**Example**:
```urscript
Example command: set_flag(1,True)
• Example Parameters:
• n is flag number 1
• b = True will set the bit to True
```

---

<a id="set_standard_analog_out"></a>
### `set_standard_analog_out(n, f)`
**Section**: URScript 17.1.46

**Description**:
Set standard analog output signal level

**Parameters**:
- **`n`**: The number (id) of the output, integer: [0:1]
- **`f`**: The relative signal level [0;1] (float)

**Return Value**: `None`

**Example**:
```urscript
Example command: set_standard_analog_out(1,1.0)
• Example Parameters:
• n is standard analog output port 1
• f = 1.0, that corresponds to 10V (or 20mA depending on domain setting) on the output port
```

---

<a id="set_standard_digital_out"></a>
### `set_standard_digital_out(n, b)`
**Section**: URScript 17.1.47

**Description**:
Set standard digital output signal level
See also set_configurable_digital_out and set_tool_digital_out.

**Parameters**:
- **`n`**: The number (id) of the output, integer: [0:7]
- **`b`**: The signal level. (boolean)

**Return Value**: `None`

**Example**:
```urscript
Example command: set_standard_digital_out(1,True)
• Example Parameters:
• n is standard digital output 1
• f = True
```

---

<a id="set_tool_digital_out"></a>
### `set_tool_digital_out(n, b)`
**Section**: URScript 17.1.48

**Description**:
Set tool digital output signal level
See also set_configurable_digital_out and set_standard_digital_out.

**Parameters**:
- **`n`**: The number (id) of the output, integer: [0:1]
- **`b`**: The signal level. (boolean)

**Return Value**: `None`

**Example**:
```urscript
Example command: set_tool_digital_out(1,True)
• Example Parameters:
• n is tool digital output 1
• b = True
```

---

<a id="set_tool_communication"></a>
### `set_tool_communication(enabled, baud_rate, parity, stop_ bits, This function will activate or deactivate the ’Tool Communication Interface’ (TCI). The TCI will enable communication with a external tool via the robots analog inputs hereby avoiding external wiring. >>> set_tool_communication(True, 115200, 1, 2, 1.0, 3.5)  enabled: Boolean to enable or disable the TCI (string). Valid values: True (enable), False (disable) baud_rate: The used baud rate (int). Valid values: 9600, 19200, 38400, 57600, 115200, 1000000, 2000000, 5000000. parity: The used parity (int). Valid values: 0 (none), 1 (odd), 2 (even). stop_bits: The number of stop bits (int). Valid values: 1, 2. rx_idle_chars: Amount of chars the RX unit in the tool should wait before marking a message as over / sending it to the PC (float). Valid values: min=1.0 max=40.0. tx_idle_chars: Amount of chars the TX unit in the tool should wait before starting a new transmission since last activity on bus (float). Valid values: min=0.0 max=40.0. Return Value None Note: Enabling this feature will disable the robot tool analog inputs. Example command: set_tool_communication(True, 115200, 1, 2, 1.0, 3.5) • Example Parameters: • enabled = True • baud rate = 115200 • parity = ODD • stop bits = 2 • rx idle time = 1.0 • tx idle time = 3.5      Parameters`
**Section**: URScript 17.1.49

**Description**: *Executes built-in URScript operation.*

**Parameters**:
- *None / No arguments required.*

**Return Value**: `None`

---

<a id="set_tool_digital_output_mode"></a>
### `set_tool_digital_output_mode (n, mode)`
**Section**: URScript 17.1.50

**Description**:
Sets the output mode of the tool output pin.

**Parameters**:
- **`n`**: The number (id) of the output, integer: [0:1]
- **`Mode`**: The pin mode.
- **`Integer`**: [1:3] • 1=Sinking/NPN • 2=Sourcing/PNP • 3=Push-Pull

**Return Value**: `None`

**Example**:
```urscript
Example command: set_tool_digital_output_mode(0,2)
• Example Parameters:
• 0 is digital output pin 0.
• 2 is pin mode sourcing/PNP.
The pin sources current when it is set to 1.
The pin is high impedance when it is set to 0.
```

---

<a id="set_tool_output_mode"></a>
### `set_tool_output_mode (mode)`
**Section**: URScript 17.1.51

**Description**:
Sets the tool digital output mode.

**Parameters**:
- **`Mode`**: 1=power (dual pin) mode.

**Return Value**: `None`

**Example**:
```urscript
Example command: set_tool_output_mode(1)
• Example Parameters:
• 1 is the power (dual pin) mode.
The digital outputs are used as extra supply
```

---

<a id="set_tool_voltage"></a>
### `set_tool_voltage(voltage)`
**Section**: URScript 17.1.52

**Description**:
Sets the voltage level for the power supply that delivers power to the connector plug in the tool flange of
the robot. The votage can be 0, 12 or 24 volts.

**Parameters**:
- **`voltage`**: The voltage (as an integer) at the tool connector, integer: 0, 12 or 24.

**Return Value**: `None`

**Example**:
```urscript
Example command: set_tool_voltage(24)
• Example Parameters:
• voltage = 24 volts
```

---

<a id="socket_close"></a>
### `socket_close(socket_name=’socket_0’)`
**Section**: URScript 17.1.53

**Description**:
Closes TCP/IP socket communication
Closes down the socket connection to the server.

**Parameters**:
- **`socket_name`**: Name of socket (string)

**Return Value**: `None`

**Example**:
```urscript
socket_comm_close()
Example command: socket_close(socket_name="socket_0")
• Example Parameters:
```

---

<a id="socket_get_var"></a>
### `socket_get_var(name, socket_name=’socket_0’)`
**Section**: URScript 17.1.54

**Description**:
Reads an integer from the server
Sends the message "GET <name>\n" through the socket, expects the response "<name> <int>\n" within 2
seconds. Returns 0 after timeout

**Parameters**:
- **`name`**: Variable name (string)
- **`socket_name`**: Name of socket (string)

**Return Value**:
an integer from the server (int), 0 is the timeout value

**Example**:
```urscript
Example command: x_pos = socket_get_var("POS_X")
Sends: GET POS_X\n to socket_0, and expects response within 2s
• Example Parameters:
• name = POS_X -> name of variable
• socket_name = default: socket_0
```

---

<a id="socket_open"></a>
### `socket_open(address, port, socket_name=’socket_0’)`
**Section**: URScript 17.1.55

**Description**:
Open TCP/IP ethernet communication socket
Attempts to open a socket connection, times out after 2 seconds.

**Parameters**:
- **`address`**: Server address (string)
- **`port`**: Port number (int)
- **`socket_name`**: Name of socket (string)

**Return Value**:
• socket_name = socket_0
False if failed, True if connection succesfully established

> [!NOTE]
> Note: The used network setup influences the performance of client/server communication. For instance,
> TCP/IP communication is buffered by the underlying network interfaces.
> • Example command: socket_open("192.168.5.1", 50000, "socket_10")
> • Example Parameters:
> • address = 192.168.5.1
> • port = 50000
> • socket_name = socket_10

---

<a id="socket_read_ascii_float"></a>
### `socket_read_ascii_float(number, socket_name=’socket_0’, timeout=2)`
**Section**: URScript 17.1.56

**Description**:
Reads a number of ascii formatted floats from the socket. A maximum of 30 values can be read in one
command.
The format of the numbers should be in parantheses, and seperated by ",". An example list of four
numbers could look like "( 1.414 , 3.14159, 1.616, 0.0 )".
The returned list contains the total numbers read, and then each number in succession. For example a
read_ascii_float on the example above would return [4, 1.414, 3.14159, 1.616, 0.0].
A failed read or timeout will return the list with 0 as first element and then "Not a number (nan)" in the
following elements (ex. [0, nan, nan, nan] for a read of three numbers).

**Parameters**:
- **`number`**: The number of variables to read (int)
- **`socket_name`**: Name of socket (string)
- **`timeout`**: The number of seconds until the read action times out (float). A timeout of 0 or negative number indicates that the function should not return until a read is completed.

**Return Value**:
A list of numbers read (length=number+1, list of floats)
• Example command: list_of_four_floats = socket_read_ascii_float(4,"socket_
10")
• Example Parameters:
• number = 4 → Number of floats to read
• socket_name = socket_10
• returns list

---

<a id="socket_read_binary_integer"></a>
### `socket_read_binary_integer(number, socket_ name=’socket_0’, timeout=2)`
**Section**: URScript 17.1.57

**Description**:
Reads a number of 32 bit integers from the socket. Bytes are in network byte order. A maximum of 30
values can be read in one command.
Returns (for example) [3,100,2000,30000], if there is a timeout or the reply is invalid, [0,-1,-1,-1] is
returned, indicating that 0 integers have been read

**Parameters**:
- **`number`**: The number of variables to read (int)
- **`socket_name`**: Name of socket (string)
- **`timeout`**: The number of seconds until the read action times out (float). A timeout of 0 or negative number indicates that the function should not return until a read is completed. A list of numbers read (length=number+1, list of ints)

**Return Value**: `None`

**Example**:
```urscript
Example command: list_of_ints = socket_read_binary_integer(4,"socket_10")
• Example Parameters:
• number = 4 -> Number of integers to read
• socket_name = socket_10
```

---

<a id="socket_read_byte_list"></a>
### `socket_read_byte_list(number, socket_name=’socket_0’, timeout=2)`
**Section**: URScript 17.1.58

**Description**:
Reads a number of bytes from the socket. A maximum of 30 values can be read in one command.
Returns (for example) [3,100,200,44], if there is a timeout or the reply is invalid, [0,-1,-1,-1] is returned,
indicating that 0 bytes have been read

**Parameters**:
- **`number`**: The number of bytes to read (int)
- **`socket_name`**: Name of socket (string)
- **`timeout`**: The number of seconds until the read action times out (float). A timeout of 0 or negative number indicates that the function should not return until a read is completed.

**Return Value**:
A list of numbers read (length=number+1, list of ints)

**Example**:
```urscript
Example command: list_of_bytes = socket_read_byte_list(4,"socket_10")
• Example Parameters:
• number = 4 -> Number of byte variables to read
• socket_name = socket_10
```

---

<a id="socket_read_line"></a>
### `socket_read_line(socket_name=’socket_0’, timeout=2)`
**Section**: URScript 17.1.59

**Description**:
Deprecated: Reads the socket buffer until the first "\r\n" (carriage return and newline) characters or just the
"\n" (newline) character, and returns the data as a string. The returned string will not contain the "\n" nor
the "\r\n" characters.
Returns (for example) "reply from the server:", if there is a timeout or the reply is invalid, an empty line is
returned (""). You can test if the line is empty with an if-statement.

**Parameters**:
- **`socket_name`**: Name of socket (string)
- **`timeout`**: The number of seconds until the read action times out (float). A timeout of 0 or negative number indicates that the function should not return until a read is completed.

**Return Value**:
One line string
Deprecated: The socket_read_string replaces this function. Set flag "interpret_escape" to "True" to
enable the use of escape sequences "\n" "\r" and "\t" as a prefix or suffix.

**Example**:
```urscript
if(line_from_server) :
popup("the line is not empty")
end
Example command: line_from_server = socket_read_line("socket_10")
• Example Parameters:
• socket_name = socket_10
```

---

<a id="socket_read_string"></a>
### `socket_read_string(socket_name=’socket_0’, prefix =’’, suffix =’’, interpret_escape=’False’, timeout=2)`
**Section**: URScript 17.1.60

**Description**:
Reads all data from the socket and returns the data as a string.
Returns (for example) "reply from the server:\n Hello World". if there is a timeout or the reply is invalid, an
empty string is returned (""). You can test if the string is empty with an if-statement.
Maxium length of received string including termination characters is limited to 1024 characters.

**Parameters**:
- **`prefix`**: Defines a prefix (string)
- **`suffix`**: Defines a suffix (string)
- **`interpret_escape`**: Enables the interpretation of escape sequences (bool)
- **`timeout`**: The number of seconds until the read action times out (float). A timeout of 0 or negative number indicates that the function should not return until a read is completed.

**Return Value**:
String

**Example**:
```urscript
if(string_from_server) :
popup("the string is not empty")
end
The optional parameters "prefix" and "suffix", can be used to express what is extracted from the socket.
The "prefix" specifies the start of the substring (message) extracted from the socket. The data up to the
end of the "prefix" will be ignored and removed from the socket. The "suffix" specifies the end of the
substring (message) extracted from the socket. Any remaining data on the socket, after the "suffix", will be
preserved.
By using the "prefix" and "suffix" it is also possible send multiple string to the controller at once, because
the suffix defines where the message ends. E.g. sending ">hello<>world<" and calling this script function
with the prefix=">" and suffix="<".
Note that leading spaces in the prefix and suffix strings are ignored in the current software and may cause
communication errors in future releases.
The optional parameter "interpret_escape" can be used to allow the use of escape sequences "\n", "\t" and
"\r" as part of the prefix or suffix.
Example command: string_from_server = socket_read_string("socket_
10",prefix=">",suffix="<")
```

---

<a id="socket_send_byte"></a>
### `socket_send_byte(value, socket_name=’socket_0’)`
**Section**: URScript 17.1.61

**Description**:
Sends a byte to the server
Sends the byte <value> through the socket. Expects no response. Can be used to send special ASCII
characters: 10 is newline, 2 is start of text, 3 is end of text.

**Parameters**:
- **`value`**: The number to send (byte)
- **`socket_name`**: Name of socket (string)

**Return Value**:
a boolean value indicating whether the send operation was successful

**Example**:
```urscript
Example command: socket_send_byte(2,"socket_10")
• Example Parameters:
• value = 2
• socket_name = socket_10
• Returns True or False (sent or not sent)
socket_name: Name of socket (string)
```

---

<a id="socket_send_int"></a>
### `socket_send_int(value, socket_name=’socket_0’)`
**Section**: URScript 17.1.62

**Description**:
Sends an int (int32_t) to the server
Sends the int <value> through the socket. Send in network byte order. Expects no response.

**Parameters**:
- **`value`**: The number to send (int)
- **`socket_name`**: Name of socket (string)

**Return Value**:
a boolean value indicating whether the send operation was successful

**Example**:
```urscript
Example command: socket_send_int(2,"socket_10")
• Example Parameters:
• value = 2
• socket_name = socket_10
• Returns True or False (sent or not sent)
```

---

<a id="socket_send_line"></a>
### `socket_send_line(str, socket_name=’socket_0’)`
**Section**: URScript 17.1.63

**Description**:
Sends a string with a newline character to the server - useful for communicating with the UR dashboard
server
Sends the string <str> through the socket in ASCII coding. Expects no response.

**Parameters**:
- **`str`**: The string to send (ascii)
- **`socket_name`**: Name of socket (string)

**Return Value**:
a boolean value indicating whether the send operation was successful

**Example**:
```urscript
Example command: socket_send_line("hello","socket_10")
Sends: hello\n to socket_10
• Example Parameters:
• str = hello
• socket_name = socket_10
• Returns True or False (sent or not sent)
```

---

<a id="socket_send_string"></a>
### `socket_send_string(str, socket_name=’socket_0’)`
**Section**: URScript 17.1.64

**Description**:
Sends a string to the server
Sends the string <str> through the socket in ASCII coding. Expects no response.

**Parameters**:
- **`str`**: The string to send (ascii)
- **`socket_name`**: Name of socket (string)

**Return Value**:
a boolean value indicating whether the send operation was successful

**Example**:
```urscript
Example command: socket_send_string("hello","socket_10")
Sends: hello to socket_10
• Example Parameters:
• str = hello
• socket_name = socket_10
```

---

<a id="socket_set_var"></a>
### `socket_set_var(name, value, socket_name=’socket_0’)`
**Section**: URScript 17.1.65

**Description**:
Sends an integer to the server
Sends the message "SET <name> <value>\n" through the socket. Expects no response.

**Parameters**:
- **`name`**: Variable name (string)
- **`value`**: The number to send (int)
- **`socket_name`**: Name of socket (string)

**Return Value**: `None`

**Example**:
```urscript
Example command: socket_set_var("POS_Y",2200,"socket_10")
Sends string: SET POS_Y 2200\n to socket_10
• Example Parameters:
• name = POS_Y -> name of variable
• value = 2200
• socket_name = socket_10
```

---

<a id="write_output_boolean_register"></a>
### `write_output_boolean_register(address, value)`
**Section**: URScript 17.1.66

**Description**:
Writes the boolean value into one of the output registers, which can also be accessed by a Field bus. Note,
uses it’s own memory space.

**Parameters**:
- **`address`**: Address of the register (0:127)
- **`value`**: Value to set in the register (True, False) • Returns True or False (sent or not sent)

**Return Value**: `None`

> [!NOTE]
> Note: The lower range of the boolean output registers [0:63] is reserved for FieldBus/PLC interface usage.
> The upper range [64:127] cannot be accessed by FieldBus/PLC interfaces, since it is reserved for external
> RTDE clients.

**Example**:
```urscript
write_output_boolean_register(3, True)
Example command: write_output_boolean_register(3,True)
• Example Parameters:
• address = 3
• value = True
```

---

<a id="write_output_float_register"></a>
### `write_output_float_register(address, value)`
**Section**: URScript 17.1.67

**Description**:
Writes the float value into one of the output registers, which can also be accessed by a Field bus. Note,
uses it’s own memory space.

**Parameters**:
- **`address`**: Address of the register (0:47)
- **`value`**: Value to set in the register (float)

**Return Value**: `None`

> [!NOTE]
> Note: The lower part of the float output registers [0:23] is reserved for FieldBus/PLC interface usage. The
> upper range [24:47] cannot be accessed by FieldBus/PLC interfaces, since it is reserved for external
> RTDE clients.

**Example**:
```urscript
write_output_float_register(3, 37.68)
Example command: write_output_float_register(3,37.68)
• Example Parameters:
• address = 3
• value = 37.68
```

---

<a id="write_output_integer_register"></a>
### `write_output_integer_register(address, value)`
**Section**: URScript 17.1.68

**Description**:
Writes the integer value into one of the output registers, which can also be accessed by a Field bus. Note,
uses it’s own memory space.

**Parameters**:
- **`address`**: Address of the register (0:47)
- **`value`**: Value to set in the register [-2,147,483,648 : 2,147,483,647]

**Return Value**: `None`

> [!NOTE]
> Note: The lower range of the integer output registers [0:23] is reserved for FieldBus/PLC interface usage.
> The upper range [24:47] cannot be accessed by FieldBus/PLC interfaces, since it is reserved for external
> RTDE clients.

**Example**:
```urscript
write_output_integer_register(3, 12)
Example command: write_output_integer_register(3,12)
• Example Parameters:
• address = 3
• value = 12
```

---

<a id="write_port_bit"></a>
### `write_port_bit(address, value)`
**Section**: URScript 17.1.69

**Description**:
Writes one of the ports, which can also be accessed by Modbus clients

**Parameters**:
- **`address`**: Address of the port (See port map on Support site, page "Modbus Server" )
- **`value`**: Value to be set in the register (True, False)

**Return Value**: `None`

**Example**:
```urscript
write_port_bit(3,True)
Example command: write_port_bit(3,True)
• Example Parameters:
• Address = 3
• Value = True
```

---

<a id="write_port_register"></a>
### `write_port_register(address, value)`
**Section**: URScript 17.1.70

**Description**:
Writes one of the ports, which can also be accessed by Modbus clients

**Parameters**:
- **`address`**: Address of the port (See port map on Support site, page "Modbus Server" )
- **`value`**: Value to be set in the port (0 : 65536) or (-32768 : 32767)

**Return Value**: `None`

**Example**:
```urscript
write_port_register(3,100)
Example command: write_port_register(3,100)
• Example Parameters:
• Address = 3
• Value = 100
```

---

<a id="zero_ftsensor"></a>
### `zero_ftsensor()`
**Section**: URScript 17.1.71

**Description**:
Zeroes the TCP force/torque measurement from the builtin force/torque sensor by subtracting the current
measurement from the subsequent.

**Parameters**:
- *None / No arguments required.*

**Return Value**: `None`

---

<a id="request_boolean_from_primary_client"></a>
### `request_boolean_from_primary_client(message)`
**Section**: URScript 17.1.72

**Description**:
Request input from operator. Polyscope shows dialog box with "yes" and "no" buttons.
Function blocks until operator selects option on the Polyscope screen.

**Parameters**:
- **`message`**: A string with a message shown on Polyscope dialog box. Can not be empty.

**Return Value**:
True or False: Value selected by the operator.

> [!NOTE]
> NOTE: Operator can also stop program by pressing "Cancel" button

**Example**:
```urscript
Example command: mark_part = request_boolean_from_primary_client("Should part
be marked?")
Show message to the operator, and save reply to mark_part variable
```

---

<a id="request_float_from_primary_client"></a>
### `request_float_from_primary_client(message)`
**Section**: URScript 17.1.73

**Description**:
Request input from operator. Polyscope shows dialog box with decimal number entry field.
Function blocks until operator enters value on the Polyscope screen.

**Parameters**:
- **`message`**: A string with a message shown on Polyscope dialog box. Can not be empty.

**Return Value**:
Float: Value entered by the operator.

> [!NOTE]
> NOTE: Operator can also stop program by pressing "Cancel" button

**Example**:
```urscript
Example command: offset_mm = request_float_from_primary_client("Enter gripping
offset [mm]")
Show message to the operator, and save reply to offset_mm variable
```

---

<a id="request_integer_from_primary_client"></a>
### `request_integer_from_primary_client(message)`
**Section**: URScript 17.1.74

**Description**:
Request input from operator. Polyscope shows dialog box with integer number entry field.
Function blocks until operator enters value on the Polyscope screen.

**Parameters**:
- **`message`**: A string with a message shown on Polyscope dialog box. Can not be empty.

**Return Value**:
Integer: Value entered by the operator.

> [!NOTE]
> NOTE: Operator can also stop program by pressing "Cancel" button

**Example**:
```urscript
Example command: number_of_parts = request_integer_from_primary_client("Enter
number of parts")
Show message to the operator, and save reply to number_of_parts variable
```

---

<a id="request_string_from_primary_client"></a>
### `request_string_from_primary_client(message)`
**Section**: URScript 17.1.75

**Description**:
Request input from operator. Polyscope shows dialog box with string entry field.
Function blocks until operator enters value on the Polyscope screen.

**Parameters**:
- *None / No arguments required.*

**Return Value**:
String: Value entered by the operator.

> [!NOTE]
> NOTE: Operator can also stop program by pressing "Cancel" button

**Example**:
```urscript
Example command: part_name = request_string_from_primary_client("Enter name of
the part")
Show message to the operator, and save reply to part_name variable
message: A string with a message shown on Polyscope dialog box. Can not be empty.
18.1. Functions
```

---

## Navigation

[⬅️ Back to Table of Contents](../README.md)
