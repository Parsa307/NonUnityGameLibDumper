import subprocess
import sys
import os

def dump_lib(libname, filename):
    try:
        result = subprocess.run(f'rabin2 -s {libname} >> {filename}', shell=True, stderr=subprocess.PIPE, check=True)
        if result.returncode == 0:
            print(f"Dump successfully saved to {filename}")
        else:
            print(f"Error dumping lib: {result.stderr.decode().strip()}")

    except FileNotFoundError:
        print("Error: rabin2 not found. Please ensure it is installed and in your PATH.")

def main():
    while True:
        print("1. Dump Lib")
        print("2. Quit")
        selection = input("Enter your selection: ")

        if selection == '1':
            while True:
                libname = input("Enter the library name: ")
                if (libname) and os.path.isfile(libname):
                    break
                else:
                    print("The specified library file does not exist or is invalid.")

            while True:
                filename = input("Enter the output filename: ")
                if (filename):
                    break

            dump_lib(libname, filename)
            sys.exit()
        elif selection == '2':
            print("Goodbye!")
            break
        else:
            print("Invalid selection. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
