# Generated by Django 5.1.2 on 2024-12-02 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_alter_receta_imagen_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='compra',
            name='estado',
        ),
        migrations.AddField(
            model_name='compra',
            name='metodo_pago',
            field=models.CharField(choices=[('Paypal', 'Paypal'), ('Visa', 'Visa'), ('Mastercard', 'Mastercard'), ('American express', 'American Express')], default='Visa', max_length=20),
        ),
        migrations.DeleteModel(
            name='Pago',
        ),
    ]
