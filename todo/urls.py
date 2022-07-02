from rest_framework import routers
from .views import TodoApp

router = routers.DefaultRouter()
router.register("todo", TodoApp)