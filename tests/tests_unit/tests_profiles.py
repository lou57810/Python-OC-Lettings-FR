from django.test import TestCase
import pytest
from django.urls import reverse
from django.contrib.auth.models import User
# from lettings.models import Address, Letting
from profiles.models import Profile


""" Test création d'une instance de profile models: """


@pytest.mark.django_db
def test_profile_creation():
    # Créer un utilisateur pour lier au profil
    user = User.objects.create_user(username='testuser', password='password123')

    # Créer un profil
    profile = Profile.objects.create(user=user, favorite_city='Test City')

    # Vérifier si le profil est créé avec succès
    assert profile.user.username == 'testuser'
    assert profile.favorite_city == 'Test City'


@pytest.mark.django_db
class ProfilePageTest(TestCase):
    def test_profile_page_status_code(self):
        response = self.client.get(reverse('profiles_index'))
        self.assertEqual(response.status_code, 200)

    def test_profile_page_template(self):
        response = self.client.get(reverse('profiles_index'))
        self.assertTemplateUsed(response, 'profiles/index.html')
