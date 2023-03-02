# Generated by Django 4.1.5 on 2023-02-25 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_comentaries_alter_post_blogger_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Enter coment title', max_length=20)),
                ('content', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='post',
            name='comentaries',
        ),
    ]