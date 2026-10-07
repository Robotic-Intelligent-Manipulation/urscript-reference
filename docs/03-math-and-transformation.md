# Module URMath (Spatial Math & Kinematic Transformations)

> **Reference Module**: URScript Specification (Chapter 16)
> **Total Functions**: 35 functions
> **Target Controllers**: Universal Robots e-Series, UR20, UR30, CB-Series (SW 5.16+)

## Overview

Spatial mathematics and transformation utilities for robotics. Covers 3D pose algebra where rotations are represented in axis-angle rotation vectors r = theta * u (in radians), analytic/numerical forward and inverse kinematics (`get_forward_kin`, `get_inverse_kin`), pose interpolation, vector operations, and trigonometry.

## Function Index (35 Functions)

- [`acos(f )`](#acos)
- [`asin(f )`](#asin)
- [`atan(f )`](#atan)
- [`atan2(x, y)`](#atan2)
- [`binary_list_to_integer(l)`](#binary_list_to_integer)
- [`ceil(f )`](#ceil)
- [`cos(f )`](#cos)
- [`d2r(d)`](#d2r)
- [`floor(f )`](#floor)
- [`make_list(length, initial_value, capacity=length)`](#make_list)
- [`get_list_length(v)`](#get_list_length)
- [`integer_to_binary_list(x)`](#integer_to_binary_list)
- [`interpolate_pose(p_from, p_to, alpha)`](#interpolate_pose)
- [`inv(m)`](#inv)
- [`length(v)`](#length)
- [`log(b, f )`](#log)
- [`norm(a)`](#norm)
- [`normalize(v)`](#normalize)
- [`point_dist(p_from, p_to)`](#point_dist)
- [`pose_add(p_1, p_2)`](#pose_add)
- [`pose_dist(p_from, p_to)`](#pose_dist)
- [`pose_inv(p_from)`](#pose_inv)
- [`pose_sub(p_to, p_from)`](#pose_sub)
- [`pose_trans(p_from, p_from_to)`](#pose_trans)
- [`pow(base, exponent)`](#pow)
- [`r2d(r)`](#r2d)
- [`random()`](#random)
- [`rotvec2rpy(rotation_vector)`](#rotvec2rpy)
- [`rpy2rotvec(rpy_vector)`](#rpy2rotvec)
- [`sin(f )`](#sin)
- [`size(v)`](#size)
- [`sqrt(f )`](#sqrt)
- [`tan(f)`](#tan)
- [`transpose(m)`](#transpose)
- [`wrench_trans(T_from_to, w_from)`](#wrench_trans)

---

## API Documentation

<a id="acos"></a>
### `acos(f )`
**Section**: URScript 16.1.1

**Description**:
Returns the arc cosine of f
Returns the principal value of the arc cosine of f, expressed in radians. A runtime error is raised if f lies
outside the range [-1, 1].

**Parameters**:
- **`f`**: floating point value

**Return Value**:
the arc cosine of f.

**Example**:
```urscript
Example command: acos(0.707)
• Example Parameters:
• f is the cos of 45 deg. (.785 rad)
• Returns .785
```

---

<a id="asin"></a>
### `asin(f )`
**Section**: URScript 16.1.2

**Description**:
Returns the arc sine of f
Returns the principal value of the arc sine of f, expressed in radians. A runtime error is raised if f lies
outside the range [-1, 1].

**Parameters**:
- **`f`**: floating point value

**Return Value**:
the arc sine of f.

**Example**:
```urscript
Example command: asin(0.707)
• Example Parameters:
• f is the sin of 45 deg. (.785 rad)
• Returns .785
```

---

<a id="atan"></a>
### `atan(f )`
**Section**: URScript 16.1.3

**Description**:
Returns the arc tangent of f
Returns the principal value of the arc tangent of f, expressed in radians.

**Parameters**:
- **`f`**: floating point value

**Return Value**:
the arc tangent of f.

**Example**:
```urscript
Example command: atan(1.)
• Example Parameters:
• f is the tan of 45 deg. (.785 rad)
• Returns .785
```

---

<a id="atan2"></a>
### `atan2(x, y)`
**Section**: URScript 16.1.4

**Description**:
Returns the arc tangent of x/y
Returns the principal value of the arc tangent of x/y, expressed in radians. To compute the value, the
function uses the sign of both arguments to determine the quadrant.

**Parameters**:
- **`x`**: floating point value
- **`y`**: floating point value

**Return Value**:
the arc tangent of x/y.

**Example**:
```urscript
Example command: atan2(.5,.5)
• Example Parameters:
• x is the one side of the triangle
• y is the second side of a triangle
• Returns atan(.5/.5) = .785
```

---

<a id="binary_list_to_integer"></a>
### `binary_list_to_integer(l)`
**Section**: URScript 16.1.5

**Description**:
Returns the value represented by the content of list l
Returns the integer value represented by the bools contained in the list l when evaluated as a signed
binary number.

**Parameters**:
- **`l`**: The list of bools to be converted to an integer. The bool at index 0 is evaluated as the least significant bit. False represents a zero and True represents a one. If the list is empty this function returns 0. If the list contains more than 32 bools, the function returns the signed integer value of the first 32 bools in the list.

**Return Value**:
The integer value of the binary list content.

**Example**:
```urscript
Example command: binary_list_to_integer([True,False,False,True])
• Example Parameters:
• l represents the binary values 1001
• Returns 9
```

---

<a id="ceil"></a>
### `ceil(f )`
**Section**: URScript 16.1.6

**Description**:
Returns the smallest integer value that is not less than f
Rounds floating point number to the smallest integer no greater than f.

**Parameters**:
- **`f`**: floating point value

**Return Value**:
rounded integer

**Example**:
```urscript
Example command: ceil(1.43)
• Example Parameters:
• Returns 2
```

---

<a id="cos"></a>
### `cos(f )`
**Section**: URScript 16.1.7

**Description**:
Returns the cosine of f
Returns the cosine of an angle of f radians.

**Parameters**:
- **`f`**: floating point value

**Return Value**:
the cosine of f.

**Example**:
```urscript
Example command: cos(1.57)
• Example Parameters:
• f is angle of 1.57 rad (90 deg)
• Returns 0.0
```

---

<a id="d2r"></a>
### `d2r(d)`
**Section**: URScript 16.1.8

**Description**:
Returns degrees-to-radians of d
Returns the radian value of ’d’ degrees. Actually: (d/180)*MATH_PI

**Parameters**:
- **`d`**: The angle in degrees

**Return Value**:
The angle in radians

**Example**:
```urscript
Example command: d2r(90)
• Example Parameters:
• d angle in degrees
• Returns 1.57 angle in radians
```

---

<a id="floor"></a>
### `floor(f )`
**Section**: URScript 16.1.9

**Description**:
Returns largest integer not greater than f

**Parameters**:
- **`f`**: floating point value

**Return Value**:
rounded integer

**Example**:
```urscript
Example command: floor(1.53)
• Example Parameters:
• Returns 1
```

---

<a id="make_list"></a>
### `make_list(length, initial_value, capacity=length)`
**Section**: URScript 16.1.10

**Description**:
Create a new list of length "length" with the initial value of each element given by "initial_value" and assign
it to a variable.
The "initial_value" sets the type of the list. It can be a complex type like struct. If not provided, the
"capacity" will be defaulted to "length".
Creation list of list with this function is not supported (they are matrices in URScript).

**Parameters**:
- **`length`**: Number of elements which will be initialized
- **`initial_value`**: Initial value of the elements
- **`capacity`**: Maximum number of elements. List can be extended and contracted between 0, and capacity (Optional default value equals to length) Example command 1: list_1 = make_list(5, "a") Equivalent to ["a", "a", "a", "a", "a"] Rounds floating point number to the largest integer no greater than f. • Example Parameters: • length = 5 • initial_value = "a" • capacity = 5 Example command 2: list_2 = make_list(10, 0, 100) • Example Parameters: • length = 10 • initial_value = 0 • capacity = 100 Example command 3: list_3 = make_list(0, 0, 100) Create an initially empty list with the potential to hold 100 elements of integers. • Example Parameters: • length = 0 • initial_value = 0 • capacity = 100

**Return Value**: `None`

---

<a id="get_list_length"></a>
### `get_list_length(v)`
**Section**: URScript 16.1.11

**Description**:
Returns the length of a list variable
The length of a list is the number of entries the list is composed of.

**Parameters**:
- **`v`**: A list variable

**Return Value**:
An integer specifying the length of the given list

**Example**:
```urscript
Example command: get_list_length([1,3,3,6,2])
• Example Parameters:
• v is the list 1,3,3,6,2
• Returns 5
```

---

<a id="integer_to_binary_list"></a>
### `integer_to_binary_list(x)`
**Section**: URScript 16.1.12

**Description**:
Returns the binary representation of x
Returns a list of bools as the binary representation of the signed integer value x.

**Parameters**:
- **`x`**: The integer value to be converted to a binary list.

**Return Value**:
A list of 32 bools, where False represents a zero and True represents a one. The bool at index 0 is the
least significant bit.

**Example**:
```urscript
Example command: integer_to_binary_list(57)
• Example Parameters:
• x integer 57
• Returns binary list
```

---

<a id="interpolate_pose"></a>
### `interpolate_pose(p_from, p_to, alpha)`
**Section**: URScript 16.1.13

**Description**:
When alpha is 0, returns p_from. When alpha is 1, returns p_to. As alpha goes from 0 to 1, returns a pose
going in a straight line (and geodetic orientation change) from p_from to p_to. If alpha is less than 0,
returns a point before p_from on the line. If alpha is greater than 1, returns a pose after p_to on the line.

**Parameters**:
- **`p_from`**: tool pose (pose)
- **`p_to`**: tool pose (pose)
- **`alpha`**: Floating point number

**Return Value**:
interpolated pose (pose)

**Example**:
```urscript
Example command: interpolate_pose(p[.2,.2,.4,0,0,0], p[.2,.2,.6,0,0,0], .5)
• Example Parameters:
• p_from = p[.2,.2,.4,0,0,0]
• p_to = p[.2,.2,.6,0,0,0]
• alpha = .5
• Returns p[.2,.2,.5,0,0,0]
```

---

<a id="inv"></a>
### `inv(m)`
**Section**: URScript 16.1.14

**Description**:
Get the inverse of a matrix or pose
The matrix must be square and non singular.

**Parameters**:
- **`m`**: matrix or pose (spatial vector)

**Return Value**:
inverse matrix or pose transformation (spatial vector)

**Example**:
```urscript
Example command:
Linear interpolation of tool position and orientation.
• inv([[0,1,0],[0,0,1],[1,0,0]]) -> Returns [[0,0,1],[1,0,0],[0,1,0]]
• inv(p[.2,.5,.1,1.57,0,3.14]) -> Returns p[0.19324,0.41794,0.29662,1.23993,0.0,2.47985]
```

---

<a id="length"></a>
### `length(v)`
**Section**: URScript 16.1.15

**Description**:
Returns the length of a list variable or a string
The length of a list or string is the number of entries or characters it is composed of.

**Parameters**:
- **`v`**: A list or string variable

**Return Value**:
An integer specifying the length of the given list or string

**Example**:
```urscript
Example command: length("here I am")
• Example Parameters:
• v equals string "here I am"
• Returns 9
```

---

<a id="log"></a>
### `log(b, f )`
**Section**: URScript 16.1.16

**Description**:
Returns the logarithm of f to the base b
Returns the logarithm of f to the base b. If b or f is negative, or if b is 1 a runtime error is raised.

**Parameters**:
- **`b`**: floating point value
- **`f`**: floating point value

**Return Value**:
the logarithm of f to the base of b.

**Example**:
```urscript
Example command: log(10.,4.)
• Example Parameters:
• b is base 10
• f is log of 4
• Returns 0.60206
```

---

<a id="norm"></a>
### `norm(a)`
**Section**: URScript 16.1.17

**Description**:
Returns the norm of the argument
The argument can be one of four different types:
Pose: In this case the euclidian norm of the pose is returned.
Float: In this case fabs(a) is returned.
Int: In this case abs(a) is returned.
List: In this case the euclidian norm of the list is returned, the list elements must be numbers.

**Parameters**:
- **`a`**: Pose, float, int or List

**Return Value**:
norm of a

**Example**:
```urscript
Example command:
• norm(-5.3) -> Returns 5.3
• norm(p[-.2,.2,-.2,-1.57,0,3.14]) -> Returns 3.52768
```

---

<a id="normalize"></a>
### `normalize(v)`
**Section**: URScript 16.1.18

**Description**:
Returns the normalized form of a list of floats
Except for the case of all zeroes, the normalized form corresponds to the unit vector in the direction of v.
Throws an exception if the sum of all squared elements is zero.

**Parameters**:
- **`v`**: List of floats

**Return Value**:
normalized form of v

**Example**:
```urscript
Example command:
• normalize([1, 0, 0]) -> Returns [1, 0, 0]
• normalize([0, 5, 0]) -> Returns [0, 1, 0]
• normalize([0, 1, 1]) -> Returns [0, 0.707, 0.707]
```

---

<a id="point_dist"></a>
### `point_dist(p_from, p_to)`
**Section**: URScript 16.1.19

**Description**:
Point distance

**Parameters**:
- **`p_from`**: tool pose (pose)
- **`p_to`**: tool pose (pose)

**Return Value**:
• norm(-8) -> Returns 8
Distance between the two tool positions (without considering rotations)

**Example**:
```urscript
Example command: point_dist(p[.2,.5,.1,1.57,0,3.14], p[.2,.5,.6,0,1.57,3.14])
• Example Parameters:
• p_from = p[.2,.5,.1,1.57,0,3.14] -> The first point
• p_to = p[.2,.5,.6,0,1.57,3.14] -> The second point
• Returns distance between the points regardless of rotation
```

---

<a id="pose_add"></a>
### `pose_add(p_1, p_2)`
**Section**: URScript 16.1.20

**Description**:
Pose addition
Both arguments contain three position parameters (x, y, z) jointly called P, and three rotation parameters
(R_x, R_y, R_z) jointly called R. This function calculates the result x_3 as the addition of the given poses
as follows:
p_3.P = p_1.P + p_2.P
p_3.R = p_1.R * p_2.R

**Parameters**:
- **`p_1`**: tool pose 1(pose)
- **`p_2`**: tool pose 2 (pose)

**Return Value**:
Sum of position parts and product of rotation parts (pose)

**Example**:
```urscript
Example command: pose_add(p[.2,.5,.1,1.57,0,0], p[.2,.5,.6,1.57,0,0])
• Example Parameters:
• p_1 = p[.2,.5,.1,1.57,0,0] -> The first point
• p_2 = p[.2,.5,.6,1.57,0,0] -> The second point
• Returns p[0.4,1.0,0.7,3.14,0,0]
```

---

<a id="pose_dist"></a>
### `pose_dist(p_from, p_to)`
**Section**: URScript 16.1.21

**Description**:
Pose distance

**Parameters**:
- **`p_from`**: tool pose (pose)
- **`p_to`**: tool pose (pose)

**Return Value**:
distance

**Example**:
```urscript
Example command: pose_dist(p[.2,.5,.1,1.57,0,3.14], p[.2,.5,.6,0,1.57,3.14])
• Example Parameters:
• p_from = p[.2,.5,.1,1.57,0,3.14] -> The first point
• p_to = p[.2,.5,.6,0,1.57,3.14] -> The second point
• Returns distance between two poses including rotation
```

---

<a id="pose_inv"></a>
### `pose_inv(p_from)`
**Section**: URScript 16.1.22

**Description**:
Get the inverse of a pose

**Parameters**:
- **`p_from`**: tool pose (spatial vector)

**Return Value**:
inverse tool pose transformation (spatial vector)

**Example**:
```urscript
Example command: pose_inv(p[.2,.5,.1,1.57,0,3.14])
• Example Parameters:
• p_from = p[.2,.5,.1,1.57,0,3.14] -> The point
• Returns p[0.19324,0.41794,-0.29662,1.23993,0.0,2.47985]
```

---

<a id="pose_sub"></a>
### `pose_sub(p_to, p_from)`
**Section**: URScript 16.1.23

**Description**:
Pose subtraction

**Parameters**:
- **`p_to`**: tool pose (spatial vector)
- **`p_from`**: tool pose (spatial vector)

**Return Value**:
tool pose transformation (spatial vector)

**Example**:
```urscript
Example command: pose_sub(p[.2,.5,.1,1.57,0,0], p[.2,.5,.6,1.57,0,0])
• Example Parameters:
• p_1 = p[.2,.5,.1,1.57,0,0] -> The first point
• p_2 = p[.2,.5,.6,1.57,0,0] -> The second point
• Returns p[0.0,0.0,-0.5,0.0,.0.,0.0]
```

---

<a id="pose_trans"></a>
### `pose_trans(p_from, p_from_to)`
**Section**: URScript 16.1.24

**Description**:
Pose transformation
The first argument, p_from, is used to transform the second argument, p_from_to, and the result is then
returned. This means that the result is the resulting pose, when starting at the coordinate system of p_
from, and then in that coordinate system moving p_from_to.
This function can be seen in two different views. Either the function transforms, that is translates and
rotates, p_from_to by the parameters of p_from. Or the function is used to get the resulting pose, when
first making a move of p_from and then from there, a move of p_from_to.
If the poses were regarded as transformation matrices, it would look like:
T_world->to = T_world->from * T_from->to T_x->to = T_x->from * T_from->to

**Parameters**:
- **`p_from`**: starting pose (spatial vector)
- **`p_from_to`**: pose change relative to starting pose (spatial vector)

**Return Value**:
resulting pose (spatial vector)

**Example**:
```urscript
Example command: pose_trans(p[.2,.5,.1,1.57,0,0], p[.2,.5,.6,1.57,0,0])
• Example Parameters:
• p_1 = p[.2,.5,.1,1.57,0,0] → The first point
• p_2 = p[.2,.5,.6,1.57,0,0] → The second point
• Returns p[0.4,-0.0996,0.60048,3.14,0.0,0.0]
```

---

<a id="pow"></a>
### `pow(base, exponent)`
**Section**: URScript 16.1.25

**Description**:
Returns base raised to the power of exponent
Returns the result of raising base to the power of exponent. If base is negative and exponent is not an
integral value, or if base is zero and exponent is negative, a runtime error is raised.

**Parameters**:
- **`base`**: floating point value
- **`exponent`**: floating point value

**Return Value**:
base raised to the power of exponent

**Example**:
```urscript
Example command: pow(5.,3)
• Example Parameters:
• Base = 5
• Exponent = 3
• Returns 125.
```

---

<a id="r2d"></a>
### `r2d(r)`
**Section**: URScript 16.1.26

**Description**:
Returns radians-to-degrees of r
Returns the degree value of ’r’ radians.

**Parameters**:
- **`r`**: The angle in radians

**Return Value**:
The angle in degrees

**Example**:
```urscript
Example command: r2d(1.57)
• Example Parameters:
• r 1.5707 rad
```

---

<a id="random"></a>
### `random()`
**Section**: URScript 16.1.27

**Description**:
Random Number

**Parameters**:
- *None / No arguments required.*

**Return Value**:
pseudo-random number between 0 and 1 (float)

---

<a id="rotvec2rpy"></a>
### `rotvec2rpy(rotation_vector)`
**Section**: URScript 16.1.28

**Description**:
Returns RPY vector corresponding to rotation_vector
Returns the RPY vector corresponding to ’rotation_vector’ where the rotation vector is the axis of rotation
with a length corresponding to the angle of rotation in radians.

**Parameters**:
- **`rotation_vector`**: The rotation vector (Vector3d) in radians, also called the Axis-Angle vector (unitaxis of rotation multiplied by the rotation angle in radians).

**Return Value**:
The RPY vector (Vector3d) in radians, describing a roll-pitch-yaw sequence of extrinsic rotations about the
X-Y-Z axes, (corresponding to intrinsic rotations about the Z-Y’-X” axes). In matrix form the RPY vector is
defined as Rrpy = Rz(yaw)Ry(pitch)Rx(roll).

**Example**:
```urscript
Example command: rotvec2rpy([3.14,1.57,0])
• Example Parameters:
• rotation_vector = [3.14,1.57,0] -> rx=3.14, ry=1.57, rz=0
• Returns [-2.80856, -0.16202, 0.9] -> roll=-2.80856, pitch=-0.16202, yaw=0.9
• Returns 90 deg
```

---

<a id="rpy2rotvec"></a>
### `rpy2rotvec(rpy_vector)`
**Section**: URScript 16.1.29

**Description**:
Returns rotation vector corresponding to rpy_vector
Returns the rotation vector corresponding to ’rpy_vector’ where the RPY (roll-pitch-yaw) rotations are
extrinsic rotations about the X-Y-Z axes (corresponding to intrinsic rotations about the Z-Y’-X” axes).

**Parameters**:
- **`rpy_vector`**: The RPY vector (Vector3d) in radians, describing a roll-pitch-yaw sequence of extrinsic rotations about the X-Y-Z axes, (corresponding to intrinsic rotations about the Z-Y’-X” axes). In matrix form the RPY vector is defined as Rrpy = Rz(yaw)Ry(pitch)Rx(roll).

**Return Value**:
The rotation vector (Vector3d) in radians, also called the Axis-Angle vector (unit-axis of rotation multiplied
by the rotation angle in radians).

**Example**:
```urscript
Example command: rpy2rotvec([3.14,1.57,0])
• Example Parameters:
• rpy_vector = [3.14,1.57,0] -> roll=3.14, pitch=1.57, yaw=0
• Returns [2.22153, 0.00177, -2.21976] -> rx=2.22153, ry=0.00177, rz=-2.21976
```

---

<a id="sin"></a>
### `sin(f )`
**Section**: URScript 16.1.30

**Description**:
Returns the sine of f
Returns the sine of an angle of f radians.

**Parameters**:
- **`f`**: floating point value

**Return Value**:
the sine of f.

**Example**:
```urscript
Example command: sin(1.57)
• Example Parameters:
• f is angle of 1.57 rad (90 deg)
• Returns 1.0
```

---

<a id="size"></a>
### `size(v)`
**Section**: URScript 16.1.31

**Description**:
Returns the size of a matrix variable, the length of a list or string variable

**Parameters**:
- **`v`**: A matrix, list or string variable

**Return Value**:
Given a list or a string the length is returned as an integer. Given a matrix the size is returned as a list of
two numbers representing the number of rows and columns, respectively.

**Example**:
```urscript
Example command:
• size("here I am") -> Returns 9
• size([1,2,3,4,5]) -> Returns 5
• size([[1,2],[3,4],[5,6]]) -> Returns [3,2]
```

---

<a id="sqrt"></a>
### `sqrt(f )`
**Section**: URScript 16.1.32

**Description**:
Returns the square root of f
Returns the square root of f. If f is negative, a runtime error is raised.

**Parameters**:
- **`f`**: floating point value

**Return Value**:
the square root of f.

**Example**:
```urscript
Example command: sqrt(9)
• Example Parameters:
• f=9
• Returns 3
```

---

<a id="tan"></a>
### `tan(f)`
**Section**: URScript 16.1.33

**Description**:
Returns the tangent of f
Returns the tangent of an angle of f radians.

**Parameters**:
- **`f`**: floating point value

**Return Value**:
the tangent of f.

**Example**:
```urscript
Example command: tan(.7854)
• Example Parameters:
• f is angle of .7854 rad (45 deg)
• Returns 1.0
```

---

<a id="transpose"></a>
### `transpose(m)`
**Section**: URScript 16.1.34

**Description**:
Get the transpose of a matrix

**Parameters**:
- **`m`**: matrix or an array

**Return Value**:
transposed matrix or array

**Example**:
```urscript
Example command:
transpose([[1,2],[3,4],[5,6]]) -> Returns [[1,3,5],[2,4,6]]
transpose([1,2,3]) -> Returns [[1],[2],[3]]
transpose([[1],[2],[3]]) -> Returns [1,2,3]
```

---

<a id="wrench_trans"></a>
### `wrench_trans(T_from_to, w_from)`
**Section**: URScript 16.1.35

**Description**:
Wrench transformation
Move the point of view of a wrench.

**Parameters**:
- **`T_from_to`**: The transformation to the new point of view (Pose)
- **`w_from`**: wrench to transform in list format [F_x, F_y, F_z, M_x, M_y, M_z]

**Return Value**:
resulting wrench, w_to in list format [F_x, F_y, F_z, M_x, M_y, M_z]
17.1. Functions

> [!NOTE]
> Note: Transforming wrenches is not as trivial as transforming poses as the torque scales with the length of
> the translation.
> w_to = T_from->to * w_from

---

## Navigation

[⬅️ Back to Table of Contents](../README.md)
