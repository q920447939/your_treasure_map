## SpringBoot web记一次标记了@RestController和@RequestMapping,但是提示 No static resource 

使用了`@RestController 和 @RequestMapping("/api/xx")`

发送`HTTP`请求，提示`No static resource `

第一感觉是把请求当做静态资源了，但是这个接口标记了`@RestController` ，并不是作为静态资源`controller`使用的





```java
	at org.springframework.web.servlet.resource.ResourceHttpRequestHandler.handleRequest(ResourceHttpRequestHandler.java:585)
	at org.springframework.web.servlet.mvc.HttpRequestHandlerAdapter.handle(HttpRequestHandlerAdapter.java:52)
	at org.springframework.web.servlet.DispatcherServlet.doDispatch(DispatcherServlet.java:1089)
```



根据报错信息 ,在`DispatcherServlet.java:1089` 打上断点。

排查了一段时间发现，原来是`mappedHandler`解析的结果不对。

贴一下这个方法的主要代码

```java
protected void doDispatch(HttpServletRequest request, HttpServletResponse response) throws Exception {
    HttpServletRequest processedRequest = request;
    HandlerExecutionChain mappedHandler = null;
    boolean multipartRequestParsed = false;

    WebAsyncManager asyncManager = WebAsyncUtils.getAsyncManager(request);

    ModelAndView mv = null;
    Exception dispatchException = null;
    processedRequest = checkMultipart(request);
    //1. 获取mappedHandler  主要是在这里获取的mappedHandler有问题
	mappedHandler = getHandler(processedRequest);
    
    ... 省略代码
        
     //2. HandlerAdapter    
    HandlerAdapter ha = getHandlerAdapter(mappedHandler.getHandler());
    
     //3. 执行    
    mv = ha.handle(processedRequest, response, mappedHandler.getHandler());
				
```



当解析成不是想要的那个时，`mappedHandler`是`ResourceHttpRequestHandler [classpath [META-INF/xxx/]]`

实际上需要的是`HandlerExecutionChain with xxx`



观察`getHandler(processedRequest);`的执行逻辑

```java
protected HandlerExecutionChain getHandler(HttpServletRequest request) throws Exception {
		for (HandlerMapping mapping : this.handlerMappings) {
            HandlerExecutionChain handler = mapping.getHandler(request);
            if (handler != null) {
                return handler;
            }
         }
		return null;
	}
```

在这里`this.handlerMappings`是一个集合，如何是正常逻辑，应该是`mapping`应该是`RequestMappingHandlerMapping` (想知道为什么是`RequestMappingHandlerMapping`? 很简单，拿一个正常的`@RestController` `DEBUG`一次就可以了)

```java
public final HandlerExecutionChain getHandler(HttpServletRequest request) throws Exception {
   Object handler = getHandlerInternal(request);
}

protected HandlerMethod getHandlerInternal(HttpServletRequest request) throws Exception {
	String lookupPath = initLookupPath(request);
	HandlerMethod handlerMethod = lookupHandlerMethod(lookupPath, request);
}

protected HandlerMethod lookupHandlerMethod(String lookupPath, HttpServletRequest request) throws Exception {
	List<T> directPathMatches = this.mappingRegistry.getMappingsByDirectPath(lookupPath);
}

public List<T> getMappingsByDirectPath(String urlPath) {
	return this.pathLookup.get(urlPath);
}

private final MultiValueMap<String, T> pathLookup = new LinkedMultiValueMap<>();
```



最终发现在`getMappingsByDirectPath`方法中，通过`this.pathLookup(map数据结构)`获取结果的时候，返回为空

看了一下`this.pathLookup` 发现注册上去的`Requestmapping url` 多了一个前缀，

比如我预想的是访问`api/get`

实际上由于都加了一个统一的前缀，需要加前缀访问，比如前缀是`v2` ，那么最终的结果是 `/v2/api/get`



### 总结

根据`org.springframework.web.servlet.DispatcherServlet#getHandler` 获取到`RequestMappingHandlerMapping`排查