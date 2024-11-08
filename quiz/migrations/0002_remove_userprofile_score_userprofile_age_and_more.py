# Generated by Django 5.0.7 on 2024-10-29 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='score',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='first_name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='highest_qualification',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='last_name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='preferred_test',
            field=models.CharField(choices=[('test1', 'Test 1'), ('test2', 'Test 2'), ('test3', 'Test 3')], default='test1', max_length=20),
        ),
        migrations.AlterField(
            model_name='question',
            name='option1',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='question',
            name='option2',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='question',
            name='option3',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='question',
            name='option4',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_text',
            field=models.TextField(),
        ),
    ]
