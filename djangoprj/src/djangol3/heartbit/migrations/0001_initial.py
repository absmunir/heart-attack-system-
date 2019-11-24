# Generated by Django 2.2.1 on 2019-05-23 14:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Medecin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_medecin', models.CharField(max_length=30)),
                ('prenom_medecin', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=30)),
                ('adresse_cabinet', models.CharField(max_length=100)),
                ('telephone', models.CharField(default='', max_length=100)),
                ('password', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_patient', models.CharField(max_length=30)),
                ('prenom_patient', models.CharField(max_length=30)),
                ('age', models.IntegerField(default=0)),
                ('email', models.EmailField(max_length=30)),
                ('adresse', models.CharField(max_length=100)),
                ('telephone', models.CharField(default='', max_length=100)),
                ('sexe', models.CharField(choices=[('F', 'Female'), ('M', 'Male')], max_length=1)),
                ('password', models.CharField(default='', max_length=100)),
                ('medecin', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='heartbit.Medecin')),
            ],
        ),
        migrations.CreateModel(
            name='Analyses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cp', models.IntegerField(default=0)),
                ('trestbps', models.IntegerField(default=0)),
                ('fbs', models.IntegerField(default=0)),
                ('restecg', models.IntegerField(default=0)),
                ('chol', models.IntegerField(default=0)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='heartbit.Patient')),
            ],
        ),
    ]
