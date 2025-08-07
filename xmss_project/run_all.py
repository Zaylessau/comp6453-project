import os
import subprocess

def run_tests():
    print("\n====================")
    print(" Running Unit Tests ")
    print("====================")
    subprocess.run(["python", "-m", "unittest", "discover", "-s", "tests"])

def run_benchmarks():
    print("\n=========================")
    print(" Running Signing Benchmark ")
    print("=========================")
    subprocess.run(["python", "benchmark/benchmark_signing.py"])

    print("\n===========================")
    print(" Running Verification Benchmark ")
    print("===========================")
    subprocess.run(["python", "benchmark/benchmark_verify.py"])

def run_demo():
    print("\n====================")
    print(" Running XMSS Demo ")
    print("====================")
    subprocess.run(["python", "main.py"])

if __name__ == "__main__":
    run_tests()
    run_benchmarks()
    run_demo()


print("\n====================")
print(" Running Aggregation Test ")
print("====================")

import unittest
from tests import test_aggregate

unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromModule(test_aggregate))
