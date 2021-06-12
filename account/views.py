from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

from account.api.serializers import AccountSerializer
from account.models import Account

class AccountListAPIView(ListAPIView):
    try:
        queryset = Account.objects.all()
        serializer_class = AccountSerializer

    except Exception as e:
        print(e)



class AccountDetailAPIView(RetrieveAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    lookup_field = 'pk' #'pk'=id

class AccountDeleteAPIView(DestroyAPIView):
        queryset = Account.objects.all()
        serializer_class = AccountSerializer
        lookup_field = 'pk'  # 'pk'=id

class AccountUpdateAPIView(UpdateAPIView):
        queryset = Account.objects.all()
        serializer_class = AccountSerializer
        lookup_field = 'pk'  # 'pk'=id

