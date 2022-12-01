from example_celery.my_tasks import add


if __name__ == '__main__':
    result = add.delay(2, 5)
    print(result.id)
