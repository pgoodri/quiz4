import argparse

def main():
    # Create ArgumentParser object
    parser = argparse.ArgumentParser(description='Parse string, integer, and float inputs.')

    # Add arguments
    parser.add_argument('string', type=str, help='Input string')
    parser.add_argument('integer', type=int, help='Input integer')
    parser.add_argument('float', type=float, help='Input float')

    # Parse the arguments
    args = parser.parse_args()

    # Access parsed arguments
    input_string = args.string
    input_integer = args.integer
    input_float = args.float

    # Display the parsed arguments
    print("String: ", input_string)
    print("Integer: ", input_integer)
    print("Float", input_float)

if __name__ == "__main__":
    main()

