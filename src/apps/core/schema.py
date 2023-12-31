import graphene
from graphene_django import DjangoObjectType

from .models import Fraction, FactionKeyword, WeaponType, CoreAbility


class FractionNode(DjangoObjectType):
    class Meta:
        model = Fraction


class FactionKeywordNode(DjangoObjectType):
    class Meta:
        model = FactionKeyword


class WeaponTypeNode(DjangoObjectType):
    class Meta:
        model = WeaponType


class CoreAbilityNode(DjangoObjectType):
    class Meta:
        model = CoreAbility


class Query(graphene.ObjectType):
    fractions = graphene.List(FractionNode)
    factions_keywords = graphene.List(FactionKeywordNode)
    weapons_types = graphene.List(WeaponTypeNode)
    core_abilities = graphene.List(CoreAbilityNode)

    def resolve_fractions(self, info):
        return Fraction.objects.all()

    def resolve_factions_keywords(self, info):
        return FactionKeyword.objects.all()

    def resolve_weapons_types(self, info):
        return WeaponType.objects.all()

    def resolve_core_abilities(self, info):
        return CoreAbility.objects.all()
