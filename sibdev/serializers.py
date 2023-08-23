from rest_framework import serializers
from sibdev.models import Client


class TopFiveSerializer(serializers.ModelSerializer):
    spent_money = serializers.IntegerField()
    gems_field = serializers.SerializerMethodField()

    class Meta:
        model = Client
        fields = ('username', 'spent_money', 'gems_field')

    def get_gems_field(self, *args):
        gems_set = set()
        gems_list = []
        for client in self.instance:
            for gem in client.gems.all().distinct():
                gem = gem.title
                if gem in gems_set:
                    gems_list.append(gem)
                else:
                    gems_set.add(gem)
        return gems_list
