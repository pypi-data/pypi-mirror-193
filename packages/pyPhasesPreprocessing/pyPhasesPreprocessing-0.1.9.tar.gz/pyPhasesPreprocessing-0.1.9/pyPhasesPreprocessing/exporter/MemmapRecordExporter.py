from pathlib import Path

import numpy as np
from pyPhases.Data import DataNotFound
from pyPhases.exporter.DataExporter import DataExporter


class MemmapRecordExporter(DataExporter):
    includesStorage = True
    batchFillProcess = None

    def initialOptions(self):
        return {
            "basePath": "data/",
            "dtype": "float32",
        }

    def getShapeFilePath(self, dataId, tmp=False):
        add = "-tmp" if tmp else ""
        return self.getPath(dataId) + add + "-shape.npy"

    def checkType(self, type):
        return type == np.memmap

    def getPath(self, dataId):
        return self.getOption("basePath") + dataId

    def stream(self, dataId, options):
        return np.memmap(self.getPath(dataId + "-tmp"), **options)

    def exists(self, dataId, options={}):
        return Path(self.getPath(dataId)).is_file()

    def read(self, dataId, options):

        for f, k in self.options.items():
            options.setdefault(f, k)

        if not self.exists(dataId):
            raise DataNotFound("Data with id %s nof found" % dataId)

        shapePath = self.getShapeFilePath(dataId)
        if not Path(shapePath).exists():
            raise Exception("Shape file not found: %s" % shapePath)

        # load complete shape, and record lengths
        lengths, shape = np.load(shapePath, allow_pickle=True)
        self.recordLengths = lengths
        self.fileShape = tuple(shape)
        self.type = options["dtype"]
        self.CurrentItemIndex = 0
        self.dataId = dataId

        self.memmap = np.memmap(self.getPath(dataId), dtype=self.type, mode="r", shape=self.fileShape)

        return self

    def __iter__(self):
        self.CurrentItemIndex = 0
        return self

    def __next__(self):
        if self.CurrentItemIndex >= len(self):
            raise StopIteration
        else:
            self.CurrentItemIndex += 1
            return self[self.CurrentItemIndex - 1]

    def __getitem__(self, index):
        start = sum(self.recordLengths[:index])
        end = start + self.recordLengths[index]
        return self.memmap[0, start:end, :]

    def __len__(self):
        return len(self.recordLengths)
