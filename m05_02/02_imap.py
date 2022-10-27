from multiprocessing import Pool


def worker(val):
    return val ** 2


if __name__ == '__main__':
    with Pool() as pool:
        r = pool.map(worker, range(1, 11))
        print(r)

        iterator = pool.imap(worker, range(1, 11))
        print(iterator)
        print(next(iterator))
        print(next(iterator))

        r = pool.apply_async(worker, (10, ))
        print(r.get())
