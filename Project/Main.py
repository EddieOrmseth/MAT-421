import os
import json
from Tester import Tester, TestConfiguration
from DataLoader import make_all_data_loaders
from PiecewiseLinearInterpolation import PiecewiseLinearInterpolator
from SplineInterpolation import SplineInterpolator
from NewtonInterpolation import NewtonInterpolator
from LagrangeInterpolation import LagrangeInterpolator


if __name__ == '__main__':

    loaders = make_all_data_loaders()
    interpolators = [PiecewiseLinearInterpolator(), SplineInterpolator(k=3, s=0), NewtonInterpolator(), SplineInterpolator(k=5, s=0)]
    test_configs = [TestConfiguration("One In The Middle", [1, 1, 1, 0, 1, 1, 1]), 
                    TestConfiguration("Two In The Middle", [1, 1, 1, 0, 0, 1, 1, 1]),
                    TestConfiguration("Medium Gap", [1, 1, 1, 0, 0, 0, 1, 1, 1]),
                    TestConfiguration("Big Gap", [1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1]),
                    TestConfiguration("Missing Gaps", [1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1]),
                    TestConfiguration("Medium Gaps", [1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1])]

    tester: Tester = Tester()
    tester.loaders = loaders
    tester.interpolators = interpolators
    tester.test_configs = test_configs

    tester.setup_results()
    tester.run_all_tests()

    output = json.dumps(tester.consolidate_results(), indent=4).replace("\'", "\"")
    print(output)

    file = open(os.path.join(os.path.dirname(__file__), "view.json"), mode='w')
    file.write(output)
    file.close()


    # A, B, C = tester.consolidate_results()
    # print(A)
    # print(B)
    # print(C)
