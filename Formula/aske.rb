class Aske < Formula
  include Language::Python::Virtualenv

  desc "Platform Architect Development Framework"
  homepage "https://github.com/caraveo/aske"
  url "https://github.com/caraveo/aske/dist/v0.1.0.tar.gz"
  sha256 "YOUR_TARBALL_SHA256_HERE"
  license "MIT"

  depends_on "python@3.11"

  resource "click" do
    url "https://files.pythonhosted.org/packages/96/d3/f04c7bfcf5c1862a2a5b845c6b2b360488cf47af55dfa79c98f6a6bf98b5/click-8.1.7.tar.gz"
    sha256 "ca9853ad459e787e2192211578cc907e7594e294c7ccc834310722b41b9ca6de"
  end

  resource "python-dotenv" do
    url "https://files.pythonhosted.org/packages/bc/57/e84d88dfe0aec03b7a2d4327012c1627ab5f03652216c63d49846d7a6c58/python-dotenv-1.0.1.tar.gz"
    sha256 "e324ee90a023d808f1959c46bcbc04446a10ced277783dc6ee09987c37ec10ca"
  end

  resource "PyYAML" do
    url "https://files.pythonhosted.org/packages/cd/e5/af35f7ea75cf72f2cd079c95ee16797de7cd71f29ea7c68ae5ce7be1eda0/PyYAML-6.0.1.tar.gz"
    sha256 "bfdf460b1736c775f2ba9f6a92bca30bc2095067b8a9d77876d1fad6cc3b4a43"
  end

  def install
    virtualenv_install_with_resources

    # Create shell completion scripts
    generate_completions_from_executable(bin/"aske", shells: [:bash, :zsh, :fish])

    # Install shell wrapper script
    (buildpath/"aske-wrapper.sh").write <<~EOS
      #!/bin/bash
      if [ "$1" = "python" ]; then
          output=$(command aske "$@")
          echo "$output"
          cd_command=$(echo "$output" | grep "^cd '" | tail -n 1)
          if [ ! -z "$cd_command" ]; then
              eval "$cd_command"
          fi
      else
          command aske "$@"
      fi
    EOS

    (bin/"aske-wrapper").write <<~EOS
      #!/bin/bash
      source #{prefix}/aske-wrapper.sh
    EOS

    chmod 0755, bin/"aske-wrapper"
    prefix.install "aske-wrapper.sh"
  end

  def caveats
    <<~EOS
      To enable automatic directory changing, add this to your shell's config file:
      
      For bash (~/.bashrc):
        alias aske=". aske-wrapper"
      
      For zsh (~/.zshrc):
        alias aske=". aske-wrapper"
      
      Then restart your shell or run:
        source ~/.bashrc  # or source ~/.zshrc
    EOS
  end

  test do
    system bin/"aske", "--version"
  end
end 