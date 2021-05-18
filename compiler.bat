echo Installing packages from requirements.txt...
pip install -r requirements.txt

pyinstaller --onefile --windowed trojan.py

RD __pycache__ /Q /S
RD build /Q /S
DEL trojan.spec /Q

echo Done
pause