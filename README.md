# Data Structures and Algorithms in Python

Collection of Data Structures and Algorithms implementations in Python.

## Data Structures

| Data Structure | Insert | Delete | Search | Access |
|----------------|--------|--------|--------|--------|
| **Array** | O(n) | O(n) | O(n) | O(1) |
| **Singly Linked List** | O(1) | O(1) | O(n) | O(n) |
| **Doubly Linked List** | O(1) | O(1) | O(n) | O(n) |
| **Stack** | O(1) | O(1) | O(n) | O(n) |
| **Queue** | O(1) | O(1) | O(n) | O(n) |
| **Hash Table** | O(1) | O(1) | O(1) | O(1) |
| **Binary Search Tree** | O(log n) | O(log n) | O(log n) | O(log n) |
| **AVL Tree** | O(log n) | O(log n) | O(log n) | O(log n) |
| **Red-Black Tree** | O(log n) | O(log n) | O(log n) | O(log n) |
| **Heap** | O(log n) | O(log n) | O(n) | O(1) |
| **Graph (Adjacency List)** | O(1) | O(V) | O(V) | O(1) |
| **Graph (Adjacency Matrix)** | O(1) | O(1) | O(1) | O(1) |

## Algorithms

### Sorting Algorithms

| Algorithm | Best Case | Average Case | Worst Case | Space |
|-----------|-----------|--------------|------------|-------|
| **Bubble Sort** | O(n) | O(n²) | O(n²) | O(1) |
| **Selection Sort** | O(n²) | O(n²) | O(n²) | O(1) |
| **Insertion Sort** | O(n) | O(n²) | O(n²) | O(1) |
| **Merge Sort** | O(n log n) | O(n log n) | O(n log n) | O(n) |
| **Quick Sort** | O(n log n) | O(n log n) | O(n²) | O(log n) |
| **Heap Sort** | O(n log n) | O(n log n) | O(n log n) | O(1) |
| **Radix Sort** | O(nk) | O(nk) | O(nk) | O(n+k) |
| **Counting Sort** | O(n+k) | O(n+k) | O(n+k) | O(k) |

### Searching Algorithms

| Algorithm | Best Case | Average Case | Worst Case | Space |
|-----------|-----------|--------------|------------|-------|
| **Linear Search** | O(1) | O(n) | O(n) | O(1) |
| **Binary Search** | O(1) | O(log n) | O(log n) | O(1) |
| **Jump Search** | O(1) | O(√n) | O(√n) | O(1) |
| **Interpolation Search** | O(1) | O(log log n) | O(n) | O(1) |

### Graph Algorithms

| Algorithm | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| **Depth First Search (DFS)** | O(V + E) | O(V) |
| **Breadth First Search (BFS)** | O(V + E) | O(V) |
| **Dijkstra's Algorithm** | O((V + E) log V) | O(V) |
| **Bellman-Ford Algorithm** | O(VE) | O(V) |
| **Floyd-Warshall Algorithm** | O(V³) | O(V²) |
| **Kruskal's Algorithm** | O(E log E) | O(V) |
| **Prim's Algorithm** | O((V + E) log V) | O(V) |

### Tree Algorithms

| Algorithm | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| **Tree Traversal (DFS)** | O(n) | O(h) |
| **Tree Traversal (BFS)** | O(n) | O(w) |
| **Lowest Common Ancestor** | O(log n) | O(log n) |
| **Tree Diameter** | O(n) | O(h) |

### Dynamic Programming

| Algorithm | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| **Fibonacci** | O(n) | O(n) |
| **Longest Common Subsequence** | O(mn) | O(mn) |
| **Knapsack Problem** | O(nW) | O(nW) |
| **Edit Distance** | O(mn) | O(mn) |
| **Coin Change** | O(n × amount) | O(amount) |

## 🚀 Getting Started

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

3. **Install dependencies (if any):**
   ```bash
   pip install -r requirements.txt  # If requirements.txt exists
   ```

## 💡 Usage Examples

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

## ⏱️ Time Complexity Guide

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

## 🎯 Learning Path

### Beginner Level
1. Start with **Arrays** and basic operations
2. Learn **Linked Lists** (Singly → Doubly)
3. Understand **Stacks** and **Queues**
4. Practice **Linear Search** and **Bubble Sort**

### Intermediate Level
1. Explore **Trees** (Binary Tree → BST)
2. Learn **Hash Maps** and collision resolution
3. Practice **Binary Search** and **Merge Sort**
4. Understand **Graph** representations

### Advanced Level
1. Master **Advanced Trees** (AVL, Red-Black)
2. Learn **Graph Algorithms** (Dijkstra, A*)
3. Practice **Dynamic Programming**
4. Explore **Advanced Sorting** (Quick Sort, Heap Sort)

## 🤝 Contributing

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

## 📚 Resources

### Books
- "Introduction to Algorithms" by Cormen, Leiserson, Rivest, and Stein
- "Data Structures and Algorithms in Python" by Goodrich, Tamassia, and Goldwasser

### Online Resources
- [Big O Cheat Sheet](https://www.bigocheatsheet.com/)
- [Python Time Complexity](https://wiki.python.org/moin/TimeComplexity)
- [LeetCode](https://leetcode.com/) for practice problems

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Thanks to the Python community for excellent documentation
- Inspired by classic computer science textbooks
- Built for educational purposes and interview preparation

---

⭐ **Star this repository if you find it helpful!**

📧 **Questions?** Feel free to open an issue or reach out!

---

*Happy Coding! 🚀*
