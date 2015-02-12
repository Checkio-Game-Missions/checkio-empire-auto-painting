For each step the system can paint only one side of an item.
After that, an operator must reload the machine and paint the other side
(the system detects painted sides automatically).
The painting process always takes the same amount of time.

The camera can paint K surfaces at a time.
You should write a program
which will allow him to paint N (0 < N ≤ 10) surfaces in the shortest possible timeframe.
Be careful that you don't paint the item more than two times.


![Paint](system.png)

The items are numbered from 0 to 9.
You are given the paint holding capacity of the machine (K) and the quantity of items (N).
You should return the sequence Stephen must paint as a string,
where each action is the numbers of painted items. Actions separated by comma (",").
