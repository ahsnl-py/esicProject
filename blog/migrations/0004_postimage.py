# Generated by Django 3.0 on 2020-07-05 19:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('post', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='blog.Post')),
            ],
        ),
    ]
