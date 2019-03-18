


# Demo1



## get-from-db

get-from-db function gets data from MongoDB based on request from python notebook and resend it to end user.

Preconditions:
 Python3 installed on machine.
 Open-FaaS has been installed upon kubernetes and already run.
 MongoDB is up.

Steps to start deploy get-from-db:
 Go to directory where get-from-db.yml is lying. 
 Open terminal in it and enter "faas-cli deploy -f get-from-db.yml"

Something goes wrong?
 Check batch-mod, stream-mod and save-to-db readmies. Then go back to get-from-db readme file.



## Jupyter as ui

### Build docker container
docker build . -t jupyter-ui

### Join to kubernetes
kubectl apply -f jupyter.yaml --namespace jupyter

kubectl get pods (check pod name)

kubectl port-forward "pod name" 8888:8888 -n jupyter
