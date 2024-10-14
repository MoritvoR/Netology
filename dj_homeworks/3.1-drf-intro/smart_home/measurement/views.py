from django.core.exceptions import ObjectDoesNotExist
from rest_framework.generics import ListAPIView, ListCreateAPIView, \
    CreateAPIView, RetrieveUpdateAPIView
from rest_framework.response import Response

from measurement.models import Sensor, Measurement
from measurement.serializers import SensorSerializer, MeasurementSerializer, SensorDetailSerializer


class SensorView(ListCreateAPIView):
    """Список датчиков / Добавить датчик"""
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class SensorDetailView(RetrieveUpdateAPIView):
    """Получить данные по датчику / Изменить данные по датчику"""
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


class MeasurementCreateView(CreateAPIView):
    """Добавить температуру"""
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

    def post(self, request, *args, **kwargs):

        try:
            sen = Sensor.objects.get(id=request.data.get('sensor'))

            match request.data:
                case {**kwargs} if len(kwargs) != 2 or 'temperature' not in kwargs:
                    return Response({'Ошибка запроса': 'Необходимо передать '
                                                       'строго 2 ключа (sensor'
                                                       ' и temperature)'})
                case {'sensor': int(sen.id), 'temperature': int() | float() as tem}:
                    Measurement.objects.create(sensor_id=sen.id, temperature=tem)
                    return Response({'sensor': sen.id, 'temperature': tem})

        except ObjectDoesNotExist:
            return Response({'Ошибка запроса': 'Датчик не указан или '
                                               'отсутствует в БД'})
