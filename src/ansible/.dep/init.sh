get_template(){
  srcdir=~/src/.uni
  mkdir -p $srcdir ; cd $srcdir 
  git clone git@github.com:Source-Graph/ansible.template.git
  cd -
}

link_this(){
  ln -srf ~/src/.uni/ansible.template/simplest/src/ansible/.dep/dep .
}

get_template
link_this
