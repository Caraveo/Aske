class SpringModel:
    """Model for generating Spring Boot project structure and files"""

    @staticmethod
    def get_pom_xml(name):
        """Generate pom.xml content"""
        return f'''<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    
    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>3.2.0</version>
    </parent>

    <groupId>com.example</groupId>
    <artifactId>{name}</artifactId>
    <version>0.0.1-SNAPSHOT</version>
    <name>{name}</name>
    <description>Spring Boot project created with ASKE</description>

    <properties>
        <java.version>17</java.version>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
        <project.reporting.outputEncoding>UTF-8</project.reporting.outputEncoding>
    </properties>

    <dependencies>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-actuator</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-validation</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-devtools</artifactId>
            <scope>runtime</scope>
            <optional>true</optional>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-test</artifactId>
            <scope>test</scope>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
            </plugin>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-checkstyle-plugin</artifactId>
                <version>3.3.1</version>
                <configuration>
                    <configLocation>google_checks.xml</configLocation>
                </configuration>
            </plugin>
        </plugins>
    </build>
</project>
'''

    @staticmethod
    def get_application_class(name):
        """Generate main Application class"""
        package_name = name.replace("-", "").lower()
        return f'''package com.example.{package_name};

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class Application {{
    public static void main(String[] args) {{
        SpringApplication.run(Application.class, args);
    }}
}}
'''

    @staticmethod
    def get_hello_controller(name):
        """Generate HelloController class"""
        package_name = name.replace("-", "").lower()
        return f'''package com.example.{package_name}.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class HelloController {{
    @GetMapping(value = {{"/", "/hello"}})
    public String hello() {{
        return "Hello, World!";
    }}
}}
'''

    @staticmethod
    def get_application_test(name):
        """Generate Application test class"""
        package_name = name.replace("-", "").lower()
        return f'''package com.example.{package_name};

import org.junit.jupiter.api.Test;
import org.springframework.boot.test.context.SpringBootTest;

@SpringBootTest
class ApplicationTests {{
    @Test
    void contextLoads() {{
    }}
}}
'''

    @staticmethod
    def get_hello_controller_test(name):
        """Generate HelloController test class"""
        package_name = name.replace("-", "").lower()
        return f'''package com.example.{package_name}.controller;

import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.AutoConfigureMockMvc;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.web.servlet.MockMvc;

import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.get;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.content;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.status;

@SpringBootTest
@AutoConfigureMockMvc
class HelloControllerTest {{
    @Autowired
    private MockMvc mockMvc;

    @Test
    void shouldReturnHelloWorld() throws Exception {{
        mockMvc.perform(get("/hello"))
            .andExpect(status().isOk())
            .andExpect(content().string("Hello, World!"));
    }}
}}
'''

    @staticmethod
    def get_application_properties():
        """Generate application.properties"""
        return '''# Server Configuration
server.port=8080

# Actuator Configuration
management.endpoints.web.exposure.include=health,info,metrics

# Error Handling
server.error.whitelabel.enabled=false
server.error.include-message=always
server.error.include-binding-errors=always
server.error.include-stacktrace=never

# Logging Configuration
logging.level.root=INFO
logging.level.com.example=DEBUG
'''

    @staticmethod
    def get_java_gitignore():
        """Get standard Java .gitignore content"""
        return '''# Compiled class files
*.class

# Log files
*.log

# BlueJ files
*.ctxt

# Mobile Tools for Java (J2ME)
.mtj.tmp/

# Package Files
*.jar
*.war
*.nar
*.ear
*.zip
*.tar.gz
*.rar

# virtual machine crash logs
hs_err_pid*
replay_pid*

# Maven
target/
pom.xml.tag
pom.xml.releaseBackup
pom.xml.versionsBackup
pom.xml.next
release.properties
dependency-reduced-pom.xml
buildNumber.properties
.mvn/timing.properties
.mvn/wrapper/maven-wrapper.jar

# Gradle
.gradle/
build/

# IntelliJ IDEA
.idea/
*.iws
*.iml
*.ipr

# Eclipse
.settings/
.classpath
.project
.factorypath

# VS Code
.vscode/

# Mac
.DS_Store

# Spring Boot
*.pid
*.port
'''

    @staticmethod
    def get_readme(name):
        """Generate README.md content"""
        return f'''# {name}

A Spring Boot application created with ASKE.

## Requirements

- Java 17+
- Maven 3.8+
- Spring Boot 3.2+

## Setup

1. Ensure Java is installed:
```bash
# Check Java version
java -version

# Install Java if needed
brew install openjdk@17
```

2. Build the project:
```bash
./mvnw clean install
```

3. Run the application:
```bash
./mvnw spring-boot:run
```

4. Test the endpoint:
```bash
curl http://localhost:8080/hello
```

## Development

- The main application class is in `src/main/java/com/example/{name.lower()}/Application.java`
- Controllers are in the `controller` package
- Tests are in `src/test/java`
- Configuration is in `src/main/resources/application.properties`

## Testing

Run tests with:
```bash
./mvnw test
```

## Code Quality

Run checkstyle:
```bash
./mvnw checkstyle:check
```
'''

    @staticmethod
    def get_error_controller(name):
        """Generate custom error controller"""
        package_name = name.replace("-", "").lower()
        return f'''package com.example.{package_name}.controller;

import org.springframework.boot.web.servlet.error.ErrorController;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class CustomErrorController implements ErrorController {{
    @RequestMapping("/error")
    public String handleError() {{
        return "Error occurred! Please try /hello endpoint.";
    }}
}}
''' 