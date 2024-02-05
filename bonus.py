from typing import Union, List

def count_lengths(arr: List[Union[str, int]]) -> List[int]:
    return [len(str(item)) for item in arr]

def main():
    # Test cases
    input1 = ["abc", "apple", "orange"]
    input2 = [12, 456, 9000]

    # Output 
    output1 = count_lengths(input1)
    output2 = count_lengths(input2)

    print("Input:", input1)
    print("Output:", output1)

    print("\nInput:", input2)
    print("Output:", output2)

if __name__ == "__main__":
    main()