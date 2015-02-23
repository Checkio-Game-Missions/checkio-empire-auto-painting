We are using a semi-automatized painting system,
but this system is not perfect.
As such we need to develop an optimisation algorithm for it.
For each step the system can paint only one side of an item.
After that, an operator must reload the machine and paint the other side. The system will detect painted sides automatically.
The painting process always takes the same length of of time to complete and K surfaces may be painted at a time.

You should write a program which will allow us to paint N (0 < N ≤ 10) surfaces in the shortest possible timeframe.
Be careful that you don't paint the same item more than twice.


![Paint](system.png)

Items are numbered from 0 to 9.
You are given the paint holding capacity of the machine (K) and the quantity of items (N).
You should return the sequence  which needs painting as a string where each action is the number of painted items. 
Actions separated by comma (",").

**Input:** Capacity of the painting system and quantity of items as integers. 

**Output:** The sequence of actions as a string.

**Example:**

```python
paint(2, 3)  # "01,12,02"
paint(6, 3)  # "012,012"
paint(3, 6)  # "012,012,345,345"
paint(1, 4)  # "0,0,1,1,2,2,3,3"
paint(2, 5)  # "01,01,23,42,34"
```
**How it is used:**

This is similar to trying to cook three steaks in one frying pan.
Each steak has two sides and it takes a minute to cook one side of two steaks, so
how would you cook each of the steaks in three minutes?
This task takes the concept,  but models it in a technical way.
This is a technological process which you oftnen find in a factories where certain goods must be made with precision timing.

**Precondition:**

```python
0 < capacity <= 10<br>
0 < number <= 10
```

