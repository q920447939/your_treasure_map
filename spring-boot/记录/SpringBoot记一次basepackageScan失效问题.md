## SpringBoot记一次basepackageScan失效问题



先交代一下`maven`模块结构

```
父模块
	A 模块 (包路径 com.a.xxx)
	B 模块 (包路径 com.b.xxx)
```



项目原始是使用`@SpringBootApplication(scanBasePackages = {"com.a"})`注解，然后运行的。

这一次增加了一个`B`模块，所以理所应当的修改成为`@SpringBootApplication(scanBasePackages = {"com.a","com.b"})`

结果启动发现`B`模块里面的`bean`没有被扫描进来(这里先忽略`A`模块依赖`B`模块的问题，因为正常的两个模块通过`@Resouce`等依赖，如果没找到的话，那么启动会失败)

一开始尝试在网上找，但是没找到具体的原因。

由于又想着自己看看`@SpringBootApplication`的源码，看是哪里实现的，

我们知道`@SpringBootApplication.scanBasePackages()` 注解方法是派生`@ComponentScan basePackages`

当在自己的项目按住`ctrl` 点击`@ComponentScan` 类的时，发现没有找到对应实现的地方。



于是只能取翻一下`spring-boot的源码`，在`spring-boot`源码中，没有发现`@ComponentScan` 的实现逻辑

反手一查`@ComponentScan` ，原来所处的包是`spring-context`

于是乎有下载了一下`spring-context`的源码，根据`@ComponentScan`，找到这个类，以及对应的实现

虽然有很多，但是在`org.springframework.context.annotation.ClassPathBeanDefinitionScanner#doScan`方法中，大概的代码逻辑有点相同(`获取包，然后扫描这个包和子包的bean`)

在项目中，在`org.springframework.context.annotation.ClassPathBeanDefinitionScanner#doScan`位置打上断点。



确实就出现了`"com.a","com.b"`,不过`"com.a"` 找到了`bean` ,`"com.b"` **没找到**了`bean` 

又随着代码找到了`org.springframework.context.annotation.ClassPathScanningCandidateComponentProvider#findCandidateComponents` -> `org.springframework.context.annotation.ClassPathScanningCandidateComponentProvider#scanCandidateComponents`

看到了实现逻辑，原来是在通过`Resource`的方式加载的  ，拼接出一个路径，大概的结果是`classpath:classes/com/a/xxx`

于是去看了一下`b`模块下面，点开`target`目录下，并没有`classpath:classes/com/b/xxx`。

所以扫描不到是正常的

在重新尝试`build`、`maven package` 、`IDEA restart 清理 缓存后`，终于生成了`classpath:classes/com/b/xxx`



### 总结

1.当未扫描到时，可以看下`org.springframework.context.annotation.ClassPathBeanDefinitionScanner#doScan`，查看是否扫描到了对应的包

2.看下`target`目录下，生成了`classpath:classes/com/xxx` 文件(`.class`)没有