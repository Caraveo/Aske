"""Revel framework model for Go projects"""
from .gin import GinModel
import os

class RevelModel(GinModel):
    """Model for generating Revel framework projects"""

    @staticmethod
    def create_project_structure(path):
        """Create the Revel project directory structure"""
        directories = [
            'app',
            'app/controllers',
            'app/models',
            'app/views',
            'conf',
            'public',
            'public/css',
            'public/js',
            'public/images',
            'test',
        ]
        
        for dir in directories:
            os.makedirs(os.path.join(path, dir), exist_ok=True)

    @staticmethod
    def get_mod_file(name):
        """Generate go.mod content for Revel"""
        return f'''module {name}

go 1.21

require (
    github.com/revel/revel v1.1.0
    github.com/revel/cmd v1.1.0
    github.com/revel/modules v1.1.0
    github.com/revel/config v1.1.0
    github.com/joho/godotenv v1.5.1
)
'''

    @staticmethod
    def get_main_file():
        """Generate main.go content for Revel"""
        return '''package main

import (
    "github.com/revel/cmd"
)

func main() {
    cmd.Run("dev")
}
'''

    @staticmethod
    def get_app_controller():
        """Generate app controller content"""
        return '''package controllers

import "github.com/revel/revel"

type App struct {
    *revel.Controller
}

func (c *App) Index() revel.Result {
    return c.RenderJSON(map[string]string{
        "message": "Welcome to Revel",
    })
}

func (c *App) Ping() revel.Result {
    return c.RenderJSON(map[string]string{
        "message": "pong",
    })
}

func (c *App) Health() revel.Result {
    return c.RenderJSON(map[string]string{
        "status": "ok",
    })
}
'''

    @staticmethod
    def get_routes():
        """Generate routes file content"""
        return '''# Routes
# This file defines all application routes (Higher priority routes first)
# ~~~~

module:testrunner

GET     /                       App.Index
GET     /ping                   App.Ping
GET     /api/health            App.Health
'''

    @staticmethod
    def get_app_conf():
        """Generate app.conf content"""
        return '''################################################################################
# Revel configuration file
################################################################################

# Sets the `AppName` variable which can be used in your code as
#   `revel.AppName`.
app.name = myapp

# A secret string which is passed to cryptographically sign the cookie to prevent
# (and detect) user modification.
# Keep this string secret or users will be able to inject arbitrary cookie values
# into your application
app.secret = secret123

# The IP address on which to listen.
http.addr =

# The port on which to listen.
http.port = 8080

# Whether to use SSL or not.
http.ssl = false

# Path to an X509 certificate file, if using SSL.
#http.sslcert =

# Path to an X509 certificate key, if using SSL.
#http.sslkey =

# For any cookies set by Revel (Session,Flash,Error) these properties will set
# the fields of:
# http://golang.org/pkg/net/http/#Cookie
#
# Each cookie set by Revel is prefixed with this string.
cookie.prefix = REVEL

# A secure cookie has the secure attribute enabled and is only used via HTTPS,
# ensuring that the cookie is always encrypted when transmitting from client to
# server.
cookie.secure = false

# Limit cookie access to a given domain
#cookie.domain =

# Define when your session cookie expires. Possible values:
# "720h"
#   A time duration (http://golang.org/pkg/time/#ParseDuration) after which
#   the cookie expires and the session is invalid.
# "session"
#   Sets a session cookie which invalidates the session when the user close
#   the browser.
session.expires = 720h

# The date format used by Revel. Possible formats defined by the Go `time`
# package (http://golang.org/pkg/time/#Parse)
format.date     = 01/02/2006
format.datetime = 01/02/2006 15:04

# Determines whether the template rendering should use chunked encoding.
# Chunked encoding can decrease the time to first byte on the client side by
# sending data in chunks and flushing it to the client directly.
results.chunked = false

# Prefixes for each log message line
log.trace.prefix = "TRACE "
log.info.prefix  = "INFO  "
log.warn.prefix  = "WARN  "
log.error.prefix = "ERROR "

# The default language of this application.
i18n.default_language = en

# Module to serve static content such as CSS, JavaScript and Media files
# Allows Routes like this:
#  `Static.ServeModule("modulename","public")`
module.static=github.com/revel/modules/static

################################################################################
# Section: dev
# This section is evaluated when running Revel in dev mode. Like so:
#   `revel run path/to/myapp`
[dev]
# This sets `DevMode` variable to `true` which can be used in your code as
#   `if revel.DevMode {...}`
#   or in your templates with
#   `<no value>`
mode.dev = true

# Pretty print JSON/XML when calling RenderJson/RenderXml
results.pretty = true

# Automatically watches your applicaton files and recompiles on-demand
watch = true

# If you set watch.mode = "eager", the server starts to recompile
# your application every time your application's files change.
watch.mode = "normal"

# Watch the entire `$GOPATH` for changes.
# Uses a lot more resources, but is more accurate.
watch.gopath = true

# Module to run code tests in the browser
# See:
#   http://revel.github.io/manual/testing.html
module.testrunner = github.com/revel/modules/testrunner

# Where to log the various Revel logs
log.trace.output = off
log.info.output  = stderr
log.warn.output  = stderr
log.error.output = stderr

################################################################################
# Section: prod
# This section is evaluated when running Revel in production mode. Like so:
#   `revel run path/to/myapp prod`
# See:
#  [dev] section for documentation of the various settings
[prod]
mode.dev = false

results.pretty = false

watch = false

module.testrunner =

log.trace.output = off
log.info.output  = off
log.warn.output  = stderr
log.error.output = stderr
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
   - test/: Test files

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