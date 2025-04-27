import os
import numpy as np
import pandas as pd


class DataLoader:

    t_data: np.array = None
    x_data: np.array = None
    y_data: np.array = None


    def load(self):
        raise "DataLoader::load must be implemented"
    

    def name(self):
        raise "DataLoader::name must be implemented"
    

    def getIdx(self):
        raise "DataLoader::getIDx must be implemented"


class TennisDataLoader(DataLoader):

    path: str = ""
    idx: int = -1


    def __init__(self, path: str, idx: int):
        self.path = path


    def load(self):
        data = pd.read_csv(self.path)

        self.x_data = data["x-coordinate"].to_numpy(dtype=np.float32)
        self.y_data = data["y-coordinate"].to_numpy(dtype=np.float32)

        raw_t_data = data["file name"]
        self.t_data = np.zeros_like(self.x_data, dtype=np.float32)
        for i in range(len(self.t_data)): self.t_data[i] = float(raw_t_data[i][0:4])

        valid_t = np.where(~np.isnan(self.x_data))
        self.t_data = self.t_data[valid_t]
        self.x_data = self.x_data[valid_t]
        self.y_data = self.y_data[valid_t]

        self.x_data = ((self.x_data) / (1280.0))
        self.y_data = ((self.y_data) / (720.0))


    def name(self):
        return "Tennis"


    def getIdx(self):
        return self.idx
    

class SoccerDataLoader(DataLoader):

    path: str = ""
    idx: int = -1


    def __init__(self, path: str, idx: int):
        self.path = path


    def load(self):
        data = pd.read_csv(self.path, header=None)

        block = data[1].to_numpy(dtype=np.float32)
        self.t_data = data[0].to_numpy(dtype=np.float32) + (block - 1) * 750
        self.x_data = data[2].to_numpy(dtype=np.float32)
        self.y_data = data[3].to_numpy(dtype=np.float32)

        valid_t = np.where(~np.isnan(self.x_data))
        self.t_data = self.t_data[valid_t]
        self.x_data = self.x_data[valid_t]
        self.y_data = self.y_data[valid_t]

        self.x_data = ((self.x_data) / (1920.0))
        self.y_data = ((self.y_data) / (1080.0))


    def name(self):
        return "Soccer"


def make_all_data_loaders() -> list[TennisDataLoader]:
    loaders = []

    tennis_path = os.path.join(os.path.dirname(__file__), "data\\tennis")
    i: int = 0
    for entry in os.scandir(tennis_path):
        loaders.append(TennisDataLoader(entry.path, i))
        i += 1

    scocer_path = os.path.join(os.path.dirname(__file__), "data\\soccer")
    i = 0
    for entry in os.scandir(scocer_path):
        loaders.append(SoccerDataLoader(entry.path, i))
        i += 1
    
    return loaders
    

if __name__ == "__main__":

    loaders = make_all_data_loaders()
    print(len(loaders))
    loaders[0].load()
    print(loaders[0].x_data)
    print(loaders[0].y_data)
