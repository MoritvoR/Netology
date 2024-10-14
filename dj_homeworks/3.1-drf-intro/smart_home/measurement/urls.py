from django.urls import path
from measurement.views import SensorView, MeasurementCreateView, SensorDetailView

urlpatterns = [
    path('sensors/', SensorView.as_view(), name='sensors'),
    path('measurements/', MeasurementCreateView.as_view(), name='measurements'),
    path('sensors/<int:pk>/', SensorDetailView.as_view(), name='sensordetail'),
]

