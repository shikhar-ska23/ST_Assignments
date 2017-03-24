Aim:
Implementation of the Fixed-Point Iteration Algorithm in Python.

The Algorithm:
1. Given a function of type x = f (x)
2. Now make an assumption for the value of x, labelling it a.
3. Compute the value of:
f (a),
4. Compute the value of:
f (f (a)),
5. Compare the values obtained in step 3 and step 4
	1. Case 1: If the difference between these two is less than the permissible
	   error, print the root and exit.
	2. Case 2: Otherwise set a = f(a) and continue.
6. Return to step 3.

Assignment:
1. Implement the Fixed-Point Iteration method in Python
2. Calculate the solution for:
i.
1
x = 1 +
x
ii.
x
3
+ 2
x =
7
Note: Use Initial Guess = 1, and Allowed Error = 0.0005, for both.
