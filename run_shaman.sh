#!/bin/bash

export ALEMBIC_CONFIG="alembic.ini"
export PECAN_CONFIG="config/dev.py"

pecan serve config/run.py
