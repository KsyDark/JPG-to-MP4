color 2
::Убиваем процесс программы
taskkill /f /im "JPG to MP4.exe"
:: Запускает комплицию проекта с помощью pyinstaller
:: Предварительно установите кодировку - Кирилица OEM 866
pyinstaller --onefile --noconsole --icon=ico.ico "JPG to MP4.py"
:: Запускаем программу после компиляции
cd dist
start "JPG to MP4" "JPG to MP4.exe"