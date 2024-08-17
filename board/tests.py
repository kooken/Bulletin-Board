import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from board.models import Ad, Comment

User = get_user_model()

@pytest.mark.django_db
class AdTestCase:

    @pytest.fixture(autouse=True)
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(email="user@example.com", password="password")
        self.client.force_authenticate(user=self.user)
        self.ad = Ad.objects.create(
            title="Test Ad",
            price=100,
            author=self.user,
            description="This is a test ad"
        )

    def test_ad_creation(self):
        url = reverse("ad-list")
        data = {
            "title": "New Ad",
            "price": 200,
            "description": "New ad description"
        }
        response = self.client.post(url, data)
        assert response.status_code == status.HTTP_201_CREATED
        assert Ad.objects.count() == 2
        assert Ad.objects.get(title="New Ad").description == "New ad description"

    def test_ad_list(self):
        url = reverse("ad-list")
        response = self.client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data['results']) == 1
        assert response.data['results'][0]['title'] == self.ad.title

    def test_ad_update(self):
        url = reverse("ad-detail", args=[self.ad.pk])
        data = {
            "title": "Updated Ad Title"
        }
        response = self.client.patch(url, data)
        assert response.status_code == status.HTTP_200_OK
        assert Ad.objects.get(pk=self.ad.pk).title == "Updated Ad"
