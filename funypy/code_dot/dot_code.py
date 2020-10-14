import sys
import argparse


def main():
    parser = argparse.ArgumentParser(description="Process . .. to data")
    parser.add_argument("-i", type=str, required=True, help="input . ..")

    args = parser.parse_args()
    _input = args.i.strip()
    _input_array = _input.split(" ")

    _array = []
    for idx, _  in enumerate(_input_array[::8]):
        _bitlist = []
        for _code in _input_array[idx*8 : idx*8 + 8]:
            _bitcode = ""
            if _code == "..":
                _bitcode = "1"
            elif _code == ".":
                _bitcode = "0"
            _bitlist.append(_bitcode)
        _code = int("".join(_bitlist), 2)
        _array.append(_code)

    print(bytearray(_array).decode("utf8"))


if __name__ == "__main__":
    main()
