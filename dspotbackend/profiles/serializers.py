from profiles.models import Profile, ProfilePhoto
from rest_framework import serializers


class ProfilePhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfilePhoto
        fields = ['photo']


class ProfileSerializer(serializers.ModelSerializer):
    profilephotos = ProfilePhotoSerializer(many=True)
    text_tatus = serializers.SerializerMethodField()

    def get_text_tatus(self, instance):
        return instance.get_status_display()

    class Meta:
        model = Profile
        fields = ['id', 'photo', 'first_name', 'last_name', 'phone', 'address', 'city', 'state', 'zipcode', 'bio',
                  'status', 'available', 'friends', 'profilephotos', 'textStatus']
