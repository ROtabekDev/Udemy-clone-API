# Generated by Django 4.1 on 2022-08-16 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_alter_course_course_section_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='comments',
            field=models.ManyToManyField(blank=True, to='courses.comment'),
        ),
    ]