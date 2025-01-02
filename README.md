# RustScript
RustScript is a Rust-like programming language. RustScript relies on the rustc compiler and is an interpreted Rust-based language with easier syntax. RustScript is like a Rust interprter with easier syntax and is compiled line by line, at runtime, kind of like mainstream interpreted programming languages like Python. The interpreter itself is writen in Python3 and does not have any dependencies except the rustc compiler (for compiling the code at runtime).
***
# RustScript Syntax
RustScript syntax is very similar to Rust, with slight differences. Below are the key differences:
- You do not need to add a semicolon at the end of each line unlike Rust, since the RustScript interpreter takes this in account for you.
- For working with variables, you need to provide all the commands and code related to the variables you are using in the same line, as each line is compiled and executed one by one at runtime.
- RustScript does not currently support external libraries or Cargo. To work with provided built in libraries, you can directly use the "use" command followed by the library name.
