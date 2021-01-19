# Generated by Django 3.1.3 on 2021-01-13 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CheckboxPoll',
            fields=[
                ('checkbox_id', models.AutoField(primary_key=True, serialize=False)),
                ('quest', models.TextField()),
                ('opt_one', models.CharField(max_length=30)),
                ('opt_two', models.CharField(max_length=30)),
                ('opt_three', models.CharField(max_length=30)),
                ('opt_four', models.CharField(max_length=30)),
                ('opt_one_count', models.IntegerField(default=0)),
                ('opt_two_count', models.IntegerField(default=0)),
                ('opt_three_count', models.IntegerField(default=0)),
                ('opt_four_count', models.IntegerField(default=0)),
                ('head_image', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='RadioPoll',
            fields=[
                ('radio_id', models.AutoField(primary_key=True, serialize=False)),
                ('question', models.TextField()),
                ('option_one', models.CharField(max_length=30)),
                ('option_two', models.CharField(max_length=30)),
                ('option_three', models.CharField(max_length=30)),
                ('option_four', models.CharField(max_length=30)),
                ('option_one_count', models.IntegerField(default=0)),
                ('option_two_count', models.IntegerField(default=0)),
                ('option_three_count', models.IntegerField(default=0)),
                ('option_four_count', models.IntegerField(default=0)),
                ('header_image', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
        ),
    ]
