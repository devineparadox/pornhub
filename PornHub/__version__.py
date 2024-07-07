import subprocess
from subprocess import run

result = subprocess.run(["git", "rev-list", "--count", "HEAD"], capture_output=True, text=True)
__version__ = result.stdout.strip()
__version__ = "2.0.1b4"
__version_code__ = (
    run(["git", "rev-list", "--count", "HEAD"], capture_output=True)
    .stdout.decode()
    .strip()
    or "0"
)
