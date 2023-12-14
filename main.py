import subprocess

def main():
    print("\f") 
    print("Python Bildebehandlingsprogram v2023")
    print("\f") 
    print("Gjør et valg:")
    print("a. Instagram-filter")
    print("b. Sort-hvitt")
    print("c. Rotasjon")
    print("d. Resize til 1080px bredde")
    print("e. Utgår")
    print("f. N/A")
    print("g. Legg en hvit ramme rundt bildet")
    print("\f") 
    valg = input("Valg: ")

    # Combine everything into the subprocess.run line
    subprocess.run(["python", f"bildeapplikasjon/oppgave_{valg}.py"])

if __name__ == "__main__":
    main()