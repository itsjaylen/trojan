@echo off
echo Installing packages from requirements.txt...
pip install -r requirements.txt

pyarmor pack --clean -e "--onefile --windowed" trojan.py

RD build /Q /S

echo Done
pause
