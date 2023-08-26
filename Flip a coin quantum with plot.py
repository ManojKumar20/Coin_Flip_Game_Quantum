# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 16:08:47 2023

@author: DELL
"""


# Importing standard Qiskit libraries and configuring account
from qiskit import QuantumCircuit, execute, Aer, IBMQ
from qiskit.compiler import transpile, assemble
from qiskit.tools.jupyter import *
from qiskit.visualization import *

# create a circuit with 1 qubit to process information, and 1 classical bit to store the result
circuit = QuantumCircuit(1, 1)
circuit.draw()

# apply a Hadamard gate to transform the qubit into a superposition state
circuit.h(0)

# apply a measurement to retrieve the definite state of a qubit in superposition, and store it in the classical bit
circuit.measure([0], [0])

circuit.draw()

# run in a simulator
backend = Aer.get_backend('qasm_simulator')

# use this to run in a real quantum computer provided by IBM
# you can see the options in IBM Quantum Experience dashboard, here I use ibmq_london
# backend = provider.get_backend('ibmq_london')

# execute the job in 1 shot, run it multiple times to get a different results
job = execute(circuit, backend, shots=1)
counts = job.result().get_counts(circuit)

print("Result:")

if '0' in counts.keys():
    print("tail")
else:
    print("head")

# we can also run it in 100 shots, this will show us the counts of '0' and '1' appeared in 100 shots/experiments
job = execute(circuit, backend, shots=100)
counts = job.result().get_counts(circuit)

print("Result:", counts)

plot_histogram(counts)