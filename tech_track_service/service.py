from email import header
import os
import time
import json
import socket
from urllib import response
from venv import create
import psutil
import platform
import requests
from django.core.management import execute_from_command_line
from django.utils.timezone import now
from tech_track_service import equipment
from tech_track_service.equipment.models import Equipment

#Configuracion de la API destino
API_URL = 'http://127.0.0.1:8000/api/equipment/'

def get_system_info():
     """
     Obtiene el nombre del equipo, IP y estado (activo/inactivo)
     """

     # Obtener el nombre del equipo
     name = platform.node()

     # Obtener la dirección IP local
     ip_address = socket.gethostbyname(socket.gethostname())


     #verifica si el equipo esta activo (no suspendido)
     is_active = not psutil.sensors_battery().power_plugged

     status = 'Active' if is_active else 'Inactive'

     return {
         'name': name,
         'ip_address': ip_address,
         'status': status
    }

def save_equipment(data):
     """
     Guarda o actualiza el equipo en la base de datos.
     """
     # Guarda la informacion del equipo en la base de datos
     equipment, created = Equipment.objects.update_or_create(
          name=data['name'],
          defaults={
               'ip_address': data['ip_address'],
               'status': data['status'],
               'updated_at': now()
          }
     )
     return equipment 

def post_to_api(data):
     """
     Envia la informacion del equipo a la API
     """
     headers = {'Content-Type': 'application/json'}
     response = requests.post(API_URL, json=data, headers=headers)
     return response

def run_service():
     """
     Ejecuta el servicio cada 15 minutos.
     """
     while True:
          print("Consultando y guardando informacion del equipo...")

          #Obtener informacion del sistam
          data = get_system_info()

          equipment = save_equipment(data)

          response = post_to_api(data)

          if response.status_code == 201:
               print("Informacion enviada a la API.")
          else:
               print(f"Error al enviar la informacion: {response.status_code} - {response.text}")

          time.sleep(15 * 60)

if __name__ == '__main__':
     os.environ.setdefault('DJANGO_SETTINGS', 'tech_track_service.settings.py')
     execute_from_command_line(['manage.py','migrate'])

     run_service()