from profiles.models import Profile, ProfilePhoto
from rest_framework import serializers


class ProfilePhotoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProfilePhoto
        fields = ['photo']


class ProfileSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()
    textStatus = serializers.SerializerMethodField()

    def get_images(self, instance):
        images = instance.profilephotos
        ser = ProfilePhotoSerializer(images, many=True)
        return [image['photo'] for image in ser.data]
    def get_textStatus(self, instance):
        return instance.get_status_display()

    class Meta:
        model = Profile
        fields = ['id', 'photo', 'first_name', 'last_name', 'phone', 'address', 'city', 'state', 'zipcode', 'bio', 'status',
                  'available', 'friends', 'images', 'textStatus']
