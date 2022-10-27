import pathlib
from queue import Queue
from multiprocessing import Process, Queue, Event
import logging


class Writer:
    def __init__(self, mainfile: str, event: Event):
        self.data_queue = Queue()
        self.event = event
        self.filename = mainfile
        self.file = open(self.filename, 'w', encoding='utf-8')

    def __call__(self, *args, **kwargs):
        while True:
            if self.data_queue.empty():
                if self.event.is_set():
                    print('Operation completed')
                    break
            else:
                r_file, data = self.data_queue.get()
                print(f"Writing file {r_file.name}")
                self.file.write(f"{data}\n")

    def __getstate__(self):
        attributes = {**self.__dict__}
        attributes['file'] = None
        return attributes

    def __setstate__(self, value):
        self.__dict__ = value
        self.file = open(self.filename, 'w', encoding='utf-8')

    def __del__(self):
        self.file.close()


def reader(data_queue: Queue, files: Queue):
    while True:
        if files.empty():
            break

        r_file = files.get()
        print(f'read file {r_file.name}')
        with open(r_file, 'r', encoding="utf-8") as fr:
            data = []
            for line in fr:
                data.append(line)
            all_data = ''.join(data)
            data_queue.put((r_file, all_data))


if __name__ == '__main__':
    event = Event()
    files = Queue()

    list_files = pathlib.Path('.').joinpath("files").glob('*.js')

    [files.put(file) for file in list_files]

    writer = Writer('main.js', event)

    if files.empty():
        logging.info("Nothing!")
    else:
        tw = Process(target=writer, name='writer')
        tw.start()

        processes = []
        for i in range(2):
            pr = Process(target=reader, args=(writer.data_queue, files), name=f"reader-{i}")
            processes.append(pr)
            pr.start()

        [pr.join() for pr in processes]
        event.set()
