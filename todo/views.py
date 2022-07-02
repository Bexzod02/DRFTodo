from django.db.models import Q

from .serializer import Todoserializer
from .models import Todo
from rest_framework import viewsets


class TodoApp(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = Todoserializer

    def get_queryset(self):
        qs = super().get_queryset()
        # q = self.request.GET.get('q')
        q = self.request.query_params.get('q')
        c = self.request.query_params.get('c')
        q_condition = Q()
        if q:
            q_condition = Q(title__icontains=q)
        c_condition = Q()
        if c:
            c_condition = Q(description__icontains=c)
        return qs.filter(q_condition, c_condition)