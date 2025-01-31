### Exercise 0
# How to format the output from a Python script

# The general function to use is 'print'. such function 
# does accept an expression, as argument, which is directed 
# to the standard output (terminal) in the form of a string.
# The string can be formed by including 'variables' that can be 
# formatted, converted in characters and added together to form
# the final string.

# For instance:
# >> N=6.02214076e23
# >> ss="The Avogadro's number is {:.3e}".format(N)
# >> print(ss)
#
# Or
#
# >> ss=f"The Avogadro's number is {N:.3e}"
# >> print(ss)



print("\n**** Printing: a primer ****\n")

help(print)

a=2
b=3

c=a+b

print("String expressions:\n")

# Method 1
print("Method 1) %s + %s = %s" % (str(a), str(b), str(c)))

# Method 2
ss=f"Method 2) {a} + {b} = {c}"
print(ss)

# Method 3
ss="Method 3) {} + {} = {}"
print(ss.format(a,b,c)) 

# ---------
# Format descriptors

d=2.
print("\nPrinting formats: representations of the number d=2. in different ways")
print("according to the printing format and/or conversion chosen\n")

print("d = %4.2f,    %4.2e (scient.), %4i (interger),     %s (string)" % 
      (d, d, int(d), str(d)))


print("d = {:.3f}".format(d))


e=[0.1, 1.23, 2.00, 3.23, 4.34, 5.12]
print("\nPrinting lists")
print("\ne = ", e)


print("e = ", end='')
[print("%4.2f" % e[j], end=' ') for j in range(len(e))]
print()

ss="e = " + '  '.join(f'{j:.2e}'.format(j) for j in e) + "\n"
print(ss)