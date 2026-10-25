#!/bin/sh

current_branch=$(git rev-parse --abbrev-ref HEAD)
if [ "$current_branch" != "main" ]; then
  echo "The current branch must be 'main'."
  exit 1
fi

rm -rf dist
uv build
uvx twine upload dist/*
