INTRUCCIONES GENERALES:
- MASTER estará reservado para entregas finales
- CADA equipo trabajando en su modulo tendrá su rama siguiendo esta nomenclatura: equipo_modulo 


Al principio del semestre:
- cada persona tendrá su propia rama y se encargará de seguir la clase
- cada rama tendrá nombre_apellido 

-- DESCARGAR IMAGENES --
docker pull mongo:7.0


-- CADA QUE CAMBIEN EL CÓDIGO EN EL BACKEND TIENE QUE CORRER ESTOS DOS: -- 

- CREAR LA IMAGEN EN LOCAL:
docker build -t backend_productos .

- ⁠SUBIRLA A LOS KIND NODES:
kind load docker-image backend_productos:latest --name web3

-- Aplicar nuestro deployment del backend -- 
kubectl apply -f backend_deployment.yaml

-- Aplicar nuestro deployment de mongo -- 
kubectl apply -f mongo_statefulset.yaml

-- SUBIR IMAGENES AL KIND NODE --
kind load docker-image backend_productos:latest --name web3

-- EXPORTAR E IMPORTAR IMAGENES DE MONGO -- 
--- Importar --- 
docker save -o kind-node.tar kindest/node

--- Exportar --- 
docker import kind-node.tar kindest/node

-- COMO SABER SI MI KUBERNTES CLUSTER DE KIND ESTÁ VIVO -- 
kubectl cluster-info --context kind-web3
kubectl get nodes

-- CREAR CLUSTER DE KIND --
kind create cluster --config kind-config.yaml --name web3