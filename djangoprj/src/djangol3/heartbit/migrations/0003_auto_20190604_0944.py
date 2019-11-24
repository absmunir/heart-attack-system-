# Generated by Django 2.2.1 on 2019-06-04 08:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('heartbit', '0002_auto_20190524_1408'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='analyses',
            name='patient',
        ),
        migrations.CreateModel(
            name='RendezVous',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(max_length=8)),
                ('medecin_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='heartbit.Medecin')),
                ('patient_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='heartbit.Patient')),
            ],
        ),
        migrations.CreateModel(
            name='Diagnostic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diag_result', models.IntegerField(default=0)),
                ('analyse_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='heartbit.Analyses')),
                ('patient_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='heartbit.Patient')),
            ],
        ),
    ]
