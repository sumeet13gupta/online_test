# Generated by Django 3.0.7 on 2020-09-09 02:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('yaksh', '0022_release_0_22_1'),
    ]

    operations = [
        migrations.AddField(
            model_name='answerpaper',
            name='extra_time',
            field=models.FloatField(default=0.0, verbose_name='Additional time in mins'),
        ),
        migrations.AddField(
            model_name='answerpaper',
            name='is_special',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='MicroManager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('special_attempt', models.BooleanField(default=False)),
                ('attempts_permitted', models.IntegerField(default=0)),
                ('permitted_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('attempts_utilised', models.IntegerField(default=0)),
                ('wait_time', models.IntegerField(default=0, verbose_name='Days to wait before special attempt')),
                ('attempt_valid_for', models.IntegerField(default=90, verbose_name='Validity days')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yaksh.Course')),
                ('manager', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='micromanaging', to=settings.AUTH_USER_MODEL)),
                ('quiz', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='yaksh.Quiz')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='micromanaged', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('student', 'course', 'quiz')},
            },
        ),
    ]