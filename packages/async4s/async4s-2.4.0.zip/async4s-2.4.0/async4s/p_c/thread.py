#!/usr/bin/env python

"""
Producer-Consumer模型-线程实现方式
"""

from __future__ import annotations

import abc
import threading
from queue import Queue
from typing import Type


class Runnable(metaclass=abc.ABCMeta):
    def __init__(self, buffer: Queue, count_worker: int):
        self._buffer = buffer
        self._count_worker = count_worker
        self._workers = []

    @abc.abstractmethod
    def run(self):
        pass

    def start(self):
        for _ in range(self._count_worker):
            worker = threading.Thread(target=self.run, name=self.__class__.__name__, daemon=True)
            self._workers.append(worker)
            worker.start()

    def join(self):
        for worker in self._workers:
            worker.join()
        self._workers.clear()

    @property
    def buffer(self):
        return self._buffer

    @property
    def count_worker(self):
        return self._count_worker


class Producer(Runnable):
    pass


class Consumer(Runnable):
    pass


class Manager(object):
    def __init__(self, producer_cls: Type[Producer], producer_cnt: int, consumer_cls: Type[Consumer], consumer_cnt: int, buffer_size=1024):
        self._buffer = self._create_buffer(buffer_size)
        self._producer = producer_cls(self._buffer, producer_cnt)
        self._consumer = consumer_cls(self._buffer, consumer_cnt)

    def _create_buffer(self, buffer_size=1024):
        return Queue(buffer_size)

    def start(self):
        self._producer.start()
        self._consumer.start()

    def join(self):
        self._producer.join()
        self._consumer.join()

    @property
    def buffer(self):
        return self._buffer

    @property
    def producer(self):
        return self._producer

    @property
    def consumer(self):
        return self._consumer
