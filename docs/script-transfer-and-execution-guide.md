# PC Script Authoring, Transfer & Execution Guide (SSH & FTP/SFTP)

This guide explains how to author custom URScript files on a PC and deploy them to a Universal Robots controller (e-Series, UR20, UR30, and CB-Series) using **SSH (SCP)** and **FTP / SFTP**.

---

## 1. Authoring URScript on a PC

URScript files are plain ASCII/UTF-8 text files typically saved with the `.script` extension. You can edit them using any code editor (such as VS Code with URScript extensions).

### Basic Program Template
```urscript
# my_robot_program.script
def my_robot_program():
  # Setup tool parameters
  set_tcp(p[0.0, 0.0, 0.15, 0.0, 0.0, 0.0])
  set_payload(1.5, [0.0, 0.0, 0.05])
  
  # Notification
  textmsg("Program started from external script!")
  
  # Motion execution
  # q: [Base, Shoulder, Elbow, Wrist1, Wrist2, Wrist3] in radians
  q_home = [0.0, -1.5708, 1.5708, -1.5708, -1.5708, 0.0]
  movej(q_home, a=1.4, v=1.05)
  
  # Linear move in tool space: delta Z -50mm
  p_current = get_actual_tcp_pose()
  p_target = pose_trans(p_current, p[0.0, 0.0, -0.05, 0.0, 0.0, 0.0])
  movel(p_target, a=0.5, v=0.1)
  
  textmsg("Program finished successfully.")
end
```

### Essential Formatting Rules
1. **Root Scope**: The primary function declaration (`def ...():`) must start in column 1 (no leading spaces).
2. **Termination**: The closing keyword `end` must be in column 1.
3. **Indentation**: All statements inside functions, loops, and conditions must be indented by at least one whitespace.
4. **Line Endings**: Unix-style line endings (`LF`, `\n`) are recommended over Windows `CRLF`.

---

## 2. Controller Setup: Enabling Network Access

By default on PolyScope 5 (e-Series):
1. Navigate to **Hamburger Menu (Top Right) ➔ Settings ➔ System ➔ Security ➔ Secure Shell (SSH)**.
2. Toggle **Enable SSH**.
3. Under **Security ➔ General / Firewall**, ensure **Port 22** is open (default: allowed).

### Default Controller Credentials
| Controller Generation | Username | Default Password | Target Script Folder |
| :--- | :---: | :---: | :--- |
| **CB-Series (CB3.x)** | `root` | `easybot` | `/programs/` |
| **e-Series (SW ≤ 5.14)** | `root` | `easybot` | `/programs/` |
| **e-Series (SW ≥ 5.15+)** | `ur` / `root` | `easybot` | `/programs/` |

> [!WARNING]
> Always change default controller passwords in production environments to prevent unauthorized remote access.

---

## 3. Method 1: Transfer via SSH / SCP (Command Line)

SSH provides secure command-line access and allows file copying via `scp` (Secure Copy Protocol).

### A. Uploading Script using SCP
Run this command from your PC terminal (Linux / macOS / Windows PowerShell):

```bash
# Syntax: scp <local_file> <user>@<robot_ip>:/programs/
scp my_robot_program.script root@192.168.1.10:/programs/

# If connecting with 'ur' user on newer e-Series firmware:
scp my_robot_program.script ur@192.168.1.10:/programs/
```

### B. Remote Terminal Session via SSH
Log in to the controller Linux shell directly:
```bash
ssh root@192.168.1.10
# Enter password: easybot
```

Once inside the robot controller:
```bash
# Verify the uploaded script
ls -la /programs/my_robot_program.script

# Instant Injection Test: Send script directly to URControl without Teach Pendant:
nc 127.0.0.1 30002 < /programs/my_robot_program.script
```

---

## 4. Method 2: Transfer via FTP / SFTP (GUI Client)

Universal Robots controllers support **SFTP (SSH File Transfer Protocol on Port 22)** natively. Graphical FTP clients like **FileZilla** or **WinSCP** provide a drag-and-drop interface.

### Step-by-Step with FileZilla Client:
1. Open **FileZilla Client** on your PC.
2. In the top connection bar, enter:
   - **Host**: `sftp://<robot_ip>` (e.g. `sftp://192.168.1.10`)
   - **Username**: `root` (or `ur`)
   - **Password**: `easybot`
   - **Port**: `22` (SFTP port)
3. Click **Quickconnect** (accept host key fingerprint on first connection).
4. In the **Remote Site** panel (right side), navigate to:
   ```text
   /programs/
   ```
5. Drag and drop your `.script` file from the **Local Site** panel (left side) into `/programs/`.

*(Note: If a dedicated classic FTP daemon like `vsftpd` / `proftpd` has been installed and started on port 21, use standard `ftp://` protocol on port 21 with the configured FTP credentials).*

---

## 5. Running the Transferred Script on the Robot

Once your script file is located in `/programs/`:

### Option A: Via PolyScope GUI (Recommended for Lab Operators)
1. On the Teach Pendant, open or create a program (`.urp`).
2. Go to the **Structure** tab ➔ **Advanced** ➔ Add a **Script** node.
3. In the Command pane on the right:
   - Change the dropdown from **Line** to **File**.
   - Tap **Edit / Browse**.
   - Select `/programs/my_robot_program.script`.
4. Press the **Play** button on the bottom toolbar. PolyScope will include and execute your external script.

### Option B: Remote Execution via Dashboard Server & Port 30002
From your PC (no teach pendant touch required):
```bash
# 1. Release brakes & power on robot via Dashboard Server (Port 29999)
echo "power on" | nc 192.168.1.10 29999
sleep 3
echo "brake release" | nc 192.168.1.10 29999
sleep 2

# 2. Inject and execute the script via Secondary Client Interface (Port 30002)
nc 192.168.1.10 30002 < my_robot_program.script
```
