# Generated by Django 3.1.3 on 2020-12-04 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='status',
            field=models.CharField(choices=[('P', 'placed'), ('S', 'best seller'), ('D', 'delivered')], default='P', max_length=1),
        ),
    ]
