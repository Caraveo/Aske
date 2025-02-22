# ASKE - Platform Architect Development Framework

ASKE is a command-line tool designed to simplify and accelerate the process of initializing and managing development projects. Initially, ASKE focuses on Python, providing an automated way to set up a Python environment complete with virtual environments, git initialization, and essential project files. This allows developers to focus on coding rather than repetitive setup tasks.

## Why ASKE?

In modern development, setting up a new project can be time-consuming with manual steps for configuration and environment setup. ASKE was created to:

- **Automate Repetitive Tasks:** Quickly initialize a new project with a standardized structure.

- **Boost Productivity:** Reduce setup time so you can concentrate on development.

- **Lay the Foundation for Multi-Framework Support:** While ASKE currently focuses on Python, future versions will support additional frameworks such as Node.js, 
Ruby, Java, Go, and PHP.

## Installation

### Using pip

Install ASKE globally via pip:

```pip install aske```

Using Homebrew

Alternatively, if you prefer Homebrew (note that the Homebrew formula is pending integration into the official Homebrew-core):

```brew install aske```

Usage

To create a new Python project, use the following command:

```aske python project-name```

### This command will:
	- Create a new project directory named project-name.
	- Set up a Python virtual environment inside the directory.
	- Generate essential project files (e.g., requirements.txt, .env, and a starter app.py).
	- Initialize a Git repository for version control.

## Future Framework Support

### ASKE is built with extensibility in mind. Planned future enhancements include support for:
	- Node.js: (e.g., Express, NestJS)
	- Ruby: (e.g., Rails, Sinatra)
	- Java: (e.g., Spring Boot)
	- Go: (e.g., Gin, Echo)
	- PHP: (e.g., Laravel)

These additions will make ASKE a versatile initializer for a wide range of development environments.

## Contributing

Contributions are welcome! If you have ideas for improvements or additional features, please fork the repository and submit a pull request. For major changes, feel free to open an issue first to discuss your ideas.

## License

ASKE is released under the MIT License. See the LICENSE file for more details.
