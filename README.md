
## Custom Instruction Compiler for Equation `z = a * a + b * b - 2 * a * b`

### Overview

This project demonstrates the design and implementation of **custom assembly instructions** to compute the equation `z = a * a + b * b - 2 * a * b`. The project involves using **NASM (Netwide Assembler)** to compile assembly code, **Python** to interact with the user and control execution, and **objdump** for disassembling the generated binary to view the assembly code.

The project also includes a **token generation**, **symbol table**, and **three-address code** output, which are essential for understanding how the computation is carried out at a lower level in assembly.

---

## Tech Stack

- **Python 3**: The scripting language to manage user interaction, handle inputs, and automate execution.
- **NASM (Netwide Assembler)**: The assembler used to convert the custom assembly code into object files and binaries.
- **objdump**: Tool used to inspect the binary file and view the assembly code generated from the executable.
- **Bash (optional)**: To automate the assembly process (can be skipped on Windows).

---

## Prerequisites

Before running the project, make sure you have the following installed:

1. **Python 3**:
   - [Download Python](https://www.python.org/downloads/)
   - Install dependencies using pip:
     ```bash
     pip install -r requirements.txt
     ```

2. **NASM (Netwide Assembler)**:
   - [Download NASM](https://www.nasm.us/)
   - Ensure `nasm` is in your PATH by running:
     ```bash
     nasm -v
     ```

3. **objdump**:
   - This is typically bundled with GCC or other developer tools.
   - On Linux:
     ```bash
     sudo apt-get install binutils
     ```

   - On Windows, use tools like **MinGW** or **WSL (Windows Subsystem for Linux)** to access `objdump`.

---

## Project Setup

### 1. Clone the Repository

Start by cloning the project to your local machine:

```bash
git clone https://github.com/your-username/mini_compiler.git
cd mini_compiler
```

### 2. Install Python Dependencies

If you haven't installed the Python dependencies, run:

```bash
pip install -r requirements.txt
```

### 3. Assemble the Assembly Code (with NASM)

Use **NASM** to assemble the custom assembly code:

```bash
nasm -f elf64 compute_z.asm -o compute_z.o
```

This step generates the **object file** (`compute_z.o`).

### 4. Link the Object File

Now link the object file to create an executable:

```bash
ld -o compute_z compute_z.o
```

This generates the **executable file** (`compute_z`).

---

## Running the Program

To compute `z = a * a + b * b - 2 * a * b` using the custom assembly code, run the Python script `main.py`:

### Example Command:

```bash
python main.py COMPUTE_Z 2 3
```

Where `2` and `3` are the values for `a` and `b`.

### Output:

Upon running the command, the output will display:
1. **Computed result**: The value of `z`.
2. **Tokens**: The sequence of instructions used in the computation.
3. **Symbol Table**: A table showing the name, type, and value of variables used.
4. **Three-Address Code**: The intermediate three-address code used for computation.


---

## Viewing Assembly Code with `objdump`

To inspect the generated assembly code from the binary file, you can use **objdump**:

```bash
objdump -d compute_z
```

This will display the **disassembled machine code** and provide insight into the underlying assembly code.

### Example Output:

```bash
Disassembly of section .text:
...
```

---

## File Structure

```bash
mini_compiler/
├── compute_z.asm         # Your custom assembly code
├── compute_z.o           # Object file (generated from NASM)
├── compute_z             # Executable (generated from the object file)
├── main.py               # Python CLI to run everything
└── compiler/
    ├── input_writer.py   # Writes values of a and b to assembly
    ├── compiler_utils.py # Helper functions to generate tokens, symbol table, and three-address code
```

---

## Helper Commands for Step-by-Step Execution

Here are the key commands for assembling and running the project:

### 1. **Assemble the Code** (Generate `.o` Object File)

```bash
nasm -f elf64 compute_z.asm -o compute_z.o
```

### 2. **Link the Object File** (Generate the Executable)

```bash
ld -o compute_z compute_z.o
```

### 3. **Run the Python Script** (To compute the result)

```bash
python main.py COMPUTE_Z 2 3
```

### 4. **Inspect the Assembly Code** (Using `objdump`)

```bash
objdump -d compute_z
```

---

## Conclusion

This project is designed to help you learn about custom assembly instructions and how compilers work at a low level. It uses **NASM** to write and assemble custom instructions, while **Python** controls the flow and generates tokens, symbol tables, and three-address code. The output is displayed in an easy-to-understand format, allowing you to track how the computation is performed at every stage.

---
