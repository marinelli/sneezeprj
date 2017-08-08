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
    printf '!!! %s\n' "$_CMD_MANAGE_PY not found" 1>&2
fi


if [ ! -f 'requirements.txt' ] ; then
    printf '!!! %s\n' 'requirements.txt not found' 1>&2
else
    "$_CMD_PIP3" list --format freeze > packages.txt

    cat requirements.txt | \
      while read _CUR_DEPENDENCY ; do
	  grep -q -i -- "$_CUR_DEPENDENCY" packages.txt

	  if [ "$?" -ne 0 ] ; then
	      "$_CMD_PIP3" install --user "$_CUR_DEPENDENCY"
	  fi
      done

    test -f packages.txt && rm packages.txt

    "$_CMD_PYTHON3" manage.py makemigrations || \
      exit "$?"

    "$_CMD_PYTHON3" manage.py migrate || \
      exit "$?"

    "$_CMD_PYTHON3" manage.py runserver || \
      exit "$?"
fi

