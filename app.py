@@ -0,0 +1,32 @@
import os

if os.path.exists('example.txt'):
    print("\nThe file 'example.txt' exists.")
else:
    print("\nThe file 'example.txt' does not exist.")


with open('example.txt', 'w') as file:
    file.write("Jayrick M. Siscon!\n")
    file.write("Studied at ACLC College of Butuan City.\n")

print("File created and content written.")



with open('example.txt', 'a') as file:
    file.write("BSCS 4-A.\n")





print("\nReading content from the file:")
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)  
