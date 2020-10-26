from rest_framework import serializers
from .models import Profiles,Contact_info


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profiles
        fields = ("user", "bio","profile_pic")
        

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact_info
        fields = ("user", "tel_number","github_u","facebook_u","instagram_u","twiter_u","linkedin_u","user")