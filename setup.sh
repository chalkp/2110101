#!/bin/bash
output_file=$(pwd)$'/.activate'
_pip_packages=$''

_standard_deps=("python3" "python3-pip" "python3-venv" "jupyter-core" "pandoc")
_texlive_deps=("texlive-xetex" "texlive-fonts-recommended" "texlive-plain-generic")

sudo apt-get install $(printf " %s" "${_standard_deps[@]}")
sudo apt-get install $(printf " %s" "${_texlive_deps[@]}")

cat <<EOF >$output_file
_pip_packages=$'$_pip_packages'
function venv() {
  local _venv_dir=\$(pwd)/.venv
  python3 -m venv \$_venv_dir
  echo initialized venv at: \$_venv_dir
  echo installing: \$_pip_packages
  echo ...
  .venv/bin/pip install \$_pip_packages > /dev/null
  echo $'installation successful.\n'
  alias python="\$_venv_dir/bin/python3"
  alias pip="\$_venv_dir/bin/pip3"
  echo $'new alias commands:\npython -> self explanatory.\npip -> self explanatory.\n'
}
alias venv=venv
echo $'new alias commands:\nvenv -> initialize venv and install common pip packages'
EOF

echo $'\n\n\n\ndependencies installed\n\nnext step:\n>source '$output_file
