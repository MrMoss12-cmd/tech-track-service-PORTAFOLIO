from html import parser
import os
from string import Template
import sys
import argparse
import subprocess
import win32serviceutil

SERVICE_NAME = "TechTrackService"
DISPLAY_NAME = "Tech Track Service"
DESCRIPTION = "Servicio para gestionar Tech Track como un servicio de windows."

#la ruta del script del servicio
SERVICE_SCRIPT = os.path.join(os.path.dirname(__file__), "service.py")

def install_service():
    """Instalar el servicio en windows."""
    print("Instalando Servicio...")
    subprocess.run([sys.executable, SERVICE_SCRIPT, "install"], check=True)
    subprocess.run([sys.executable, SERVICE_SCRIPT, "start"], check=True)
    print(f"Servicio '{SERVICE_NAME}' instalado y en ejecucion.")

def uninstall_service():
    """Desintalar el servicio en windows"""
    print("Desintalando el servicio...")
    try:
        subprocess.run([sys.executable, SERVICE_SCRIPT, "stop"], check=True)
    except Exception:
        print(f"El servicio '{SERVICE_NAME}' '{Exception}' no estaba en ejecucion.")
    subprocess.run([sys.executable, SERVICE_SCRIPT, "remove"], check=True)
    print(f"Servicio '{SERVICE_NAME}'desinstalado.")

def repair_service():
    """Reparar el servicio en windows"""
    print("Reparado el servicio...")
    uninstall_service()
    install_service()
    print("Servicio reparado.")

def status_service():
    """Mostrar el estado del servicio"""
    try:
        win32serviceutil.QueryServiceStatus(SERVICE_NAME)
        print(f"El servicio '{SERVICE_NAME}' esta instalado y activo.")
    except Exception as e:
        print(f"Error al consultar el estado del servicio: {e}")

def main():
    parser = argparse.ArgumentParser(description="Gestor del servicio Tech Track.")
    parser.add_argument("action", choices=["install", "uninstall", "repair","status"],
                        help="Accion a realizar(install, uninstall, repair, status).")
    args = parser.parse_args()

    if args.action == "install":
        install_service()
    elif args.action == "uninstall":
        uninstall_service()
    elif args.action == "repair":
        repair_service()
    elif args.action == "status":
        status_service()
    else:
        print("Accion no valida. Usa --help para mas informacion.")

if __name__ == "__main__":
    main()

