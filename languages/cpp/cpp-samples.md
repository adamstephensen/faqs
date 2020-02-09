## C++ Samples

### Creating References

A reference variable is a "reference" to an existing variable, and it is created with the & operator:

```cpp
string food = "Pizza";
string &meal = food;

cout << food << "\n";  // Outputs Pizza
cout << meal << "\n";  // Outputs Pizza
```
Source: https://www.w3schools.com/cpp/cpp_references.asp


### Memory Address

```cpp
string food = "Pizza";

cout << &food; // Outputs 0x6dfed4
```
Source: https://www.w3schools.com/cpp/cpp_references_memory.asp


### Creating Pointers

```cpp
string food = "Pizza";  // A food variable of type string
string* ptr = &food;    // A pointer variable, with the name ptr, that stores the address of food

cout << food << "\n"; // Output the value of food (Pizza)

cout << &food << "\n"; // Output the memory address of food (0x6dfed4)

cout << ptr << "\n"; // Output the memory address of food with the pointer (0x6dfed4)
```

different ways to declare pointers: 

```cpp
string* mystring; // Preferred
string *mystring;
string * mystring;
```

Source: https://www.w3schools.com/cpp/cpp_pointers.asp


### Dereference: Get Memory Address and Value

```cpp
string* ptr = &food;    // Pointer declaration

// Reference: Output the memory address of food with the pointer (0x6dfed4)
cout << ptr << "\n";

// Dereference: Output the value of food with the pointer (Pizza)
cout << *ptr << "\n";
```

Note that the * sign can be confusing here, as it does two different things in our code:

When used in declaration (string* ptr), it creates a pointer variable.
When not used in declaration, it act as a dereference operator.


### Pass by reference 

```cpp
void swapNums(int &x, int &y) {
  int z = x;
  x = y;
  y = z;
}
```
Source: https://www.w3schools.com/cpp/cpp_function_reference.asp

