Cam-hacker - это python-скрипт, работающий на API сайта insecam.org, который позволяет просматривать камеры.

# Инструкция по установке:
# 1. Установка Python.
    Windows: Установить по ссылке: https://www.python.org/downloads/
    Linux:
        Debian-based: sudo apt install python
        Red Hat-based: sudo dnf install python
        Arch-based: sudo pacman -S python

# 2. Клонирование репозитория:
    Windows: На странице проекта нажмите зелёную кнопку code, и скачайте zip-файл.
    Linux:
        Debian-based: sudo apt install git; git clone https://github.com/arsenykuznetsov005/Cam-hacker.git
        Red Hat-based: sudo dnf install git; git clone https://github.com/arsenykuznetsov005/Cam-hacker.git
        Arch-based: sudo pacman -S git; git clone https://github.com/arsenykuznetsov005/Cam-hacker.git

# 3. Установка зависимостей:
    Windows:
        1. Разархивируйте скачанный zip-архив
        2. Откройте cmd
        3. Передите в директорию проекта, командой: cd путь_проекта
        4. Выполните: pip install -r requirements.txt

    Linux (не зависимо от базы):
        1. Передите в директорию проекта, и откройте его через консоль
        2. Выполните: pip install -r requirements.txt
