# Generated by Django 4.1 on 2024-08-06 08:36

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45, unique=True)),
                ('system', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('username', models.CharField(blank=True, max_length=16, null=True, unique=True, verbose_name='Username')),
                ('email', models.EmailField(blank=True, max_length=254, unique=True, verbose_name='Email Address')),
                ('phone_no', models.CharField(blank=True, max_length=15, null=True, unique=True, verbose_name='Phone Number')),
                ('user_id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True, verbose_name='User ID')),
                ('gender', models.CharField(blank=True, choices=[('F', 'Female'), ('M', 'Male'), ('NB', 'None Binary')], max_length=2, verbose_name='Gender')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='Date Joined')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='Last Login')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active')),
                ('is_admin', models.BooleanField(default=False, verbose_name='Is Admin')),
                ('groups', models.ManyToManyField(blank=True, related_name='user_groups', to='auth.group')),
                ('roles', models.ManyToManyField(blank=True, related_name='users', to='core.role')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
