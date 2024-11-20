from django import template
from vacancy.cosine_similarity import cosine_similarity, vectorize

register = template.Library()


@register.simple_tag
def calculate_recommendation(user_skill=[], vacancy_skill=[]):
    recommend=cosine_similarity(vectorize(user_skill),vectorize(vacancy_skill))
    recommend=round(recommend*100, 2)
    return recommend
