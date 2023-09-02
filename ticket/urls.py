from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .serializers import TicketViewSet
from .views import(
    ticket_list,
    airplane_list,
    seat_list,
    flight_list,
    delete_flight,
    delete_ticket,
    delete_airplane,
    delete_seat,
    update_ticket,
    update_airplane,
    update_flight,
    update_seat,
    
)


router = DefaultRouter()
router.register('ticket', TicketViewSet, basename='ticket')


urlpatterns = [
    path('', include(router.urls)),
    path('airplane/', airplane_list),
    path('ticket/', ticket_list),
    path('seat/', seat_list),
    path('flight/', flight_list),
    path('del-f/<int:id>/', delete_flight),
    path('del-t/<int:id>/', delete_ticket),
    path('del-a/<int:id>/', delete_airplane),
    path('del-s/<int:id>/', delete_seat),
    path('update-t/<int:id>/', update_ticket),
    path('update-a/<int:id>/', update_airplane),
    path('update-f/<int:id>/', update_flight),
    path('update-s/<int:id>/', update_seat),
    

]