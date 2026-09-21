#!/bin/bash

#docker build --no-cache -t desarollo_web_3-backend:latest .

kind load docker-image mongo:7.0 --name web3
kind load docker-image desarollo_web_3-backend:latest --name web3

kubectl apply -f ./mongo_statefulset.yaml
kubectl apply -f ./backend_deployment.yaml