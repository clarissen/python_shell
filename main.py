import sys

import os
import shlex
import subprocess
import sys

def main():
    while True:
        try:
            cwd = os.getcwd()
            command = input(f"{cwd} $ ")  # prompt shows current dir
        except (EOFError, KeyboardInterrupt):
            print()
            break

        args = shlex.split(command)
        if not args:
            continue

        program = args[0]

        # Builtins
        if program == "exit":
            break
        elif program == "cd":
            try:
                os.chdir(args[1])
            except IndexError:
                print("cd: missing operand")
            except FileNotFoundError:
                print(f"cd: {args[1]}: No such file or directory")
            continue

        # External commands
        try:
            subprocess.run(args)
        except FileNotFoundError:
            print(f"{program}: command not found")

if __name__ == "__main__":
    main()
