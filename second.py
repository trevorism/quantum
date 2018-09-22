from pyquil.gates import X
from pyquil.quil import Program
from pyquil.api import QVMConnection

p = Program()

p.inst(X(0)).measure(0, 0)
print(p)

qvm = QVMConnection()

print(qvm.run(p, [0]))