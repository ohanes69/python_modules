import sys

if __name__ == '__main__':
    print('=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n')
    id: str = input('Input Stream active. Enter archivist ID: ')
    status: str = input('Input Stream active. Enter status report: ')

    sys.stdout.write(f'\n[STANDARD] Archive status from {id}: {status}\n')
    sys.stderr.write(
        '[ALERT] System diagnostic: Communication channels verified\n'
    )
    sys.stdout.write('[STANDARD] Data transmission complete\n\n')

    print('Three-channel communication test successful.')
