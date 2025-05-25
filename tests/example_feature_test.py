import subprocess
import sys

def test_example_feature():
    result = subprocess.run([sys.executable, 
                             'example_feature.py'], 
                            stdout=subprocess.PIPE, 
                            stderr=subprocess.PIPE,
                            universal_newlines=True)
    if result.returncode == 0 and result.stdout.strip() == 'Example feature':
        print('Test passed')
    else:
        print('There was an error')
        print('returncode:', result.returncode)
        print('stdout:', result.stdout)
        print('stderr:', result.stderr)

if __name__ == '__main__':
    test_example_feature()
