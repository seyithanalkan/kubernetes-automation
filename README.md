
# Kubernetes Automation Project - Pulumi - Helm - ArgoCD - AWS EKS

**This project uses Github Actions for Continuous Integration (CI). The CI pipeline includes the following tasks:**

- Running pulumi up to create a Kubernetes cluster on AWS EKS.

- Packaging a Helm chart for a React application.

- Pushing the packaged Helm chart to a private ECR repository.

- Building a Docker image for the React application and pushing it to ECR.

- Deploying the ArgoCD server as a Helm chart to the EKS cluster using Pulumi.

- Deploying an ArgoCD job using Pulumi, which deploys the React application Helm chart from the private ECR repository.

**The project sets up a complete CI/CD pipeline for deploying a React application to a Kubernetes cluster on AWS EKS, managed by ArgoCD.**



## Requirements:

- AWS Secret ID and Secret Key: In order to access AWS resources, you will need to provide the AWS Secret ID and Secret Key for authentication purposes.

- Pulumi Account: To use Pulumi, you need to register for an organizational account. Pulumi offers a 14-day trial period, during which you can test the product without the need for a credit card.

- Pulumi Stack Name: A Pulumi stack represents a set of infrastructure resources. You need to provide a stack name, which will be used to identify and manage the resources created by Pulumi in your organizational account.

- Pulumi Token: To access your Pulumi organizational account and manage the resources created by Pulumi, you need to create a Pulumi Token.

**By fulfilling these requirements, you will be able to run the Github Actions CI pipeline and deploy the React application to a Kubernetes cluster on AWS EKS, managed by ArgoCD.**

## Usage:

- Clone the project repository.

- Create your own repository and add the following secrets:

    **AWS_ACCESS_KEY_ID**  
    **AWS_REGION**  
    **AWS_SECRET_ACCESS_KEY**  
    **PULUMI_ACCESS_TOKEN**  
    **STACK_NAME**  

- Push your repository to Github.

**By following these steps, you will have set up your own repository with the required secrets, allowing you to run the Github Actions CI pipeline and deploy the React application to a Kubernetes cluster on AWS EKS, managed by ArgoCD.**


## Screenshots:

![Secrets](https://drive.google.com/thumbnail?id=1hLPdYy--L7RWFy5oq-iMh8ix3M1wdSp-&sz=w1000)  
![Github-Action](https://drive.google.com/thumbnail?id=1TRAZ5abc19xMf3E_jHSZE7D2_zssSt83&sz=w1000)  
![Kubernetes-Cluster](https://drive.google.com/thumbnail?id=1gTVBp22nSxx8jR05kzMZZuz9-kZ7b3Dz&sz=w1000)  
![React-App](https://drive.google.com/thumbnail?id=1JDVejJiv1yNUVC59E0ISqGzJZqhM0VOC&sz=w1000)  
![ArgoCD-Access](https://drive.google.com/thumbnail?id=1JoymQ6T0h8ypVGfPSxY310fSyqe-0BrZ&sz=w1000)   
![ArgoCD-Login](https://drive.google.com/thumbnail?id=1NHzM9vYxwVCG_PRFCCjHSldqvH-HWHTy&sz=w1000)  
![ArgoCD-Job](https://drive.google.com/thumbnail?id=116au4DrU81IaUYd7qDYsBguoCvFdll1b&sz=w1000)    








