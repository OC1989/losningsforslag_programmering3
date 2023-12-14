import subprocess

def main():
    print("Choose a script to run:")
    print("1. script1.py")
    print("2. script2.py")
    print("3. script3.py")
    print("4. script4.py")
    print("5. script5.py")
    print("6. script6.py")

    choice = input("Enter the number of the script you want to run: ")

    # Run the selected script using subprocess
    script_name = f"script{choice}.py"
    subprocess.run(["python", script_name])

    # Fortelle Python at dette er hovedskriptet vårt, at det er her vi starter.
if __name__ == "__main__":
    main()