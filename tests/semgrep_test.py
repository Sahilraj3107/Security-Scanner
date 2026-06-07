import hashlib
import os
import random
import subprocess
import yaml


SECRET_KEY = "my_super_secret_key_123"
AWS_SECRET = "AKIAIOSFODNN7EXAMPLE"


def weak_hash(password):
    return hashlib.md5(password.encode()).hexdigest()


def predictable_token():
    return random.random()


def command_execution():
    cmd = input("Command: ")
    subprocess.Popen(cmd, shell=True)


def unsafe_yaml_load(data):
    return yaml.load(data, Loader=yaml.Loader)


def path_traversal(filename):
    with open(f"uploads/{filename}", "r") as f:
        return f.read()


if __name__ == "__main__":
    print(weak_hash("password123"))