# Demo1

## Jupyter as ui

### Build docker container
docker build . -t jupyter-ui

### Join to kubernetes
kubectl apply -f jupyter.yaml --namespace jupyter

kubectl get pods (check pod name)

kubectl port-forward "pod name" 8888:8888 -n jupyter
