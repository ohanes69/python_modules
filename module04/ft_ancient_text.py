if __name__ == '__main__':
    print('=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n')
    try:
        with open('ancient_fragment.txt') as f:
            print('Accessing Storage Vault: ancient_fragment.txt')
            print('Connection established...\n')
            print('RECOVERED DATA:')
            print(f.read())
            print('\nData recovery complete. Storage unit disconnected.')
    except FileNotFoundError:
        print('ERROR: Storage vault not found. Run data generator first.')
