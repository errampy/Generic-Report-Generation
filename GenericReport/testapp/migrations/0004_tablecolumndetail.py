# Generated by Django 4.1.5 on 2023-01-03 08:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0003_agent_reportmaster'),
    ]

    operations = [
        migrations.CreateModel(
            name='TableColumnDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('table_column_name', models.CharField(max_length=50)),
                ('table_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='table_n', to='testapp.tablemaster')),
            ],
        ),
    ]