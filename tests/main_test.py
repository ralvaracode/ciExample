import subprocess
import sys

def test_main():
    print("\nRunning test_main...")
    print("Expected output: 'Hello World'")
    
    result = subprocess.run([sys.executable, 'main.py'], 
                            stdout=subprocess.PIPE, 
                            stderr=subprocess.PIPE,
                            universal_newlines=True)
    
    print("\nTest Output:")
    print("Return code:", result.returncode)
    print("Stdout:", result.stdout.strip())
    print("Stderr:", result.stderr.strip())
    
    if result.returncode == 0:
        print("\nTest passed")
    else:
        print("\nTest failed")
        print("Expected: 'Hello World'")
        print("Got: '", result.stdout.strip(), "'")

if __name__ == '__main__':
    test_main()
