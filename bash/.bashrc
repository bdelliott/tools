PATH=/usr/local/bin:/usr/local/share/python
PATH=${PATH}:/bin:/sbin:/usr/bin:/usr/sbin:/sbin
PATH=${PATH}:/bin
PATH=${PATH}:/usr/local/sbin
PATH=${PATH}:/usr/local/Cellar/ruby/1.9.3-p0/bin
PATH=${HOME}/bin:${PATH}

export PATH
#export TERM=xterm-256color
export ANT_HOME=/Developer/Java/Ant

MANPATH=/usr/local/share/man:/usr/local/man:/usr/share/man

# add shell support for managing python virtualenvs:
source /usr/local/share/python/virtualenvwrapper.sh

alias blackcat='ssh blackcat'
alias gph='git push heroku master'
alias hairbender='ssh blackcat'
alias hl='heroku logs'
alias hlt='heroku logs -t'
alias mountsq='sshfs sq:/home/bde/openstack ./sq'
alias overseer="rackssh.py overseer.staging.dfw2.ohthree.com"
alias paladin='ssh paladin.local'
alias pm='python -W ignore::DeprecationWarning manage.py'
alias pmd='python2.5 manage.py deploy --email=brian@sparklesoftware.com'
alias pmr='python manage.py runserver'
alias proxysetup='ssh -N -D localhost:12345 blackcat'
alias rmorig='find . -name "*.orig" -exec rm {} \;'
alias rmpyc='find . -name "*.pyc" -exec rm {} \;'
alias ruby='ruby -w'
alias sq='ssh bde@sq'
alias srcb='source ~/.bashrc'
alias srcba='source bin/activate'
alias sshtunnelfinancedb='ssh -L 5432:127.0.0.1:5432 bde@web102.webfaction.com'
alias sshtunneloldfinancedb='ssh -L 3306:127.0.0.1:3306 bde@web102.webfaction.com'

alias wf='ssh bde@elliottsoft.com'
alias wfsp='ssh sparkle@sparkle.webfactional.com'
alias dhddt='ssh urboturbo@stage.dantesdunktank.com'
#alias wfddt='ssh ddtbde@web116.webfaction.com'
alias wfddt='ssh supertank@web116.webfaction.com'
alias xen='ssh root@xen'
alias yeti='ssh yeti.local'

export JAVA_HOME=/System/Library/Frameworks/JavaVM.framework/Versions/1.5/Home

PYTHONPATH=${HOME}/dev/sshpass
export PYTHONPATH

GREEN="\[\e[01;32m\]"
BLUE="\[\e[01;34m\]"
export PS1="${GREEN}\u${BLUE}@${GREEN}`hostname -s` ${BLUE}\w $ \[\e[00m\]"

export SVN_EDITOR=vim

# per-environment dev config
export DEV_HOSTNAME="maelstrom"

export EDITOR=/usr/bin/vim

# set locale to utf8
export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8

# runtime shared libraries
#export DYLD_LIBRARY_PATH=${LOCAL_DIR}/lib

# pkg-config
#export PKG_CONFIG_PATH=${LOCAL_DIR}/lib/pkgconfig


# add git command completion
source ~/.git-completion.bash

# unset old OS auth type variables
# keystone admin magic.  these 2 entries let me manage
# keystone users/roles/tenants from the CLI:
#export SERVICE_ENDPOINT=http://localhost:35357/v2.0
#export SERVICE_TOKEN=123456

# keystone auth info to make glance CLI work:
#export OS_PASSWORD=damned
#export OS_AUTH_URL=http://localhost:35357/v2.0
#export OS_USERNAME=bde
#export OS_TENANT_NAME=brian_tenant
#export OS_IDENTITY_API_VERSION=2.0
