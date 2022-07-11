from django.contrib import admin

from Rh.models import Funcionario
from Rh.models import Departamento

# Register your models here.
admin.site.register(Funcionario)

admin.site.register(Departamento)
