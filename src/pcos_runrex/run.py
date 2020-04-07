from runrex.main import process
from runrex.schema import validate_config

from pcos_runrex.algo.hyperandrogenism import get_hyperandrogenism
from pcos_runrex.algo.menarche import get_menarche
from pcos_runrex.algo.pcom import get_pcom


def main(config_file):
    conf = validate_config(config_file)
    algorithms = {
        'hyperandrogenism': get_hyperandrogenism,
        'pcom': get_pcom,
        'menarche': get_menarche,
    }
    process(**conf, algorithms=algorithms)


if __name__ == '__main__':
    import sys

    try:
        main(sys.argv[1])
    except IndexError:
        raise AttributeError('Missing configuration file: Usage: run.py file.(json|yaml|py)')
