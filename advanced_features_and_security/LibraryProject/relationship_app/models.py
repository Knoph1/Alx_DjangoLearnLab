from django.db import models
from django.conf import settings 
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver 
# Create your models here.
class Author(models.Model):
  name = models.CharField(max_length=100)
  
  def __str__(self):
    return self.name

class Book(models.Model):
  title = models.CharField(max_length=200)
  author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name= 'Book')
  class Meta:
    permissions = [
      ("can_add_book", "Can add book"),
      ("can_change_book", "Can change book"),
      ("can_delete_book", "Can delete book"),
    ]
  def __str__(self):
    return self.title

class Library(models.Model):
  name = models.CharField(max_length=150)
  books = models.ManyToManyField(Book)

  def __str__(self):
    return self.name

class Librarian(models.Model):
  name = models.CharField(max_length=100)
  library = models.OneToOneField(Library, on_delete=models.CASCADE)

  def __str__(self):
    return self.name

ROLE_CHOICES = [
  ('Admin', 'Admin'),
  ('Librarian', 'Librarian'),
  ('Member', 'Member'),
]

class UserProfile(models.Model):
  user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  role = models.CharField(max_length=10, choices=ROLE_CHOICES)

  def __str__(self):
    return self.user.username

  def save(self, *args, **kwargs):
    super().save(*args, **kwargs)
    if self.role == 'Admin':
      try:
        content_type = ContentType.objects.get_for_model(UserProfile)
        permission = Permission.object.get(
          codename='can_view_access_admin_view',
          content_type=content_type,
      )

        if self.user and not self.user.has_perm(permission.codename):
          self.user.user_permissions.add(permission)
      except ObjectDoesNotExist:
        print("Permission 'can_view_access_admin_view' does not exist for this User Progile.")
      except Exception as e:
        print(f"An error occured: {e}")

  @receiver(post_save, sender=User)
  def create_user_profile(self, sender, instance, created, **kwargs):
    if created:
      UserProfile.objects.create(user=instance)

  @receiver(post_save, sender=User)
  def save_user_profile(self, sender, instance, **kwargs):
    instance.userprofile.save()