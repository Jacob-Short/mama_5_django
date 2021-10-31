from django.shortcuts import redirect, render, reverse
from django.views.generic import View

# models
from user_message.models import Message



def get_notifications(user):
    '''gets new notifications based on user'''



class AllNotificationsView(View):

    def get(self, request):
        ...
        # target_user = request.user
        # signed_in_user = target_user
        # new_notifications = []
        # user_messages = Message.objects.filter(recipient=target_user)
        # new_message_notifications = MessageNotification.objects.filter(
        #     Q(user_notified=target_user) & Q(isNew=True)
        # )
        # new_review_notifications = ReviewNotification.objects.filter(
        #     Q(user_notified=target_user) & Q(isNew=True)
        # )
        # new_faq_notifications = FaqNotification.objects.filter(
        #     Q(user_notified=target_user) & Q(isNew=True)
        # )

        # new_notifications = (
        #     list(new_message_notifications)
        #     + list(new_review_notifications)
        #     + list(new_faq_notifications)
        # )

        # notifications_count = get_notification_count(request.user)

        # # old notifications
        # old_message_notifications = MessageNotification.objects.filter(
        #     Q(user_notified=target_user) & Q(isNew=False)
        # )
        # old_review_notifications = ReviewNotification.objects.filter(
        #     Q(user_notified=target_user) & Q(isNew=False)
        # )
        # old_faq_notifications = FaqNotification.objects.filter(
        #     Q(user_notified=target_user) & Q(isNew=False)
        # )

        # old_notifications = (
        #     list(old_message_notifications)
        #     + list(old_review_notifications)
        #     + list(old_faq_notifications)
        # )

        # print(new_notifications)
        # print(f"user_messages: {new_message_notifications}")
        # print(f"reviews: {new_review_notifications}")

        # context = {
        #     "request": request,
        #     "notifications_count": notifications_count,
        #     "new_message_notifications": new_message_notifications,
        #     "new_review_notifications": new_review_notifications,
        #     "new_faq_notifications": new_faq_notifications,
        #     "old_notifications": old_notifications,
        #     "user_messages": user_messages
        # }

        # notify_seen(new_notifications)
        # return render(request, "notifications.html", context)


    def post(self, request):
        ...