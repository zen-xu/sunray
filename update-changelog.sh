#!/usr/bin/env bash

export GIT_CLIFF_TAG=$CZ_PRE_NEW_VERSION
git cliff -o CHANGELOG.md
