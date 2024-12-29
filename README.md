# Shared Mouse

**Shared Mouse** is a simple Python-based tool that allows you to control two computers using a single mouse connected to one of the devices. This is achieved through local network communication, making it an efficient and hardware-free solution.

## How It Works

The project consists of two Python scripts:

- **`sender.py`**: Runs on the computer where the mouse is physically connected. This script captures the mouse input and sends it to the receiver device.
- **`receiver.py`**: Runs on the second computer to receive and simulate the mouse input from the sender.

The two devices communicate via a local network. Once connected, the sender script streams mouse events to the receiver, allowing you to control the receiver's cursor.

## Features

- Seamlessly share one mouse between two computers.
- Local network-based communication without additional hardware.
- Supports disabling the sender device's mouse during sharing with a transparent blocking window.

## Platform Compatibility

- **`sender.py`**:
  - Fully tested on Windows.
  - May work on Linux depending on the distribution (requires additional testing).
  - Not tested on macOS.
- **`receiver.py`**: Works on both Windows and Linux.

## How to Use

1. **Prerequisites**:
   - Ensure Python is installed on both devices.
   - Both devices must be connected to the same local network.
   - Install all required Python dependencies.

   To install dependencies, run:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Receiver Script**:
   - On the device you want to control (receiver), run `receiver.py`.
   - The script will start a server and display the local network IP address for this device.

   Example command:
   ```bash
   python receiver.py
   ```  
   Example output:
   ```
   🌍 Your local IP is: 192.168.0.115 🌍
   ```

3. **Run the Sender Script**:
   - On the computer where the mouse is plugged in, run `sender.py`.
   - The script will prompt for the IP address of the receiver device. Enter the IP address displayed by the receiver script.

   Example command:
   ```bash
   python sender.py
   ```  
   Example input:
   ```
   IP: 192.168.0.115
   ```

4. **Start Mouse Sharing**:
   - Press the `Esc` key on the sender computer to start sharing the mouse.
   - Once sharing starts:
     - A transparent window will appear on the sender device, blocking mouse activity.
     - If the transparent window does not automatically activate, select it manually from the taskbar.

5. **Stop Mouse Sharing**:
   - Press the `Esc` key again on the sender device to stop sharing.
   - The transparent blocking window will close, and the mouse will be fully functional on the sender device again.

## Key Notes

- **Local Network**: Both devices must be on the same network for the scripts to communicate.
- **Transparent Window**:
  - The transparent blocking window is designed to prevent accidental mouse usage on the sender device during sharing.
  - If it doesn’t automatically activate, it can be selected manually from the taskbar.
- **Platform Compatibility**:
  - The `sender.py` script is optimized for Windows and may not work consistently on Linux due to platform-specific differences.
  - The `receiver.py` script works reliably on both Windows and Linux.
  - macOS functionality has not been tested for either script.

## Troubleshooting

- **Connection Issues**:
  - Ensure both devices are on the same local network.
  - Check firewall settings if the connection fails.
- **Transparent Window Not Showing**:
  - If the transparent window doesn’t appear, try manually selecting it from the taskbar.

## Contribution

Contributions are welcome! If you’d like to improve this project, feel free to:
- Fork the repository
- Create a new branch
- Submit a pull request



Enjoy smooth and seamless control of multiple devices with **Shared Mouse**! 🎉

