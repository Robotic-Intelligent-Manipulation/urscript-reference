# Module IO Configuration (Hardware Electrical & Signal Setup)

> **Reference Module**: URScript Specification (Chapter 18)
> **Total Functions**: 14 functions
> **Target Controllers**: Universal Robots e-Series, UR20, UR30, CB-Series (SW 5.16+)

## Overview

Hardware I/O configuration for electrical domains (0–10V, 4–20mA), wrist tool power supply (0V, 12V, 24V), and automatic physical button action bindings (run, pause, stop, or freedrive triggers).

## Function Index (14 Functions)

- [`modbus_set_runstate_dependent_choice(signal_name, runstate_choice)`](#modbus_set_runstate_dependent_choice)
- [`set_analog_outputdomain(port, domain)`](#set_analog_outputdomain)
- [`set_configurable_digital_input_action(port, action)`](#set_configurable_digital_input_action)
- [`set_gp_boolean_input_action(port, action)`](#set_gp_boolean_input_action)
- [`set_input_actions_to_default()`](#set_input_actions_to_default)
- [`set_runstate_configurable_digital_output_to_value(outputId, state)`](#set_runstate_configurable_digital_output_to_value)
- [`set_runstate_gp_boolean_output_to_value(outputId, state)`](#set_runstate_gp_boolean_output_to_value)
- [`set_runstate_standard_analog_output_to_value(outputId, state)`](#set_runstate_standard_analog_output_to_value)
- [`set_runstate_standard_digital_output_to_value(outputId, state)`](#set_runstate_standard_digital_output_to_value)
- [`set_runstate_tool_digital_output_to_value(outputId, state)`](#set_runstate_tool_digital_output_to_value)
- [`set_standard_analog_input_domain(port, domain)`](#set_standard_analog_input_domain)
- [`set_standard_digital_input_action(port, action)`](#set_standard_digital_input_action)
- [`set_tool_analog_input_domain(port, domain)`](#set_tool_analog_input_domain)
- [`set_tool_digital_input_action(port, action)`](#set_tool_digital_input_action)

---

## API Documentation

<a id="modbus_set_runstate_dependent_choice"></a>
### `modbus_set_runstate_dependent_choice(signal_name, runstate_choice)`
**Section**: URScript 18.1.1

**Description**:
Sets the output signal levels depending on the state of the program.

**Parameters**:
- **`signal_name`**: A string identifying a digital or register output signal that in advance has been added. Can not be empty.
- **`state`**: 
- **`0`**: Preserve signal state,
- **`1`**: Set signal Low when program is not running,
- **`2`**: Set signal High when program is not running,
- **`3`**: Set signal High when program is running and low when it is stopped,
- **`4`**: Set signal Low when program terminates unscheduled,
- **`5`**: Set signal High from the moment a program is started and Low when a program terminates unscheduled.

**Return Value**: `None`

> [!NOTE]
> Note: An unscheduled program termination is caused when a Protective stop, Fault, Violation or Runtime
> exception occurs.

**Example**:
```urscript
Example command:
modbus_set_runstate_dependent_choice("output2", 3)
• Example Parameters:
• Signal name = output2
• Runstate dependent choice = 3 ! set Low when a program is stopped and High when a
program is running
```

---

<a id="set_analog_outputdomain"></a>
### `set_analog_outputdomain(port, domain)`
**Section**: URScript 18.1.2

**Description**:
Set domain of analog outputs

**Parameters**:
- **`port`**: analog output port number
- **`domain`**: analog output domain: 0: 4-20mA, 1: 0-10V

**Return Value**: `None`

**Example**:
```urscript
Example command: set_analog_outputdomain(1,1)
• Example Parameters:
• port is analog output port 1 (on controller)
• domain = 1 (0-10 volts)
```

---

<a id="set_configurable_digital_input_action"></a>
### `set_configurable_digital_input_action(port, action)`
**Section**: URScript 18.1.3

**Description**:
Using this method sets the selected configurable digital input register to either a "default" or "freedrive"
action.
See also:
• set_input_actions_to_default
• set_standard_digital_input_action
• set_gp_boolean_input_action

**Parameters**:
- **`port`**: The configurable digital input port number. (integer)
- **`action`**: The type of action. The action can either be "default" or "freedrive". (string)

**Return Value**: `None`

**Example**:
```urscript
Example command: set_configurable_digital_input_action(0, "freedrive")
• Example Parameters:
• n is the configurable digital input register 0
• f is set to "freedrive" action
```

---

<a id="set_gp_boolean_input_action"></a>
### `set_gp_boolean_input_action(port, action)`
**Section**: URScript 18.1.4

**Description**:
Using this method sets the selected gp boolean input register to either a "default" or "freedrive" action.

**Parameters**:
- **`port`**: The gp boolean input port number. integer: [0:127]
- **`action`**: The type of action. The action can either be "default" or "freedrive". (string)

**Return Value**: `None`

> [!NOTE]
> Note: The lower range of the boolean input registers [0:63] is reserved for FieldBus/PLC interface usage.
> The upper range [64:127] cannot be accessed by FieldBus/PLC interfaces, since it is reserved for external
> RTDE clients.
> See also:
> set_input_actions_to_default
> set_standard_digital_input_action
> set_configurable_digital_input_action
> set_tool_digital_input_action

**Example**:
```urscript
Example command: set_gp_boolean_input_action(64, "freedrive")
• set_tool_digital_input_action
• Example Parameters:
• n is the gp boolean input register 0
• f is set to "freedrive" action
```

---

<a id="set_input_actions_to_default"></a>
### `set_input_actions_to_default()`
**Section**: URScript 18.1.5

**Description**:
Using this method sets the input actions of all standard, configurable, tool, and gp_boolean input registers
to "default" action.
See also:
set_standard_digital_input_action
set_configurable_digital_input_action
set_tool_digital_input_action
set_gp_boolean_input_action

**Parameters**:
- *None / No arguments required.*

**Return Value**: `None`

**Example**:
```urscript
Example command: set_input_actions_to_default()
```

---

<a id="set_runstate_configurable_digital_output_to_value"></a>
### `set_runstate_configurable_digital_output_to_value(outputId, state)`
**Section**: URScript 18.1.6

**Description**:
Sets the output signal levels depending on the state of the program (running or stopped).

**Parameters**:
- **`outputId`**: The output signal number (id), integer: [0:7]
- **`state`**: 
- **`0`**: Preserve signal state,
- **`1`**: Set signal Low when program is not running,
- **`2`**: Set signal High when program is not running,
- **`3`**: Set signal High when program is running and low when it is stopped,
- **`4`**: Set signal Low when program terminates unscheduled,
- **`5`**: Set signal High from the moment a program is started and Low when a program terminates unscheduled.

**Return Value**: `None`

> [!NOTE]
> Note: An unscheduled program termination is caused when a Protective stop, Fault, Violation or Runtime
> exception occurs.

**Example**:
```urscript
Example: Set configurable digital output 5 to high when program is not running.
set_runstate_configurable_digital_output_to_value(5, 2)
Example command:
set_runstate_configurable_digital_output_to_value(5, 2)
• Example Parameters:
• outputid = configurable digital output on port 5
• Runstate choice = 4 ! configurable digital output on port 5 goes low when a program is
terminated unscheduled.
```

---

<a id="set_runstate_gp_boolean_output_to_value"></a>
### `set_runstate_gp_boolean_output_to_value(outputId, state)`
**Section**: URScript 18.1.7

**Description**:
Sets the output value depending on the state of the program (running or stopped).

**Parameters**:
- **`outputId`**: The output signal number (id), integer: [0:127]
- **`state`**: 
- **`1`**: Set signal to False when program is not running,
- **`2`**: Set signal to True when program is not running,
- **`3`**: Set signal to True when program is running and False when it is stopped,
- **`4`**: Set signal to False when program terminates unscheduled,
- **`5`**: Set signal to True from the moment a program is started and False when a program terminates unscheduled.
- **`Notes`**: • The lower range of the boolean output registers [0:63] is reserved for FieldBus/PLC interface usage. The upper range [64:127] cannot be accessed by FieldBus/PLC interfaces, since it is reserved for external RTDE clients. • An unscheduled program termination is caused when a Protective stop, Fault, Violation or Runtime exception occurs.

**Return Value**: `None`

**Example**:
```urscript
Example command:
set_runstate_gp_boolean_output_to_value(64, 2)
• Example Parameters:
• outputid = output on port 64
• Runstate choice = 2 ! sets signal on port 64 to True when program is not running
```

---

<a id="set_runstate_standard_analog_output_to_value"></a>
### `set_runstate_standard_analog_output_to_value(outputId, state)`
**Section**: URScript 18.1.8

**Description**:
Sets the output signal levels depending on the state of the program (running or stopped).

**Parameters**:
- **`0`**: Preserve signal state,
- **`outputId`**: The output signal number (id), integer: [0:1]
- **`state`**: 
- **`0`**: Preserve signal state,
- **`1`**: Set signal Low when program is not running,
- **`2`**: Set signal High when program is not running,
- **`3`**: Set signal High when program is running and low when it is stopped,
- **`4`**: Set signal Low when program terminates unscheduled,
- **`5`**: Set signal High from the moment a program is started and Low when a program terminates unscheduled.

**Return Value**: `None`

> [!NOTE]
> Note: An unscheduled program termination is caused when a Protective stop, Fault, Violation or Runtime
> exception occurs.

**Example**:
```urscript
Example: Set standard analog output 1 to high when program is not running.
set_runstate_standard_analog_output_to_value(1, 2)
Example command:
set_runstate_standard_analog_output_to_value(1, 2)
• Example Parameters:
• outputid = standard analog output on port 1
• Runstate choice = 2 ! analog output on port 1 goes High when program is not running
```

---

<a id="set_runstate_standard_digital_output_to_value"></a>
### `set_runstate_standard_digital_output_to_value(outputId, state)`
**Section**: URScript 18.1.9

**Description**:
Sets the output signal level depending on the state of the program (running or stopped).

**Parameters**:
- **`outputId`**: The output signal number (id), integer: [0:7]
- **`state`**: 
- **`0`**: Preserve signal state,
- **`1`**: Set signal Low when program is not running,
- **`2`**: Set signal High when program is not running,
- **`3`**: Set signal High when program is running and low when it is stopped,
- **`4`**: Set signal Low when program terminates unscheduled,
- **`5`**: Set signal High from the moment a program is started and Low when a program terminates unscheduled.

**Return Value**: `None`

> [!NOTE]
> Note: An unscheduled program termination is caused when a Protective stop, Fault, Violation or Runtime
> exception occurs.

**Example**:
```urscript
Example: Set standard digital output 5 to high when program is not running.
set_runstate_standard_digital_output_to_value(5, 2)
Example command:
set_runstate_standard_digital_output_to_value(5, 2)
• Example Parameters:
• outputid = standard digital output on port 1
• Runstate choice = 2 ! sets digital output on port 1 to High when program is not running
```

---

<a id="set_runstate_tool_digital_output_to_value"></a>
### `set_runstate_tool_digital_output_to_value(outputId, state)`
**Section**: URScript 18.1.10

**Description**:
Sets the output signal level depending on the state of the program (running or stopped).

**Parameters**:
- The output signal number (id), integer: [0:1]
- **`state`**: 
- **`0`**: Preserve signal state,
- **`1`**: Set signal Low when program is not running,
- **`2`**: Set signal High when program is not running,
- **`3`**: Set signal High when program is running and low when it is stopped,
- **`4`**: Set signal Low when program terminates unscheduled,
- **`5`**: Set signal High from the moment a program is started and Low when a program terminates unscheduled.

**Return Value**: `None`

> [!NOTE]
> Note: An unscheduled program termination is caused when a Protective stop, Fault, Violation or Runtime
> exception occurs.

**Example**:
```urscript
Example: Set tool digital output 1 to high when program is not running.
set_runstate_tool_digital_output_to_value(1, 2)
Example command:
set_runstate_tool_digital_output_to_value(1, 2)
• Example Parameters:
• outputid = tool digital output on port 1
• Runstate choice = 2 ! digital output on port 1 goes High when program is not running
```

---

<a id="set_standard_analog_input_domain"></a>
### `set_standard_analog_input_domain(port, domain)`
**Section**: URScript 18.1.11

**Description**:
Set domain of standard analog inputs in the controller box
For the tool inputs see set_tool_analog_input_domain.

**Parameters**:
- **`port`**: analog input port number: 0 or 1
- **`domain`**: analog input domains: 0: 4-20mA, 1: 0-10V

**Return Value**: `None`

**Example**:
```urscript
Example command: set_standard_analog_input_domain(1,0)
outputId:
• Example Parameters:
• port = analog input port 1
• domain = 0 (4-20 mA)
```

---

<a id="set_standard_digital_input_action"></a>
### `set_standard_digital_input_action(port, action)`
**Section**: URScript 18.1.12

**Description**:
Using this method sets the selected standard digital input register to either a "default" or "freedrive" action.
See also:
• set_input_actions_to_default
• set_configurable_digital_input_action
• set_tool_digital_input_action
• set_gp_boolean_input_action

**Parameters**:
- **`port`**: The standard digital input port number. (integer)
- **`action`**: The type of action. The action can either be "default" or "freedrive". (string)

**Return Value**: `None`

**Example**:
```urscript
Example command: set_standard_digital_input_action(0, "freedrive")
• Example Parameters:
• n is the standard digital input register 0
• f is set to "freedrive" action
```

---

<a id="set_tool_analog_input_domain"></a>
### `set_tool_analog_input_domain(port, domain)`
**Section**: URScript 18.1.13

**Description**:
Set domain of analog inputs in the tool
For the controller box inputs see set_standard_analog_input_domain.

**Parameters**:
- **`port`**: analog input port number: 0 or 1
- **`domain`**: analog input domains: 0: 4-20mA, 1: 0-10V

**Return Value**: `None`

**Example**:
```urscript
Example command: set_tool_analog_input_domain(1,1)
• Example Parameters:
• port = tool analog input 1
• domain = 1 (0-10 volts)
```

---

<a id="set_tool_digital_input_action"></a>
### `set_tool_digital_input_action(port, action)`
**Section**: URScript 18.1.14

**Description**:
Using this method sets the selected tool digital input register to either a "default" or "freedrive" action.
See also:
• set_input_actions_to_default
• set_standard_digital_input_action
• set_configurable_digital_input_action
• set_gp_boolean_input_action

**Parameters**:
- **`port`**: The tool digital input port number. (integer)
- **`action`**: The type of action. The action can either be "default" or "freedrive". (string)

**Return Value**: `None`

> [!NOTE]
> NOTE:
> 1. These script functions are only accessible if the program is being run from within Polyscope.
> 2. The Remote TCP & Toolpath URCap Controller must run in order for the script functions to work. Go to
> Installation > URCaps > Remote TCP & Toolpath URCap to start the controller from the URCap home
> page.
> 3. The script functions are available in the Functions dropdown within the Script node (Program >
> Advanced > Script). Note: mc_add_circular() requires six arguments, but only five arguments are
> displayed in the Functions dropdown. Please make sure to specify the sixth argument ‘mode’ when
> using this function.
> 19.2. Functions

**Example**:
```urscript
Example command: set_tool_digital_input_action(0, "freedrive")
• Example Parameters:
• n is the tool digital input register 0
• f is set to "freedrive" action
19.1. This module contains Remote TCP and toolpath
APIs.
```

---

## Navigation

[⬅️ Back to Table of Contents](../README.md)
