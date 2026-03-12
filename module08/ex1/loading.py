if __name__ == '__main__':

    print('\nLOADING STATUS: Loading programs...\n')
    print('Checking dependencies:')
    try:
        import pandas
        print(f"[OK] pandas ({pandas.__version__}) - Data manipulation ready")
    except ImportError:
        print("[KO] pandas is missing!")
    try:
        import requests
        print(f"[OK] requests ({requests.__version__}) - Network access ready")
    except ImportError:
        print("[KO] requests is missing!")
    try:
        import matplotlib
        print(
            f"[OK] matplotlib ({matplotlib.__version__}) - Visualization ready"
        )
    except ImportError:
        print(
            "[KO] matplotlib is missing!"
        )
