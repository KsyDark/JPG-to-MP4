color 2
::������� ����� �ணࠬ��
taskkill /f /im "JPG to MP4.exe"
:: ����᪠�� �������� �஥�� � ������� pyinstaller
:: �।���⥫쭮 ��⠭���� ����஢�� - ��ਫ�� OEM 866
pyinstaller --onefile --noconsole --icon=ico.ico "JPG to MP4.py"
:: ����᪠�� �ணࠬ�� ��᫥ �������樨
cd dist
start "JPG to MP4" "JPG to MP4.exe"