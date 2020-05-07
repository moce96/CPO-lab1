 

# Different approach for algorithms and data structure implementation

 - **list of group members:**
 192050214  Mu Yuankai
 192050208 Jia Yuebin
 - **variant description:**
 Hash-map (collision resolution: separate chaining, for array and bucket you can use built-in list) based set.
 
 - **synopsis:**
 Build a hash map, use chain addresses to solve address conflicts, write two versions of mutable and immutable, respectively: add, delete, size, transform list, find, filter, map, reduce, concate, iterator.
 
 - **contribution summary for each group member**
 Mu Yuanai complete the hash_mutable module  
Jia Yuebin complete the hash_immutable module
 - **explanation of taken design decisions and analysis;**
 Firstly, the implementation method of hash table in data structure is introduced.
Secondly, the teacher gives a reference to the realization of single linked list structure.
Third, dig into the hashmap structure and design the structure accordingly
Finally, divide the work into two parts and finish them separately.
 - **work demonstration**
 In the hash_mutabable module, I defined a class HashMap and used chained addresses to resolve address conflicts.It is a data structure that USES stored data to define functions.In HashMap_mutable, I tested this function.
In hashMap_immutable, the chain address method is used to resolve address conflicts.The generated hash table is stored in a two-dimensional array. The functions are: add, delete, size, transform list, find, filter, map, reduce, concate, iterator.In the end, he passed the exam successfully.
 - **conclusion.**
Hash mapping is to calculate the mapped address according to the incoming key, and each key has a different mapped address. For the mapped address, the value stored therein is immutable, but for the hash table, the value should be mutable. This experiment implements hash mapping by writing two different versions of mutable and immutable, and solves the object's mutable and immutable by different methods and tests it. In the experiment, list is used as the hash mapping table. In the mutable and immutable versions, re-hashing and linear detection in the open address method are used to solve the address conflict problem. In the mutable version, we can directly operate on the original data. On the contrary, we cannot directly operate on the data in the immutable version. It is necessary to indirectly operate by introducing intermediate variables or local variables.  
```




 

 
 

