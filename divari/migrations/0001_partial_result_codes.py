# Generated by Django 2.2.12 on 2020-07-01 15:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('results', '0006_partial_result_codes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Competition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Date')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='divari_competition', to='results.Organization')),
            ],
            options={
                'verbose_name': 'Competition',
                'verbose_name_plural': 'Competitions',
            },
        ),
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='Season name')),
                ('date_start', models.DateField(verbose_name='Start date')),
                ('date_end', models.DateField(verbose_name='End date')),
                ('result_count', models.SmallIntegerField(verbose_name='Number of included results')),
                ('start_level_recurve', models.SmallIntegerField(verbose_name='Recurve start level')),
                ('start_level_compound', models.SmallIntegerField(verbose_name='Compound start level')),
                ('start_level_barebow', models.SmallIntegerField(verbose_name='Barebow start level')),
            ],
            options={
                'verbose_name': 'Season',
                'verbose_name_plural': 'Seasons',
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bow_type', models.CharField(choices=[('recurve', 'Recurve'), ('compound', 'Compound'), ('barebow', 'Barebow/Longbow')], default='recurve', max_length=8, verbose_name='Bow type')),
                ('number', models.SmallIntegerField(verbose_name='Number')),
                ('division', models.SmallIntegerField(verbose_name='Division')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='divari_team', to='results.Organization')),
                ('season', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='divari.Season')),
            ],
            options={
                'verbose_name': 'Team',
                'verbose_name_plural': 'Teams',
            },
        ),
        migrations.CreateModel(
            name='TeamResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.SmallIntegerField(verbose_name='Result')),
                ('competition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='divari.Competition')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='divari.Team')),
            ],
            options={
                'verbose_name': 'Team result',
                'verbose_name_plural': 'Team results',
            },
        ),
        migrations.CreateModel(
            name='SeasonResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.SmallIntegerField(verbose_name='result')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='divari.Team')),
            ],
            options={
                'verbose_name': 'Season result',
                'verbose_name_plural': 'Season results',
                'ordering': ['team__bow_type', 'team__division', '-result'],
            },
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bow_type', models.CharField(choices=[('recurve', 'Recurve'), ('compound', 'Compound'), ('barebow', 'Barebow/Longbow')], default='recurve', max_length=8, verbose_name='Bow type')),
                ('target_type', models.CharField(choices=[('40', '40 cm'), ('60', '60 cm')], default='40', max_length=2, verbose_name='Target type')),
                ('athlete', models.CharField(max_length=50, verbose_name='Athlete')),
                ('result', models.SmallIntegerField(verbose_name='result')),
                ('competition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='divari.Competition')),
            ],
            options={
                'verbose_name': 'Result',
                'verbose_name_plural': 'Results',
            },
        ),
    ]
