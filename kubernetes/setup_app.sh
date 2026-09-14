kind load docker-image desarrollo_web_3-backend:latest --name web3
kind load docker-image mongo:latest --name web3

kubectl apply -f ./mongo_statefulset.yaml
kubectl apply -f ./backend_deployment.yaml