#!/bin/sh

set -e

# build frontend
cd frontend
npm install
npm run test
npm run build

cd ..
mkdir -p server/static
cp -r frontend/build/*  server/static/
