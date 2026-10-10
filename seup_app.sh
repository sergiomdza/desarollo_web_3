#!/bin/bash

kind load docker-image mongo:7.0 --name kind
kind load docker-image backend_productos:latest --name kind 

kubectl apply -f ./mongo_statefulset.yaml
kubectl apply -f ./backend_deployment.yaml