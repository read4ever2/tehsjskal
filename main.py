# test.py
"""
Docstring
"""

import secrets


def main():
    for _ in range(10):
        print(f'{secrets.randbelow(1_000_000)}'.zfill(6))


if __name__ == "__main__":
    main()
