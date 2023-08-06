#!/usr/bin/env bash

set -e
set -x

mypy --show-error-codes sql_fixture tests
