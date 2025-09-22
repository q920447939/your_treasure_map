flutter 启动报错

`Module was compiled with an incompatible version of Kotlin. The binary version of its metadata is 1.9.0, expected version is 1.7.1.`



1  android/build.gradle修改

```
buildscript {
    ext.kotlin_version = '1.9.24'
    repositories {
        google()
        mavenCentral()
    }
    dependencies {
        classpath 'com.android.tools.build:gradle:7.3.1'
        classpath "org.jetbrains.kotlin:kotlin-gradle-plugin:$kotlin_version"
    }
    }
    allprojects {
        repositories {
        google()
        mavenCentral()
    }
}
```



2 android/settings.gradle修改

```
plugins {
	id "dev.flutter.flutter-plugin-loader" version "1.0.0"
	id "com.android.application" version "7.3.0" apply false
	id "org.jetbrains.kotlin.android" version "1.9.24" apply false // here I updated the version to 1.9.24 latest version as of now
}
```

