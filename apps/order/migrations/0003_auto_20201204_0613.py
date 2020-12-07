# Generated by Django 3.1.3 on 2020-12-04 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_orderitem_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='status',
            field=models.CharField(choices=[('P', 'Placed'), ('S', 'Shipped'), ('D', 'Delivered')], default='P', max_length=1),
        ),
    ]