# Generated by Django 4.2 on 2023-04-16 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_remove_user_projects'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='descricao',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='project',
            name='setor',
            field=models.CharField(choices=[('Recursos Humanos', 'Recursos Humanos'), ('Desenvolvimento', 'Desenvolvimento'), ('Produção', 'Produção'), ('Marketing', 'Marketing')], default='Desenvolvimento', max_length=20),
        ),
        migrations.AddField(
            model_name='project',
            name='status',
            field=models.CharField(choices=[('Sob Controle', 'Sob Controle'), ('Atrasado', 'Atrasado'), ('Finalizado', 'Finalizado')], default='Sob Controle', max_length=20),
        ),
    ]
