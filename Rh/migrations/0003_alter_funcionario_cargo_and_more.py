# Generated by Django 4.0.5 on 2022-06-30 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Rh', '0002_alter_funcionario_data_nascimento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionario',
            name='cargo',
            field=models.CharField(choices=[('ES', 'Estagiário'), ('AS', 'Assitente'), ('JR', 'Júnior'), ('PL', 'Pleno'), ('SR', 'Senior'), ('GR', 'Gerente')], max_length=2),
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='data_nascimento',
            field=models.DateField(null=True),
        ),
    ]
