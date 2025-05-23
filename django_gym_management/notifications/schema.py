import graphene
from graphene_django import DjangoObjectType
from .models import Notification
from graphql import GraphQLError

class NotificationType(DjangoObjectType):
    class Meta:
        model = Notification
        fields = ('id', 'message', 'time_posted')

class Query(graphene.ObjectType):
    notifications = graphene.List(NotificationType)
    notification = graphene.Field(NotificationType, id=graphene.Int())

    def resolve_notifications(self, info):
        return Notification.objects.all()

    def resolve_notification(self, info, id):
        try:
            return Notification.objects.get(id=id)
        except Notification.DoesNotExist:
            return None

class CreateNotification(graphene.Mutation):
    class Arguments:
        message = graphene.String(required=True)

    notification = graphene.Field(NotificationType)

    def mutate(self, info, message):
        notification = Notification(message=message)
        notification.save()
        return CreateNotification(notification=notification)

class Mutation(graphene.ObjectType):
    create_notification = CreateNotification.Field()