from rest_framework_json_api import serializers
from opinion_ate.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'real_name', 'tz','one','two','three')