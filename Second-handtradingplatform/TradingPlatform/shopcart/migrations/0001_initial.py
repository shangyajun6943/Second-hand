# Generated by Django 2.0.1 on 2018-01-25 03:55

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
        ('showgoods', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Drder_item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('isdelete', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'order_item',
            },
            managers=[
                ('orderitem', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.IntegerField(unique=True)),
                ('order_time', models.DateTimeField()),
                ('delivery_time', models.DateTimeField()),
                ('shopping_state', models.IntegerField()),
                ('isdelete', models.IntegerField(default=0)),
                ('shopid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.Shop_user')),
                ('userid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.User')),
            ],
            options={
                'db_table': 'order',
            },
            managers=[
                ('orders', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name='drder_item',
            name='order_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shopcart.Order'),
        ),
        migrations.AddField(
            model_name='drder_item',
            name='pro_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='showgoods.Product'),
        ),
    ]