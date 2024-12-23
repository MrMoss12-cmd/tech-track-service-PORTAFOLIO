from django.db import models

class Equipment(models.Model):
    name = models.CharField(max_length=255, verbose_name="Nombre del Equipo")
    ip_address = models.GenericIPAddressField(verbose_name="Direccion IP")
    status = models.CharField(
        max_length=50, 
        choices=[('Active','Active'),('Inactive','Inactive')],
        default='Inactive',
        verbose_name="Estado"
        )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Ultima actualizacion")

    class Meta:
        db_table = 'payload'
        verbose_name = "Equipo"
        verbose_name_plural = "Equipos"
        ordering = ['-created_at']


    def __str__(self):
        return f"{self.name} ({self.ip_address}) "
    
    #Metodos personalizados
    def is_active(self):
        """Verifica si el equipo esta activo."""
        return self.status == "Active"
    
    def active(self):
        """Cambia el estado del equipo a activo"""
        if not self.is_active():
            self.status = 'Active'
            self.save()
        return self
    
    def desactive(self):
        """Cambia el estado del equipo a Inactivo"""
        if self.is_active():
            self.status = 'Inactive'
            self.save()
        return self
    
    def update_ip(self, new_ip):
        """Actualiza la direccion IP del equipo"""
        self.ip_address = new_ip
        self.save()
        return self.ip_address
    
    def summary(self):
        """Devuelve un resumen del equipo"""
        return {
            'name': self.name,
            'ip_address': self.ip_address,
            'status': self.status,
            'created_at': self.created_at,
            'updated_at': self.updated_at,                         
        }