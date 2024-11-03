import os

files = os.listdir()
print('Available files:')
for i in files:
    print(i)


fn = input('Enter the file you want to open/Create: ')


while True:

    print("1. Write to File")
    print("2. Read File")
    print("3. Count Words, Lines, and Characters")
    print("4. Exit")
    
    choice = input("Enter your choice: ")

    if choice == '1':
   
        mode = input("Do you want to (o)verwrite or (a)ppend? ").lower()
 
        if mode == 'o':
            with open(fn, 'w') as f:
                print("Opened in overwrite mode.")
                print("Start writing. To stop writing, press Ctrl+C.")
                try:
                    while True:
                        con = input()
                        f.write(con + '\n')
                except KeyboardInterrupt:
                    print("\nContent written successfully in overwrite mode.")
        
        elif mode == 'a':
            with open(fn, 'a') as f:
                print("Opened in append mode.")
                print("Start writing. To stop writing, press Ctrl+C.")
                try:
                    while True:
                        con = input()
                        f.write(con + '\n')
                except KeyboardInterrupt:
                    print("\nContent written successfully in append mode.")
        
        else:
            print("Invalid choice. Returning to main menu.")

    elif choice == '2':
       
        if os.path.exists(fn):
            with open(fn, 'r') as o:
                content = o.read()
                print("\nFile content:\n", content)
        else:
            print("File does not exist.")
    
    elif choice == '3':
        
        if os.path.exists(fn):
            with open(fn, 'r') as fcount:
                fstr = fcount.read()
                line_count = fstr.count('\n') + 1
                word_count = len(fstr.split())  
                char_count = len(fstr) - fstr.count(' ') - fstr.count('\n')  
                with_space_count = len(fstr) 

            
            print("Words:", word_count)
            print("Lines:", line_count)
            print("Characters (without spaces):", char_count)
            print("Characters (with spaces):", with_space_count)
        else:
            print("File does not exist.")
    
    elif choice == '4':
        print("Exiting program.")
        break
    
    else:
        print("Invalid choice. Please try again.")
