# filepath: django_gym_management/schema.py
import graphene
from notifications.schema import Query as NotificationsQuery
from notifications.schema import Mutation as NotificationsMutation

class Query(NotificationsQuery, graphene.ObjectType):
    pass

class Mutation(NotificationsMutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)