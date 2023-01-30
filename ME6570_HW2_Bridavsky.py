import sympy as s

# Problem One

        ##Set One:
#phi1 = -3*t
#phi2 = 4*t + t^2
#phi3 = 2*t^2

# Linearly dependent if I can represent any phi as a function of the others:

# phi2 = -4/3*(phi1) + 1/2*phi3  <<----- I can represent phi2 as a function of phi1 and phi3, therefore this set is linearly dependent regardless of domain boundaries.

        ##Set One Mk.2: 
## change one of the functions so that all three are linearly independent
## I choose phi1 = -3t^3

t = s.symbols('t')


print('wronskian with phi3 = -3t^3:', s.wronskian([(-3*t**3), (4*t + t**2), (2*t**2)], t)) # This returns -48t^3 - if Wronskian is =/= 0 then linearly independent



## Problem Two: write code that calculates the Wronskian and plots it over the range [0, 2]. Show that the functions are linearly independent.

incrementedTime = []

for i in range(101):
    incrementedTime.append((i)*0.02)

x = s.symbols('x')
s.plot(s.wronskian([(s.sin(x)), (s.sin(2*x)), (s.cos(x)), (s.cos(2*x))], x), xlim = (0,2))


## As you can see here, the Wronskian for this set of equations is 0 at all 100 points on (0.02, 0.02, 2), which means that they are linearly dependent.