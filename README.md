## 🛠️ Custom Instruction for Equation: `z = a² + b² - 2ab`

### 🎯 Objective  
The objective of this project is to **design a custom instruction** for the arithmetic equation:

> `z = a² + b² - 2ab`

within a **mini compiler** setup. The compiler:

- Generates custom **assembly instructions** for the equation  
- Simulates the computation at the low-level using registers and memory  
- Displays:
  - ✅ **Computed Result**
  - 🧾 **Lexical Tokens**
  - 📋 **Symbol Table**
  - 🧮 **Three-Address Code**
  - 🌳 **Parse Tree**

This showcases how a specific arithmetic expression can be handled from **high-level input** down to **low-level execution**.

---

## 🔄 Flow of Execution (from Input to Output)

When you run:

```bash
python3 main.py COMPUTE_Z 2 3
```

### 1️⃣ **User Input**  
**File:** `main.py`

- Takes user input from the terminal (e.g., `a = 2`, `b = 3`).
- Passes these values to other modules for further processing.

---

### 2️⃣ **Assembly Code Generation**  
**File:** `compiler/input_writer.py`

- Creates `compute_z.asm`, a **custom assembly file** containing the instructions to compute `z = a² + b² - 2ab`.
- Inserts the values of `a` and `b` into the `.data` section.

---

### 3️⃣ **Assembling the Code**  
**Tool:** `NASM`

```bash
nasm -f elf64 compute_z.asm -o compute_z.o
```

- Compiles the `.asm` file to an **object file** `compute_z.o`.

---

### 4️⃣ **Linking to Executable**  
**Tool:** `ld`

```bash
ld -o compute_z compute_z.o
```

- Links the object file to create the final executable `compute_z`.

---

### 5️⃣ **Execution of Custom Instruction**  
**Command:**  
```bash
./compute_z
```

- Runs the compiled binary.  
- Performs the equation `z = a² + b² - 2ab` using low-level assembly instructions.
- Result is displayed directly in the terminal.

---

### 6️⃣ **Compiler Backend Output**  
**File:** `compiler/compiler_utils.py`

- Python prints the following to the terminal:
  - 🧾 **Tokens** – Lexical breakdown of the expression  
  - 📋 **Symbol Table** – Variables and their values  
  - 🧮 **Three-Address Code** – Intermediate representation 
---




---

## 🔧 Prerequisites

Before running this project, make sure the following tools are installed on your system:

### ✅ 1. Python 3
Used for scripting and automation.

- 📥 **Install Python**: [Download from official site](https://www.python.org/downloads/)
- 🔍 Check if it's installed:
  ```bash
  python3 --version
  ```
- 📦 (Optional) Install dependencies:
  ```bash
  pip install -r requirements.txt
  ```

---

### ✅ 2. NASM (Netwide Assembler)
Used to assemble the `.asm` file into an object file.

- 📥 **Install NASM**:
  - **Linux**:
    ```bash
    sudo apt update
    sudo apt install nasm
    ```
  - **Windows**: [Download NASM](https://www.nasm.us/pub/nasm/releasebuilds/)
  - **macOS**:
    ```bash
    brew install nasm
    ```
- 🔍 Check if it's installed:
  ```bash
  nasm -v
  ```

---

### ✅ 3. LD (Linker)
Used to link object files and create an executable.

- **Usually comes pre-installed** with build tools.
- 🔍 Check:
  ```bash
  ld --version
  ```

> If not installed on Linux:
```bash
sudo apt install binutils
```

---

### ✅ 4. `objdump`
Used to disassemble the binary and inspect the machine code.

- **Linux/macOS**: Comes with `binutils`.
  ```bash
  sudo apt install binutils
  ```
- **Windows**:
  - Install **MinGW** or **WSL (Windows Subsystem for Linux)**.
  - Or use [MSYS2](https://www.msys2.org/) to get `objdump`.

- 🔍 Verify:
  ```bash
  objdump --version
  ```

---

## 📁 Project Structure

```bash
mini_compiler/
├── compute_z.asm         # Assembly with custom instruction
├── compute_z.o           # Object file from NASM
├── compute_z             # Final executable
├── main.py               # Entry point to run everything
└── compiler/
    ├── input_writer.py   # Writes input into compute_z.asm
    ├── compiler_utils.py # Generates tokens, symbol table, and 3AC
```

---

## 🛠️ Register Pseudo Execution (R1, R2 format)

Here’s how your custom instruction works at register level:

```asm
mov    a, %eax        ; R1 = a
imul   %eax, %eax     ; R1 = R1 * a    ; now R1 = a * a
mov    %eax, %r8d     ; R2 = R1        ; now R2 = a^2

mov    b, %eax        ; R1 = b
imul   %eax, %eax     ; R1 = R1 * b    ; now R1 = b * b
add    %eax, %r8d     ; R2 = R2 + R1   ; now R2 = a^2 + b^2

mov    a, %eax        ; R1 = a
imul   b, %eax        ; R1 = R1 * b    ; now R1 = a * b
add    %eax, %eax     ; R1 = R1 + R1   ; now R1 = 2 * a * b
sub    %eax, %r8d     ; R2 = R2 - R1   ; now R2 = a^2 + b^2 - 2ab

mov    %r8d, z        ; store R2 (the result) into memory at z

```

---

## 🌳 Parse Tree for `z = a*a + b*b - 2*a*b`

```
                (=)
              /     \
           (z)       (-)
                    /     \
                (+)       (*)
               /   \     /   \
             (*)   (*)  (2)  (*)
            / \    / \       / \
          (a)(a) (b)(b)     (a)(b)
```
---

## 🌟 Benefits of Custom Instruction for `z = a*a + b*b - 2*a*b`

- ⚡ **Faster Execution** – Minimal instructions, optimized register use.
- 🧠 **Low-Level Control** – Full control over hardware behavior and data flow.
- 🛠️ **Customizable** – Easy to adapt for other math expressions or formulas.
- 🎓 **Educational** – Reinforces compiler concepts like parsing, TAC, and assembly.
- 📉 **Reduced Overhead** – No dependency on high-level runtime or libraries.
- 💡 **Real-World Insight** – Shows how compilers and CPUs work behind the scenes.

--- 
## 🧪 How to Run

### 🔧 1. Assemble Assembly File
```bash
nasm -f elf64 compute_z.asm -o compute_z.o
```

### 🔗 2. Link Object File
```bash
ld -o compute_z compute_z.o
```

### ▶️ 3. Run the Program via Python
```bash
python3 main.py COMPUTE_Z 2 3
```

### 🧠 4. View Disassembled Code
```bash
objdump -d compute_z
```

## ✅ Conclusion

You've successfully built a **mini compiler** that:
- Parses input and builds a syntax tree 🌳
- Generates **three-address intermediate code** 🧾
- Produces **custom assembly instructions** 🛠️
- Assembles, links, and runs the machine code using NASM + Python 🚀
- Offers full visibility via `objdump` 🔍

This project gives hands-on understanding of **compiler construction**, **register-level computation**, and **low-level architecture**. 🧠
