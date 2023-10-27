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
