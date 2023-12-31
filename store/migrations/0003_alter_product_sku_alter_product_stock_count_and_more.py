# Generated by Django 4.2.7 on 2023-11-14 07:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_product_sku_alter_product_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='sku',
            field=models.CharField(default='', max_length=20, unique=True, verbose_name='Stock Keeping Unit'),
        ),
        migrations.AlterField(
            model_name='product',
            name='stock_count',
            field=models.IntegerField(help_text='Number of items in stock'),
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.product')),
            ],
        ),
    ]
