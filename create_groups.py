# create_groups.py
from django.contrib.auth.models import Group

# Create Manager group
manager_group, created = Group.objects.get_or_create(name='Manager')
if created:
    print("Manager group created")
else:
    print("Manager group already exists")

# Create Delivery crew group
delivery_crew_group, created = Group.objects.get_or_create(name='Delivery crew')
if created:
    print("Delivery crew group created")
else:
    print("Delivery crew group already exists")
