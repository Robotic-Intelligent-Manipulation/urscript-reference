"""URScript Interpreter Client (Port 30020).

This Python utility connects to the Universal Robots Interpreter Mode
on TCP Port 30020 to stream URScript commands line-by-line dynamically
without interrupting or restarting the robot controller.

Target Controllers: Universal Robots e-Series / UR20 / UR30 (SW 5.9+)
"""

import socket
import sys
import time


class URInterpreterClient:
    """Client for streaming script statements to the UR Interpreter socket."""

    def __init__(self, robot_ip: str, port: int = 30020, timeout: float = 5.0):
        self.robot_ip = robot_ip
        self.port = port
        self.timeout = timeout
        self.sock: socket.socket | None = None

    def connect(self) -> None:
        """Establish TCP connection to the interpreter server."""
        print(f"Connecting to UR Interpreter at {self.robot_ip}:{self.port}...")
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.settimeout(self.timeout)
        self.sock.connect((self.robot_ip, self.port))
        print("Connected successfully!")
        # Read greeting banner if present
        try:
            greeting = self.sock.recv(1024).decode("utf-8", errors="ignore")
            if greeting:
                print(f"Server banner: {greeting.strip()}")
        except socket.timeout:
            pass

    def send_command(self, cmd: str) -> str:
        """Send a single URScript statement and return the interpreter response."""
        if not self.sock:
            raise RuntimeError("Socket is not connected.")

        formatted_cmd = cmd.strip() + "\n"
        self.sock.sendall(formatted_cmd.encode("utf-8"))

        # Wait for interpreter response
        response = self.sock.recv(4096).decode("utf-8", errors="ignore")
        return response.strip()

    def close(self) -> None:
        """Close the socket connection cleanly."""
        if self.sock:
            try:
                self.send_command("end_interpreter()")
            except Exception:
                pass
            self.sock.close()
            self.sock = None
            print("Interpreter connection closed.")


def main() -> None:
    robot_ip = sys.argv[1] if len(sys.argv) > 1 else "192.168.1.10"
    client = URInterpreterClient(robot_ip=robot_ip)

    try:
        client.connect()

        # Example: Query digital input status
        print("\n--> Querying digital input status...")
        resp = client.send_command("get_standard_digital_in(0)")
        print(f"<-- Response: {resp}")

        # Example: Set tool digital output
        print("\n--> Setting tool digital output 0 to True...")
        resp = client.send_command("set_tool_digital_out(0, True)")
        print(f"<-- Response: {resp}")

        time.sleep(1.0)

        # Example: Reset tool digital output
        print("\n--> Setting tool digital output 0 to False...")
        resp = client.send_command("set_tool_digital_out(0, False)")
        print(f"<-- Response: {resp}")

    except Exception as exc:
        print(f"Error during communication: {exc}")
    finally:
        client.close()


if __name__ == "__main__":
    main()
