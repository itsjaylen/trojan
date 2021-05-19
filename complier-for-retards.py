import os

def complier():
    print("If ur using this ur so dumb on god just read the install instructions!\n"
          "PLEASE HAVE THE requirements.txt FILE IN THE SAME DIRECTORY!!!!")
    os.system("pip install -r requirements.txt")
    def cleanup():
        cmds = ["RD __pycache__ /Q /S",
                 "RD build /Q /S",
                 "DEL trojan.spec /Q"]
        
        for commands in cmds:
            os.system(commands)
        
    
    logo = input("Use custom icon (Y/N) ")

    args = "pyinstaller --onefile --windowed"

    if logo.lower() == "y":
        try:
            logo_name = input("Input name of logo (must be .ico) ")
            args += f" --icon={os.getcwd()}{logo_name} trojan.py"
            print(f"Using args: {args}")
            os.system(args)
            cleanup()
        except Exception as e:
            print(e)
            cleanup()
            os.system("pause")

    if logo.lower() == "n":
        try:
            os.system("pyinstaller --onefile --windowed trojan.py")
            print(f"Using args: {args}")
            cleanup()
        except Exception as e:
            print(e)
            cleanup()
            os.system("pause")
complier()