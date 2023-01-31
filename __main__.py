import json
import pulumi, pulumi_aws as aws
from pulumi_aws import s3
import pulumi_awsx as awsx, pulumi_eks as eks
import pulumi_kubernetes as k8s
from pulumi import ResourceOptions
from pulumi_eks import Cluster
import pulumi_kubernetes as kubernetes



#Create VPC

vpc = awsx.ec2.Vpc('seyithan-vpc', number_of_availability_zones=2, nat_gateways=awsx.ec2.NatGatewayConfigurationArgs(strategy=(awsx.ec2.NatGatewayStrategy.SINGLE)))


#Create Security Group

kubernetes_sg = aws.ec2.SecurityGroup('Kubernetes-Sg', description='Allow TLS inbound traffic',
  vpc_id=(vpc.vpc_id),
  ingress=[
 aws.ec2.SecurityGroupIngressArgs(description='allow SSH access from anywhere',
   from_port=22,
   to_port=22,
   protocol='tcp',
   cidr_blocks=[
  '0.0.0.0/0']),
 aws.ec2.SecurityGroupIngressArgs(description='allow HTTP access from anywhere',
   from_port=80,
   to_port=80,
   protocol='tcp',
   cidr_blocks=[
  '0.0.0.0/0'])],
  egress=[
 aws.ec2.SecurityGroupEgressArgs(from_port=0,
   to_port=0,
   protocol='-1',
   cidr_blocks=[
  '0.0.0.0/0'])])

#Create Kubernetes Cluster 

cluster = eks.Cluster(resource_name='seyithan', vpc_id=(vpc.vpc_id),
  public_subnet_ids=(vpc.public_subnet_ids),
  node_associate_public_ip_address=True,
  public_access_cidrs=[
 '0.0.0.0/0'],
  desired_capacity=1,
  min_size=1,
  max_size=2,
  instance_type='t3.large',
  storage_classes={'gp2': eks.StorageClassArgs(type='gp3',
          allow_volume_expansion=True,
          default=True,
          encrypted=True)},
  enabled_cluster_log_types=[
 'api',
 'audit',
 'authenticator'])
alb = aws.lb.LoadBalancer('react-lb',
  security_groups=[
 kubernetes_sg.id],
  subnets=(vpc.public_subnet_ids))
target_group = aws.lb.TargetGroup('react-tg',
  port=80,
  protocol='HTTP',
  target_type='ip',
  vpc_id=(vpc.vpc_id))
listener = aws.lb.Listener('web',
  load_balancer_arn=(alb.arn),
  port=80,
  default_actions=[
 aws.lb.ListenerDefaultActionArgs(type='forward',
   target_group_arn=(target_group.arn))])

pulumi.export("kubeconfig", cluster.kubeconfig)

eks_provider = kubernetes.Provider("eks-provider", kubeconfig=cluster.kubeconfig_json)


# Create the argocd server deployment
helm = kubernetes.helm.v3.Release("helm", chart="https://github.com/argoproj/argo-helm/releases/download/argo-cd-5.17.4/argo-cd-5.17.4.tgz",
   
    opts=pulumi.ResourceOptions(provider=eks_provider)
)

#Service Account Deployment

guestbook1 = k8s.yaml.ConfigFile('guestbook', opts=ResourceOptions(depends_on=[cluster], provider=eks_provider),
    file = 'Argocd/serviceacc.yaml'
)

#Create Helm Chart deployment job in Argocd Server

guestbook2 = k8s.yaml.ConfigGroup('guestbook', opts=ResourceOptions(depends_on=[helm], provider=eks_provider),
    files = ['Argocd/job.yaml', 'Argocd/repo.yaml']
)




pulumi.export('vpcId', vpc.vpc_id)
pulumi.export('publicSubnetIds', vpc.public_subnet_ids)
pulumi.export('privateSubnetIds', vpc.private_subnet_ids)



