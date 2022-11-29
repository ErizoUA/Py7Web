from models import Post, User

if __name__ == '__main__':
    posts = Post.objects()
    for post in posts:
        print(post.to_mongo().to_dict())

    steve = User.objects(first_name='Steve')
    steve.delete()

    posts = Post.objects()
    for post in posts:
        print(post.to_mongo().to_dict())