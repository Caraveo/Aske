"""Revel framework model for Go projects"""
from .gin import GinModel

class RevelModel(GinModel):
    """Model for generating Revel framework projects"""

    @staticmethod
    def get_mod_file(name):
        """Generate go.mod content for Revel"""
        return f'''module {name}

go 1.21

require (
    github.com/revel/revel v1.1.0
    github.com/revel/modules v1.1.0
    github.com/joho/godotenv v1.5.1
)
'''

    @staticmethod
    def get_main_file():
        """Generate main.go content for Revel"""
        return '''package app

import (
    "github.com/revel/revel"
)

func init() {
    // Filters is the default set of global filters.
    revel.Filters = []revel.Filter{
        revel.PanicFilter,             // Recover from panics and display error page
        revel.RouterFilter,            // Use the routing table
        revel.FilterConfiguringFilter, // A hook for adding or removing per-Action filters
        revel.ParamsFilter,            // Parse parameters into Controller.Params
        revel.SessionFilter,           // Restore and write the session cookie
        revel.FlashFilter,             // Restore and write the flash cookie
        revel.ValidationFilter,        // Restore and write the validation cookie
        revel.I18nFilter,             // Resolve the requested language
        HeaderFilter,                  // Add some security based headers
        revel.InterceptorFilter,       // Run interceptors around the action
        revel.CompressFilter,          // Compress the result
        revel.ActionInvoker,          // Invoke the action
    }

    // Register startup functions
    revel.OnAppStart(InitDB)
}

// HeaderFilter adds common security headers
var HeaderFilter = func(c *revel.Controller, fc []revel.Filter) {
    c.Response.Out.Header().Add("X-Frame-Options", "SAMEORIGIN")
    c.Response.Out.Header().Add("X-XSS-Protection", "1; mode=block")
    c.Response.Out.Header().Add("X-Content-Type-Options", "nosniff")
    c.Response.Out.Header().Add("Referrer-Policy", "strict-origin-when-cross-origin")

    fc[0](c, fc[1:]) // Execute the next filter stage
}

func InitDB() {
    // Initialize your database connection here
}
'''

    @staticmethod
    def get_controller_example():
        """Generate example controller"""
        return '''package controllers

import "github.com/revel/revel"

type App struct {
    *revel.Controller
}

func (c App) Index() revel.Result {
    return c.Render()
}

func (c App) Health() revel.Result {
    return c.RenderJSON(map[string]string{
        "status": "ok",
    })
}
'''

    @staticmethod
    def get_post_create_instructions():
        """Get Revel-specific post-creation instructions"""
        return '''
🚀 Revel Framework Quick Start:

1. Project Structure:
   - app/: Application code
     - controllers/: Request handlers
     - models/: Data models
     - views/: Templates
   - conf/: Configuration files
   - public/: Static assets
   - tests/: Test files

2. Key Features:
   - Hot reload
   - Built-in validation
   - Templating engine
   - Interceptors
   - Session handling

3. Best Practices:
   - Use proper routing
   - Implement interceptors
   - Handle errors gracefully
   - Write comprehensive tests
   - Use configuration properly

4. Documentation:
   - Revel Manual: https://revel.github.io/manual/index.html
   - API Reference: https://pkg.go.dev/github.com/revel/revel

5. Development Tools:
   - revel run: Development server
   - revel test: Run tests
   - revel package: Build for deployment
''' 