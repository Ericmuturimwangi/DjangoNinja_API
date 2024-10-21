from ninja import NinjaAPI
from django.shortcuts import get_object_or_404
from devices.models import Device, Location
from devices.schemas import DeviceSchema, LocationSchema, DeviceCreateSchema, Error


app = NinjaAPI()

@app.get("devices/", response=list[DeviceSchema])
def get_devices(request):
    return Device.objects.all()

@app.get('devices/{slug}/', response=DeviceSchema)
def get_devices(request, slug:str):
    device = get_object_or_404(Device, slug=slug)
    return device

@app.get("locations/", response=list[LocationSchema])
def get_locations(request):
    return Location.objects.all()


@app.post("devices/", response={200: DeviceSchema, 404:Error})
def create_device(request, device: DeviceCreateSchema):
    if device.location_id:
        location_exists = Location.objects.filter(id=device.location_id).exists()
        if not location_exists:
            return 404, {'message': 'Location not found'}

    device_data = device.model_dump()
    device_model = Device.objects.create(**device_data)
    return device_model