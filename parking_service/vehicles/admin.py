from django.contrib import admin
from vehicles.models import Vehicle, VehicleBrand, VehicleType


@admin.register(VehicleType)
class VehicleTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ['name']
    
    
@admin.register(VehicleBrand)
class VehicleBrandAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ['name']
    
@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ['license_plate', 'model', 'color']
    search_fields = ['license_plate']
    list_filter = ['vehicle_type', 'vehicle_brand']

