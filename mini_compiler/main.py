import sys
import subprocess
from compiler.input_writer import write_values_to_asm
from compiler.compiler_utils import generate_tokens, generate_three_address_code, generate_symbol_table

def run_compute_z(a, b):
    # Step 1: Generate tokens for the equation
    tokens = generate_tokens(a, b)
    
    # Step 2: Generate the symbol table for the variables and their values
    symbol_table = generate_symbol_table(a, b)
    
    # Step 3: Generate the three-address code (TAC) for the equation
    tac = generate_three_address_code(a, b)

    # Step 4: Compute result using assembly
    write_values_to_asm(a, b)
    subprocess.run(["as", "compute_z.asm", "-o", "compute_z.o"], check=True)
    subprocess.run(["ld", "compute_z.o", "-o", "compute_z"], check=True)
    result = subprocess.check_output(["./compute_z"]).decode("utf-8").strip()

    # Step 5: Show output
    print("Computed result:", result)

    
    # Step 6: Show symbol table with column names
    print("\nTokens:")
    tokens_array = [f"{token['value']} ({token['type']})" for token in tokens]
    print(f"[{', '.join(tokens_array)}]")
    
    # Step 7: Show tokens without ID (in array format)
    print("\nSymbol Table:")
    print(f"{'Name':<10} | {'Type':<10} | {'Value'}")
    print("-" * 30)
    for entry in symbol_table:
        print(f"{entry['name']:<10} | {entry['type']:<10} | {entry['value']}")

    
    
    # Step 8: Show Three-Address Code (TAC)
    print("\nThree-Address Code:")
    for line in tac:
        print(line)

def main():
    if len(sys.argv) != 4:
        print("Usage: python main.py COMPUTE_Z <a> <b>")
        sys.exit(1)
    
    command = sys.argv[1]
    a = int(sys.argv[2])
    b = int(sys.argv[3])

    if command == "COMPUTE_Z":
        run_compute_z(a, b)
    else:
        print("Unknown command")

if __name__ == "__main__":
    main()
