if __name__ == '__main__':
    print('=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n')

    with open('classified_data.txt', 'r') as f:
        print('Initiating secure vault access...')
        print('Vault connection established with failsafe protocols\n')
        print('SECURE EXTRACTION:')
        print(f.read())

    with open('security_protocols.txt', 'w') as f:
        f.write(
            '[CLASSIFIED] New security protocols archived'
        )
    with open('security_protocols.txt', 'r') as f:
        print('\nSECURE PRESERVATION:')
        print(f.read())

    print('Vault automatically sealed upon completion\n')
    print('All vault operations completed with maximum security.')
