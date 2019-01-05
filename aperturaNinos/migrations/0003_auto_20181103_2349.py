# Generated by Django 2.0.4 on 2018-11-04 04:49

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('aperturaNinos', '0002_auto_20181103_2337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historianiño',
            name='parto',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('A termino', 'A termino'), ('Prematuro', 'Prematuro'), ('Cesarea', 'Cesarea'), ('Inducido', 'Inducido'), ('Prolongado', 'Prolongado'), ('Sufrimiento fetal', 'sufrimiento fetal'), ('Presentacion podalica', 'presentacion podalica'), ('Se usó forceps', 'se usó forceps'), ('Anoxia', 'Anoxia'), ('Complicaciones', 'Complicaciones'), ('Problemas respiratorios', 'Problemas respiratorios'), ('Cordon umbilical al cuello', 'Cordon umbilical al cuello'), ('Requirio fototerapia', 'Requirio fototerapia'), ('Llanto debil', 'Llanto debil'), ('Requirio transfuciones', 'Requirio transfuciones'), ('Requirio respirador', 'Requirio respirador'), ('Problemas con la alimentacion', 'Problemas con la alimentacion'), ('Bebe activo', 'Bebe activo')], max_length=294),
        ),
    ]