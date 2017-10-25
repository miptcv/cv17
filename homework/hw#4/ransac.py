from __future__ import print_function
from sys import argv
import os.path, json


def generate_data(img_size, line_params, n_points, sigma, inlier_ratio):
    pass


def compute_ransac_thresh(alpha, sigma):
    pass


def compute_ransac_iter_count(conv_prob, inlier_ratio):
    pass


def compute_line_ransac(data, t, n):
    pass


def main():
    print(argv)
    assert len(argv) == 2
    assert os.path.exists(argv[1])

    with open(argv[1]) as fin:
        params = json.load(fin)

    """
    params:
    line_params: (a,b,c) - line params (ax+by+c=0)
    img_size: (w, h) - size of the image
    n_points: count of points to be used

    sigma - Gaussian noise
    alpha - probability of point is an inlier

    inlier_ratio - ratio of inliers in the data
    conv_prob - probability of convergence
    """

    data = generate_data((params['w'], params['h']),
                         (params['a'], params['b'], params['c']),
                         params['n_points'], params['sigma'],
                         params['inlier_ratio'])

    t = compute_ransac_thresh(params['alpha'], params['sigma'])
    n = compute_ransac_iter_count(params['conv_prob'], params['inlier_ratio'])

    detected_line = compute_line_ransac(data, t, n)
    print(detected_line)


if __name__ == '__main__':
    main()
