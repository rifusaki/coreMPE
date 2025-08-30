import os
import sys

PACKAGE_ROOT = os.path.dirname(os.path.dirname(__file__))

build_paths = dict([(os.path.normpath(x[0]), os.path.normpath(x[1])) for x in [
    ("icon.ico", "icon.ico"),
    ("adenzu_panel/ai-models/2024-11-00/best.pt", "models/best.pt"),
]])

# Function to get the correct path to bundled resources
def resource_path(relative_path: str) -> str:
    if hasattr(sys, '_MEIPASS'):
        # Running in a PyInstaller bundle
        return os.path.join(sys._MEIPASS, os.path.basename(relative_path))

    return os.path.join(PACKAGE_ROOT, relative_path)
