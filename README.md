# Data-Structures-and-Algorithum

In this Repository I will upload Data structures, Algorithms and I will also explains the BIG O Complexity regarding each algorithum.

## LINKED LISTS :- 

Linked list is a data structure similar to array in a sense that it stores bunch of items. But unlike array, linked lists are not stored in contiguous memory locations. They are instead chained by an element storing address location of next element. This makes insertion very easy. Also unlike dynamic arrays you don't have to pre-allocate some memory capacity.

Advantage : 1) We don't need to pre allocate space.
            2) Insertion is easier.
            
BIG O complexities :- 

- Insert element at beginning = O(1)
- Delete element at beginning = O(1)
- Insert element at end = O(n)
- Delete element at end = O(n)
- Linked List Transversal = O(n)
- Access element by Value = O(n)


## HASH TABLE :-

Hash tables are a type of data structure in which the address or the index value of the data element is generated from a hash function. That makes accessing the data faster as the index value behaves as a key for the data value. In other words Hash table stores key-value pairs but the key is generated through a hashing function.

In Python, the Dictionary data types represent the implementation of hash tables. I have made a python file in which a Hash function is used to locate the data element value by its index value.

BIG O complexities :- 

- Insertion on average = O(1)
- Deletion on average = O(1)
- Look up by Key on average = O(1)
     
