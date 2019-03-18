Function that generate random stream data as IoT devices and send to modification OpenFaaS function.



![Example architecture](https://github.com/DevOpsKV-049/Demo1/1.png)

Getting started:

You should have installed Python3(with installed module requests), Docker, Kubernetes.


1. Install faas-cli using brew or curl -sL cli.openfaas.com | sudo sh
2. Clone the code git clone https://github.com/openfaas/faas-netes
3. Deploy OpenFaaS
 - openfaas - for OpenFaaS services
 - openfaas-fn - for functions
kubectl apply -f https://raw.githubusercontent.com/openfaas/faas-netes/master/namespaces.yml

and deploy 
cd faas-netes && \
kubectl apply -f ./yaml

For additional information, please, use manual https://docs.openfaas.com/deployment/kubernetes/

Also port 8080 should be forwarding:  kubectl port-forward svc/gateway -n openfaas 8080:8080

Deploy FaaS function

Run from current directory:
faas-cli deploy -f stream-mod.yml

Before run generator IoT_streaming_generator.py: export FAAS=http://127.0.0.1:8080
