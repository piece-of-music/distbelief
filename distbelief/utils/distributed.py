
from enum import Enum
import logging
import os
import torch
import torch.distributed as dist

logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')

_LOGGER = logging.getLogger(__name__)



def init_processes(rank, size, fn, backend='tcp'):
    """ Initialize the distributed environment.
    Server and clients must call this as an entry point.
    """
    os.environ['MASTER_ADDR'] = 'localhost'
    os.environ['MASTER_PORT'] = '29500'
    dist.init_process_group(backend, rank=rank, world_size=size)
    fn()
