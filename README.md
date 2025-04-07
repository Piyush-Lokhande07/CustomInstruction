# 🔧 Custom Instruction for `z = a*a + b*b - 2*a*b`

## 🎯 Objective

This project demonstrates how to **design and implement custom assembly instructions** to compute the mathematical equation:

```
z = a*a + b*b - 2*a*b
```

It simulates a mini-compiler that performs the full compilation flow using:
- ✅ NASM (Netwide Assembler)
- ✅ Python for automation
- ✅ objdump to inspect the generated assembly

---

## 🔄 Flow of Execution

When you run:

```bash
python3 main.py COMPUTE_Z 2 3
```

Here’s what happens step-by-step:

1. 📥 **Input Handling**
   - Python (`main.py`) reads values for `a` and `b`.

2. 📝 **Assembly File Update**
   - `compute_z.asm` is updated with these values via `compiler/input_writer.py`.

3. 🏗️ **Assembly & Linking**
   - The assembly file is compiled into machine code using `nasm` and `ld`.

4. 🚀 **Execution**
   - The generated executable computes the value and prints the result.

5. 🧠 **Compiler Internals Output**
   - You also get:
     - 🧩 **Tokens**
     - 📘 **Symbol Table**
     - 🛠️ **Three-Address Code (TAC)**

---

## 📦 Pseudo-Register Loading (Easy Explanation)

Think of CPU registers as R1, R2, etc. Here’s how the equation is calculated:

```assembly
; Step 1: a*a
R1 = a
R1 = R1 * a        ; R1 = a^2
R2 = R1            ; Store in R2

; Step 2: b*b
R1 = b
R1 = R1 * b        ; R1 = b^2
R2 = R2 + R1       ; R2 = a^2 + b^2

; Step 3: 2*a*b
R1 = a
R1 = R1 * b        ; R1 = a*b
R1 = R1 * 2        ; R1 = 2*a*b
R2 = R2 - R1       ; Final: z = a^2 + b^2 - 2*a*b
```

✅ Final result is in `R2`, and it's stored in variable `z`.

---

## 📋 Prerequisites

Make sure you have these installed:

- 🐍 **Python 3**  
  [Download](https://www.python.org/downloads/)  
  *(Optional)* Install dependencies:  
  ```bash
  pip install -r requirements.txt
  ```

- 🛠️ **NASM (Assembler)**  
  [Download](https://www.nasm.us/)  
  Verify:
  ```bash
  nasm -v
  ```

- 🔗 **ld (Linker)**  
  Linux:  
  ```bash
  sudo apt-get install build-essential
  ```

- 🔍 **objdump**  
  For inspecting binaries:  
  ```bash
  sudo apt-get install binutils
  ```

- 💻 **Bash**  
  (Default on Linux/macOS, use Git Bash or WSL on Windows)

---

## 🧪 Steps to Run

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Piyush-Lokhande07/CustomInstruction.git
cd mini_compiler
```

### 2️⃣ Assemble the Code

```bash
nasm -f elf64 compute_z.asm -o compute_z.o
```

### 3️⃣ Link the Object File

```bash
ld -o compute_z compute_z.o
```

### 4️⃣ Run the Python Script

```bash
python3 main.py COMPUTE_Z 2 3
```

🖥️ Output:
- Computed result of `z`
- Tokens
- Symbol Table
- Three-Address Code

### 5️⃣ View the Assembly Code (Optional)

```bash
objdump -d compute_z
```

---

## 🗂️ File Structure

```bash
mini_compiler/
├── compute_z.asm         # Custom assembly logic
├── compute_z.o           # Object file (generated)
├── compute_z             # Executable (linked)
├── main.py               # Main Python controller
└── compiler/
    ├── input_writer.py   # Writes a, b into the ASM file
    └── compiler_utils.py # Generates tokens, symbol table, TAC
```

---

## ✅ Conclusion

This project simulates how a real compiler works under the hood:

🔹 **Lexical Analysis** → Tokens  
🔹 **Syntax & Semantic Analysis** → Symbol Table  
🔹 **Intermediate Code** → Three-Address Code  
🔹 **Target Code Generation** → Custom Assembly  
🔹 **Assembler & Linker** → Machine Code & Executable  
🔹 **Execution** → Result printed in terminal  

⚙️ The result of `z = a*a + b*b - 2*a*b` is calculated using hand-written assembly, with compiler-style analysis and automation.

---
