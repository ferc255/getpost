#!/bin/bash
. ../../env/bin/activate
export DJANGO_SETTINGS_MODULE=$(basename $(dirname $(pwd))).settings
export PYTHONPATH="$(pwd)/.."
