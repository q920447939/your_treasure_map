### 背景

`Flutter`项目希望嵌入`Android`原生项目，按照Flutter 官方指导[将 Flutter module 集成到 Android 项目](https://flutter.cn/docs/development/add-to-app/android/project-setup) 步骤创建了demo项目，实际上是创建失败的。

此文档解决 嵌入失败问题

### 先贴一波环境配置信息

**系统**  

Windows10 

**Flutter doctor**

```
PS E:\work_space\Android\flutter\mix\flutter_test\flutter_test_module> flutter doctor
Flutter assets will be downloaded from https://storage.flutter-io.cn. Make sure you trust this source!
Doctor summary (to see all details, run flutter doctor -v):
[√] Flutter (Channel stable, 3.13.4-0.0.pre.34, on Microsoft Windows [版本 10.0.16299.15], locale zh-CN)
[√] Windows Version (Installed version of Windows is version 10 or higher)
[!] Android toolchain - develop for Android devices (Android SDK version 34.0.0)
    X Android license status unknown.
      Run `flutter doctor --android-licenses` to accept the SDK licenses.
      See https://flutter.dev/docs/get-started/install/windows#android-setup for more details.
[√] Chrome - develop for the web
[X] Visual Studio - develop Windows apps
    X Visual Studio not installed; this is necessary to develop Windows apps.
      Download at https://visualstudio.microsoft.com/downloads/.
      Please install the "Desktop development with C++" workload, including all of its default components
[√] Android Studio (version 2022.2)
[√] Connected device (2 available)
[√] Network resources

! Doctor found issues in 2 categories.
```

**Android Studio**(安装的Flutter插件版本和Dart版本都可以看到)

```
Android Studio Flamingo | 2022.2.1 Patch 2
Build #AI-222.4459.24.2221.10121639, built on May 12, 2023
Runtime version: 17.0.6+0-b2043.56-9586694 amd64
VM: OpenJDK 64-Bit Server VM by JetBrains s.r.o.
Windows 10 10.0
GC: G1 Young Generation, G1 Old Generation
Memory: 1280M
Cores: 6
Registry:
    external.system.auto.import.disabled=true
    ide.text.editor.with.preview.show.floating.toolbar=false
    gradle.version.catalogs.dynamic.support=true

Non-Bundled Plugins:
    Dart (222.4582)
    io.flutter (75.1.1)
```

**Android SDK**

33

**Gradle Version**

8.0



项目构造大概如下：

```
flutter_test3  //安卓项目
 -- app
 -- flutter_test3_module   //flutter 模块
    -- .android
      -- include_flutter.groovy
 -- settings.gradle
```



报错信息如下：

```

FAILURE: Build failed with an exception.

* Where:
Script 'E:\flutter\packages\flutter_tools\gradle\src\main\groovy\flutter.groovy' line: 197

* What went wrong:
A problem occurred evaluating script.
> Failed to apply plugin class 'FlutterPlugin'.
   > Build was configured to prefer settings repositories over project repositories but repository 'maven' was added by plugin class 'FlutterPlugin'

* Try:
> Run with --info or --debug option to get more log output.
> Run with --scan to get full insights.

* Exception is:
org.gradle.api.GradleScriptException: A problem occurred evaluating script.
	at org.gradle.groovy.scripts.internal.DefaultScriptRunnerFactory$ScriptRunnerImpl.run(DefaultScriptRunnerFactory.java:93)
	at org.gradle.configuration.DefaultScriptPluginFactory$ScriptPluginImpl.lambda$apply$0(DefaultScriptPluginFactory.java:135)
	at org.gradle.configuration.DefaultScriptTarget.addConfiguration(DefaultScriptTarget.java:74)
	at org.gradle.configuration.DefaultScriptPluginFactory$ScriptPluginImpl.apply(DefaultScriptPluginFactory.java:138)
	at org.gradle.configuration.BuildOperationScriptPlugin$1.run(BuildOperationScriptPlugin.java:65)
	at org.gradle.internal.operations.DefaultBuildOperationRunner$1.execute(DefaultBuildOperationRunner.java:29)
	at org.gradle.internal.operations.DefaultBuildOperationRunner$1.execute(DefaultBuildOperationRunner.java:26)
	at org.gradle.internal.operations.DefaultBuildOperationRunner$2.execute(DefaultBuildOperationRunner.java:66)
	at org.gradle.internal.operations.DefaultBuildOperationRunner$2.execute(DefaultBuildOperationRunner.java:59)
	at org.gradle.internal.operations.DefaultBuildOperationRunner.execute(DefaultBuildOperationRunner.java:157)
	at org.gradle.internal.operations.DefaultBuildOperationRunner.execute(DefaultBuildOperationRunner.java:59)
	at org.gradle.internal.operations.DefaultBuildOperationRunner.run(DefaultBuildOperationRunner.java:47)
	at org.gradle.internal.operations.DefaultBuildOperationExecutor.run(DefaultBuildOperationExecutor.java:68)
	at org.gradle.configuration.BuildOperationScriptPlugin.lambda$apply$0(BuildOperationScriptPlugin.java:62)
	at org.gradle.configuration.internal.DefaultUserCodeApplicationContext.apply(DefaultUserCodeApplicationContext.java:44)
	at org.gradle.configuration.BuildOperationScriptPlugin.apply(BuildOperationScriptPlugin.java:62)
	at org.gradle.api.internal.plugins.DefaultObjectConfigurationAction.applyScript(DefaultObjectConfigurationAction.java:156)
	at org.gradle.api.internal.plugins.DefaultObjectConfigurationAction.access$000(DefaultObjectConfigurationAction.java:43)
	at org.gradle.api.internal.plugins.DefaultObjectConfigurationAction$1.run(DefaultObjectConfigurationAction.java:76)
	at org.gradle.api.internal.plugins.DefaultObjectConfigurationAction.execute(DefaultObjectConfigurationAction.java:190)
	at org.gradle.groovy.scripts.DefaultScript.apply(DefaultScript.java:133)
	at org.gradle.api.Script$apply.callCurrent(Unknown Source)
	at flutter_4duys3hzpflkf919qaf9y7nw1.run(E:\flutter\packages\flutter_tools\gradle\flutter.gradle:9)
	at org.gradle.groovy.scripts.internal.DefaultScriptRunnerFactory$ScriptRunnerImpl.run(DefaultScriptRunnerFactory.java:91)
	at org.gradle.configuration.DefaultScriptPluginFactory$ScriptPluginImpl.lambda$apply$0(DefaultScriptPluginFactory.java:135)
	at org.gradle.configuration.DefaultScriptTarget.addConfiguration(DefaultScriptTarget.java:74)
	at org.gradle.configuration.DefaultScriptPluginFactory$ScriptPluginImpl.apply(DefaultScriptPluginFactory.java:138)
	at org.gradle.configuration.BuildOperationScriptPlugin$1.run(BuildOperationScriptPlugin.java:65)
	at org.gradle.internal.operations.DefaultBuildOperationRunner$1.execute(DefaultBuildOperationRunner.java:29)
	at org.gradle.internal.operations.DefaultBuildOperationRunner$1.execute(DefaultBuildOperationRunner.java:26)
	at org.gradle.internal.operations.DefaultBuildOperationRunner$2.execute(DefaultBuildOperationRunner.java:66)
	at org.gradle.internal.operations.DefaultBuildOperationRunner$2.execute(DefaultBuildOperationRunner.java:59)
	at org.gradle.internal.operations.DefaultBuildOperationRunner.execute(DefaultBuildOperationRunner.java:157)
	at org.gradle.internal.operations.DefaultBuildOperationRunner.execute(DefaultBuildOperationRunner.java:59)
	at org.gradle.internal.operations.DefaultBuildOperationRunner.run(DefaultBuildOperationRunner.java:47)
	at org.gradle.internal.operations.DefaultBuildOperationExecutor.run(DefaultBuildOperationExecutor.java:68)
	at org.gradle.configuration.BuildOperationScriptPlugin.lambda$apply$0(BuildOperationScriptPlugin.java:62)
	at org.gradle.configuration.internal.DefaultUserCodeApplicationContext.apply(DefaultUserCodeApplicationContext.java:44)
	at org.gradle.configuration.BuildOperationScriptPlugin.apply(BuildOperationScriptPlugin.java:62)
	at org.gradle.api.internal.plugins.DefaultObjectConfigurationAction.applyScript(DefaultObjectConfigurationAction.java:156)
	at org.gradle.api.internal.plugins.DefaultObjectConfigurationAction.access$000(DefaultObjectConfigurationAction.java:43)
	at org.gradle.api.internal.plugins.DefaultObjectConfigurationAction$1.run(DefaultObjectConfigurationAction.java:76)
	at org.gradle.api.internal.plugins.DefaultObjectConfigurationAction.execute(DefaultObjectConfigurationAction.java:190)
	at org.gradle.api.internal.project.AbstractPluginAware.apply(AbstractPluginAware.java:49)
	at org.gradle.api.internal.project.ProjectScript.apply(ProjectScript.java:37)
	at org.gradle.api.Script$apply.callCurrent(Unknown Source)
	at build_927juh6hmyh7sc5ilchg7av4j.run(E:\work_space\Android\flutter\mix\flutter_test\flutter_test_module\.android\Flutter\build.gradle:27)
	at org.gradle.groovy.scripts.internal.DefaultScriptRunnerFactory$ScriptRunnerImpl.run(DefaultScriptRunnerFactory.java:91)
	at org.gradle.configuration.DefaultScriptPluginFactory$ScriptPluginImpl.lambda$apply$0(DefaultScriptPluginFactory.java:135)
	at org.gradle.configuration.ProjectScriptTarget.addConfiguration(ProjectScriptTarget.java:79)
	at org.gradle.configuration.DefaultScriptPluginFactory$ScriptPluginImpl.apply(DefaultScriptPluginFactory.java:138)
	at org.gradle.configuration.BuildOperationScriptPlugin$1.run(BuildOperationScriptPlugin.java:65)
	at org.gradle.internal.operations.DefaultBuildOperationRunner$1.execute(DefaultBuildOperationRunner.java:29)
	at org.gradle.internal.operations.DefaultBuildOperationRunner$1.execute(DefaultBuildOperationRunner.java:26)
	at org.gradle.internal.operations.DefaultBuildOperationRunner$2.execute(DefaultBuildOperationRunner.java:66)
	at org.gradle.internal.operations.DefaultBuildOperationRunner$2.execute(DefaultBuildOperationRunner.java:59)
	at org.gradle.internal.operations.DefaultBuildOperationRunner.execute(DefaultBuildOperationRunner.java:157)
	at org.gradle.internal.operations.DefaultBuildOperationRunner.execute(DefaultBuildOperationRunner.java:59)
	at org.gradle.internal.operations.DefaultBuildOperationRunner.run(DefaultBuildOperationRunner.java:47)
	at org.gradle.internal.operations.DefaultBuildOperationExecutor.run(DefaultBuildOperationExecutor.java:68)
	at org.gradle.configuration.BuildOperationScriptPlugin.lambda$apply$0(BuildOperationScriptPlugin.java:62)
	at org.gradle.configuration.internal.DefaultUserCodeApplicationContext.apply(DefaultUserCodeApplicationContext.java:44)
	at org.gradle.configuration.BuildOperationScriptPlugin.apply(BuildOperationScriptPlugin.java:62)
	at org.gradle.api.internal.project.DefaultProjectStateRegistry$ProjectStateImpl.lambda$applyToMutableState$0(DefaultProjectStateRegistry.java:388)
	at org.gradle.api.internal.project.DefaultProjectStateRegistry$ProjectStateImpl.fromMutableState(DefaultProjectStateRegistry.java:406)
	at org.gradle.api.internal.project.DefaultProjectStateRegistry$ProjectStateImpl.applyToMutableState(DefaultProjectStateRegistry.java:387)
	at org.gradle.configuration.project.BuildScriptProcessor.execute(BuildScriptProcessor.java:42)
	at org.gradle.configuration.project.BuildScriptProcessor.execute(BuildScriptProcessor.java:26)
	at org.gradle.configuration.project.ConfigureActionsProjectEvaluator.evaluate(ConfigureActionsProjectEvaluator.java:35)
	at org.gradle.configuration.project.LifecycleProjectEvaluator$EvaluateProject.lambda$run$0(LifecycleProjectEvaluator.java:109)
	at org.gradle.api.internal.project.DefaultProjectStateRegistry$ProjectStateImpl.lambda$applyToMutableState$0(DefaultProjectStateRegistry.java:388)
	at org.gradle.api.internal.project.DefaultProjectStateRegistry$ProjectStateImpl.fromMutableState(DefaultProjectStateRegistry.java:406)
	at org.gradle.api.internal.project.DefaultProjectStateRegistry$ProjectStateImpl.applyToMutableState(DefaultProjectStateRegistry.java:387)
	at org.gradle.configuration.project.LifecycleProjectEvaluator$EvaluateProject.run(LifecycleProjectEvaluator.java:100)
	at org.gradle.internal.operations.DefaultBuildOperationRunner$1.execute(DefaultBuildOperationRunner.java:29)
	at org.gradle.internal.operations.DefaultBuildOperationRunner$1.execute(DefaultBuildOperationRunner.java:26)
	at org.gradle.internal.operations.DefaultBuildOperationRunner$2.execute(DefaultBuildOperationRunner.java:66)
	at org.gradle.internal.operations.DefaultBuildOperationRunner$2.execute(DefaultBuildOperationRunner.java:59)
	at org.gradle.internal.operations.DefaultBuildOperationRunner.execute(DefaultBuildOperationRunner.java:157)
	at org.gradle.internal.operations.DefaultBuildOperationRunner.execute(DefaultBuildOperationRunner.java:59)
	at org.gradle.internal.operations.DefaultBuildOperationRunner.run(DefaultBuildOperationRunner.java:47)
	at org.gradle.internal.operations.DefaultBuildOperationExecutor.run(DefaultBuildOperationExecutor.java:68)
	at org.gradle.configuration.project.LifecycleProjectEvaluator.evaluate(LifecycleProjectEvaluator.java:72)
	at org.gradle.api.internal.project.DefaultProject.evaluate(DefaultProject.java:792)
	at org.gradle.api.internal.project.DefaultProject.evaluate(DefaultProject.java:156)
	at org.gradle.api.internal.project.ProjectLifecycleController.lambda$ensureSelfConfigured$2(ProjectLifecycleController.java:84)
	at org.gradle.internal.model.StateTransitionController.lambda$doTransition$13(StateTransitionController.java:247)
	at org.gradle.internal.model.StateTransitionController.doTransition(StateTransitionController.java:258)
	at org.gradle.internal.model.StateTransitionController.doTransition(StateTransitionController.java:246)
	at 
* Get more help at https://help.gradle.org

CONFIGURE FAILED in 384ms

```



### 修复

1.确保`Andrio`、`Flutter`项目能够**单独**正常运行、确保**网络正常**、确保新建的`flutter`项目类型是`module`而不是`application`

2.调整`flutter_test3`项目根目录下的`settings.gradle`文件

```gr
注释
//dependencyResolutionManagement {
 //   repositoriesMode.set(RepositoriesMode.FAIL_ON_PROJECT_REPOS)
    // repositories {
    // google()
    // mavenCentral()
    // }
//}


//在最后加入如下配置
setBinding(new Binding([gradle: this]))                                // new
def file = new File(                                                     // new
        settingsDir.parentFile,                                              // new
        "flutter_test3/flutter_test3_module/.android/include_flutter.groovy"                         // new ，替换自己实际的路径
)
evaluate(file)
```



此时点击Android Studio 右上角的 `Try Sync` ，虽然不会报错，但是会出现警告，实际上在`Flutter`的依赖还没有被下载下来

![flutter依赖未下载](https://s2.loli.net/2023/10/18/oscqZYPLdizTk5p.png)

3.调整`flutter_test3_module/.android/build.gradle`配置，把右边的红色标记处移除

![调整flutter build.gradle配置](https://s2.loli.net/2023/10/18/P2nENwyi7hAgxJC.png)

调整后的配置如下：

```
// Generated file. Do not edit.

buildscript {
    ext.kotlin_version = '1.7.10'

    dependencies {
        classpath 'com.android.tools.build:gradle:7.3.0'
        classpath "org.jetbrains.kotlin:kotlin-gradle-plugin:$kotlin_version"
    }
}

apply plugin: 'com.android.library'
apply plugin: 'kotlin-android'

android {
    // Conditional for compatibility with AGP <4.2.
    if (project.android.hasProperty("namespace")) {
        namespace 'com.example.flutter_test3_module'
    }

    compileSdkVersion 33
    defaultConfig {
        minSdkVersion 19
    }
}

dependencies {
    implementation "org.jetbrains.kotlin:kotlin-stdlib-jdk7:$kotlin_version"
}

```



4.调整项目跟目录下的`build.gradle`文件，增加内容

```
// Top-level build file where you can add configuration options common to all sub-projects/modules.
plugins {
    id 'com.android.application' version '8.0.2' apply false
    id 'com.android.library' version '8.0.2' apply false
    id 'org.jetbrains.kotlin.android' version '1.7.20' apply false
}
//增加部分开始
allprojects {
    repositories {
        google()
        jcenter()
    }
}
//增加部分结束
```

5.再次点击Android Studio 右上角的 `Try Sync`，发现已经没有警告了

6.此时我们还需要把`Flutter module`在父工程引入一下，调整`flutter_test3/app/build.gradle`，增加绿色标记配置

![引入flutter配置](https://s2.loli.net/2023/10/18/o34F8tcrZUACspw.png)

7.在`com.example.flutter_test3.MainActivity`验证引入的`flutter`模块

![引入flutter模块成功.png](https://s2.loli.net/2023/10/18/DOakfwnpFxrtPoe.png)



### 参考

1. [将 Flutter module 集成到 Android 项目 - Flutter 中文文档 - Flutter 中文开发者网站 - Flutter](https://flutter.cn/docs/development/add-to-app/android/project-setup)
2. [Android导入Flutter Module报错Failed to apply plugin class ‘FlutterPlugin’._failed to apply plugin class 'flutterplugin'.-CSDN博客](https://blog.csdn.net/bi3220628/article/details/121649776)
3. [Failed to apply plugin class 'FlutterPlugin'. · Issue #136640 · flutter/flutter (github.com)](https://github.com/flutter/flutter/issues/136640)
4. [Gradle buildscripts of Flutter plugins interfere with `app` project · Issue #130616 · flutter/flutter (github.com)](https://github.com/flutter/flutter/issues/130616)
5. [android - Build was configured to prefer settings repositories over project repositories but repository 'maven' was added by build file 'build.gradle' - Stack Overflow](https://stackoverflow.com/questions/69163511/build-was-configured-to-prefer-settings-repositories-over-project-repositories-b)