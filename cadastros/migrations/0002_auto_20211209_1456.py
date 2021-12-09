# Generated by Django 3.2.9 on 2021-12-09 17:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Usuario',
        ),
        migrations.AddField(
            model_name='multa',
            name='data_limite',
            field=models.DateField(default=18.712962962962962, verbose_name='Data da Multa'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='categoria',
            name='nome',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='emprestimo',
            name='objeto_emprestado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastros.objeto', verbose_name='Objeto Emprestado'),
        ),
        migrations.AlterField(
            model_name='multa',
            name='data_multa',
            field=models.DateField(auto_now_add=True, verbose_name='Data da Multa'),
        ),
        migrations.AlterField(
            model_name='multa',
            name='valor',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
        migrations.AlterField(
            model_name='objeto',
            name='categoria',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='objeto',
            name='emprestado',
            field=models.BooleanField(default=False),
        ),
    ]