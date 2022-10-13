from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template('index.html')
    context = {}
    rendered_page = template.render(context, request)
    return HttpResponse(rendered_page)
    # most_popular_posts = Post.objects.popular_with_author_and_tags_and_comments_count()
    # most_fresh_posts = Post.objects.fresh_with_author_and_tags_and_comments_count()
    # most_popular_tags = Tag.objects.popular_with_posts_count()

    # context = {
    #     'most_popular_posts': [serialize_post(post) for post in most_popular_posts],
    #     'page_posts': [serialize_post(post) for post in most_fresh_posts],
    #     'popular_tags': [serialize_tag(tag) for tag in most_popular_tags],
    # }
    # return render(request, 'index.html', context)