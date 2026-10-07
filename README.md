# Universal Robots URScript API Reference & Cookbook

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Target: UR PolyScope](https://img.shields.io/badge/PolyScope-SW%205.16%2B-orange.svg)](https://www.universal-robots.com/)
[![Robotic Intelligent Manipulation](https://img.shields.io/badge/PBL-Cluster%204%20Polibatam-red.svg)](https://github.com/Robotic-Intelligent-Manipulation)

Comprehensive reference manual and laboratory programming cookbook for **URScript**, the real-time procedural programming language used to control Universal Robots manipulators (UR3e, UR5e, UR10e, UR16e, UR20, UR30, and CB-Series).

## Table of Contents

- [1. Runtime Architecture & Execution Levels](#1-runtime-architecture--execution-levels)
- [2. Controller Network Ports & Protocols](#2-controller-network-ports--protocols)
- [3. Language Fundamentals & Data Types](#3-language-fundamentals--data-types)
- [4. Modular API Reference (240 Built-in Functions)](#4-modular-api-reference-240-built-in-functions)
- [5. PC Script Authoring & Transfer Guide (SSH & FTP)](#5-pc-script-authoring--transfer-guide-ssh--ftp)
- [6. Laboratory Recipes & Cookbook](#6-laboratory-recipes--cookbook)
- [7. License & Contributing](#7-license--contributing)

---

## 1. Runtime Architecture & Execution Levels

Universal Robots systems operate across three primary programming layers:

1. **PolyScope Graphical UI Level**: High-level teach pendant interface using visual nodes and wizards.
2. **Script Level (URScript)**: Real-time programs executed natively in the **URControl RuntimeMachine (RTMachine)**.
   - On **e-Series, UR20, and UR30**, RTMachine executes at **500 Hz (2 ms control loop)**.
   - On **CB-Series**, RTMachine executes at **125 Hz (8 ms control loop)**.
3. **Low-Level C-API & Fieldbus Level**: Real-Time Data Exchange (RTDE) synchronizers and kernel drivers.

## 2. Controller Network Ports & Protocols

| Port | Name | Direction | Rate | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`30001`** | Primary Client Interface | Bidirectional | 10 Hz | Streams controller status; accepts full URScript program execution. |
| **`30002`** | Secondary Client Interface | Bidirectional | 10 Hz | Secondary script execution and monitoring channel. |
| **`30003`** | Real-Time Client Interface | Outbound | 500 Hz / 125 Hz | High-speed broadcast of joint positions, velocities, torques, and TCP poses. |
| **`30004`** | RTDE (Real-Time Data Exchange) | Bidirectional | 500 Hz / 125 Hz | Synchronized binary register exchange (ideal for ROS 2 `ur_robot_driver`). |
| **`30020`** | Interpreter Mode | Bidirectional | Interactive | Dynamic line-by-line script execution stream without program restarts. |
| **`29999`** | Dashboard Server | Bidirectional | Request/Reply | Remote pendant control (power on, brake release, load/play/pause/stop program, dismiss errors). |

## 3. Language Fundamentals & Data Types

URScript features syntax similar to a combination of Python and Pascal:

- **Program Structure**: Must begin with `def <prog_name>():` in column 1, indented body, and terminate with `end` in column 1.
- **Data Types**:
  - `bool`: `True` or `False`
  - `int`: Signed 32-bit integer (e.g. `42`, `-10`)
  - `float`: 64-bit IEEE 754 floating-point number (e.g. `3.14159`)
  - `string`: Double-quoted text sequence (e.g. `"Tool Attached"`)
  - `pose`: Cartesian 6-DOF coordinate vector `p[X, Y, Z, Rx, Ry, Rz]`.
    - Linear components `X, Y, Z` in **meters (m)**.
    - Rotational components `Rx, Ry, Rz` in **Rotation Vector (axis-angle)** format in **radians (rad)**.
    - Rotation magnitude $|\mathbf{r}| = \sqrt{Rx^2 + Ry^2 + Rz^2} = \theta$ (angle), and unit axis $\mathbf{u} = \mathbf{r} / \theta$.
  - `list`: Indexed homogeneous collections `[q0, q1, q2, q3, q4, q5]` (joint positions in **radians**).
  - `struct`: Named records for heterogeneous grouping.
  - `matrix`: 2D arrays for linear algebra operations.
- **Multithreading & Synchronization**:
  - `sync()`: Suspends thread execution until the next controller cycle (2 ms on e-Series). Essential inside `while` loops to prevent CPU thread starvation.
  - Threads are spawned via `th_id = run MyThread()` and managed with `join th_id` or `kill th_id`.

## 4. Modular API Reference (240 Built-in Functions)

The complete URScript library is documented in dedicated files under [`docs/`](docs/):

| Documentation Module | Chapter | Functions | Key Highlights |
| :--- | :---: | :---: | :--- |
| **[`Module Motion (Robot Movement & Trajectory Planning)`](docs/01-motion.md)** | Ch 14 | **47** | Core motion generation module for joint-space and Cartesian space robot trajectories. Runs deterministically in real-tim... |
| **[`Module Internals (State Telemetry, Sensors & System Modes)`](docs/02-internals-and-status.md)** | Ch 15 | **57** | System telemetry and status inspection. Provides actual and target joint positions, speeds, torques, temperatures, Tool ... |
| **[`Module URMath (Spatial Math & Kinematic Transformations)`](docs/03-math-and-transformation.md)** | Ch 16 | **35** | Spatial mathematics and transformation utilities for robotics. Covers 3D pose algebra where rotations are represented in... |
| **[`Module Interfaces (I/O, TCP/IP Sockets, RTDE & Fieldbuses)`](docs/04-interfaces-and-communication.md)** | Ch 17 | **75** | Low-level hardware and peripheral communication interfaces. Includes digital and analog I/O lines for the controller and... |
| **[`Module IO Configuration (Hardware Electrical & Signal Setup)`](docs/05-io-configuration.md)** | Ch 18 | **14** | Hardware I/O configuration for electrical domains (0–10V, 4–20mA), wrist tool power supply (0V, 12V, 24V), and automatic... |
| **[`Module ProcessPath (Remote TCP & CNC G-Code Execution)`](docs/06-process-path-and-remote-tcp.md)** | Ch 19 | **12** | Toolpath process and Remote TCP (RTCP) controller module. Executes CAD/CAM CNC .nc G-code files and controls application... |
| **Total API Coverage** | — | **240 Functions** | Fully documented with signatures, parameters, returns, and examples. |

## 5. PC Script Authoring & Transfer Guide (SSH & FTP)

For comprehensive instructions on writing `.script` files on your PC and deploying them to physical or simulated UR controllers, see the dedicated guide:
👉 **[`docs/script-transfer-and-execution-guide.md`](docs/script-transfer-and-execution-guide.md)**

### Quick Comparison of Transfer Methods:
- **Method 1: SSH / SCP (Command Line / Automation)**:
  - Copy file: `scp my_program.script root@<robot_ip>:/programs/` (or user `ur` on newer e-Series).
  - Default password: `easybot`.
  - Remote shell: `ssh root@<robot_ip>` enables direct testing and pipeline scripting via `nc 127.0.0.1 30002 < /programs/my_program.script`.
- **Method 2: FTP / SFTP (FileZilla / GUI)**:
  - Connect using **SFTP protocol on Port 22** (native on all UR Linux controllers).
  - Target destination: `/programs/`.
  - Load into PolyScope: **Structure ➔ Advanced ➔ Script ➔ Set to "File" ➔ Select `/programs/my_program.script`**.

## 6. Laboratory Recipes & Cookbook

Ready-to-use URScript and Python templates are located in [`examples/`](examples/):

- **[`01_servoj_realtime_loop.script`](examples/01_servoj_realtime_loop.script)**: 500 Hz high-frequency closed-loop joint tracking loop for reinforcement learning and gamepad teleoperation.
- **[`02_force_mode_compliance.script`](examples/02_force_mode_compliance.script)**: Force-guided peg-in-hole assembly using the internal 6-axis F/T sensor.
- **[`03_socket_vision_client.script`](examples/03_socket_vision_client.script)**: TCP/IP client script communicating with an external OpenCV/Python vision server.
- **[`python_interpreter_client.py`](examples/python_interpreter_client.py)**: Python client connecting to Port 30020 for interactive step-by-step script streaming.

## 7. License & Contributing

Developed by **Rifky Afriza** & **Fitri** for the **Robotic Intelligent Manipulation (PBL Cluster 4)** initiative at **Politeknik Negeri Batam**.

Released under the [MIT License](LICENSE).
