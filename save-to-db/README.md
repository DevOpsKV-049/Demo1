How to deploy mongo on yours prods  
Please finde mongodb-service.yaml and run this comand
kubectl create -f mongodb-service.yaml

If you have some problem with mongoDB you can use this comand
kubectl exec -it "container name" bash
container name you can finde in kubernetes or run this comands
kubectl get pods | grep mongo
