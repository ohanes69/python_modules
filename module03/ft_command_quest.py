import sys

if __name__ == '__main__':
    print('=== Command Quest ===')
    if len(sys.argv) == 1:
        sys.stdout.write('No arguments provided!\n')
        sys.stdout.write(f'Program name: {sys.argv[0]}\n')
        sys.stdout.write(f'Total arguments: {len(sys.argv)}\n')

    elif len(sys.argv) > 1:
        sys.stdout.write(f'Program name: {sys.argv[0]}\n')
        sys.stdout.write(f'Arguments received: {len(sys.argv) - 1}\n')
        for i in range(1, len(sys.argv)):
            sys.stdout.write(f'Argument {i}: {sys.argv[i]}\n')
        sys.stdout.write(f'Total arguments: {len(sys.argv)}\n')
