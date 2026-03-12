import sys
import os
import site


def global_environment():
    print("\nMATRIX STATUS: You're still plugged in\n")

    print(f"Current Python: {sys.executable}")
    print("Virtual Environment: None detected\n")

    print(
        "WARNING: You're in the global environment!\n"
        "The machines can see everything you install."
    )

    print(
        "\nTo enter the construct, run:\n"
        "python -m venv matrix_env\n"
        "source matrix_env/bin/activate # On Unix\n"
        "matrix_env\n"
        "Scripts\n"
        "activate # On Windows\n"
    )

    print("Then run this program again.")


def virtual_environment():
    print("\nMATRIX STATUS: Welcome to the construct\n")

    print(f"Current Python: {sys.executable}")
    print(f"Virtual Environment: {os.path.basename(sys.prefix)}")
    print(f"Environment Path: {sys.prefix}")

    print(
        "\nSUCCESS: You're in an isolated environment!\n"
        "Safe to install packages without affecting the global system."
    )

    print(
        "\nPackage installation path:\n"
        f"{site.getsitepackages()[0]}"
    )


if __name__ == '__main__':

    if sys.prefix == sys.base_prefix:
        global_environment()
    else:
        virtual_environment()
