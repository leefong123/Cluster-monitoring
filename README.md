### Cluster-monitoring
Use Prometheus to monitor a containerized application running on Minikube within VMware Workstation  

  a. Track HTTP requests and automate alerting when HTTP errors are detected  
  
  b. Monitor container restarts within the pods, and automate alerting  
  
  
#### Setting up the environment
1. Install Python3
2. Install Docker
3. Install Git
4. Install Minikube
5. Install helm
6. Install Prometheus Operator onto Minilkube
7. Install ArgoCD onto Minikube
8. Clone this repo 

#### To build application image 
9. docker build -t myflask .

#### Load the image from docker registry to minikube
10. minikube image load myflask 

#### Deploy Service Monitor to monitor the application service
11. kubectl create -f myflask-servicemonitor.yml 

#### Deploy Alerting rules
12. kubectl create -f myflask-alertrule.yml

#### Create application deployment and service
13 kubectl create -f deploy-myflask.yml

#### To monitor if your pods are running
14a ./gp.sh  

or  

14b. kubectl get po -n default


#### To run the application on your local host
 python3 myFlask.py  
 
Follow the instructions to install modules as per required


#### To access the UI for Prometheus, Grafana, AlertManager, ArgoCD and MyFlask Application , you need to port forward from your local host to Kubernetes services
E.g. kubectl port-forward service/argocd-server -n argocd  10000:80 & 

#### Create the Application in ArgoCD using the following details. It will pull Kubernetes manifests from a GitHub repo and deploy them to Minikube. For detalied instruction on deploying Application, please refer to the ArgoCD documentation

![image](https://github.com/user-attachments/assets/1bed5ad9-437c-4b3d-b48e-6a9f0003318b)


#### After the application is deployed to Minikube, it will show as synchornized

![image](https://github.com/user-attachments/assets/10a4774f-fe42-4aef-916f-45e07b839572)

#### Pods are being created on Minikube

![image](https://github.com/user-attachments/assets/a6a3fe00-b868-4ac1-81f9-3dfb158355e9)

#### To simulate container restarts within the pods, a workaround was added to make the application to restart so that Prometheus can detect the restarts and trigger alerts

![image](https://github.com/user-attachments/assets/9041f5bc-bd9b-4c26-8128-92e68164859d)

#### Prometheus detected that application had restarted and the rule conditions were met, therefore, it fired alerts

![image](https://github.com/user-attachments/assets/8f8e1e51-0fb2-4fd5-a4e1-32aaf207c352)

#### AlertManager received alerts for container restrats

![image](https://github.com/user-attachments/assets/0734e49f-93e4-45cb-8c6d-05c1711d4fc7)



#### To access the Application, you need to port forward to local host to Kubernetes Service

k port-forward service/myflask-service --address 0.0.0.0 18001:8001&

#### The application has not received any HTTP requests

![image](https://github.com/user-attachments/assets/28984e54-d240-4fb5-a68f-148c6b7cc345)

#### To access the application and generate HTTP requests

Open web browser, and key in http://<localhost ip address>:18001/  

Keep reloading the same page to generate HTTP requests  

Key in http://192.168.244.128:18002/error to generate errors

#### 


