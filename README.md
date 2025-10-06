# Data Structures and Algorithms in Python

Collection of Data Structures and Algorithms implementations in Python.

## Data Structures

- Array
- Singly Linked List
- Doubly Linked List
- Stack
- Queue
- Hash Table
- Binary Tree
- Binary Search Tree
- AVL Tree
- Heap and Priority Queue


## Algorithms

### Sorting Algorithms

- Heap Sort --> *O(N log N)*
- Bubble Sort --> *O(N^2)*
- Selection Sort --> *O(N^2)*
- Insertion Sort --> *O(N^2)*
- Merge Sort --> *O(N log N)*
- Quick Sort --> *O(N log N)*
- Counting Sort --> *O(N+K)*
- Radix Sort --> *O(N log N)*


### Searching Algorithms

- Linear Search
- Binary Search

### Graph Algorithms

- 

### Tree Algorithms

- Inorder Traversal *(Recursive DFS)*
- Preorder Traversal *(Recursive DFS)*
- Postorder Traversal *(Recursive DFS)*
- Inorder Successor
- Level Order Traversal *(BFS)*
- Iterative DFS

### Dynamic Programming

- 

## Problem Sovling Techniques

- Recursion
- Two Pointer Approach

##  Getting Started

### Prerequisites
- Python 3.7 or higher
- Basic understanding of Python programming

### Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd DSA
   ```

2. **Set up virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```



##  Usage Examples

### Doubly Linked List
```python
from doubly_LL import DoublyLL

# Create a new doubly linked list
dll = DoublyLL()

# Insert elements
dll.insertAtHead(1)
dll.insertAtTail(2)
dll.insertAtAnyPos(3, 2)

# Display the list
dll.traverseList()  # Output: 1 -> 3 -> 2 ->

# Get length in O(1) time
print(len(dll))  # Output: 3

# Update elements
dll.updateListByPos(5, 2)
dll.traverseList()  # Output: 1 -> 5 -> 2 ->
```

### Stack Implementation
```python
from stack_LL import Stack

# Create a new stack
stack = Stack()

# Push elements
stack.push(1)
stack.push(2)
stack.push(3)

# Pop elements
while not stack.isEmpty():
    print(stack.pop())  # Output: 3, 2, 1
```

### Queue Implementation
```python
from queue_LL import Queue

# Create a new queue
queue = Queue()

# Enqueue elements
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

# Dequeue elements
while not queue.isEmpty():
    print(queue.dequeue())  # Output: 1, 2, 3
```

##  Time Complexity Guide

### Common Time Complexities (Best to Worst)
- **O(1)** - Constant: Array access, Stack push/pop
- **O(log n)** - Logarithmic: Binary search, Balanced tree operations
- **O(n)** - Linear: Linear search, Array traversal
- **O(n log n)** - Linearithmic: Merge sort, Heap sort
- **O(n²)** - Quadratic: Bubble sort, Selection sort
- **O(2ⁿ)** - Exponential: Recursive Fibonacci (naive)

### Space Complexity Considerations
- **In-place algorithms**: O(1) extra space
- **Recursive algorithms**: O(h) where h is recursion depth
- **Dynamic programming**: Often O(n) for memoization



##  Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Contribution Guidelines
- Follow Python PEP 8 style guidelines
- Include time/space complexity analysis
- Add comprehensive comments and docstrings
- Include example usage in your implementations

##  Resources

### Online Resources
- [Data Structures & Algorithms in Python - The Complete Pathway by Greg Hogg](https://youtube.com/playlist?list=PLKYEe2WisBTFEr6laH5bR2J19j7sl5O8R&si=rOMs6Jhsw5YMApVw)
- [W3Schools Python Tutorial](https://www.w3schools.com/python/)
- [LeetCode](https://leetcode.com/) for practice problems


##  Acknowledgments

- Thanks to the Python community for excellent documentation
- Thanks to Greg Hogg Youtube Channel as his playlist is a wonderful kickstart for mastering DSA 
- Inspired by classic computer science textbooks
- Built for educational purposes and interview preparation

---

 **Star this repository if you find it helpful!**

 **Questions?** Feel free to open an issue or reach out!

---

**Happy Coding!** 
