import sys
import time


def main() -> None:
    version = sys.version_info
    while True:
        print(f"Hello Python {version.major}.{version.minor}.{version.micro}!")
        time.sleep(1)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt as e:
        sys.exit(130)
