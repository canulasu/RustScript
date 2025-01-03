import argparse
import os

parser = argparse.ArgumentParser(description="RustScript Interpreter")

parser.add_argument('-e', '--execute', type=str, help='Execute a RustScript program.')
parser.add_argument('-v', '--version', action='store_true', help='RustScript version.')

args = parser.parse_args()

if args.execute:

    libraries = []

    choosefile = args.execute

    if '.rscript' in choosefile:

        with open(choosefile, 'r') as file:


            lines = file.readlines()

            read = 0

            for line in lines:

                linetoread = lines[read]

                command = linetoread

                if command.startswith('use'):
                    libraries.append(command.replace('use ', '').strip())

                else:

                    with open('compile.rs', 'a') as file:
                        pass
                    with open('compile.rs', 'w') as file:
                        pass
                    with open('compile.rs', 'a') as file:
                        file.write('#![allow(unused_imports)]\n')
                        loop = 0
                        for item in libraries:
                            file.write(f'use {libraries[loop]};\n')
                            loop += 1
                        file.write('fn main() {\n')
                        file.write(f'    {command};\n')
                        file.write('}\n')
                    os.system('rustc compile.rs > ' + os.devnull + ' 2>&1')
                    try:
                        os.remove('compile.rs')
                    except:
                        print('ERROR: Code Execution Failed: CODE ERROR')
                    os.system('./compile')
                    os.remove('compile') 

                read += 1


    else:
        print('ERROR: Incorrect file type, RustScript files need to be .rscript')

elif args.version:

    print('RustScript v0.0.2')

else:

    import os

    libraries = []

    print('RustScript v0.0.2')

    while True:

        command = input('>>> ')

        if command.startswith('use'):
            libraries.append(command.replace('use ', '').strip())

        else:
            with open('compile.rs', 'a') as file:
                pass
            with open('compile.rs', 'w') as file:
                pass
            with open('compile.rs', 'a') as file:
                file.write('fn main() {\n')
                file.write(f'    {command}\n')
                file.write('}\n')

            os.system('rustc compile.rs > ' + os.devnull + ' 2>&1')

            try:
                os.remove('compile.rs')
            except:
                print('ERROR: Code Execution Failed: CODE ERROR')
            os.system('./compile')
            os.remove('compile')
