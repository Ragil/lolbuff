#!/bin/sh

set -e

# build frontend
cd frontend
npm install
npm run clean
npm run test
npm run build

cd ..
rm -rf server/static
mkdir -p server/static
cp -r frontend/build/*  server/static/
