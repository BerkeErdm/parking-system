from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import RetrieveUpdateAPIView, get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from signin.api.serializers import UserSerializer, ChangePasswordSerializer

class ProfileView(RetrieveUpdateAPIView):


    #GÜVENLİK İÇİN - permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, id=self.request.user.id)
        return obj

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

class UpdatePass(APIView):
        permission_classses = (IsAuthenticated,)

        def put(self, request, *args, **kwargs):
            self.object = self.request.user
            data = {
                "old_password": request.data["old_password"],
                "new_password": request.data["new_password"]
            }

            serializer = ChangePasswordSerializer(data = data)

            if serializer.is_valid():
                print(serializer.data)
                old_password=serializer.data.get(("old_password"))
                if not self.object.check_password(old_password):
                    return Response({"old_password": "wrong_password"},status=status.HTTP_400_BAD_REQUEST)

                self.object.set_password(serializer.data.get("new_password"))
                self.object.save(),
                #update_session_auth_hash(request, self.object)
                return Response( status= status.HTTP_204_NO_CONTENT)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#{
#"new_password":"",
#"old_password":""
#}