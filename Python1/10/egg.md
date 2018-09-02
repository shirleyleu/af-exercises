### My answer
Given 100 floors and 2 eggs  
Start dropping an egg from the floor at intervals of 10, starting with 10.  
    E.g. Drop from 10, 20, 30... until the egg breaks  
When the egg breaks, drop the second egg from 9 floors below until the egg breaks.  
    E.g. The first egg broke at floor 20. Drop second egg from 11, 12, 13... in order.  

### More thoughts
For 100 floors and 2 eggs, the maximum number of drops for this method is 19.

#### Some generalizations
Given:  
f = number of floors  
e = number of eggs


Compute the eth root of f. `f^(1/e)`   
This value is the approximate number of times that each egg will be dropped.
