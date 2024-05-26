import os
import subprocess
import sys

def create_virtual_environment(venv_dir="venv"):
    """Creates a virtual environment if not created already."""
    if not os.path.exists(venv_dir):
        subprocess.check_call([sys.executable, "-m", "venv", venv_dir])
        print(f"Virtual environment created at {venv_dir}")


def get_installed_packages(pip_executable):
    """Returns a set of installed packages in the virtual environment."""
    result = subprocess.run([pip_executable, 'freeze'], stdout=subprocess.PIPE, text=True)
    installed_packages = set()
    for line in result.stdout.splitlines():
        package_name = line.split('==')[0]
        installed_packages.add(package_name.lower())
    return installed_packages

def get_required_packages(requirements_file):
    """Returns a set of required packages listed in requirements.txt."""
    required_packages = set()
    with open(requirements_file, 'r') as file:
        for line in file:
            package_name = line.strip().split('==')[0]
            required_packages.add(package_name.lower())
    return required_packages

def install_requirements(requirements_file="requirements.txt", venv_dir="venv"):
    """Installs packages from requirements.txt into the virtual environment if not already installed."""
    pip_executable = os.path.join(venv_dir, "bin", "pip") if os.name != 'nt' else os.path.join(venv_dir, "Scripts", "pip")
    required_packages = get_required_packages(requirements_file)

    if not required_packages:
        print("No packages to install. The requirements.txt file is empty.")
        return
    
    installed_packages = get_installed_packages(pip_executable)

    packages_to_install = required_packages - installed_packages

    if packages_to_install:
        subprocess.check_call([pip_executable, "install", "-r", requirements_file])
        print(f"Installed packages from {requirements_file}")
    else:
        print("All required packages are already installed.")
       

def main():
    create_virtual_environment()
    install_requirements()

if __name__ == "__main__":
    main()
