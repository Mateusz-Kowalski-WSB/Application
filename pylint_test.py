import os
import subprocess

def test_pylint():
    app_name = "myproject"
    os.chdir(f"./{app_name}")
    result = subprocess.run(['pylint', '-E', '.'], capture_output=True, text=True)
    assert result.returncode == 0, result.stdout
