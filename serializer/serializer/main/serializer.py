from dataclasses import fields
from rest_framework import serializers
from .models import Profile,Hobby, Person, Interest


class HobbySerializer(serializers.ModelSerializer):
    class Meta:
        model=Hobby
        fields='__all__'


class InterestSerializer(serializers.ModelSerializer):
    class Meta:
        model=Interest
        fields='__all__'


class ProfileSerializer(serializers.ModelSerializer):
    user_hobby=HobbySerializer(many=True)

    class Meta:
        model=Profile
        fields='__all__'

    def create(self, validated_data):
        user_hobby=validated_data.pop('user_hobby')
        profile_instance=Profile.objects.create(**validated_data)
        for hobby in user_hobby:
            Hobby.objects.create(user=profile_instance,**hobby)
        return profile_instance

    def update(self, instance, validated_data):
        user_hobby_list = validated_data.pop('user_hobby')
        instance.display_name = validated_data.get('display_name', instance.display_name)
        instance.mobile = validated_data.get('mobile', instance.mobile)
        instance.email = validated_data.get('email', instance.email)

        hobbies_with_same_userinstance=Hobby.objects.filter(user=instance.pk).values_list('id',flat=True)

        hobbies_id_pool = []

        for hobby in user_hobby_list:
            if "id" in hobby.keys():
                if Hobby.objects.filter(id=hobby['id']).exists():
                    hobby_instance = Hobby.objects.get(id=hobby['id'])
                    hobby_instance.name = hobby.get('name', hobby_instance.name)
                    hobby_instance.description = hobby.get('description',hobby_instance.description)
                    hobby_instance.save()
                    hobbies_id_pool.append(hobby_instance.id)

                else:
                    continue
            else:
                hobbies_instance = Hobby.objects.create(user=instance, **hobby)
                hobbies_id_pool.append(hobbies_instance.id)
        
        for hobby_id in hobbies_with_same_userinstance:
            if hobby_id not in hobbies_id_pool:
                Hobby.objects.filter(pk=hobby_id).delete()
        return instance


class PersonSerializer(serializers.ModelSerializer):
    interest = InterestSerializer(many=True)
    class Meta: 
        model=Person
        fields='__all__'
