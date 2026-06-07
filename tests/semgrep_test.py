import os
import subprocess
import pickle


def command_injection():
    user_input = input("Enter command: ")
    os.system(user_input)


def subprocess_injection():
    command = input("Command: ")
    subprocess.run(command, shell=True)


def insecure_deserialization():
    data = input("Pickle data: ")
    pickle.loads(data.encode())


if __name__ == "__main__":
    command_injection()
    subprocess_injection()
    insecure_deserialization()