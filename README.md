# ASKE - Platform Architect Development Framework

ASKE is an opinionated command-line tool designed to simplify and accelerate the process of initializing and managing development projects. By being opinionated, ASKE makes specific technology choices to fast-track framework creation:

- Python: Uses venv for virtual environments
- Ruby: Uses Rails with rbenv
- Java: Uses Spring Boot with Maven
- Node.js: Uses Express.js or Next.js
- Database: Defaults to PostgreSQL where applicable

> **Note:** Currently, ASKE is optimized for macOS environments, particularly those running on Apple Silicon. Future versions will aim to provide better cross-platform support and modularity.

## Why ASKE?

In modern development, setting up a new project can be time-consuming with manual steps for configuration and environment setup. ASKE was created to:

- **Automate Repetitive Tasks:** Quickly initialize a new project with a standardized structure.
- **Boost Productivity:** Reduce setup time so you can concentrate on development.
- **Enforce Best Practices:** Make opinionated choices that follow industry standards.

## Current Target Audience

- **Platform Support:** Primary focus on macOS/Apple Silicon
- **Package Managers:** Uses Homebrew for system dependencies
- **Fixed Choices:** Limited flexibility in technology selection
- **Environment Management:** Specific choices (venv, rbenv, etc.)

## Future Plans

We plan to make ASKE more modular and flexible in future releases:
- Support for multiple operating systems
- Configurable technology choices
- Alternative package manager support
- Pluggable architecture for custom pipelines

## Installation

### Using pip

Install ASKE globally via pip:

```pip install aske```

Using Homebrew

Alternatively, if you prefer Homebrew (note that the Homebrew formula is pending integration into the official Homebrew-core):

```brew tap caraveo/aske && brew install aske```

Usage

To create a new Python project, use the following command:

```aske python project-name```

[![Video: Python Environment](media/python-env.png)](https://youtu.be/oPxNfZsv1z8)


### This command will:
	- Create a new project directory named project-name.
	- Set up a Python virtual environment inside the directory.
	- Generate essential project files (e.g., requirements.txt, .env, and a starter app.py).
	- Provide a starting point for your project with a basic Python application.

## Future Framework Support

### ASKE is built with extensibility in mind. Planned future enhancements include support for:
	- Java: (e.g., Spring Boot)
	- Go: (e.g., Gin, Echo)
	- PHP: (e.g., Laravel)


Available commands:

```aske node project-name```

```aske next project-name```

```aske express project-name```

```aske ruby project-name```

```aske java project-name```


Initialize a projects git repository and add a .gitignore file:

```aske init```


These additions will make ASKE a versatile initializer for a wide range of development environments.

## Contributing

Contributions are welcome! If you have ideas for improvements or additional features, please fork the repository and submit a pull request. For major changes, feel free to open an issue first to discuss your ideas.

## License

ASKE is released under the MIT License. See the LICENSE file for more details.
