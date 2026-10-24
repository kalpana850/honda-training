import argparse

def add(a, b):
    return a + b

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Add two numbers"
    )

    parser.add_argument("num1", type=float)
    parser.add_argument("num2", type=float)

    args = parser.parse_args()

    result = add(args.num1, args.num2)
    print("Result:", result)