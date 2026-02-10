if __name__ == '__main__':
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")
    print("Initiating secure vault access...")
    print("Vault connection established with failsafe protocols")
    print("SECURE EXTRACTION:")
    with open('classified_data.txt', 'r') as f:
        content = f.read()
        print(content)
    print()
    print("SECURE PRESERVATION:")
    with open('classified_data.txt', 'w') as f:
        f.write("[CLASSIFIED] New security protocols archived")
    print("[CLASSIFIED] New security protocols archived")
    print("Vault automatically sealed upon completion\n")
    print("All vault operations completed with maximum security.")
