import sys
import argparse


def main():
    parser = argparse.ArgumentParser(description="Process Data to . ..")
    parser.add_argument("-i", type=str, required=True, help="input data")

    args = parser.parse_args()
    _input = args.i
    _binslash = ""
    for _code in _input:

        _bitcode = bin(ord(_code))[2:]
        for i in range(8 - len(_bitcode)):
            _bitcode = "0" + _bitcode
        _binslash += _bitcode

    print(_binslash.replace("1", ".. ").replace("0", ". ").strip())


if __name__ == "__main__":
    main()
