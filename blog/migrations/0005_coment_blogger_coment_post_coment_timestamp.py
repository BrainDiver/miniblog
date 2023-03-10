# Generated by Django 4.1.5 on 2023-02-25 15:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_coment_remove_post_comentaries'),
    ]

    operations = [
        migrations.AddField(
            model_name='coment',
            name='blogger',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='blogger_comments', to='blog.blogger'),
        ),
        migrations.AddField(
            model_name='coment',
            name='post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='post_comment', to='blog.post'),
        ),
        migrations.AddField(
            model_name='coment',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
