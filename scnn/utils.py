from addict import Dict as ADDict
import argparse
from collections import Counter
import functools
import logging
import os
import sys
from tabulate import tabulate
from termcolor import colored
import time
import torch
from typing import Dict, Optional
import yaml


class _ColorfulFormatter(logging.Formatter):
    def __init__(self, *args, **kwargs):
        self._root_name = kwargs.pop("root_name") + "."
        self._abbrev_name = kwargs.pop("abbrev_name", "")
        if len(self._abbrev_name):
            self._abbrev_name = self._abbrev_name + "."
        super(_ColorfulFormatter, self).__init__(*args, **kwargs)

    def formatMessage(self, record):
        record.name = record.name.replace(self._root_name, self._abbrev_name)
        log = super(_ColorfulFormatter, self).formatMessage(record)
        if record.levelno == logging.WARNING:
            prefix = colored("WARNING", "red", attrs=["blink"])
        elif record.levelno == logging.ERROR or record.levelno == logging.CRITICAL:
            prefix = colored("ERROR", "red", attrs=["blink", "underline"])
        else:
            return log
        return prefix + " " + log


# cache the opened file object, so that different calls to `setup_logger`
# with the same file name can safely write to the same file.
@functools.lru_cache(maxsize=None)
def _cached_log_stream(filename):
    return open(filename, "a")


# so that calling setup_logger multiple times won't add many handlers
@functools.lru_cache()
def setup_logger(
    output=None, *, color=True, name="scnn", abbrev_name='scnn'
):
    """
    Initialize the logger and set its verbosity level to "DEBUG".

    Args:
        output (str): a file name or a directory to save log. If None, will not save log file.
            If ends with ".txt" or ".log", assumed to be a file name.
            Otherwise, logs will be saved to `output/log.txt`.
        name (str): the root module name of this logger
        abbrev_name (str): an abbreviation of the module, to avoid long names in logs.
            Set to "" to not log the root module in logs.
            By default, will abbreviate "zvdetectron" to "zvd" and leave other
            modules unchanged.

    Returns:
        logging.Logger: a logger
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    logger.propagate = False

    if abbrev_name is not None:
        abbrev_name = "scnn" if name == "scnn" else name

    plain_formatter = logging.Formatter(
        "[%(asctime)s] %(name)s %(levelname)s %(lineno)d: %(message)s", datefmt="%m/%d %H:%M:%S"
    )

    # stdout logging
    ch = logging.StreamHandler(stream=sys.stdout)
    ch.setLevel(logging.DEBUG)
    if color:
        formatter = _ColorfulFormatter(
            colored("[%(asctime)s %(name)s %(levelname)s lineno:%(lineno)d]: ", "green") + "%(message)s",
            datefmt="%m/%d %H:%M:%S",
            root_name=name,
            abbrev_name=str(abbrev_name),
        )
    else:
        formatter = plain_formatter
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    # file logging
    if output:
        if output.endswith(".txt") or output.endswith(".log"):
            filename = output
        else:
            filename = os.path.join(output, "log.txt")

        fh = logging.StreamHandler(_cached_log_stream(filename))
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(plain_formatter)
        logger.addHandler(fh)

    return logger


"""
Below are some other convenient logging methods.
They are mainly adopted from
https://github.com/abseil/abseil-py/blob/master/absl/logging/__init__.py
"""

def _find_caller():
    """
    Returns:
        str: module name of the caller
        tuple: a hashable key to be used to identify different callers
    """
    frame = sys._getframe(2)
    while frame:
        code = frame.f_code
        if os.path.join("utils", "logger.") not in code.co_filename:
            mod_name = frame.f_globals["__name__"]
            if mod_name == "__main__":
                mod_name = "zvdetectron"
            return mod_name, (code.co_filename, frame.f_lineno, code.co_name)
        frame = frame.f_back


_LOG_COUNTER = Counter()
_LOG_TIMER = {}


def log_first_n(lvl, msg, n=1, *, name=None, key="caller"):
    """
    Log only for the first n times.

    Args:
        lvl (int): the logging level
        msg (str):
        n (int):
        name (str): name of the logger to use. Will use the caller's module by default.
        key (str or tuple[str]): the string(s) can be one of "caller" or
            "message", which defines how to identify duplicated logs.
            For example, if called with `n=1, key="caller"`, this function
            will only log the first call from the same caller, regardless of
            the message content.
            If called with `n=1, key="message"`, this function will log the
            same content only once, even if they are called from different places.
            If called with `n=1, key=("caller", "message")`, this function
            will not log only if the same caller has logged the same message before.
    """
    if isinstance(key, str):
        key = (key,)
    assert len(key) > 0

    caller_module, caller_key = _find_caller()
    hash_key = ()
    if "caller" in key:
        hash_key = hash_key + caller_key
    if "message" in key:
        hash_key = hash_key + (msg,)

    _LOG_COUNTER[hash_key] += 1
    if _LOG_COUNTER[hash_key] <= n:
        logging.getLogger(name or caller_module).log(lvl, msg)


def log_every_n(lvl, msg, n=1, *, name=None):
    """
    Log once per n times.

    Args:
        lvl (int): the logging level
        msg (str):
        n (int):
        name (str): name of the logger to use. Will use the caller's module by default.
    """
    caller_module, key = _find_caller()
    _LOG_COUNTER[key] += 1
    if n == 1 or _LOG_COUNTER[key] % n == 1:
        logging.getLogger(name or caller_module).log(lvl, msg)


def log_every_n_seconds(lvl, msg, n=1, *, name=None):
    """
    Log no more than once per n seconds.

    Args:
        lvl (int): the logging level
        msg (str):
        n (int):
        name (str): name of the logger to use. Will use the caller's module by default.
    """
    caller_module, key = _find_caller()
    last_logged = _LOG_TIMER.get(key, None)
    current_time = time.time()
    if last_logged is None or current_time - last_logged >= n:
        logging.getLogger(name or caller_module).log(lvl, msg)
        _LOG_TIMER[key] = current_time


def create_small_table(small_dict):
    """
    Create a small table using the keys of small_dict as headers. This is only
    suitable for small dictionaries.

    Args:
        small_dict (dict): a result dictionary of only a few items.

    Returns:
        str: the table as a string.
    """
    keys, values = tuple(zip(*small_dict.items()))
    table = tabulate(
        [values],
        headers=keys,
        tablefmt="pipe",
        floatfmt=".3f",
        stralign="center",
        numalign="center",
    )
    return table


'''
Parse cfg.yaml
'''

def default_argument_parser() -> argparse.Namespace:
    """
    Create a parser with some common arguments used by detectron2 users.

    Args:
        epilog (str): epilog passed to ArgumentParser describing the usage.

    Returns:
        argparse.ArgumentParser:
    """
    info = f"""
Examples:

Run on single machine:
    $ {sys.argv[0]} train.py cfg.yaml
        """
    parser = argparse.ArgumentParser(
        epilog=info,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("cfgfile", type=str, metavar='Config File', help="path to config file")

    return parser


def print_cfg(cfg: Optional[Dict], level: int, out_str: str) -> str:
    '''
    Print config dict in pretty format.
    '''
    for k, v in cfg.items():
        if not isinstance(v, dict):
            out_str += ('  ' * level + str(k) + ': ' + str(v) + '\n')
        else:
            out_str += ('  ' * level + str(k) + ':\n')
            out_str = print_cfg(v, level+1, out_str)
    return out_str


class DictNoDefault(ADDict):
    def __missing__(self, key):
        return None


def get_cfg() -> Dict:
    '''
    Get config from cfg file.

    Args:
        argparse.ArgumentParser: 
    Returns:
        cfg: dict
    '''
    args = default_argument_parser().parse_args()

    assert os.path.exists(args.cfgfile), f'{args.cfgfile} is not exists!'
    with open(args.cfgfile) as fr:
        cfg = DictNoDefault(yaml.safe_load(fr))

    # every time to run get_cfg will make a new output directory if it is exists
    output_dir = cfg.OUTPUT_DIR = cfg.OUTPUT_DIR + '_' + cfg.MODEL.TYPE
    if output_dir is not None:
        assert '' != output_dir
        if not os.path.exists(output_dir):
            os.mkdir(output_dir)

    logger = setup_logger(output_dir)

    # cudnn benchmark has large overhead. It shouldn't be used considering the small size of
    # typical validation set.
    if cfg.EVAL_ONLY:
        cfg.CUDNN_BENCHMARK = False
    if torch.cuda.is_available():
        torch.backends.cudnn.benchmark = cfg.CUDNN_BENCHMARK

    logger.info('Running with full config:\n{}'.format(print_cfg(cfg, 0, '')))

    return cfg