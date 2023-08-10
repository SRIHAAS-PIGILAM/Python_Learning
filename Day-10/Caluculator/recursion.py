"""Certainly, I'd be happy to explain recursion in Python.

Recursion is a programming technique in which a function calls itself in order to solve a problem. In essence, a recursive function is one that performs its task by breaking it down into smaller, similar subproblems. Each of these subproblems is solved in a similar manner, often using the same function."""

# Here's a classic example of recursion: calculating the factorial of a number.


import turtle


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


result = factorial(5)  # Calculates 5!
print(result)  # Output: 120


# In this example:
"""
- The `factorial` function calculates the factorial of a given number `n`.
- The base case is when `n` is 0; in this case, the function returns 1 (0! is defined as 1).
- Otherwise, the function recursively calls itself with a smaller value (`n - 1`) and multiplies it by `n`.

It's important to have a base case in recursive functions to prevent infinite recursion. Each recursive call should reduce the problem's size towards the base case.

Recursion can be powerful for solving problems that have a naturally recursive structure, but it's essential to manage memory usage and performance. Recursion can sometimes lead to excessive memory consumption and slow execution for very large problems. In some cases, an iterative (loop-based) approach might be more efficient."""

# Here's another example of a recursive function that calculates the nth term of the Fibonacci sequence:


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


result = fibonacci(6)  # Calculates the 6th Fibonacci number
print(result)  # Output: 8 (0, 1, 1, 2, 3, 5, 8)

"""
Recursion is a powerful and elegant technique, but it can be tricky to understand and debug at times. Ensuring proper termination conditions and understanding how the function's state changes with each recursive call is key to successful recursive programming."""


# **Example 1: Sum of List Elements**

def sum_list_elements(arr):
    if not arr:
        return 0
    else:
        return arr[0] + sum_list_elements(arr[1:])


numbers = [1, 2, 3, 4, 5]
result = sum_list_elements(numbers)
print(result)  # Output: 15 (1 + 2 + 3 + 4 + 5)


# **Example 2: Power Calculation**

def power(base, exponent):
    if exponent == 0:
        return 1
    else:
        return base * power(base, exponent - 1)


result = power(2, 3)  # Calculates 2^3
print(result)  # Output: 8 (2 * 2 * 2)


# **Example 3: Palindrome Checking**

def is_palindrome(s):
    if len(s) <= 1:
        return True
    else:
        return s[0] == s[-1] and is_palindrome(s[1:-1])


word = "racecar"
print(is_palindrome(word))  # Output: True


# **Example 4: Tower of Hanoi**

def tower_of_hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    tower_of_hanoi(n - 1, source, auxiliary, target)
    print(f"Move disk {n} from {source} to {target}")
    tower_of_hanoi(n - 1, auxiliary, target, source)


# Moves 3 disks from 'A' to 'C' using 'B' as auxiliary
tower_of_hanoi(3, 'A', 'C', 'B')


# **Example 5: Recursive Binary Search**

def binary_search(arr, target, low, high):
    if low > high:
        return -1  # Target not found
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, target, low, mid - 1)
    else:
        return binary_search(arr, target, mid + 1, high)


sorted_numbers = [1, 3, 5, 7, 9, 11, 13, 15, 17]
target_number = 11
index = binary_search(sorted_numbers, target_number,
                      0, len(sorted_numbers) - 1)
print(index)  # Output: 5 (index of 11 in the list)

"""
Each example demonstrates a more complex use of recursion, from summing elements in a list to solving the Tower of Hanoi puzzle and implementing binary search. As you can see, recursion can be applied to various problem domains, but it's crucial to carefully design your recursive functions to ensure they terminate correctly and efficiently."""


# **Example 6: Generating Permutations**

def generate_permutations(string, prefix=""):
    if len(string) == 0:
        print(prefix)
    else:
        for i in range(len(string)):
            new_prefix = prefix + string[i]
            new_string = string[:i] + string[i+1:]
            generate_permutations(new_string, new_prefix)


word = "abc"
generate_permutations(word)  # Generates all permutations of "abc"


# **Example 7: Merge Sort**

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i, j, k = 0, 0, 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1


numbers = [12, 11, 13, 5, 6, 7]
merge_sort(numbers)
print(numbers)  # Output: [5, 6, 7, 11, 12, 13]


# **Example 8: Fractal Drawing (Sierpinski Triangle)**


def draw_sierpinski_order(n, size):
    if n == 0:
        for _ in range(3):
            turtle.forward(size)
            turtle.left(120)
    else:
        draw_sierpinski_order(n - 1, size / 2)
        turtle.forward(size / 2)
        draw_sierpinski_order(n - 1, size / 2)
        turtle.backward(size / 2)
        turtle.left(60)
        turtle.forward(size / 2)
        turtle.right(60)
        draw_sierpinski_order(n - 1, size / 2)
        turtle.left(60)
        turtle.backward(size / 2)
        turtle.right(60)


turtle.speed(0)
turtle.penup()
turtle.goto(-200, -200)
turtle.pendown()
draw_sierpinski_order(3, 400)
turtle.done()

"""
These examples showcase the versatility and complexity that recursion can bring to your programming toolkit. From generating permutations and performing merge sort to drawing intricate fractals, recursion enables you to solve a wide range of problems in an elegant and organized manner. Just remember that recursion requires careful design and consideration of base cases to ensure proper termination and correctness."""
