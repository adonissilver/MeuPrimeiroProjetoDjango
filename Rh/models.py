from mailbox import NotEmptyError
from random import choice
from django.db import models

# Create your models here.


#class Departamento(Herança)
class Departamento(models.Model):
    nome=models.CharField(max_length=20)

    #quando eu chamar essa classe , ele vai retornar o nome da classe
    def __str__(self):
        return self.nome
    



class Funcionario(models.Model):
    CARGOS=[
        ('ES','Estagiário'),
        ('AS','Assitente'),
        ('JR','Júnior'),
        ('PL','Pleno'),
        ('SR','Senior'),
        ('GR','Gerente'),

    ]

    SEXO=[
        ('M','Maculino'),
        ('F','Feminino'),
        
    ]


    matricula=models.IntegerField()
    nome=models.CharField(max_length=50) 
    cargo=models.CharField(max_length=2,choices=CARGOS)
    sexo=models.CharField(max_length=1,choices=SEXO,null=True)
    departamento=models.ForeignKey(Departamento,on_delete=models.CASCADE)
    salario=models.DecimalField(max_digits=10,decimal_places=2)
    data_nascimento=models.DateField(null=True)

    #Para ordenarmos os nomes dos funcionarios por ordem de inserçao,atualmente está aparecendo o ultimo inserido como o primeiro da lista
    class Meta():
        ordering=['nome']


