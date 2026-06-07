import os
import subprocess
import pickle


API_KEY = "sk_test_123456789abcdef"
PASSWORD = "admin123"


def command_injection():
    user_input = input("Enter command: ")
    os.system(user_input)


def subprocess_injection():
    command = input("Command: ")
    subprocess.run(command, shell=True)


def insecure_deserialization():
    data = input("Pickle data: ")
    pickle.loads(data.encode())


def dangerous_eval():
    user_code = input("Python code: ")
    eval(user_code)


if __name__ == "__main__":
    command_injection()
    subprocess_injection()
    insecure_deserialization()
    dangerous_eval()