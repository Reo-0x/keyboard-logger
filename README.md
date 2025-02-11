# Keyboard Logger for Security Testing

A Python-based keyboard logging tool designed specifically for authorized security testing and educational purposes.

## ⚠️ Legal Disclaimer

This tool is intended **ONLY** for:
- Authorized security testing
- Educational purposes
- Systems you own or have explicit permission to test

Unauthorized use of this tool to monitor keyboard input without consent is illegal and unethical. Users must comply with all applicable laws and regulations.


![Uploading image.png…]()


## 🔍 Features

- Real-time keyboard event monitoring
- Timestamp logging for each keystroke
- Automatic log file management
- Root privilege verification
- Ethical usage warning
- Clean exit handling

## 📋 Requirements

- Python 3.x
- Root/Administrator privileges
- Required Python packages:
  ```bash
  keyboard
  ```

## 🚀 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Reo-0x/keyboard-logger.git
   cd keyboard-logger
   ```

2. Install required packages:
   ```bash
   pip install keyboard
   ```

## 💻 Usage

Run the script with root privileges:

The program will:
1. Display a warning message requiring acknowledgment
2. Start monitoring keyboard input
3. Create log files in the format `keyboard_logger.log`
4. Continue logging until you press the ESC key

To stop the program:
- Press ESC to exit normally
- Press Ctrl+C for force exit

## 📝 Log Format

Logs are stored in text files with the following format:

## 🔒 Security Considerations

- Always run in a controlled environment
- Regularly review and clean log files
- Ensure proper access controls on log files
- Do not use in production environments without proper authorization

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## made by 

Reo-0x

## 🙏 Acknowledgments

- Built using the Python `keyboard` library
