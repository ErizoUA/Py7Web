from bson import ObjectId

from models import Post, User

if __name__ == '__main__':
    post = Post.objects(id='638654c60b206f8b0e8c9318')
    # post = Post.objects(title='MongoEngine Documentation')
    post.update(link_url='http://docs.mongoengine.org/')
    for p in post:
        print(p.to_mongo().to_dict())
