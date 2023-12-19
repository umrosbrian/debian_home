#!/bin/bash

find debian_home -mindepth 1 -maxdepth 1 -exec mv '{}' . \;
rmdir debian_home
