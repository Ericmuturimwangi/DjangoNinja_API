from ninja import ModelSchema, Schema
from devices.models import Device, Location
from pydantic import BaseModel


class LocationSchema(ModelSchema):
    class Meta:
        model = Location
        fields = ('id', 'name')

class DeviceSchema(ModelSchema):
    location: LocationSchema | None = None

    class Meta:
        model = Device
        fields = ('id', 'name', 'slug', 'location')

class DeviceCreateSchema(Schema):
    name: str
    location_id : int | None = None


class Error(BaseModel):
    message: str = "An error occurred"


class DeviceLocationPatch(Schema):
    location_id : int | None = None