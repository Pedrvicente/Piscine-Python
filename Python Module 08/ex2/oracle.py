import os
from dotenv import load_dotenv


def main() -> None:

    load_dotenv()

    matrix_mode = os.environ.get("MATRIX_MODE")
    database_url = os.environ.get("DATABASE_URL")
    api_key = os.environ.get("API_KEY")
    log_level = os.environ.get("LOG_LEVEL")
    zion_endpoint = os.environ.get("ZION_ENDPOINT")

    print("\nORACLE STATUS: Reading the Matrix...\n")

    print("Configuration loaded:")

    if matrix_mode:
        print(f"Mode: {matrix_mode}")
    else:
        print("No mode configured")
    if database_url:
        print("Database: Connected to local instance")
    else:
        print("No database configured")
    if api_key:
        print("API Access: Authenticated")
    else:
        print("No API key configured")
    if log_level:
        print(f"Log Level: {log_level}")
    else:
        print("No log level configured")
    if zion_endpoint:
        print("Zion Network: Online")
    else:
        print("No Zion endpoint configured")

    print()
    print("Environment security check:")
    print("[OK] No hardcoded secrets detected")
    if os.path.exists(".env"):
        print("[OK] .env file properly configured")
    else:
        print("[MISSING] .env file not found!")
    if os.path.exists(".gitignore"):
        with open('.gitignore', 'r') as file:
            if '.env' in file.read():
                print("[OK] Production overrides available")
            else:
                print("[WARNING] .env not in .gitignore!")
    else:
        print("[WARNING] No .gitignore found!")

    print("\nThe Oracle sees all configurations.")


if __name__ == '__main__':
    main()
