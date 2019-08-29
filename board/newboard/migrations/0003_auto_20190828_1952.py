# Generated by Django 2.2.4 on 2019-08-28 19:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('newboard', '0002_auto_20190828_1740'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rubric',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=20, verbose_name='title')),
            ],
            options={
                'verbose_name': 'Heading',
                'verbose_name_plural': 'Headings',
                'ordering': ['name'],
            },
        ),
        migrations.AlterModelOptions(
            name='bb',
            options={'ordering': ['-published'], 'verbose_name': 'Board', 'verbose_name_plural': 'Boards'},
        ),
        migrations.AlterField(
            model_name='bb',
            name='content',
            field=models.TextField(blank=True, null=True, verbose_name='about'),
        ),
        migrations.AlterField(
            model_name='bb',
            name='price',
            field=models.FloatField(blank=True, null=True, verbose_name='cost'),
        ),
        migrations.AlterField(
            model_name='bb',
            name='published',
            field=models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='bb',
            name='title',
            field=models.CharField(max_length=50, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='bb',
            name='rubric',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='newboard.Rubric', verbose_name='Heading'),
        ),
    ]
