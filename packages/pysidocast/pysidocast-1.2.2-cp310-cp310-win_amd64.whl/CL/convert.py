import os


for file in os.listdir('.'):
    if file.endswith('.h'):
        with open(file, 'r') as f:
            content = f.read()
            content = "\n".join([(line.replace('<CL/', '"./').replace('>', '"') if line.startswith('#include <CL') else line) for line in content.splitlines()])
        with open(file, 'w') as f:
            f.write(content)
