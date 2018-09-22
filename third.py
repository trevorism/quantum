from pyquil.quil import Program
from pyquil.gates import X, Y, Z, MEASURE

print("Multiple inst arguments with final measurement:")
print(Program().inst(X(0), Y(1), Z(0)).measure(0, 1))

print("Chained inst with explicit MEASURE instruction:")
print(Program().inst(X(0)).inst(Y(1)).measure(0, 1).inst(MEASURE(1, 2)))

print("A mix of chained inst and measures:")
print(Program().inst(X(0)).measure(0, 1).inst(Y(1), X(0)).measure(0, 0))

print("A composition of two programs:")
print(Program(X(0)) + Program(Y(0)))