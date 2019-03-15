Function that generate random batch data as IoT devices and send to modification OpenFaaS function.

Getting started:

You should have installed Python3(with installed module requests), Docker, Kubernetes.

Install faas-cli using brew or curl -sL cli.openfaas.com | sudo sh
Clone the code git clone https://github.com/openfaas/faas-netes
Deploy OpenFaaS
openfaas - for OpenFaaS services
openfaas-fn - for functions kubectl apply -f https://raw.githubusercontent.com/openfaas/faas-netes/master/namespaces.yml
and deploy cd faas-netes && 
kubectl apply -f ./yaml

For additional information, please, use manual https://docs.openfaas.com/deployment/kubernetes/

Also port 8080 should be forwarding: kubectl port-forward svc/gateway -n openfaas 8080:8080

Deploy FaaS function

Run from current directory: faas-cli deploy -f batch-mod.yml

Before run generator IoT_batch_generator.py: export FAAS=http://127.0.0.1:8080