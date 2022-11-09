import re

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from profiles.models import Profile
from profiles.serializers import ProfileSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    @action(methods=['get'], detail=False, url_name='friends', url_path='friends')
    def friends(self, request):
        #todo Method to get, given a profile id, all your friends
        profile_id = request.GET.get('profile_id')
        if not profile_id:
            return Response('El identificador del perfil es requerido.', status=400)
        else:
            int_format = re.compile(r'^\-?[1-9][0-9]*$')
            is_int = re.match(int_format, str(profile_id))
            if not is_int:
                return Response('El identificador del perfil debe ser un número entero.',
                                status=400)

        if Profile.objects.filter(pk=profile_id).exists():
            friends = Profile.objects.get(pk=profile_id).friends
            ser = ProfileSerializer(friends, many=True)
            return Response(ser.data, status=200)
        else:
            return Response('No existe perfil para el identificador ' + profile_id + '.', status=400)
