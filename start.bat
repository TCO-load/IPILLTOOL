@echo off
setlocal enabledelayedexpansion

:: Vérifier si Python est installé
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python n'est pas installe sur votre systeme.
    echo Veuillez installer Python depuis https://www.python.org/downloads/
    pause
    exit /b 1
)

:: Vérifier et installer les bibliothèques nécessaires
echo Verification et installation des bibliotheques necessaires...

:: Liste des bibliothèques requises
set "libraries=colorama psutil netifaces"

for %%i in (%libraries%) do (
    python -c "import %%i" >nul 2>&1
    if !errorlevel! neq 0 (
        echo Installation de %%i...
        pip install %%i
        if !errorlevel! neq 0 (
            echo Erreur lors de l'installation de %%i.
            pause
            exit /b 1
        )
    ) else (
        echo %%i est deja installe.
    )
)

:: Vérifier si IPILLTOOL.py existe
if not exist IPILLTOOL.py (
    echo Le fichier IPILLTOOL.py n'existe pas dans le repertoire courant.
    pause
    exit /b 1
)

:: Exécuter le programme avec des privilèges administrateur
echo.
echo Lancement de IPILLTOOL.py avec des privileges administrateur...
python IPILLTOOL.py
