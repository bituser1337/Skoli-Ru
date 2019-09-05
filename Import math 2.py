In  [1]: import math
In  [2]: radius_str = input("Enter the radius of your circle: ")
Enter the radius of your circle: 20
In  [3]: radius_str
Out [3]: '20'

In  [4]: radius_int = int(radius_str)
In  [5]: radius_int
Out [5]: 20

In  [6]: int(radius_str)
Out [6]: 20

In  [7]: radius_str
Out [7]: '20'

In  [8]: math.pi
Out [8]: 3.141592653589793

In  [9]: circumference = 2 * math.pi * radius_int
In  [10]: circumference
Out [10]: 125.66370614359172

In  [11]: area = math.pi * radius_int ** 2
In  [12]: area
Out [12]: 1256.6370614359173

In  [13]: math.pi * radius_int ** 2
Out [13]: 1256.6370614369173

In  [14]: Print("circuference: ", circuference, ", area: ", area)
Circuference:  125.66370614359172 , area: 1256.6370614359173
