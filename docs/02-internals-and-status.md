# Module Internals (State Telemetry, Sensors & System Modes)

> **Reference Module**: URScript Specification (Chapter 15)
> **Total Functions**: 57 functions
> **Target Controllers**: Universal Robots e-Series, UR20, UR30, CB-Series (SW 5.16+)

## Overview

System telemetry and status inspection. Provides actual and target joint positions, speeds, torques, temperatures, Tool Center Point (TCP) pose, wrist Force/Torque sensor wrench readings (`get_tcp_force`), safety mode indicators, dynamic payload configuration (`set_payload`, `set_payload_cog`), and data type casting utilities.

## Function Index (57 Functions)

- [`force()`](#force)
- [`estimate_payload(poses, wrenches)`](#estimate_payload)
- [`get_actual_joint_positions()`](#get_actual_joint_positions)
- [`get_actual_joint_positions_history(steps=0)`](#get_actual_joint_positions_history)
- [`get_actual_joint_speeds()`](#get_actual_joint_speeds)
- [`get_actual_tcp_pose()`](#get_actual_tcp_pose)
- [`get_actual_tcp_speed()`](#get_actual_tcp_speed)
- [`get_actual_tool_flange_pose()`](#get_actual_tool_flange_pose)
- [`get_controller_temp()`](#get_controller_temp)
- [`get_forward_kin(q=’current_joint_positions’, tcp=’active_ tcp’)`](#get_forward_kin)
- [`get_inverse_kin(x, qnear, maxPositionError =1e10,maxOrientationError =1e-10, tcp=’active_tcp’)`](#get_inverse_kin)
- [`get_inverse_kin_has_solution(pose, qnear, maxPositionError=1E-10, maxOrientationError=1e-10, tcp="active_ tcp")`](#get_inverse_kin_has_solution)
- [`get_joint_temp(j)`](#get_joint_temp)
- [`get_joint_torques()`](#get_joint_torques)
- [`get_steptime()`](#get_steptime)
- [`get_target_joint_positions()`](#get_target_joint_positions)
- [`get_target_joint_speeds()`](#get_target_joint_speeds)
- [`get_target_payload()`](#get_target_payload)
- [`get_target_payload_cog()`](#get_target_payload_cog)
- [`get_target_tcp_pose()`](#get_target_tcp_pose)
- [`get_target_tcp_speed()`](#get_target_tcp_speed)
- [`get_target_payload_inertia()`](#get_target_payload_inertia)
- [`get_target_waypoint()`](#get_target_waypoint)
- [`get_tcp_force()`](#get_tcp_force)
- [`get_tcp_offset()`](#get_tcp_offset)
- [`get_tool_accelerometer_reading()`](#get_tool_accelerometer_reading)
- [`get_tool_current()`](#get_tool_current)
- [`high_holding_torque_disable()`](#high_holding_torque_disable)
- [`high_holding_torque_enable()`](#high_holding_torque_enable)
- [`is_steady()`](#is_steady)
- [`is_within_safety_limits(pose, qnear)`](#is_within_safety_limits)
- [`popup(s, title=’Popup’, warning=False, error=False, blocking=False)`](#popup)
- [`powerdown()`](#powerdown)
- [`protective_stop()`](#protective_stop)
- [`set_base_acceleration(a)`](#set_base_acceleration)
- [`set_baselight_off()`](#set_baselight_off)
- [`set_baselight_iec()`](#set_baselight_iec)
- [`set_baselight_solid(r,g,b)`](#set_baselight_solid)
- [`set_gravity(d)`](#set_gravity)
- [`set_payload(m, cog)`](#set_payload)
- [`set_payload_cog(CoG)`](#set_payload_cog)
- [`set_payload_mass(m)`](#set_payload_mass)
- [`set_target_payload(m, cog, inertia=[0, 0, 0, 0, 0, 0], transition_time=0)`](#set_target_payload)
- [`set_tcp(pose, tcp_name="")`](#set_tcp)
- [`sleep(t)`](#sleep)
- [`str_at(src, index)`](#str_at)
- [`str_cat(op1, op2)`](#str_cat)
- [`str_empty(str)`](#str_empty)
- [`str_find(src, target, start_from=0)`](#str_find)
- [`str_len(str)`](#str_len)
- [`str_sub(src, index, len)`](#str_sub)
- [`sync()`](#sync)
- [`textmsg(s1, s2=’’)`](#textmsg)
- [`to_num(str )`](#to_num)
- [`to_str(val)`](#to_str)
- [`tool_contact(direction)`](#tool_contact)
- [`tool_contact_examples()`](#tool_contact_examples)

---

## API Documentation

<a id="force"></a>
### `force()`
**Section**: URScript 15.1.1

**Description**:
Returns the force exerted at the TCP
Return the current externally exerted force at the TCP. The force is the norm of Fx, Fy, and Fz calculated
using get_tcp_force().

**Parameters**:
- *None / No arguments required.*

**Return Value**: `None`

> [!NOTE]
> Note: Refer to force_mode() for taring the sensor.

---

<a id="estimate_payload"></a>
### `estimate_payload(poses, wrenches)`
**Section**: URScript 15.1.2

**Description**: *Executes built-in URScript operation.*

**Parameters**:
- • poses - A list of at least four TCP poses. The orientation of the poses should be as varied as
- possible, in order to get a good estimate.
- If the rotational distance between any two poses is less than Pi / (2*n) radians, where n is the
- number of poses in poses, an exception will be thrown.
- • TCP poses can be recorded with get_actual_tcp_pose().
- wrenches - A list of wrenches resulting from gravity acting on the payload. Must have the same
- length as poses. Each wrench in wrenches should be measured at the corresponding pose in
- poses. The wrenches must be given at the tool flange but in robot base orientation. Wrenches in the
- required orientation can be recorded with get_tcp_force() when in the desired pose.
- Return value:
- struct[mass, cog]
- mass is a double representing the weight of the payload in kg.
- cog is a 3d vector representing the offset from the tool flange to the payload center of
- gravity in tool frame in meters.
- Example usage (question)
- repeat n times
- movej(*some distinct pose*)
- sleep(*long enough for the arm to stabilize*)
- pose_list.append(get_tcp_force)
- wrench_list.append(get_actual_tcp_pose)
- payload = estimate_payload(pose_list, wrench_list)
- The force in Newton (float)
- set_payload(payload.mass, payload.cog)

**Return Value**: `None`

---

<a id="get_actual_joint_positions"></a>
### `get_actual_joint_positions()`
**Section**: URScript 15.1.3

**Description**:
Returns the actual angular positions of all joints
The angular actual positions are expressed in radians and returned as a vector of length 6. Note that the
output might differ from the output of get_target_joint_positions(), especially during
acceleration and heavy loads.

**Parameters**:
- *None / No arguments required.*

**Return Value**:
The current actual joint angular position vector in rad : [Base, Shoulder, Elbow, Wrist1, Wrist2, Wrist3]

---

<a id="get_actual_joint_positions_history"></a>
### `get_actual_joint_positions_history(steps=0)`
**Section**: URScript 15.1.4

**Description**:
Returns the actual past angular positions of all joints
This function returns the angular positions as reported by the function "get_actual_joint_
positions()" which indicates the number of controller time steps occurring before the current time
step.
An exception is thrown if indexing goes beyond the buffer size.

**Parameters**:
- **`steps`**: The number of controller time steps required to go back. 0 corresponds to "get_actual_ joint_positions()"

**Return Value**:
The joint angular position vector in rad : [Base, Shoulder, Elbow, Wrist1, Wrist2, Wrist3] that was actual at
the provided number of steps before the current time step.

---

<a id="get_actual_joint_speeds"></a>
### `get_actual_joint_speeds()`
**Section**: URScript 15.1.5

**Description**:
Returns the actual angular velocities of all joints
The angular actual velocities are expressed in radians pr. second and returned as a vector of length 6.
Note that the output might differ from the output of get_target_joint_speeds(), especially during
acceleration and heavy loads.

**Parameters**:
- *None / No arguments required.*

**Return Value**:
The current actual joint angular velocity vector in rad/s: [Base, Shoulder, Elbow, Wrist1, Wrist2, Wrist3]

---

<a id="get_actual_tcp_pose"></a>
### `get_actual_tcp_pose()`
**Section**: URScript 15.1.6

**Description**:
Returns the current measured tool pose
Returns the 6d pose representing the tool position and orientation specified in the base frame. The
calculation of this pose is based on the actual robot encoder readings.

**Parameters**:
- *None / No arguments required.*

**Return Value**:
The current actual TCP vector [X, Y, Z, Rx, Ry, Rz]

---

<a id="get_actual_tcp_speed"></a>
### `get_actual_tcp_speed()`
**Section**: URScript 15.1.7

**Description**:
The speed of the TCP retuned in a pose structure. The first three values are the cartesian speeds along
x,y,z, and the last three define the current rotation axis, rx,ry,rz, and the length |rz,ry,rz| defines the
angular velocity in radians/s.

**Parameters**:
- *None / No arguments required.*

**Return Value**:
The current actual TCP velocity vector [X, Y, Z, Rx, Ry, Rz]

---

<a id="get_actual_tool_flange_pose"></a>
### `get_actual_tool_flange_pose()`
**Section**: URScript 15.1.8

**Description**:
Returns the current measured tool flange pose
Returns the 6d pose representing the tool flange position and orientation specified in the base frame,
without the Tool Center Point offset. The calculation of this pose is based on the actual robot encoder
readings.

**Parameters**:
- *None / No arguments required.*

**Return Value**:
The current actual tool flange vector: [X, Y, Z, Rx, Ry, Rz]

> [!NOTE]
> Note: See get_actual_tcp_pose for the actual 6d pose including TCP offset.

---

<a id="get_controller_temp"></a>
### `get_controller_temp()`
**Section**: URScript 15.1.9

**Description**:
Returns the temperature of the control box
The temperature of the robot control box in degrees Celcius.

**Parameters**:
- *None / No arguments required.*

**Return Value**:
A temperature in degrees Celcius (float)
Returns the current measured TCP speed

---

<a id="get_forward_kin"></a>
### `get_forward_kin(q=’current_joint_positions’, tcp=’active_ tcp’)`
**Section**: URScript 15.1.10

**Description**:
Calculate the forward kinematic transformation (joint space -> tool space) using the calibrated robot
kinematics. If no joint position vector is provided the current joint angles of the robot arm will be used. If no
tcp is provided the currently active tcp of the controller will be used.

**Parameters**:
- **`q`**: joint position vector (Optional)
- **`tcp`**: tcp offset pose (Optional)

**Return Value**:
tool pose

**Example**:
```urscript
Example command: get_forward_kin([0.,3.14,1.57,.785,0,0], p[0,0,0.01,0,0,0])
• Example Parameters:
• q = [0.,3.14,1.57,.785,0,0] -> joint angles of j0=0 deg, j1=180 deg, j2=90 deg, j3=45 deg,
j4=0 deg, j5=0 deg.
• tcp = p[0,0,0.01,0,0,0] -> tcp offset of x=0mm, y=0mm, z=10mm and rotation vector of rx=0
deg., ry=0 deg, rz=0 deg.
```

---

<a id="get_inverse_kin"></a>
### `get_inverse_kin(x, qnear, maxPositionError =1e10,maxOrientationError =1e-10, tcp=’active_tcp’)`
**Section**: URScript 15.1.11

**Description**:
Calculate the inverse kinematic transformation (tool space -> joint space). If qnear is defined, the solution
closest to qnear is returned.
Otherwise, the solution closest to the current joint positions is returned. If no tcp is provided the currently
active tcp of the controller is used.

**Parameters**:
- **`x`**: tool pose
- **`qnear`**: list of joint positions (Optional)
- **`maxPositionError`**: the maximum allowed position error (Optional)
- **`maxOrientationError`**: the maximum allowed orientation error (Optional)
- **`tcp`**: tcp offset pose (Optional)

**Return Value**:
joint positions

**Example**:
```urscript
Example command: get_inverse_kin(p[.1,.2,.2,0,3.14,0], [0.,3.14,1.57,.785,0,0])
• Example Parameters:
• x = p[.1,.2,.2,0,3.14,0] -> pose with position of x=100mm, y=200mm, z=200mm and rotation
vector of rx=0 deg., ry=180 deg, rz=0 deg.
• qnear = [0.,3.14,1.57,.785,0,0] -> solution should be near to joint angles of j0=0 deg, j1=180
deg, j2=90 deg, j3=45 deg, j4=0 deg, j5=0 deg.
• maxPositionError is by default 1e-10 m
• maxOrientationError is by default 1e-10 rad
```

---

<a id="get_inverse_kin_has_solution"></a>
### `get_inverse_kin_has_solution(pose, qnear, maxPositionError=1E-10, maxOrientationError=1e-10, tcp="active_ tcp")`
**Section**: URScript 15.1.12

**Description**:
Check if get_inverse_kin has a solution and return boolean (True) or (False).
This can be used to avoid the runtime exception of get_inverse_kin when no solution exists.

**Parameters**:
- **`pose`**: tool pose
- **`qnear`**: list of joint positions (Optional)
- **`maxPositionError`**: the maximum allowed position error (Optional)
- **`maxOrientationError`**: the maximum allowed orientation error (Optional)
- **`tcp`**: tcp offset pose (Optional)

**Return Value**:
True if get_inverse_kin has a solution, False otherwise (bool)

---

<a id="get_joint_temp"></a>
### `get_joint_temp(j)`
**Section**: URScript 15.1.13

**Description**:
Returns the temperature of joint j
The temperature of the joint house of joint j, counting from zero. j=0 is the base joint, and j=5 is the last
joint before the tool flange.

**Parameters**:
- **`j`**: The joint number (int)

**Return Value**:
A temperature in degrees Celcius (float)

---

<a id="get_joint_torques"></a>
### `get_joint_torques()`
**Section**: URScript 15.1.14

**Description**:
Returns the torques of all joints
The torque on the joints, corrected by the torque needed to move the robot itself (gravity, friction, etc.),
returned as a vector of length 6.

**Parameters**:
- *None / No arguments required.*

**Return Value**:
The joint torque vector in Nm: [Base, Shoulder, Elbow, Wrist1, Wrist2, Wrist3]

---

<a id="get_steptime"></a>
### `get_steptime()`
**Section**: URScript 15.1.15

**Description**:
Returns the duration of the robot time step in seconds.
In every time step, the robot controller will receive measured joint positions and velocities from the robot,
and send desired joint positions and velocities back to the robot. This happens with a predetermined
frequency, in regular intervals. This interval length is the robot time step.

**Parameters**:
- *None / No arguments required.*

**Return Value**:
duration of the robot step in seconds

---

<a id="get_target_joint_positions"></a>
### `get_target_joint_positions()`
**Section**: URScript 15.1.16

**Description**:
Returns the desired angular position of all joints
The angular target positions are expressed in radians and returned as a vector of length 6. Note that the
output might differ from the output of get_actual_joint_positions(), especially during acceleration and
heavy loads.

**Parameters**:
- *None / No arguments required.*

**Return Value**:
The current target joint angular position vector in rad: [Base, Shoulder, Elbow, Wrist1, Wrist2, Wrist3]

---

<a id="get_target_joint_speeds"></a>
### `get_target_joint_speeds()`
**Section**: URScript 15.1.17

**Description**:
Returns the desired angular velocities of all joints
The angular target velocities are expressed in radians pr. second and returned as a vector of length 6.
Note that the output might differ from the output of get_actual_joint_speeds(), especially during
acceleration and heavy loads.

**Parameters**:
- *None / No arguments required.*

**Return Value**:
The current target joint angular velocity vector in rad/s: [Base, Shoulder, Elbow, Wrist1, Wrist2, Wrist3]

---

<a id="get_target_payload"></a>
### `get_target_payload()`
**Section**: URScript 15.1.18

**Description**:
Returns the weight of the active payload

**Parameters**:
- *None / No arguments required.*

**Return Value**:
The weight of the current payload in kilograms

---

<a id="get_target_payload_cog"></a>
### `get_target_payload_cog()`
**Section**: URScript 15.1.19

**Description**:
Retrieve the Center Of Gravity (COG) coordinates of the active payload.
This scripts returns the COG coordinates of the active payload, with respect to the tool flange

**Parameters**:
- *None / No arguments required.*

**Return Value**:
The 3d coordinates of the COG [CoGx, CoGy, CoGz] in meters
Returns the most recently set payload inertia matrix.
This script function returns the inertia matrix of the active payload in tool flange coordinates, with origin at
the CoG.
The six dimensional coordinates of the payload inertia matrix [Ixx, Iyy, Izz, Ixy, Ixz, Iyz] expressed in
kg*m^2.

---

<a id="get_target_tcp_pose"></a>
### `get_target_tcp_pose()`
**Section**: URScript 15.1.21

**Description**:
Returns the current target tool pose
Returns the 6d pose representing the tool position and orientation specified in the base frame. The
calculation of this pose is based on the current target joint positions.

**Parameters**:
- *None / No arguments required.*

**Return Value**:
The current target TCP vector [X, Y, Z, Rx, Ry, Rz]

---

<a id="get_target_tcp_speed"></a>
### `get_target_tcp_speed()`
**Section**: URScript 15.1.22

**Description**:
Returns the current target TCP speed
The desired speed of the TCP returned in a pose structure. The first three values are the cartesian speeds
along x,y,z, and the last three define the current rotation axis, rx,ry,rz, and the length |rz,ry,rz| defines the
angular velocity in radians/s.

**Parameters**:
- *None / No arguments required.*

**Return Value**:
The TCP speed (pose)

---

<a id="get_target_payload_inertia"></a>
### `get_target_payload_inertia()`
**Section**: URScript 15.1.20

**Description**: *Executes built-in URScript operation.*

**Parameters**:
- *None / No arguments required.*

**Return Value**: `None`

---

<a id="get_target_waypoint"></a>
### `get_target_waypoint()`
**Section**: URScript 15.1.23

**Description**:
Returns the target waypoint of the active move
This is different from the get_target_tcp_pose() which returns the target pose for each time step. The get_
target_waypoint() returns the same target pose for movel, movej, movep or movec during the motion. It
returns the same as get_target_tcp_pose(), if none of the mentioned move functions are running.
This method is useful for calculating relative movements where the previous move command uses blends.

**Parameters**:
- *None / No arguments required.*

**Return Value**:
The desired waypoint TCP vector [X, Y, Z, Rx, Ry, Rz]

---

<a id="get_tcp_force"></a>
### `get_tcp_force()`
**Section**: URScript 15.1.24

**Description**:
Returns the force/torque vector at the tool flange.
The function returns p[Fx(N), Fy(N), Fz(N), TRx(Nm), TRy(Nm), TRz(Nm)] where the forces: Fx, Fy, and
Fz in Newtons and the torques: TRx, TRy and TRz in Newtonmeters are all measured at the tool flange
with the orientation of the robot base coordinate system.

**Parameters**:
- *None / No arguments required.*

**Return Value**:
The force/torque vector

> [!NOTE]
> Note:
> Refer to zero_ftsensor() for taring sensor.

**Example**:
```urscript
Example:
def get_wrench_at_tool_flange():
ft = get_tcp_force()
t_flange_in_base
= pose_trans(get_target_tcp_pose(), pose_inv(get_tcp_offset())) flange_rot
= pose_inv(p[0, 0, 0, t_flange_in_base[3], t_flange_in_base[4], t_flange_in_
base[5]])
f = pose_trans(flange_rot, p[ft[0], ft[1], ft[2], 0, 0, 0])
t = pose_trans(flange_rot, p[ft[3], ft[4], ft[5], 0, 0, 0])
return [f[0], f[1], f[2], t[0], t[1], t[2]]
end
def get_wrench_at_tcp():
return wrench_trans(get_tcp_offset(), get_wrench_at_tool_flange())
end
```

---

<a id="get_tcp_offset"></a>
### `get_tcp_offset()`
**Section**: URScript 15.1.25

**Description**:
Gets the active tcp offset, i.e. the transformation from the output flange coordinate system to the TCP as a
pose.

**Parameters**:
- *None / No arguments required.*

**Return Value**:
tcp offset pose

---

<a id="get_tool_accelerometer_reading"></a>
### `get_tool_accelerometer_reading()`
**Section**: URScript 15.1.26

**Description**:
Returns the current reading of the tool accelerometer as a three-dimensional vector.
The accelerometer axes are aligned with the tool coordinates, and pointing an axis upwards results in a
positive reading.

**Parameters**:
- *None / No arguments required.*

**Return Value**:
X, Y, and Z composant of the measured acceleration in SI-units (m/s^2).

---

<a id="get_tool_current"></a>
### `get_tool_current()`
**Section**: URScript 15.1.27

**Description**:
Returns the tool current
The tool current consumption measured in ampere.

**Parameters**:
- *None / No arguments required.*

**Return Value**:
The tool current in ampere.

---

<a id="high_holding_torque_disable"></a>
### `high_holding_torque_disable()`
**Section**: URScript 15.1.28

**Description**:
Disables automatically applying high hold torque when the robot is stationary, which is the default
behavior. The UR controller automatically applies high holding torque when the following is true:
• The program state is PROGRAM_STATE_RUNNING
• All actual joint movement <= 0.01 rad/s
• All target joint velocities == 0

**Parameters**:
- None

**Return Value**: `None`

**Example**:
```urscript
Example command:
high_holding_torque_disable()
This function script disables the high holding torque behavior. Note that the default is restored to enabled
after restarting the controller.
See also:
high_holding_torque_enable()
Applications: Disable high holding torque if you want a stationary robot to issue a protective stop when
colling with an object. For example, if the robot is being transported on a linear rail or vertical lift. However,
if just the base of the robot collides with an object while moving, the protective stop may not be issued.
Adequate safety precautions should be put in place to guard against this situation.
```

---

<a id="high_holding_torque_enable"></a>
### `high_holding_torque_enable()`
**Section**: URScript 15.1.29

**Description**:
Enables high hold torque when the robot is stationary. This function is used to reverse the behavior of the
high_holding_torque_disable() command.

**Parameters**:
- None

**Return Value**: `None`

**Example**:
```urscript
Example command:
high_holding_torque_enable()
See also
high_holding_torque_disable()
```

---

<a id="is_steady"></a>
### `is_steady()`
**Section**: URScript 15.1.30

**Description**:
The function will return true when the robot has been standing still with zero target velocity for 500ms
When the function returns true, the robot is able to adapt to large external forces and torques, e.g. from
screwdrivers, without issuing a protective stop.

**Parameters**:
- *None / No arguments required.*

**Return Value**:
True when the robot able to adapt to external forces, false otherwise (bool)

---

<a id="is_within_safety_limits"></a>
### `is_within_safety_limits(pose, qnear)`
**Section**: URScript 15.1.31

**Description**:
Checks if the given pose or q is reachable and within the current safety limits of the robot.
This check considers joint limits (if the target pose is specified as joint positions), TCP orientation limit and
range of the robot.
If a solution is found when applying the inverse kinematics to the given target TCP pose, this pose is
considered reachable.

**Parameters**:
- **`pose`**: Target pose or joint position
- **`qnear`**: list of joint positions (Optional) Only used when target is a pose

**Return Value**:
True if within limits, false otherwise (bool)
Deprecated: This function is deprecated, since it does not apply the same algorithm as get_inverse_
kin. It is recommended to use get_inverse_kin_has_solution instead.

---

<a id="popup"></a>
### `popup(s, title=’Popup’, warning=False, error=False, blocking=False)`
**Section**: URScript 15.1.32

**Description**:
Display popup on GUI
Display message in popup window on GUI.

**Parameters**:
- **`s`**: message string
- **`title`**: title string
- **`warning`**: warning message?
- **`error`**: error message?
- **`blocking`**: if True, program will be suspended until "continue" is pressed

**Return Value**: `None`

**Example**:
```urscript
Example command: popup("here I am", title="Popup #1",blocking=True)
• Example Parameters:
• s popup text is "here I am"
• title popup title is "Popup #1"
• blocking = true -> popup must be cleared before other actions will be performed.
```

---

<a id="powerdown"></a>
### `powerdown()`
**Section**: URScript 15.1.33

**Description**:
Shut down the robot, and power off the robot and controller.

**Parameters**:
- *None / No arguments required.*

**Return Value**: `None`

---

<a id="protective_stop"></a>
### `protective_stop()`
**Section**: URScript 15.1.34

**Description**:
Trigger a protective stop, pausing the program and stopping motion on the planned trajectory.
Notes:
This function is not intended for use for simply pausing the running program (see Special keywords:
pause).

**Parameters**:
- *None / No arguments required.*

**Return Value**: `None`

---

<a id="set_base_acceleration"></a>
### `set_base_acceleration(a)`
**Section**: URScript 15.1.35

**Description**:
Sets the acceleration of the robot base. This function is used when the robot is attached to a moving base
such a linear rail or vertical lift. Specifying the base acceleration is used to prevent premature protective
stops by informing the control system that forces are being exerted on the robot through acceleration of
the base.

**Parameters**:
- **`a`**: the linear acceleration of the base in x, y, z directions

**Return Value**: `None`

**Example**:
```urscript
Example command:
set_base_acceleration([0.10 0.0 0.0])
Example Parameters:
a = [0.10 0 0] specifies acceleration in the linear X direction of 0.10 m/s²
```

---

<a id="set_baselight_off"></a>
### `set_baselight_off()`
**Section**: URScript 15.1.36

**Description**:
NOTICE
Only applies to UR20 / UR30
Turns the baselight completely off.

**Parameters**:
- *None / No arguments required.*

**Return Value**: `None`

---

<a id="set_baselight_iec"></a>
### `set_baselight_iec()`
**Section**: URScript 15.1.37

**Description**:
NOTICE
Only applies to UR20 / UR30
Make the baselight comply to the IEC 60204-1 standard and indicate whether the robot is in a safety stop,
in freedrive as well as the operational mode. Further details of the colors can be seen in the UR20 manual.

**Parameters**:
- *None / No arguments required.*

**Return Value**: `None`

---

<a id="set_baselight_solid"></a>
### `set_baselight_solid(r,g,b)`
**Section**: URScript 15.1.38

**Description**:
NOTICE
Only applies to UR20 / UR30
Set a color on the entire baselight ring as specified by the given RGB values in the range 0-255.

**Parameters**:
- *None / No arguments required.*

**Return Value**: `None`

---

<a id="set_gravity"></a>
### `set_gravity(d)`
**Section**: URScript 15.1.39

**Description**:
Set the direction of the acceleration experienced by the robot. When the robot mounting is fixed, this
corresponds to an accleration of g away from the earth’s centre.

**Parameters**:
- **`d`**: 3D vector, describing the direction of the gravity, relative to the base of the robot.

**Return Value**: `None`

**Example**:
```urscript
set_gravity([0, 9.82*sin(theta), 9.82*cos(theta)])
will set the acceleration for a robot that is rotated "theta" radians around the x-axis of the robot base
coordinate system
Example command: set_gravity[(0,9.82,0)]
• Example Parameters:
```

---

<a id="set_payload"></a>
### `set_payload(m, cog)`
**Section**: URScript 15.1.40

**Description**: *Executes built-in URScript operation.*

**Parameters**:
- **`m`**: mass in kilograms
- **`cog`**: Center of Gravity, a vector [CoGx, CoGy, CoGz] specifying the displacement (in meters) from the toolmount.
- **`Deprecated`**: See set_target_payload to set mass, CoG and payload inertia matrix at the same time. Set payload mass and center of gravity while resetting payload inertia matrix Sets the mass and center of gravity (abbr. CoG) of the payload. This function must be called, when the payload mass or mass CoG offset changes - i.e. when the robot picks up or puts down a workpiece.

**Return Value**: `None`

> [!NOTE]
> Note: The force torque measurements are automatically zeroed when setting the payload. That ensures
> the readings are compensated for the payload. This is similar to the behavior of zero_ftsensor()
> Warnings:
> • This script is deprecated since SW 5.10.0 because of the risk of inconsistent payload parameters.
> Use the set_target_payload instead to set mass, CoG and inertia matrix.
> • Omitting the cog parameter is not recommended. The Tool Center Point (TCP) will be used if the
> cog parameter is missing with the side effect that later calls to set_tcp will change also the CoG to
> the new TCP. Use the set_payload_mass function to change only the mass or use the get_
> target_payload_cog as second argument to not change the CoG.
> • Using this script function to modify payload parameters will reset the payload inertia matrix.

**Example**:
```urscript
Example command:
• d is vector with a direction of y (direction of the robot cable) and a magnitude of 9.82 m/s^2
(1g).
• set_payload(3., [0,0,.3])
• Example Parameters:
• m = 3 → mass is set to 3 kg payload
• cog = [0,0,.3] Center of Gravity is set to x=0 mm, y=0 mm, z=300 mm from the
center of the tool mount in tool coordinates
• set_payload(2.5, get_target_payload_cog())
• Example Parameters:
• m = 2.5 → mass is set to 2.5 kg payload
• cog = use the current COG setting
```

---

<a id="set_payload_cog"></a>
### `set_payload_cog(CoG)`
**Section**: URScript 15.1.41

**Description**:
Deprecated: See set_target_payload to set mass, CoG and payload inertia matrix at the same time.
Set the Center of Gravity (CoG) and reset payload inertia matrix
Warning: Using this script function to modify payload parameters will reset the payload inertia matrix.

**Parameters**:
- *None / No arguments required.*

**Return Value**: `None`

> [!NOTE]
> Note: The force torque measurements are automatically zeroed when setting the payload. That ensures
> the readings are compensated for the payload. This is similar to the behavior of zero_ftsensor()

---

<a id="set_payload_mass"></a>
### `set_payload_mass(m)`
**Section**: URScript 15.1.42

**Description**: *Executes built-in URScript operation.*

**Parameters**:
- **`m`**: mass in kilograms
- **`Deprecated`**: See set_target_payload to set mass, CoG and payload inertia matrix at the same time. Set payload mass and reset payload inertia matrix See also set_payload. Sets the mass of the payload and leaves the center of gravity (CoG) unchanged.

**Return Value**: `None`

> [!NOTE]
> Note: The force torque measurements are automatically zeroed when setting the payload. That ensures
> the readings are compensated for the payload. This is similar to the behavior of zero_ftsensor()
> Warnings:
> • This script is deprecated since SW 5.10.0 because of the risk of inconsistent payload parameters.
> Use the set_target_payload instead to set mass, CoG and inertia matrix.
> • Using this script function to modify payload parameters will reset the payload inertia matrix.

---

<a id="set_target_payload"></a>
### `set_target_payload(m, cog, inertia=[0, 0, 0, 0, 0, 0], transition_time=0)`
**Section**: URScript 15.1.43

**Description**:
Sets the mass, CoG (center of gravity), the inertia matrix of the active payload and the transition time for
applying new settings.
This function must be called when the payload mass, the mass displacement (CoG) or the inertia matrix
changes - (i.e. when the robot picks up or puts down a workpiece).

**Parameters**:
- **`m`**: mass in kilograms.
- **`cog`**: Center of Gravity, a vector with three elements [CoGx, CoGy, CoGz] specifying the offset (in meters) from the tool mount.
- **`transition_time`**: the duration of the payload property changes in seconds
- **`Notes`**: • This script should be used instead of the deprecated set_payload, set_payload_mass, and set_payload_cog. • The payload mass and CoG are required, the inertia matrix and transition time are optional. • When inertia matrix is left out, a zero matrix will be used. • When transition time is left out, the change will be applied instantaneously, identically to how the deprecated set_payload, set_payload_mass and set_payload_cog work. • The maximum value allowed for each of the components of the inertia matrix is +/- 133 kg*m^2. An exception is thrown if limits are exceeded. • The first three elements of the inertia matrix (i.e. Ixx, Iyy, Izz) cannot be negative. An exception is thrown if either value is negative. • The force/torque measurements are automatically zeroed when setting the payload. That ensures the readings are compensated for the payload. This is similar to the behaviour of zero_ftsensor (). • Setting a transition time larger than zero avoids the robot doing a small "jump" when payload changes. This is useful when picking up or releasing heavy objects. • The internal force/torque sensor in the robot tool is reset each time the payload is updated. This means that the final reset will be performed at the end of the payload transition time. If the payload is being accelerated at the time of the final reset, the force/torque measurement will be affected. It's always recommended to call zero_ftsensor() to reset the force/torque sensor before using it, e.g. in Force Mode.

**Return Value**: `None`

---

<a id="set_tcp"></a>
### `set_tcp(pose, tcp_name="")`
**Section**: URScript 15.1.44

**Description**:
Sets the active tcp offset, i.e., the transformation from the output flange coordinate system to the TCP as a
pose, and assigns a name to the TCP. If no name is provided, the default name is an empty string.

**Parameters**:
- **`inertia`**: payload inertia matrix (in kg*m^2), as a vector with six elements [Ixx, Iyy, Izz, Ixy, Ixz, Iyz] with origin in the CoG and the axes aligned with the tool flange axes. • pose: A pose describing the transformation. • tcp_name (optional, default=""): A string that assigns a name to the TCP.

**Return Value**: `None`

**Example**:
```urscript
Example command: set_tcp(p[0.,.2,.3,0.,3.14,0.], "custom_tcp_name")
• Example Parameters:
• pose = p[0.,.2,.3,0.,3.14,0.] -> tool center point is set to x=0mm, y=200mm, z=300mm,
rotation vector is rx=0 deg, ry=180 deg, rz=0 deg. In tool coordinates.
• tcp_name = "custom_tcp_name" -> the name assigned to the TCP.
```

---

<a id="sleep"></a>
### `sleep(t)`
**Section**: URScript 15.1.45

**Description**:
Sleep for an amount of time

**Parameters**:
- **`t`**: time [s]

**Return Value**: `None`

**Example**:
```urscript
Example command: sleep(3.)
• Example Parameters:
• t = 3. -> time to sleep
```

---

<a id="str_at"></a>
### `str_at(src, index)`
**Section**: URScript 15.1.46

**Description**:
Provides direct access to the bytes of a string.
This script returns a string containing the byte in the source string at the position corresponding to the
specified index. It may not correspond to an actual character in case of strings with special encoded
character (i.e. multi-byte or variable-length encoding)
The string is zero-indexed.

**Parameters**:
- **`src`**: source string.
- **`index`**: integer specifying the position inside the source string.

**Return Value**:
String containing the byte at position index in the source string. An exception is raised if the index is not
valid.

**Example**:
```urscript
Example command:
• str_at("Hello", 0)
• returns "H"
• str_at("Hello", 1)
• returns "e"
• str_at("Hello", 10)
• error (index out of bound)
• str_at("", 0)
• error (source string is empty)
```

---

<a id="str_cat"></a>
### `str_cat(op1, op2)`
**Section**: URScript 15.1.47

**Description**:
String concatenation
This script returns a string that is the concatenation of the two operands given as input. Both operands can
be one of the following types: String, Boolean, Integer, Float, Pose, List of Boolean / Integer / Float /
Pose. Any other type will raise an exception.
The resulting string cannot exceed 1023 characters, an exception is thrown otherwise.
Float numbers will be formatted with 6 decimals, and trailing zeros will be removed.
The function can be nested to create complex strings (see last example).

**Parameters**:
- **`op1`**: first operand
- **`op2`**: second operand

**Return Value**:
String concatenation of op1 and op2

**Example**:
```urscript
Example command:
• str_cat("Hello", " World!")
• returns "Hello World!"
• str_cat("Integer ", 1)
• returns "Integer 1"
• str_cat("", p[1.0, 2.0, 3.0, 4.0, 5.0, 6.0])
• returns "p[1, 2, 3, 4, 5, 6]"
• str_cat([True, False, True], [1, 0, 1])
• returns "[True, False, True][1, 0, 1]"
• str_cat(str_cat("", str_cat("One", "Two")),str_cat(3, 4))
• returns "OneTwo34"
```

---

<a id="str_empty"></a>
### `str_empty(str)`
**Section**: URScript 15.1.48

**Description**:
Returns true when str is empty, false otherwise.

**Parameters**:
- **`str`**: source string.

**Return Value**:
True if the string is empty, false otherwise

**Example**:
```urscript
Example command:
• str_empty("")
• returns True
• str_empty("Hello")
• returns False
```

---

<a id="str_find"></a>
### `str_find(src, target, start_from=0)`
**Section**: URScript 15.1.49

**Description**:
Finds the first occurrence of the substring target in src.
This script returns the index (i.e. byte) of the the first occurrence of substring target in str, starting from
the given (optional) position.
The result may not correspond to the actual position of the first character of target in case src contains
multi-byte or variable-length encoded characters.
The string is zero-indexed.

**Parameters**:
- **`src`**: source string.
- **`target`**: substring to search.
- **`start_from`**: optional starting position (default 0).

**Return Value**:
The index of the first occurrence of target in src, -1 if target is not found in src.

**Example**:
```urscript
Example command:
• str_find("Hello World!", "o")
• returns 4
• str_find("Hello World!", "lo")
• returns 3
• str_find("Hello World!", "o", 5)
• returns 7
• str_find("abc", "z")
• returns -1
```

---

<a id="str_len"></a>
### `str_len(str)`
**Section**: URScript 15.1.50

**Description**:
Returns the number of bytes in a string.
Please not that the value returned may not correspond to the actual number of characters in sequences of
multi-byte or variable-length encoded characters.
The string is zero-indexed.

**Parameters**:
- **`str`**: source string.
- **`src`**: source string.
- **`index`**: integer value specifying the initial byte in the range [0, src length]
- **`len`**: (optional) length of the substring in the range [0, MAX_INT]. If len is not specified, the string in the range [index, src length].

**Return Value**:
The number of bytes in the input string.
the portion of src that starts at byte index and spans len characters.

**Example**:
```urscript
Example command:
• str_len("Hello")
• returns 5
• str_len("")
• returns 0
Returns a substring of src.
The result is the substring of src that starts at the byte specified by index with length of at most len bytes.
If the requested substring extends past the end of the original string (i.e. index + len > src
length), the length of the resulting substring is limited to the size of src.
An exception is thrown in case index and/or len are out of bounds. The string is zero-indexed.
Example command:
• str_sub("0123456789abcdefghij", 5, 3)
• returns "567"
• str_sub("0123456789abcdefghij", 10)
• returns "abcdefghij"
• str_sub("0123456789abcdefghij", 2, 0)
• returns "" (len is 0)
• str_sub("abcde", 2, 50)
• returns "cde"
• str_sub("abcde", -5, 50)
• error: index is out of bounds
```

---

<a id="str_sub"></a>
### `str_sub(src, index, len)`
**Section**: URScript 15.1.51

**Description**: *Executes built-in URScript operation.*

**Parameters**:
- *None / No arguments required.*

**Return Value**: `None`

---

<a id="sync"></a>
### `sync()`
**Section**: URScript 15.1.52

**Description**:
Uses up the remaining "physical" time a thread has in the current frame.

**Parameters**:
- *None / No arguments required.*

**Return Value**: `None`

---

<a id="textmsg"></a>
### `textmsg(s1, s2=’’)`
**Section**: URScript 15.1.53

**Description**:
Send text message to log
Send message with s1 and s2 concatenated to be shown on the PolyScope log-tab.
The PolyScope log-tab is intended for general application status.
It is not recommended to add many messages at a high rate.

**Parameters**:
- **`s1`**: message string, variables of other types (int, bool poses etc.) can also be sent
- **`s2`**: message string, variables of other types (int, bool poses etc.) can also be sent

**Return Value**: `None`

**Example**:
```urscript
Example command: textmsg("value=", 3)
• Example Parameters:
• s1 set first part of message to "value="
• s2 set second part of message to 3
• message in the log is "value=3"
```

---

<a id="to_num"></a>
### `to_num(str )`
**Section**: URScript 15.1.54

**Description**:
Converts a string to a number.
to_num returns an integer or a float depending on the presence of a decimal point in the input string. Only
’.’ is recognized as decimal point independent of locale settings.
Valid strings can contains optional leading white space(s) followed by an optional plus (’+’) or minus sign
(’-’) and then one of the following:
(i) A decimal number consisting of a sequence of decimal digits (e.g. 10, -5), an optional ’.’ to indicate a
float number (e.g. 1.5234, -2.0, .36) and a optional decimal exponent that indicates multiplication by a
power of 10 (e.g. 10e3, 2.5E-5, -5e-4).
(ii) A hexadecimal number consisting of "0x" or "0X" followed by a nonempty sequence of hexadecimal
digits (e.g. "0X3A", "0xb5").
(iii) An infinity (either "INF" or "INFINITY", case insensitive)
(iv) A Not-a-Number ("NAN", case insensitive)
Runtime exceptions are raised if the source string doesn’t contain a valid number or the result is out of
range for the resulting type.

**Parameters**:
- **`str`**: string to convert

**Return Value**:
Integer or float number according to the input string.

**Example**:
```urscript
Example command:
• to_num("10")
• returns 10 //integer
• to_num("3.14")
• returns 3.14 //float
• to_num("-3.0e5")
• returns -3.0e5 //float due to ’.’ in the input string
• to_num("+5.")
• returns 5.0 //float due to ’.’ in the input string
• to_num("123abc")
• error string doesn’t contain a valid number
```

---

<a id="to_str"></a>
### `to_str(val)`
**Section**: URScript 15.1.55

**Description**:
Gets string representation of a value.
This script converts a value of type Boolean, Integer, Float, Pose (or a list of those types) to a string.
The resulting string cannot exceed 1023 characters.
Float numbers will be formatted with 6 decimals, and trailing zeros will be removed.

**Parameters**:
- **`val`**: value to convert

**Return Value**:
The string representation of the given value.

**Example**:
```urscript
Example command:
• to_str(10)
• returns "10"
• to_str(2.123456123456)
• returns "2.123456"
• to_str(p[1.0, 2.0, 3.0, 4.0, 5.0, 6.0])
• returns "p[1, 2, 3, 4, 5, 6]"
• to_str([True, False, True])
• returns "[True, False, True]"
```

---

<a id="tool_contact"></a>
### `tool_contact(direction)`
**Section**: URScript 15.1.56

**Description**:
Detects when a contact between the tool and an object happens.

**Parameters**:
- **`direction`**: List of six floats. The first three elements are interpreted as a 3D vector (in the robot base coordinate system) giving the direction in which contacts should be detected. If all elements of the list are zero, contacts from all directions are considered.

**Return Value**:
Integer. The returned value is the number of time steps back to just before the contact have started. A
value larger than 0 means that a contact is detected. A value of 0 means no contact.

---

<a id="tool_contact_examples"></a>
### `tool_contact_examples()`
**Section**: URScript 15.1.57

**Description**:
Example of usage in conjunction with the "get_actual_joint_positions_history()" function to allow the robot
to retract to the initial point of contact:

**Parameters**:
- *None / No arguments required.*

**Return Value**: `None`

**Example**:
```urscript
def testToolContact():
while True:
step_back = tool_contact()
if step_back <= 0:
# Continue moving with 100mm/s
speedl([0,0,-0.100,0,0,0], 0.5, t=get_steptime())
else:
# Contact detected!
# Get q for when the contact was first seen
q = get_actual_joint_positions_history(step_back)
# Stop the movement
stopl(3)
# Move to the initial contact point
movel(q)
break
end
end
end
Example command: tool_contact(direction = get_target_tcp_speed())
• Example Parameters:
• direction=get_target_tcp_speed() will detect contacts in the direction of TCP movement
tool_contact(direction = [1,0,0,0,0,0])
• Example Parameters:
• direction=[1,0,0,0,0,0] will detect contacts in the direction robot base X
16.1. Functions
```

---

## Navigation

[⬅️ Back to Table of Contents](../README.md)
