# java and docker

## spring boot

### build

#### spring boot + docker

[boot-docker](./Dockerfile-spring-boot)

```shell
docker build -t liubin/spring-boot .
```

#### spring boot + docker fast

[boot-docker-fast](./Dockerfile-spring-boot-fast)
> 我们先解包,它已经分为外部依赖和内部依赖。现在有三层，所有应用程序资源都在后面两层。如果应用程序依赖没有改变，第一层（from BOOT-INF/lib）不需要改变，所以构建更快，并且容器在运行时的启动也更快，只要基础层已经被缓存。

```shell
mkdir target/dependency
cd target/dependency 
jar -xf ../*.jar
docker build -t liubin/spring-boot .
```

#### spring boot(>=2.3.0) + docker fast more

[boot-docker-fast-more](./Dockerfile-spring-boot-fast-more)
> 从 Spring Boot 2.3.0 开始，使用 Spring Boot Maven 或 Gradle 插件构建的 JAR 文件在 JAR 文件中包含层信息。该层信息根据应用程序构建之间更改的可能性来分离应用程序的各个部分。这可以用来使 Docker 镜像层更加高效。

```shell
mkdir target/extracted
java -Djarmode=layertools -jar target/*.jar extract --destination target/extracted
docker build -t liubin/spring-boot .
```

#### Multi-Stage Build

[Dockerfile-spring-boot-build-run](./Dockerfile-spring-boot-build-run)
> 两阶段构建，第一阶段mvnw clean package，`settings.xml`使用镜像加速构建。第二阶段docker build -t liubin/spring-boot .

#### Multi-Stage Build cache

[Dockerfile-spring-boot-build-run-cache](./Dockerfile-spring-boot-build-run-cache)
> 两阶段构建，第一阶段mvnw clean package，`--mount=type=cache,target=/root/.m2` 缓存已经下载的依赖，加快构建速度。

### run

```shell
docker run --name boot -e JAVA_OPTS="-Xmx100m -Xms100m -XX:+UseG1GC" liubin/spring-boot
```