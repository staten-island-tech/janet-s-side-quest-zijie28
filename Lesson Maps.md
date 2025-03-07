# **Lesson: Using `map()` in Python and Skipping an Index in a Loop**

## **Objective**
By the end of this lesson, you will:
- Understand how the `map()` function works in Python.
- Learn when and how to use `map()` for efficient data transformations.
- Discover how to **skip an index** when looping through a dataset.
- Understand **list comprehensions** in the simplest way.

---

## **1. Understanding `map()` in Python**
The `map()` function lets you **apply a function to every item in a list** (or another sequence) without writing a loop.

### **Syntax**
```python
map(function, iterable)
```
- `function`: A function that will be applied to each item.
- `iterable`: A list or other sequence that will be processed.

---

### **Example 1: Doubling Numbers Using `map()`**
Instead of using a `for` loop to double numbers, `map()` can do it in one line.

#### **Using a `for` loop**
```python
numbers = [1, 2, 3, 4, 5]
doubled_numbers = []

for num in numbers:
    doubled_numbers.append(num * 2)

print(doubled_numbers)
```
#### **Using `map()`**
```python
numbers = [1, 2, 3, 4, 5]

# Use map() to double the numbers
doubled_numbers = map(lambda x: x * 2, numbers)

print(list(doubled_numbers))
```
### **Output:**
```
[2, 4, 6, 8, 10]
```

**How it works:**
- Instead of writing a `for` loop, we use `map()` to apply `x * 2` to each number.
- `map()` **automatically loops through the list** for us.
- The result is an **iterator**, so we convert it to a **list** to see the output.

---

## **2. Skipping an Index When Looping**
Sometimes, you need to **skip the first row** in a dataset, like when the first row contains column names.

### **Example 2: Skipping the First Row in a Loop**
```python
data = [
    ["Store Name", "Day 1", "Day 2", "Day 3"],  # Header row (skip this)
    ["Store A", 5000, 7000, 6500],
    ["Store B", 8000, 6000, 7500]
]

for row in data[1:]:  # Skip the first row
    print(row)
```
### **Output:**
```
['Store A', 5000, 7000, 6500]
['Store B', 8000, 6000, 7500]
```
**Key Takeaway:**  
- `data[1:]` **removes the first row**, so we only loop through the actual data.

---

## **3. Using `map()` and Skipping the First Row**
Now, let’s use `map()` to process numerical data **while skipping the first row**.

### **Example 3: Summing Each Store’s Sales**
```python
def calcRow(data):
    row_totals = {}

    for row in data[1:]:  # Skipping the first row
        store_name = row[0]  # First column is the store name
        sales = map(int, row[1:])  # Convert sales to numbers
        row_totals[store_name] = sum(sales)  # Sum up sales for the store

    return row_totals

# Example Data
sales_data = [
    ["Store Name", "Day 1", "Day 2", "Day 3"],  # Header row
    ["Store A", 5000, 7000, 6500],
    ["Store B", 8000, 6000, 7500]
]

totals = calcRow(sales_data)
print(totals)
```
### **Output:**
```
{'Store A': 18500, 'Store B': 21500}
```

---

## **4. Understanding List Comprehensions (Explained Simply)**
### **What is a List Comprehension?**
A list comprehension is just a **shortcut** to create a new list from another list.

### **Example 4: Making a New List from an Old One**
Let’s say we have a list of numbers:
```python
numbers = [1, 2, 3, 4, 5]
```
We want to **double each number** and store the result in a new list.

#### **Using a `for` loop:**
```python
doubled = []
for num in numbers:
    doubled.append(num * 2)

print(doubled)
```
#### **Using List Comprehension:**
Think of list comprehension as:
1. **Start with `[` and `]`** because we are making a new list.
2. **Inside, put the formula (`num * 2`)** for each item.
3. **Then add `for num in numbers`** to loop through the original list.

It’s like saying:  
*"For each number in `numbers`, multiply it by 2 and store it in the new list."*
```python
doubled = [num * 2 for num in numbers]
print(doubled)
```
### **Output:**
```
[2, 4, 6, 8, 10]
```



---

## **5. List Comprehensions vs. `map()`**
Both `map()` and list comprehensions **transform lists**, but they have some differences.

### **Example 5: Summing Sales Using List Comprehension**
```python
def calcRowLC(data):
    row_totals = {row[0]: sum([int(x) for x in row[1:]]) for row in data[1:]}
    return row_totals

print(calcRowLC(sales_data))
```
### **Output:**
```
{'Store A': 18500, 'Store B': 21500}
```

---

### **When to Use Which?**
| **Feature**       | **map()**                         | **List Comprehension**           |
|------------------|---------------------------------|---------------------------------|
| **Performance**  | Faster for big data            | Slightly slower                |
| **Readability**  | Can be harder to read          | Easier to understand           |
| **Flexibility**  | Works with multiple iterables  | More readable for simple cases |

---

## **6. Final Challenge**
Try using `map()` to **convert a list of temperatures from Fahrenheit to Celsius**, but **skip the first item** in the list.

### **Formula:**
\(
C = (F - 32) 	imes rac{5}{9}
\)

```python
temperatures = ["Label", 32, 50, 77, 104]

# Use map() to convert Fahrenheit to Celsius, skipping the first item
```

