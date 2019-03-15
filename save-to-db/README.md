How to deploy mongo on yours prods  
Please finde mongodb-service.yaml and run this comand
kubectl create -f mongodb-service.yaml

If you have some problem with mongoDB you can use this comand
kubectl exec -it "container name" bash
container name you can finde in kubernetes or run this comands
kubectl get pods | grep mongo

### secret creation via literal type

kubectl create secret generic secret-api-key \
 --from-literal secret-api-key="your_pass" \
 --namespace openfaas-fn

### in "fync_name.yml" add info:
functions:
  saveall:
    ---
    secrets:
      - secret-api-key

### Rebuild and redeploy function

########
Secret creation for mngodb :


# Create files needed for rest of example.
echo -n '#user_name' > ./username.txt
echo -n '#user_password' > ./password.txt

kubectl create secret generic db-user-pass --from-file=./username.txt --from-file=./password.txt

####
You can check that the secret was created like this:

kubectl get secrets

kubectl describe secrets/db-user-pass
####

###
Add this block in DB yaml

spec:
  containers:
  
    env:
      - name: SECRET_USERNAME
        valueFrom:
          secretKeyRef:
            name: mysecret
            key: username
      - name: SECRET_PASSWORD
        valueFrom:
          secretKeyRef:
            name: mysecret
            key: password
