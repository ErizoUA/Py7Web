from models import Post, User

if __name__ == '__main__':
    posts = Post.objects()
    for post in posts:
        print(post.to_mongo().to_dict())

    for post in Post.objects(tags='mongoengine'):
        print(post.title)