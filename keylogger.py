# build_standalone.py
import os
import shutil
import subprocess
import sys
import zipfile
from datetime import datetime

def clean_build():
    """Vyčistí staré build soubory"""
    dirs_to_clean = ['build', 'dist', '__pycache__']
    for dir_name in dirs_to_clean:
        if os.path.exists(dir_name):
            shutil.rmtree(dir_name)
            print(f"✓ Smazáno: {dir_name}")
    
    # Smaž .spec soubory
    for file in os.listdir('.'):
        if file.endswith('.spec'):
            os.remove(file)
            print(f"✓ Smazáno: {file}")

def install_dependencies():
    """Nainstaluje potřebné balíčky"""
    print("\n📦 Instalujem závislosti...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "keyboard", "pyinstaller"])
    print("✓ Závislosti nainstalovány")

def build_exe():
    """Vytvoří standalone .exe"""
    print("\n🔨 Buildím EXE soubor...")
    
    # PyInstaller příkaz s parametry pro standalone
    cmd = [
        'pyinstaller',
        '--onefile',                    # Jeden soubor
        '--noconsole',                  # Bez konzole (můžeš změnit na --console)
        '--name=KeySync',               # Název EXE
        '--icon=NONE',                  # Přidej --icon=icon.ico pokud máš ikonu
        '--clean',                      # Vyčistí cache
        '--add-data=README.md;.',       # Přidá README (volitelné)
        'keylogger.py'
    ]
    
    # Pokud chceš VIDĚT konzoli při spuštění, změň --noconsole na --console
    # cmd[2] = '--console'
    
    subprocess.check_call(cmd)
    print("✓ Build dokončen!")

def organize_output():
    """Uspořádá výstupní soubory"""
    print("\n📁 Organizujem výstup...")
    
    # Vytvoř release složku
    release_dir = "KeySync_Release"
    if os.path.exists(release_dir):
        shutil.rmtree(release_dir)
    os.makedirs(release_dir)
    
    # Zkopíruj EXE
    exe_path = os.path.join('dist', 'KeySync.exe')
    if os.path.exists(exe_path):
        shutil.copy(exe_path, release_dir)
        print(f"✓ EXE zkopírováno do: {release_dir}")
    
    # Vytvoř README pro uživatele
    readme_content = """
=== KeySync - Ethical Keylogger ===

POUŽITÍ:
1. Spusť KeySync.exe
2. Potvrď spuštění napsáním "ano"
3. Stiskni ESC pro ukončení
4. Logy najdeš ve složce "keyloggertest"

UPOZORNĚNÍ:
- Používej POUZE na vlastním PC
- NIKDY bez vědomí ostatních uživatelů
- Pouze pro testovací/vzdělávací účely

POŽADAVKY:
- Windows 7/8/10/11
- Žádné další instalace nejsou potřeba!

Pro podporu nebo issues navštiv GitHub.
"""
    
    with open(os.path.join(release_dir, 'README.txt'), 'w', encoding='utf-8') as f:
        f.write(readme_content)
    
    print(f"✓ README vytvořeno")
    print(f"\n🎉 HOTOVO! Tvůj standalone EXE je v: {release_dir}/")
    print(f"   Velikost: {os.path.getsize(os.path.join(release_dir, 'KeySync.exe')) / 1024 / 1024:.1f} MB")

def create_zip():
    """Vytvoří ZIP pro download"""
    print("\n📦 Vytvářím ZIP soubor pro web...")
    
    release_dir = "KeySync_Release"
    version = datetime.now().strftime('%Y%m%d')
    zip_name = f"KeySync_v{version}.zip"
    
    # Vytvoř ZIP
    with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(release_dir):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, release_dir)
                zipf.write(file_path, arcname)
                print(f"  ✓ Přidáno: {arcname}")
    
    zip_size = os.path.getsize(zip_name) / 1024 / 1024
    print(f"\n✅ ZIP vytvořen: {zip_name}")
    print(f"   Velikost: {zip_size:.2f} MB")
    print(f"\n🌐 Tento soubor nahraj na svůj web!")
    
    return zip_name

def main():
    print("="*60)
    print("  KEYSYNC - Standalone EXE Builder + Web Package")
    print("="*60)
    
    try:
        # 1. Vyčistit staré buildy
        print("\n🧹 Čistím staré buildy...")
        clean_build()
        
        # 2. Nainstalovat dependencies
        install_dependencies()
        
        # 3. Build EXE
        build_exe()
        
        # 4. Uspořádat výstup
        organize_output()
        
        # 5. Vytvoř ZIP pro web
        zip_name = create_zip()
        
        print("\n" + "="*60)
        print("  🎉 HOTOVO!")
        print("="*60)
        print(f"\n📁 Lokální verze: KeySync_Release/")
        print(f"🌐 Web verze: {zip_name}")
        print("\nINSTRUKCE PRO WEB:")
        print(f"1. Nahraj {zip_name} na svůj web")
        print("2. Přidej download link na stránku")
        print("3. Uživatelé stáhnou → rozbalí → spustí KeySync.exe")
        
    except subprocess.CalledProcessError as e:
        print(f"\n❌ Chyba při buildu: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Neočekávaná chyba: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
