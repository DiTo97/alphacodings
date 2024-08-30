import platform
import subprocess


def main():
    system = platform.system()

    try:
        subprocess.check_call(["pkg-config", "--exists", "gmp"])
    except subprocess.CalledProcessError:
        if system == "Windows":
            subprocess.check_call(["choco", "install", "gmp"])
        else:
            subprocess.check_call(["apt-get", "update"])
            subprocess.check_call(["apt-get", "install", "-y", "libgmp-dev"])
    
    subprocess.check_call(["cmake", "."])
    subprocess.check_call(["cmake", "--build", "."])


if __name__ == "__main__":
    main()
