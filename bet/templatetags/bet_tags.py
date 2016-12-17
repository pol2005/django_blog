# coding=utf-8
import re
from django import template
register = template.Library()
from bet.models import Article,Block
from bet.forms import NewsletterForm,LoginForm,UserRegistrationForm

@register.inclusion_tag('homepage/flex.html')
def show_flex_slider(count=4):
    #flex1 = Article.published.order_by('-publish')[:count]
    flex = Article.published.filter(tags__name__in=["Επίκαιρα"])[:count]
    return {'flex':flex}

@register.inclusion_tag('homepage/top_widget.html')
def top_widget():
    top_widget1 = Article.published.filter(tags__name__in=["Ειδήσεις"])[:1]
    top_widget2 = Article.published.filter(tags__name__in=["Ειδήσεις"])[1:4]
    return {'top_widget1':top_widget1,'top_widget2':top_widget2}

@register.inclusion_tag('homepage/middle_widget.html')
def middle_widget():
    middle_widget1 = Article.published.filter(tags__name__in=["Αναλύσεις Ποδοσφαίρου"])[:1]
    middle_widget2 = Article.published.filter(tags__name__in=["Αναλύσεις Ποδοσφαίρου"])[1:3]
    middle_widget3 = Article.published.filter(tags__name__in=["Αναλύσεις Ποδοσφαίρου"])[3:5]
    middle_widget4 = Article.published.filter(tags__name__in=["Αναλύσεις Ποδοσφαίρου"])[5:7]
    return {'middle_widget1':middle_widget1,'middle_widget2':middle_widget2,'middle_widget3':middle_widget3,'middle_widget4':middle_widget4}

@register.inclusion_tag('homepage/double_widget.html')
def double_widget():
    double_widget1 = Article.published.filter(tags__name__in=["Αναλύσεις Μπάσκετ"])[:1]
    double_widget2 = Article.published.filter(tags__name__in=["Αναλύσεις Βόλλευ","Αναλύσεις Τένις"])[:1]
    double_widget3 = Article.published.filter(tags__name__in=["Αναλύσεις Μπάσκετ"])[1:4]
    double_widget4 = Article.published.filter(tags__name__in=["Αναλύσεις Βόλλευ","Αναλύσεις Τένις"])[1:4]
    return {'double_widget1':double_widget1,'double_widget2':double_widget2,'double_widget3':double_widget3,'double_widget4':double_widget4}

@register.inclusion_tag('blocks/left_sidebar.html')
def blocks():
    block = Block.published.all()
    return {'block': block}

@register.inclusion_tag('bet/breaking.html')
def breaking_bar(count = 10):
    breaking_news = Article.published.order_by('-publish')[:count]
    return {'breaking_news': breaking_news}



@register.inclusion_tag('blocks/right_sidebar.html')
def sidebar_right():
    blocks = Block.published.filter(sidebar='right').order_by('-weight')
    top_block = Article.published.filter(tags__name__in=["Νόμιμες Στοιχηματικές"])[:10]
    payment = Article.published.filter(tags__name__in=["Μέθοδοι Πληρωμής"])
    return {'blocks': blocks,'top_block':top_block,'payment':payment}

@register.inclusion_tag('blocks/left_sidebar.html')
def sidebar_left():
    blocks = Block.published.filter(sidebar='left').order_by('-weight')
    kazino = Article.published.filter(tags__name__in=["Καζίνο"])
    poker = Article.published.filter(tags__name__in=["Πόκερ"])
    return {'blocks': blocks,'kazino':kazino,'poker':poker}

@register.inclusion_tag('bet/newsletter.html')
def newsletter():
    newsletter = NewsletterForm()
    return {'newsletter': newsletter}

@register.inclusion_tag('bet/footer1.html')
def footer1():
    footer1= Article.published.order_by('-publish')[:7]
    return {'footer1': footer1}

@register.inclusion_tag('bet/ad_top.html')
def ad_top():
    blockpano = Block.published.filter(sidebar='arxikipano')[:1]
    return {'blockpano': blockpano}

@register.inclusion_tag('modals/login.html')
def login_modal():
    form = LoginForm()
    return {'form': form}

@register.inclusion_tag('modals/register.html')
def register_modal():
    user_form = UserRegistrationForm()
    return {'user_form': user_form}

@register.filter(name='remove_whitespace')
def remove_whitespace(value):
    value = re.sub(r'\n', ' ', value)
    value = re.sub(r'\s+', ' ', value)
    return value
