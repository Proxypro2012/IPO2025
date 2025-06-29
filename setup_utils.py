import subprocess
import sys
import platform

def install_package(package_name: str):

    system = platform.system().lower()

    if system == "windows":
        cmd = [sys.executable, "-m", "pip", "install", package_name]
    else:
        cmd = [sys.executable, "-m", "pip3", "install", package_name]

    try:
        print(f"Running command: {' '.join(cmd)}")
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error installing package: {e.stderr}")

