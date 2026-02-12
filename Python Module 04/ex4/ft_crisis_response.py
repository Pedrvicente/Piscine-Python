def crisis() -> None:
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")

    print("CRISIS ALERT: Attempting access to 'lost_archive.txt'...")
    try:
        with open('lost_archive.txt', 'r') as f:
            content = f.read()
            print(content)
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")
    print()
    print("CRISIS ALERT: Attempting access to 'classified_vault.txt'...")
    try:
        with open('classified_vault.txt', 'r') as f:
            raise PermissionError
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained")
    print()
    print("ROUTINE ACCESS: Attempting access to 'standard_archive.txt'...")
    try:
        with open('standard_archive.txt', 'r') as f:
            print("SUCCESS: Archive recovered "
                  "-``Knowledge preserved for humanity''")
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")
    finally:
        print("STATUS: Normal operations resumed")
    print()
    print("All crisis scenarios handled successfully. Archives secure.")


if __name__ == '__main__':
    crisis()
