if __name__ == '__main__':
    print('=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n')

    try:
        with open('lost_archive.txt', 'r') as f:
            print(f.read())
    except FileNotFoundError:
        print(
            "CRISIS ALERT: Attempting access to 'lost_archive.txt'...\n"
            "RESPONSE: Archive not found in storage matrix\n"
            "STATUS: Crisis handled, system stable\n"
        )

    try:
        with open('classified_vault.txt', 'r') as f:
            print(f.read())
    except PermissionError:
        print(
            "CRISIS ALERT: Attempting access to 'classified_vault.txt'...\n"
            "RESPONSE: Security protocols deny access\n"
            "STATUS: Crisis handled, security maintained\n"
        )

    try:
        with open('standard_archive.txt', 'r') as f:
            print(
                "ROUTINE ACCESS: Attempting access to "
                "'standard_archive.txt'...\n"
                f"SUCCESS: Archive recovered - ``{f.read()}''\n"
                "STATUS: Normal operations resumed\n"
            )
    except Exception as err:
        print(f"Unexpected error occurred: {err}")

    print('All crisis scenarios handled successfully. Archives secure.')
