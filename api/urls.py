from django.urls import path

from api.views import CharacterList, CharacterDetail

urlpatterns = [
    path('sheets/', CharacterList.as_view(), name='sheets-list'),
    path('sheets/<int:pk>', CharacterDetail.as_view(), name='sheets-detail')
]
