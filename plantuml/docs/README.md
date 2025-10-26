# Kubernetes PlantUML Diagrams

This directory contains PlantUML diagrams using the Kubernetes icons from the plantum-stdlib library.

## Files

- `diagram.puml` - Comprehensive Kubernetes architecture diagram showing a full cluster setup
- `simple-example.puml` - Simple microservices example using Kubernetes components

## Available Kubernetes Icons

The k8s library provides icons for the following Kubernetes components:

### Core Components
- `KubernetesMaster` - Master/Control Plane node
- `KubernetesNode` - Worker node
- `KubernetesApi` - API Server
- `KubernetesSched` - Scheduler
- `KubernetesCcm` - Controller Manager
- `KubernetesEtcd` - etcd

### Workloads
- `KubernetesPod` - Pod
- `KubernetesDeploy` - Deployment
- `KubernetesRs` - ReplicaSet
- `KubernetesSts` - StatefulSet
- `KubernetesDs` - DaemonSet
- `KubernetesJob` - Job
- `KubernetesCronjob` - CronJob

### Services & Networking
- `KubernetesSvc` - Service
- `KubernetesIng` - Ingress
- `KubernetesEp` - Endpoints

### Storage
- `KubernetesPv` - Persistent Volume
- `KubernetesPvc` - Persistent Volume Claim
- `KubernetesSc` - Storage Class
- `KubernetesVol` - Volume

### Configuration
- `KubernetesCm` - ConfigMap
- `KubernetesSecret` - Secret

### RBAC
- `KubernetesSa` - Service Account
- `KubernetesRole` - Role
- `KubernetesRb` - RoleBinding
- `KubernetesCrole` - ClusterRole
- `KubernetesCrb` - ClusterRoleBinding

### Policies
- `KubernetesNetpol` - Network Policy
- `KubernetesPsp` - Pod Security Policy
- `KubernetesQuota` - Resource Quota
- `KubernetesLimits` - Limit Range

### Namespaces
- `KubernetesNs` - Namespace

### Autoscaling
- `KubernetesHpa` - Horizontal Pod Autoscaler

### Custom Resources
- `KubernetesCrd` - Custom Resource Definition

## Usage Examples

### Basic Component
```plantuml
!include <k8s/Common>
!include <k8s/Simplified>
!include <k8s/OSS/all>

KubernetesPod(pod, "My Pod", "nginx")
KubernetesSvc(svc, "My Service", "ClusterIP")
Rel(svc, pod, "Routes")
```

### Namespace Boundary
```plantuml
Namespace_Boundary(ns, "My Namespace") {
    KubernetesPod(pod, "Pod", "app")
    KubernetesSvc(svc, "Service", "ClusterIP")
}
```

### Cluster Boundary
```plantuml
Cluster_Boundary(cluster, "Kubernetes Cluster") {
    KubernetesNode(node, "Worker Node", "kubelet")
    KubernetesPod(pod, "Pod", "app")
}
```

## Required Includes

Always include these at the top of your PlantUML files:

```plantuml
!include <k8s/Common>
!include <k8s/Simplified>
!include <k8s/OSS/all>
```

## Styling

The k8s library provides predefined colors and styling:
- Kubernetes blue color scheme
- Consistent icon styling
- Proper spacing and alignment

## Tips

1. Use `Cluster_Boundary` to group cluster-level components
2. Use `Namespace_Boundary` to group namespace-level components
3. Use `Rel()` for relationships between components
4. Use `Rel_U()` for upward relationships (e.g., Pod to ReplicaSet)
5. Include descriptive labels and technology names for clarity

## Rendering

To render these diagrams, you can use:
- PlantUML online server
- VS Code PlantUML extension
- PlantUML command line tool
- Maven/Gradle PlantUML plugins
