# Generated by Django 4.0.5 on 2022-06-24 19:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ToDoList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, unique=True)),
            ],
            options={
                'ordering': ['pk'],
            },
        ),
        migrations.CreateModel(
            name='ToDoEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('todo_titel', models.CharField(max_length=100)),
                ('todo_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todoapp.todolist')),
            ],
            options={
                'ordering': ['pk'],
            },
        ),
    ]
