
import os

from urllib.request import urlretrieve

os.chdir(os.path.abspath(os.path.dirname(__file__)))

dataset_files = [
    'icy021ljq_raw.fits',
    'icy021l6q_raw.fits',
    'icy021m2q_raw.fits',
    'icy021kuq_raw.fits',
    'icy021lgq_raw.fits',
    'icy021kmq_raw.fits',
    'icy021k1q_raw.fits',
    'icy021kxq_raw.fits',
    'icy021lrq_raw.fits',
    'icy021l0q_raw.fits',
    'icy021lyq_raw.fits',
    'icy021ksq_raw.fits',
    'icy021kfq_raw.fits',
    'icy021llq_raw.fits',
    'icy021jzq_raw.fits',
    'icy021ltq_raw.fits',
    'icy021kkq_raw.fits',
    'icy021laq_raw.fits',
    'icy021lkq_raw.fits',
    'icy021kaq_raw.fits',
    'icy021m3q_raw.fits',
    'icy021ktq_raw.fits',
    'icy021l7q_raw.fits',
    'icy021lfq_raw.fits',
    'icy021klq_raw.fits',
    'icy021kyq_raw.fits',
    'icy021lsq_raw.fits',
    'icy021k0q_raw.fits',
    'icy021lxq_raw.fits',
    'icy021kgq_raw.fits',
    'icy021lmq_raw.fits',
    'icy021luq_raw.fits',
    'icy021k6q_raw.fits',
    'icy021kjq_raw.fits',
    'icy021l4q_raw.fits',
    'icy021m0q_raw.fits',
    'icy021kwq_raw.fits',
    'icy021lhq_raw.fits',
    'icy021kbq_raw.fits',
    'icy021k3q_raw.fits',
    'icy021l9q_raw.fits',
    'icy021kzq_raw.fits',
    'icy021lpq_raw.fits',
    'icy021leq_raw.fits',
    'icy021koq_raw.fits',
    'icy021kdq_raw.fits',
    'icy021lnq_raw.fits',
    'icy021l2q_raw.fits',
    'icy021k8q_raw.fits',
    'icy021kqq_raw.fits',
    'icy021kiq_raw.fits',
    'icy021lcq_raw.fits',
    'icy021k5q_raw.fits',
    'icy021lvq_raw.fits',
    'icy021m1q_raw.fits',
    'icy021kvq_raw.fits',
    'icy021l5q_raw.fits',
    'icy021liq_raw.fits',
    'icy021kcq_raw.fits',
    'icy021lqq_raw.fits',
    'icy021k2q_raw.fits',
    'icy021l8q_raw.fits',
    'icy021ldq_raw.fits',
    'icy021knq_raw.fits',
    'icy021keq_raw.fits',
    'icy021loq_raw.fits',
    'icy021jxq_flt.fits',
    'icy021lzq_raw.fits',
    'icy021kpq_raw.fits',
    'icy021l3q_raw.fits',
    'icy021k9q_raw.fits',
    'icy021lbq_raw.fits',
    'icy021lwq_raw.fits',
    'icy021jyq_raw.fits',
    'icy021k4q_raw.fits',
]

destination = 'iraclis_test_dataset_hatp26b'

if not os.path.isdir(destination):
    os.mkdir(destination)

if not os.path.isdir(os.path.join(destination, 'raw_data')):
    for num, dataset_file in enumerate(dataset_files):
        print('{0}/{1}: '.format(num + 1, len(dataset_files)), dataset_file)
        if not os.path.isfile(os.path.join(destination, dataset_file)):
            urlretrieve('https://mast.stsci.edu/portal/Download/file/HST/product/{0}'.format(
                dataset_file), os.path.join(destination, dataset_file))


os.system('iraclis -p {0}'.format('iraclis_test_dataset_hatp26b_parameters.txt'))

