import sys

if __name__ == '__main__':
    print("=== Command Quest ===")
    if len(sys.argv) == 1:
        print("No arguments provided!")
        print(f"Program name: {sys.argv[0]}")
        print("Total arguments: 1\n")
    elif len(sys.argv) > 1:
        print(f"Program name: {sys.argv[0]}")
        print(f"Arguments received: {len(sys.argv) - 1}")
        for i in range(1, len(sys.argv)):
            print(f"Argument {i}: {sys.argv[i]}")
        print(f"Total arguments: {len(sys.argv)}\n")
