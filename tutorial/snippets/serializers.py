from os.path import abspath

from rest_framework import serializers

from snippets.models import LANGUAGE_CHOICES, STYLE_CHOICES, Snippet

# class SnippetSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(required=False, allow_blank=True, max_length=100)
#     code = serializers.CharField(style={'base_template': 'textarea.html'})
#     linenos = serializers.BooleanField(required=False)
#     language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
#     style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')

#     def create(self, validated_data):
#         """
#         Create and return a new `Snippet` instance, given the validated data.
#         """
#         return Snippet.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         """
#         Update and return an existing `Snippet` instance, given the validated data.
#         """
#         instance.title = validated_data.get('title', instance.title)
#         instance.code = validated_data.get('code', instance.code)
#         instance.linenos = validated_data.get('linenos', instance.linenos)
#         instance.language = validated_data.get('language', instance.language)
#         instance.style = validated_data.get('style', instance.style)
#         instance.save()
#         return instance

#################################################################################
#BT - Using ModelSerializer class.
#################################################################################

# class SnippetSerializer(serializers.ModelSerializer):
#     #BT - This is used for displaying only. It will not used to write to the database.
#     owner = serializers.ReadOnlyField(source='owner.username')
#     class Meta:
#         model = Snippet
#         fields = ['id', 'title', 'code', 'linenos', 'language', 'style','owner']


from django.contrib.auth.models import User

# class UserSerializer(serializers.ModelSerializer):
#     #BT - The default ModelSerializer does not have any relation ship with user account.
#     #     We can add an additional field to represent that if we want.
#     snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

#     class Meta:
#         model = User
#         fields = ['id', 'username', 'snippets']

##############################################################################################
#BT - So if you want to have a hyperlink to a specific record you can just do so with:
#     HyperLinkedModelSerializer class and specify a 'url' along with 'id' field.
##############################################################################################
class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    #BT - Notes: the highlight is pointing to 'snippet-hightlight' url pattern and return html
    #            format so that we can see it in html otherwise, we will not see it throught the api format.
    #
    #            Our snippet and user serializers include 'url' fields that by default will refer to '{model_name}-detail', 
    #            which in this case will be 'snippet-detail' and 'user-detail'.
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')

    class Meta:
        model = Snippet
        fields = ['url', 'id', 'highlight', 'owner',
                  'title', 'code', 'linenos', 'language', 'style']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'snippets']