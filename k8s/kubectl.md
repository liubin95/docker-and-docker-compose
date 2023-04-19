# kubectl

## kubectl get

```shell
# 查看集群中的节点
kubectl get nodes
# 查看集群中的所有资源
kubectl get all
# 查看集群中的所有资源，包括未初始化的资源
kubectl get all --show-all
# 查看集群中的所有资源，包括未初始化的资源，以yaml格式输出
kubectl get all --show-all -o yaml
kubectl get pods --all-namespaces
kubectl get pods -o wide -n kube-flannel

```

## kubectl logs

```shell
# 查看pod的日志
kubectl logs -f pod-name -n kube-flannel
```

## kubectl run

```shell
kubectl run busybox2 --image=busybox --restart=Never -- sleep 3600

```

## kubectl describe

```shell
kubectl describe pod -n kube-system coredns-5d78c9869d-9dw9h

```
