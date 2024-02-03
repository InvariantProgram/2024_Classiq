import classiq
# classiq.authenticate(overwrite=True)

from classiq import *

num_qubits = 4
fraction_digits = 0
is_signed = True

@QFunc
def prepare_minus_state(x:QBit):
    X(x)
    H(x)

"""
@QFunc
def main(x: Output[QBit]):
    allocate(1, x)
    prepare_minus_state(x)
"""

@QFunc
def create_initial_state(reg: QArray[QBit]):
    apply_to_all(H, reg)

"""
@QFunc
def main(reg: Output[QArray]):
    allocate(4,reg)
    create_initial_state(reg)
"""

@QFunc
def main(x: Output[QNum], y: Output[QNum]):
    allocate_num(num_qubits=num_qubits, is_signed=is_signed, fraction_digits=fraction_digits, out=x)
    hadamard_transform(x)
    y |= x**2 + 1

quantum_model = create_model(main)
quantum_program = synthesize(quantum_model)

show(quantum_program)