## Cluster-monitoring
Use Prometheus to monitor a containerized application running on Minikube within VMware Workstation
  a. Track HTTP requests and automate alerting when HTTP errors are detected
  b. Monitor container restarts within the pods, and automate alerting
  
### Setting up the environment
1. Install Python3
2. Install Docker
3. Install Git
4. Install Minikube
5. Install helm
6. Install Prometheus Operator onto Minilkube
7. Install ArgoCD onto Minikube
8. Clone this repo 

### To build application image 
9. docker build -t myflask .

### Load the image from docker registry to minikube
10. minikube image load myflask 

### Deploy Service Monitor to monitor the application service
11. kubectl create -f myflask-servicemonitor.yml 

### Deploy Alerting rules
12. kubectl create -f myflask-alertrule.yml

### Create application deployment and service
13 kubectl create -f deploy-myflask.yml

### To monitor if your pods are running
14a ./gp.sh
or
14b. kubectl get po -n default


### To run the application on your machine
 python3 myFlask.py
Follow the instructions to install modules as per required


### To access the UI for Prometheus, Grafana, AlertManager, ArgoCD and MyFlask Application , you need to port forward from your local machine to Kubernetes services
E.g. kubectl port-forward service/argocd-server -n monitoring  18080:80 & 



![image](https://github.com/user-attachments/assets/1bed5ad9-437c-4b3d-b48e-6a9f0003318b)


