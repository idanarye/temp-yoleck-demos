import vim
from omnipytent import *
from omnipytent.ext.idan import *


@task
def run(ctx):
    local['python3']['copy-files.py'] & BANG


@task
def go(ctx):
    local['python3']['copy-files.py'] & TERMINAL_PANEL
