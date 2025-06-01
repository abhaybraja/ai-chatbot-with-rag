#!/bin/bash

docker compose build
docker compose up -d
npm run dev
