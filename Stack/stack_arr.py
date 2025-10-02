from typing import List


def main():
    # Stacks Implementation via Array
    stack: List[int] = []

    # Pushing Element into Stack - O(1)
    stack.append(1)
    stack.append(2)
    stack.append(3)

    # Poping Element from Stack - O(1)
    print(stack.pop())

    # Peeking Element from Stack - O(1)
    print(stack[-1])

    # Checking if Stack is Empty or not
    if stack:
        print(False)
    else:
        print(True)


if __name__ == "__main__":
    main()
