"""Buffalo framework model for Go projects"""
from .gin import GinModel

class BuffaloModel(GinModel):
    """Model for generating Buffalo framework projects"""

    @staticmethod
    def get_mod_file(name):
        """Generate go.mod content for Buffalo"""
        return f'''module {name}

go 1.21

require (
    github.com/gobuffalo/buffalo v1.1.0
    github.com/gobuffalo/envy v1.10.2
    github.com/gobuffalo/mw-csrf v1.0.2
    github.com/gobuffalo/mw-forcessl v1.0.2
    github.com/gobuffalo/mw-paramlogger v1.0.2
    github.com/gobuffalo/pop/v6 v6.1.1
    github.com/joho/godotenv v1.5.1
)
'''

    @staticmethod
    def get_main_file():
        """Generate main.go content for Buffalo"""
        return '''package main

import (
    "log"

    "github.com/gobuffalo/buffalo"
    "github.com/gobuffalo/buffalo/render"
    "github.com/gobuffalo/envy"
    "github.com/gobuffalo/mw-csrf"
    "github.com/gobuffalo/mw-forcessl"
    "github.com/gobuffalo/mw-paramlogger"
)

var app *buffalo.App
var r *render.Engine

func main() {
    app = buffalo.New(buffalo.Options{
        Env:         envy.Get("GO_ENV", "development"),
        SessionName: "_app_session",
    })

    // Middleware
    app.Use(forceSSL())
    app.Use(paramlogger.ParameterLogger)
    app.Use(csrf.New)

    // Routes
    app.GET("/", HomeHandler)
    app.GET("/api/health", HealthCheck)

    // Start the server
    log.Fatal(app.Serve())
}

func HomeHandler(c buffalo.Context) error {
    return c.Render(200, r.JSON(map[string]string{
        "message": "Welcome to Buffalo!",
    }))
}

func HealthCheck(c buffalo.Context) error {
    return c.Render(200, r.JSON(map[string]string{
        "status": "ok",
    }))
}

func forceSSL() buffalo.MiddlewareFunc {
    return forcessl.Middleware(secure.Options{
        SSLRedirect:     envy.Get("SSL_REDIRECT", "false") == "true",
        SSLProxyHeaders: map[string]string{"X-Forwarded-Proto": "https"},
    })
}
'''

    @staticmethod
    def get_post_create_instructions():
        """Get Buffalo-specific post-creation instructions"""
        return '''
🚀 Buffalo Framework Quick Start:

1. Project Structure:
   - actions/: HTTP handlers and business logic
   - models/: Database models
   - templates/: View templates
   - migrations/: Database migrations
   - assets/: Static files
   - grifts/: Task scripts

2. Key Features:
   - Full-stack web development
   - Hot reloading
   - Asset pipeline
   - Database integration
   - Task runners

3. Best Practices:
   - Follow MVC pattern
   - Use Buffalo generators
   - Write migrations for DB changes
   - Implement proper error handling

4. Documentation:
   - Buffalo Guide: https://gobuffalo.io/documentation
   - API Reference: https://pkg.go.dev/github.com/gobuffalo/buffalo

5. Development Tools:
   - buffalo dev: Live reload
   - buffalo task: Task runner
   - buffalo generate: Code generators
   - buffalo pop: Database tools
''' 