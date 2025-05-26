import subprocess
import sys

def test_example_feature():
    print("\nRunning test_example_feature...")
    print("Expected output: 'Example feature'")
    
    result = subprocess.run([sys.executable, 
                             'example_feature.py'], 
                            stdout=subprocess.PIPE, 
                            stderr=subprocess.PIPE,
                            universal_newlines=True)
    
    print("\nTest Output:")
    print("Return code:", result.returncode)
    print("Stdout:", result.stdout.strip())
    print("Stderr:", result.stderr.strip())
    
    if result.returncode == 0 and result.stdout.strip() == 'Example feature':
        print("\nTest passed")
    else:
        print("\nTest failed")
        print("Expected: 'Example feature'")
        print("Got: '", result.stdout.strip(), "'")

if __name__ == '__main__':
    test_example_feature()
