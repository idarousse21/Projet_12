# Generated by Django 4.1.7 on 2023-03-07 00:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("project", "0002_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="event",
            name="client",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="project.client",
            ),
            preserve_default=False,
        ),
    ]