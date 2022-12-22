# Generated by Django 4.1.4 on 2022-12-22 16:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("noteapp", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="note",
            name="user",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="tag",
            name="user",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="tag",
            name="name",
            field=models.CharField(max_length=25),
        ),
        migrations.AddConstraint(
            model_name="tag",
            constraint=models.UniqueConstraint(
                fields=("user", "name"), name="tag of username"
            ),
        ),
    ]
