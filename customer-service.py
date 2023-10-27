import pyautogui
import time



network_drive_path = r"\\network\share\path"
programs_to_install = [
    "program1.exe",
    "program2.msi",
    # Add more programs as needed
]
import subprocess

for program in programs_to_install:
    program_path = os.path.join(network_drive_path, program)

    # Install an EXE
    if program.endswith(".exe"):
        subprocess.run([program_path, '/quiet', '/norestart'])

    # Install an MSI
    elif program.endswith(".msi"):
        subprocess.run(["msiexec", "/i", program_path, "/qn", "REBOOT=ReallySuppress"])

    # Add more installation methods for other types as needed


# Define a function to automate the installation process
def automate_installation():
    # Adjust these coordinates to match the screen positions of the buttons and input fields
    # You can use pyautogui.displayMousePosition() to find the coordinates
    # Wait a few seconds for the installer to start
    time.sleep(5)

    # Click buttons or perform interactions using pyautogui functions
    pyautogui.click(x=100, y=200)  # Click a button
    pyautogui.typewrite("your_text_here")  # Type text if needed
    pyautogui.press("enter")  # Press Enter key

    # Repeat these steps to automate the entire installation process

# Run the automation
automate_installation()