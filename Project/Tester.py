from DataLoader import DataLoader
from Interpolation import Interpolator
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score


class TestCase:

    t_data: np.array = None
    x_data: np.array = None
    x_true: np.array = None
    y_data: np.array = None
    y_true: np.array = None


class TestConfiguration:

    name_str: str
    mask: str
    size: int = -1


    def __init__(self, name_str: str, mask):
        self.name_str = name_str + ": ["
        self.mask = mask
        self.size = len(mask)
        
        for i in range(len(mask)): self.name_str += str(mask[i]) + ", "
        self.name_str = self.name_str[:len(self.name_str) - 2]
        self.name_str += "]"

        for i in range(self.size): 
            if mask[i] == 0: mask[i] = np.nan
            elif not np.isnan(mask[i]): mask[i] = 1


    def name(self):
        return self.name_str


    def configure(self, loc: int, t_data: np.array, x_data: np.array, y_data: np.array) -> TestCase:
        if loc < 0 or len(t_data) < loc + self.size: return None

        t: TestCase = TestCase()
        t.t_data = t_data[loc:loc + self.size]
        t.x_true = x_data[loc:loc + self.size]
        t.y_true = y_data[loc:loc + self.size]

        t.x_data = t.x_true.copy() * self.mask
        t.y_data = t.y_true.copy() * self.mask

        return t


def get_results_dict() -> dict:
    return { "total error" : 0.0, "num cases" : 0.0, "average error": 0.0 }


class Tester:

    test_configs = list[TestConfiguration]
    loaders: list[DataLoader]
    interpolators: list[Interpolator]
    results: dict = {}

    datasets: set = set()

    def setup_results(self):
        for config in self.test_configs:
            self.results.update({ config.name() : {} })
            for loader in self.loaders:
                self.results[config.name()].update({ loader.name() : {} })
                for interp in self.interpolators:
                    self.results[config.name()][loader.name()].update({ interp.name() : get_results_dict() })

    
    def compute_test_case(self, interpolator: Interpolator, t_data, x_data: np.array, x_true: np.array, y_data: np.array, y_true: np.array):
        x_pred = interpolator.interpolate_missing_values(t_data, x_data)
        y_pred = interpolator.interpolate_missing_values(t_data, y_data)

        errors = np.sqrt((x_true - x_pred) ** 2 + (y_true - y_pred) ** 2)
        error = np.sum(errors)
        mean_true_x = np.mean(x_true)
        mean_true_y = np.mean(y_true)
        total_variance = np.sqrt((x_true - mean_true_x) ** 2 + (y_true - mean_true_y) ** 2)
        ss_res = np.sum(errors ** 2)
        ss_tot = np.sum(total_variance ** 2)

        # if error > 1000:
        #     t_more = np.linspace(np.min(t_data), np.max(t_data), 100)
        #     x_more = np.full_like(t_more, np.nan)
        #     y_more = np.full_like(t_more, np.nan)
        #     for i in range(len(t_data)):
        #         idx = np.argmin(np.abs(t_more - t_data[i]))
        #         x_more[idx] = x_data[i]
        #         y_more[idx] = y_data[i]

        #     x_more_pred = interpolator.interpolate_missing_values(t_more, x_more)
        #     y_more_pred = interpolator.interpolate_missing_values(t_more, y_more)
        #     xR2 = r2_score(x_true, x_pred)
        #     yR2 = r2_score(y_true, y_pred)

        #     plt.plot(t_data, x_true, 'o', label='X Original Points')
        #     plt.plot(t_more, x_more_pred, '--', label='X ' + interpolator.name() + " Estimate: " + str(xR2) + " r2")
        #     plt.legend()
        #     plt.show()
            
        #     plt.plot(t_data, y_true, 'o', label='Y Original Points')
        #     plt.plot(t_more, y_more_pred, '--', label='Y ' + interpolator.name() + " Estimate: " + str(yR2) + " r2")
        #     plt.legend()
        #     plt.show()

        return error, ss_res, ss_tot
    

    def run_all_tests(self):
        while len(self.loaders) > 0:
            loader = self.loaders.pop()
            loader.load()
            self.datasets.add(loader.name())
            for config in self.test_configs:
                length = len(loader.t_data)
                idxs = [int(((i + 1.0) / 6.0) * float(length)) for i in range(5)]
                testcases = [config.configure(idx, loader.t_data, loader.x_data, loader.y_data) for idx in idxs]
                for t in testcases:
                    if t is None: continue
                    for interp in self.interpolators:
                        error, ss_res, ss_tot = self.compute_test_case(interp, t.t_data, t.x_data, t.x_true, t.y_data, t.y_true)
                        self.results[config.name()][loader.name()][interp.name()]["total error"] += error
                        self.results[config.name()][loader.name()][interp.name()]["num cases"] += 1


    def consolidate_results(self):
        error_by_test_config: dict = {}
        for config in self.test_configs:
            error_by_test_config.update({ config.name() : 0.0 })

        error_by_interpolation: dict = {}
        for interp in self.interpolators:
            error_by_interpolation.update({ interp.name() : 0.0 })

        error_by_dataset: dict = {}
        for dataset in self.datasets:
            error_by_dataset.update({ dataset : 0.0 })

        for config in self.test_configs:
            for dataset in self.datasets:
                for interp in self.interpolators:
                    avgError: float = self.results[config.name()][dataset][interp.name()]["total error"] / self.results[config.name()][dataset][interp.name()]["num cases"]
                    self.results[config.name()][dataset][interp.name()]["average error"] = avgError
                    error_by_test_config[config.name()] += avgError
                    error_by_interpolation[interp.name()] += avgError
                    error_by_dataset[dataset] += avgError

        return { "Results" : self.results, "Error by Test Config" : error_by_test_config, "Error by Interpolation" : error_by_interpolation, "Error by Dataset" : error_by_dataset }
