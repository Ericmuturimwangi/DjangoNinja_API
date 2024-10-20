from ninja import NinjaAPI
from devices.models import Device, Location
from devices.schemas import DeviceSchema, LocationSchema


app = NinjaAPI()

@app.get("devices/", response=list[DeviceSchema])
def get_devices(request):
    return Device.objects.all()

@app.get("locations/", response=list[DeviceSchema])
def get_locations(request):
    return Location.objects.all()