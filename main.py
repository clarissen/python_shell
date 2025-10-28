import sys

def main(keep_running: bool): 
    while keep_running == True: 
        sys.stdout.write("$ ") 
        pass 
    # get user input 
    command = input() 
    print(f"{command}: command not found") 
    
if __name__ == "__main__": 
    main(True)