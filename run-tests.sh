#!/bin/bash
set -e

echo "Running tests in GitLab CI"
pytest -v
