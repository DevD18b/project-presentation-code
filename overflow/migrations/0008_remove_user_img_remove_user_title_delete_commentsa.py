# Generated by Django 4.0.5 on 2022-08-02 10:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('overflow', '0007_upvotes_question_downvotes_question'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='img',
        ),
        migrations.RemoveField(
            model_name='user',
            name='title',
        ),
        migrations.DeleteModel(
            name='CommentsA',
        ),
    ]
