#!/usr/bin/env sh


_CMD_PYTHON3=$( which python3 )

if [ -z "$_CMD_PYTHON3" ] ; then
    printf '!!! %s\n' 'Python 3 not found' 1>&2
fi


_CMD_PIP3=$( which pip3 )

if [ -z "$_CMD_PIP3" ] ; then
    printf '!!! %s\n' 'pip not found' 1>&2
fi


_CMD_MANAGE_PY='manage.py'

if [ ! -f "$_CMD_MANAGE_PY" ] ; then
    printf '!!! %s\n' 'manage.py not found' 1>&2
fi


"$_CMD_PIP3" install --user --requirement requirements.txt || \
    exit "$?"

"$_CMD_PYTHON3" manage.py makemigrations || \
    exit "$?"

"$_CMD_PYTHON3" manage.py migrate || \
    exit "$?"

"$_CMD_PYTHON3" manage.py runserver || \
    exit "$?"

