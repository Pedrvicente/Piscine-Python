if __name__ == '__main__':
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
    print()
    print("Accessing Storage Vault: ancient_fragment.txt")
    try:
        file = open("ancient_fragment.txt", 'r')

        content = file.read()

        file.close

        print("Connection established...")
        print()
        print("RECOVERED DATA:")
        print(content)
        print()
        print("Data recovery complete. Storage unit disconnected.")
    except FileNotFoundError:
        print("ERROR: Storage vault not found. Run data generator first.")
