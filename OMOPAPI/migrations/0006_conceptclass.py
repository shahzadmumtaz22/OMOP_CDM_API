# Generated by Django 3.2 on 2021-04-27 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OMOPAPI', '0005_conceptancestor'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConceptClass',
            fields=[
                ('concept_class_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('concept_class_name', models.CharField(max_length=255)),
                ('concept_class_concept_id', models.IntegerField()),
            ],
            options={
                'db_table': 'concept_class',
                'managed': False,
            },
        ),
    ]