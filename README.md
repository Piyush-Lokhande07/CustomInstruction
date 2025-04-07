# Custom Instruction Compiler for Equation `z = a*a + b*b - 2*a*b`

## Objective

This project demonstrates the design and implementation of **custom assembly instructions** to compute the equation:

```
z = a*a + b*b - 2*a*b
```

We use NASM (Netwide Assembler) to write and compile assembly code, and Python to drive the process, generate tokens, symbol tables, and intermediate (three-address) code. The goal is to mimic a mini compiler that processes arithmetic expressions at a low level.

---

## Flow of Execution

When you run:

```bash
python3 main.py COMPUTE_Z 2 3
```

The process works as follows:

1. **User Input**  
   The Python script (`main.py`) receives the command `COMPUTE_Z` along with values for `a` and `b` (here, `2` and `3`).

2. **Assembly File Generation**  
   The function `update_asm()` in `compiler/input_writer.py` updates `compute_z.asm` by inserting the input values. The assembly file now contains instructions that compute:
   - `a * a`
   - `b * b`
   - `2 * a * b`  
   and then combines them as:
   ```
   z = a*a + b*b - 2*a*b
   ```

3. **Assembly and Linking**  
   The script uses NASM to assemble `compute_z.asm` into an object file (`compute_z.o`), and then `ld` is used to link the object file into an executable (`compute_z`).

4. **Execution**  
   The executable is run, which loads the values from memory into registers, performs the arithmetic step-by-step, converts the result to a string, and prints the final output.

5. **Additional Compiler Internals**  
   Along with the computed result, the program also displays:
   - **Tokens**: A list of basic elements (e.g., identifiers, operators) that make up the expression.
   - **Symbol Table**: A table that shows the variables (`a`, `b`, and `z`), their types (e.g., `int`), and their values.
   - **Three-Address Code (TAC)**: An intermediate representation breaking down the expression into simple operations.

---

## Pseudo-Register Loading Explanation

In our assembly code, we use registers to hold temporary values during computation. For simplicity, we can think of registers as temporary variables named R1, R2, etc.:

1. **Compute `a*a`:**
   - **R1**: Load value of `a` from memory.
   - Multiply R1 by itself → R1 now holds `a*a`.
   - **R2**: Store the result (i.e., `a*a`) in R2.

2. **Compute `b*b`:**
   - **R1**: Reload value of `b` from memory.
   - Multiply R1 by itself → R1 now holds `b*b`.
   - Add R1 to R2, so R2 now equals `a*a + b*b`.

3. **Compute `2*a*b`:**
   - **R1**: Load value of `a` from memory.
   - Multiply R1 by `b` → R1 = `a*b`.
   - Double R1 (R1 = `2*a*b`).
   - Subtract R1 from R2, so R2 becomes `a*a + b*b - 2*a*b`.

4. **Store the Result:**
   - The final result in R2 is stored in memory variable `z`.

---

## Prerequisites

Before running this project, ensure you have the following installed:

1. **Python 3**  
   Download from [python.org](https://www.python.org/downloads/).  
   (Optionally, install dependencies via: `pip install -r requirements.txt` if a requirements file is provided.)

2. **NASM (Netwide Assembler)**  
   Download and install from [nasm.us](https://www.nasm.us/).  
   Verify installation with:
   ```bash
   nasm -v
   ```

3. **ld (Linker)**  
   Typically installed with your build-essential package.  
   On Ubuntu/Debian:
   ```bash
   sudo apt-get install build-essential
   ```

4. **objdump**  
   Install via binutils (usually pre-installed or installed with GCC):
   ```bash
   sudo apt-get install binutils
   ```

5. **Bash (optional)**  
   Needed for running shell commands. Linux and macOS have Bash by default; Windows users can use Git Bash or WSL.

---

## Steps to Run

1. **Clone the Repository**

   ```bash
   git clone https://github.com/Piyush-Lokhande07/CustomInstruction.git
   cd mini_compiler
   ```

2. **Assemble the Code**

   Use NASM to convert `compute_z.asm` into an object file:
   ```bash
   nasm -f elf64 compute_z.asm -o compute_z.o
   ```

3. **Link the Object File**

   Link the object file to create the executable:
   ```bash
   ld -o compute_z compute_z.o
   ```

4. **Run the Python Script**

   Compute the equation by running:
   ```bash
   python3 main.py COMPUTE_Z 2 3
   ```

   This will:
   - Update `compute_z.asm` with `a = 2` and `b = 3`.
   - Assemble and link the code.
   - Execute the program, printing the computed result and the compiler internals (tokens, symbol table, and TAC).

5. **View the Disassembled Assembly Code**

   To see the low-level machine code, run:
   ```bash
   objdump -d compute_z
   ```

---

## Conclusion

This project shows you how custom assembly instructions can be designed to compute a mathematical equation, with a full compiler-like flow:
- **Lexical Analysis** (tokens),
- **Syntax and Semantic Analysis** (symbol table),
- **Intermediate Code Generation** (three-address code),
- **Target Code Generation** (assembly),
- **Assembly & Linking** (NASM and ld),
- and finally, **Execution**.

By running `python3 main.py COMPUTE_Z 2 3`, you see how the equation `z = a*a + b*b - 2*a*b` is computed step by step, and you gain insight into how compilers process arithmetic expressions at a low level.

---
