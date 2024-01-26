from django.shortcuts import render, get_object_or_404
from datetime import date

from .models import Posts, Author, Tag

# Create your views here.
# all_posts = [
# {
#     "slug": "hike-in-the-mountains",
#     "image": "mountains.jpg",
#     "author": "Hassan",
#     "date": date(2021, 7, 21),
#     "title": "Mountain Hiking",
#     "excerpt": "There's nothing like the views you get when hiking in the mountains! And I wasn't even prepared for what happened whilst I was enjoying the view!",
#     "content": """
#       Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
#       aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
#       velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

#       Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
#       aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
#       velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

#       Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
#       aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
#       velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
#     """
# },
# {
#     "slug": "programming-is-fun",
#     "image": "coding.jpg",
#     "author": "Hassan",
#     "date": date(2022, 3, 10),
#     "title": "Programming Is Great!",
#     "excerpt": "Did you ever spend hours searching that one error in your code? Yep - that's what happened to me yesterday...",
#     "content": """
#       Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
#       aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
#       velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

#       Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
#       aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
#       velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

#       Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
#       aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
#       velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
#     """
# },
# {
#     "slug": "into-the-woods",
#     "image": "woods.jpg",
#     "author": "Hassan",
#     "date": date(2020, 8, 5),
#     "title": "Nature At Its Best",
#     "excerpt": "Nature is amazing! The amount of inspiration I get when walking in nature is incredible!",
#     "content": """
#       Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
#       aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
#       velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

#       Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
#       aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
#       velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

#       Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
#       aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
#       velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
#     """
# }
# ]


def starting_page(request):
    # Retrieve the three most recent posts from the database, ordered by date in descending order
    latest_post = Posts.objects.all().order_by("-date")[:3]
    # sorted_post = sorted(all_posts, key=get_date)
    # latestes_post = sorted_post[-3:]
    return render(request, "blog/index.html", {"all_posts": latest_post})


def posts(request):
    all_posts = Posts.objects.all()
    return render(request=request, template_name="blog/all-posts.html", context={"all_posts": all_posts})


def single_post(request, slug):
    # identified_post = next(post for post in all_posts if post['slug'] == slug)
    identified_post = get_object_or_404(Posts, slug=slug)

    return render(request=request, template_name="blog/post-detail.html", context={"post": identified_post, "post_tags": identified_post.tags.all()})
