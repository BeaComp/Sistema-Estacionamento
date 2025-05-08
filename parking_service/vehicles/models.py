from customer.models import Customer
from django.db import models


class VehicleType(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True, 
        verbose_name='Nome'
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name='Descrição'
    )
    created_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Criado em'
    )
    update_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Atualizado em'
    )
    
    class Meta:
        verbose_name = 'Tipo de Veículo'
        verbose_name_plural = 'Tipos de Veículos'
    
    def __str__(self):
        return self.name
    
class VehicleBrand(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True, 
        verbose_name='Nome'
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name='Descrição'
    )
    created_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Criado em'
    )
    update_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Atualizado em'
    )
    
    class Meta:
        verbose_name = 'Marca de Veículo'
        verbose_name_plural = 'Marcas de Veículos'
    
    def __str__(self):
        return self.name
    
class Vehicle(models.Model):
    vehicle_type = models.ForeignKey(
        VehicleType,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        related_name='vehicles',
        verbose_name='Tipo de Veículo',
    )
    license_plate = models.CharField(
        max_length=10,
        unique=True,
        verbose_name='Placa'
    )
    vehicle_brand = models.ForeignKey(
        VehicleBrand,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        related_name='vehicles',
        verbose_name='Marca',
    )
    model = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name='Modelo'
    )
    color = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name='Cor'
    )
    owner = models.ForeignKey(
        Customer,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        related_name='vehicles',
        verbose_name='Proprietário'
    )
    created_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Criado em'
    )
    update_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Atualizado em'
    )
    
    class Meta:
        verbose_name = 'Veículo'
        verbose_name_plural = 'Veículos'
        
    def __str__(self):
        return self.license_plate