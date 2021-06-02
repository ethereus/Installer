python3 -m eel Installer.py web --onefile --noconsole
rm -rf Installer.spec
rm -rf __pycache__
rm -rf build
cp dist/Installer Installer
rm -rf dist
