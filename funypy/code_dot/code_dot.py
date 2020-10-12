import sys
import argparse


def main():
    parser = argparse.ArgumentParser(description="Process Data to . ..")
    parser.add_argument("-i", type=str, required=True, help="input data")

    args = parser.parse_args()
    _input = args.i
    _binslash = ""
    for _code in _input:
        _binslash += bin(ord(_code))[2:]

    print(_binslash.replace("1", ".. ").replace("0", ". ").strip())


if __name__ == "__main__":
    main()
