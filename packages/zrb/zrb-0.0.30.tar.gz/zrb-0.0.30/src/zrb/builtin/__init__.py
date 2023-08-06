from . import base64
from . import env
from . import eval
from . import md5
from . import principle
from . import ubuntu
from . import update
from . import version
from .devtool import devtool_install
from .project import create as project_create
from .project.add.cmd_task import add as cmd_task_add
from .project.add.docker_compose_task import add as docker_compose_task_add

assert base64
assert env
assert eval
assert md5
assert principle
assert ubuntu
assert update
assert version
assert devtool_install
assert project_create
assert cmd_task_add
assert docker_compose_task_add
