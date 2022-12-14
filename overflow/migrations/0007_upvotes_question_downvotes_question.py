# Generated by Django 4.0.5 on 2022-07-30 09:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('overflow', '0006_rename_ans_verified_question_verified_answer'),
    ]

    operations = [
        migrations.CreateModel(
            name='upvotes_Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='get_upvotes_que', to='overflow.question')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='get_upvotes_que', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'question')},
            },
        ),
        migrations.CreateModel(
            name='downvotes_Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='get_downvotes_que', to='overflow.question')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='get_downvotes_que', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'question')},
            },
        ),
    ]
