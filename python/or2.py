def OR2_gate(A, B):
    return A or B

print("=== OR2 GATE SIMULATION ===")
print("A\tB\tOutput")

inputs = [(0, 0), (0, 1), (1, 0), (1, 1)]

for A, B in inputs:
    output = OR2_gate(A, B)
    print(f"{A}\t{B}\t{int(output)}")
