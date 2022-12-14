from django import template

register = template.Library()


@register.filter()
def active_comments(comments):
    comms = [comment for comment in comments if comment.active]
    return comms if comms else None

