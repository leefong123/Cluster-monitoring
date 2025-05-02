### This is a simple project for hands-on practice that explores using Prometheus to monitor a containerized application running on a Kubernetes cluster (Minikube).
a. Track HTTP requests and automate alerting when HTTP errors are detected (Completed on 30 April 2025)
  
b. Monitor container restarts within the pods, and automate alerting (Completed on 30 April 2025)




  
#### Setting up the environment
1. Install Python3
2. Install Docker
3. Install Git
4. Install Minikube
5. Install kubectl
6. Install helm
7. Install Prometheus Operator 
8. Install ArgoCD 

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

#### AlertManager received alerts for container restarts

![image](https://github.com/user-attachments/assets/0734e49f-93e4-45cb-8c6d-05c1711d4fc7)



#### To access the application, you need to port forward to Kubernetes service from local host

k port-forward service/myflask-service 18001:8001&

#### The application has not received any HTTP requests

![image](https://github.com/user-attachments/assets/28984e54-d240-4fb5-a68f-148c6b7cc345)

#### To access the application and generate HTTP requests

Open web browser, and key in http://local-host-ip-address:18001/  

Keep reloading the same page to generate HTTP requests  

Key in http://local-host-ip-address:18001/error to generate errors


![image](https://github.com/user-attachments/assets/c3277383-c923-4b6c-9564-ecf6e650eb08)


#### Prometheus is pending to fire an alert because more than 20 HTTP errors were detected within 5 minutes  

![image](https://github.com/user-attachments/assets/06feb810-7076-4dc9-bd7c-28910f1744af)


![image](https://github.com/user-attachments/assets/755a8028-e8dd-49f6-b84f-bf7bfada82c8)


#### AlertManager received the too many HTTP errors alert
![image](https://github.com/user-attachments/assets/65ac9e9a-61ef-4e3e-b282-afeedd5241d0)




