#!/usr/bin/bash

# ----------------- package manager -----------------
yes '' | sed 3q; echo "----------------------------- upgrading and updating apt ----------------------------"; yes '' | sed 3q
sudo apt update -y || true
sudo apt upgrade -y || true

sudo apt install nala -y || true  # nala is a command line tool for managing your Linux system
(sudo apt update && sudo apt upgrade -y) || true  # this is suprior to apt

# see if variable package_manager is defined, if not, define it as "nix"
if [ -z "$package_manager" ]; then
  package_manager="nix"
fi

if [ "$package_manager" = "nix" ]; then
  curl -L https://nixos.org/nix/install | sh  # cross *nix platforms.
  . ~/.nix-profile/etc/profile.d/nix.sh
fi

# sudo apt remove mlocate && plocate # solves wsl2 slow Initializing plocate database; this may take some time..
# ignoring indexing of windows files: https://askubuntu.com/questions/1251484/why-does-it-take-so-much-time-to-initialize-mlocate-database
#sudo cp /etc/updatedb.conf /etc/updatedb.conf.bak || true
# add /mnt/c to PRUNEPATHS of /etc/updatedb.conf using sed
#sudo sed -i 's/PRUNEPATHS="/PRUNEPATHS="\/mnt /g' /etc/updatedb.conf || true
# PRUNEPATHS /mnt /etc/updatedb.conf
# sudo sed -i "s/^ *PRUNEFS *= *[\"']/&drvfs 9p /" /etc/updatedb.conf /etc/cron.daily/locate
#exclude_dirs="/mnt /tmp /var/tmp"
#updatedb --prunepaths="$exclude_dirs"  # update the mlocate database
#updatedb --prunefs="NFS,smbfs,cifs"


# -------------------- Utilities --------------------

yes '' | sed 3q; echo "------------------------------ installing wget --------------------------------"; yes '' | sed 3q
if [ "$package_manager" = "apt" ]; then
  sudo apt install wget -y || true  # for downloading files
else
  ~/.nix-profile/bin/nix-env -iA nixpkgs.wget || true
fi
yes '' | sed 3q; echo "------------------------------- installing curl -------------------------------"; yes '' | sed 3q
if [ "$package_manager" = "apt" ]; then
  sudo apt install curl -y || true  # for handling http requests
else
  ~/.nix-profile/bin/nix-env -iA nixpkgs.curl || true
fi
# consider asdf tool for managing versions of python, node, etc.

yes '' | sed 3q; echo "--------------------------- installing nvm of nodejs --------------------------"; yes '' | sed 3q
# according to: https://docs.npmjs.com/downloading-and-installing-node-js-and-npm its best to use nvm manager
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.3/install.sh | bash
# shellcheck disable=SC2155
export NVM_DIR="$([ -z "${XDG_CONFIG_HOME-}" ] && printf %s "${HOME}/.nvm" || printf %s "${XDG_CONFIG_HOME}/nvm")"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh" # This loads nvm

nvm install node || true
#npm install -g npm || true

yes '' | sed 3q; echo "----------------------------- installing sharewifi ----------------------------"; yes '' | sed 3q
npm install sharewifi -g || true
yes '' | sed 3q; echo "----------------------------- installing easy-sharing ----------------------------"; yes '' | sed 3q
npm install -g easy-sharing  # https://github.com/parvardegr/sharing
# https://github.com/mifi/ezshare
yes '' | sed 3q; echo "----------------------------- installing sshfs ----------------------------"; yes '' | sed 3q
if [ "$package_manager" = "apt" ]; then
  sudo apt install sshfs  # mount remote filesystems over ssh
else
  ~/.nix-profile/bin/nix-env -iA nixpkgs.sshfs || true
fi
yes '' | sed 3q; echo "----------------------------- installing samba ----------------------------"; yes '' | sed 3q
#sudo apt install samba  # LAN-based file sharing

yes '' | sed 3q; echo "----------------------------- installing graphviz ----------------------------"; yes '' | sed 3q
if [ "$package_manager" = "apt" ]; then
  sudo apt install graphviz -y || true
else
  ~/.nix-profile/bin/nix-env -iA nixpkgs.graphviz || true
fi
yes '' | sed 3q; echo "----------------------------- installing make ----------------------------"; yes '' | sed 3q
sudo apt install make -y || true  # lvim and spacevim require it.
yes '' | sed 3q; echo "----------------------------- installing net-tools ----------------------------"; yes '' | sed 3q
if [ "$package_manager" = "apt" ]; then
  sudo apt install net-tools -y || true  # gives ifconfig
else
  ~/.nix-profile/bin/nix-env -iA nixpkgs.nettools || true
fi
yes '' | sed 3q; echo "----------------------------- installing git ----------------------------"; yes '' | sed 3q
if [ "$package_manager" = "apt" ]; then
  sudo apt install git -y || true  # for version control
else
  ~/.nix-profile/bin/nix-env -iA nixpkgs.git || true
fi
#curl --compressed -o- -L https://yarnpkg.com/install.sh | bash
#curl https://rclone.org/install.sh | sudo bash  # onedrive equivalent.
yes '' | sed 3q; echo "----------------------------- installing lynx ----------------------------"; yes '' | sed 3q
if [ "$package_manager" = "apt" ]; then
  sudo apt install lynx -y || true  # tex browser, just like w3m
else
  ~/.nix-profile/bin/nix-env -iA nixpkgs.lynx || true
fi


# ------------------- File Managers ---------------------------
yes '' | sed 3q; echo "----------------------------- installing bat ----------------------------"; yes '' | sed 3q
if [ "$package_manager" = "apt" ]; then
  sudo apt install bat -y || true  # cat with colors.
else
  ~/.nix-profile/bin/nix-env -iA nixpkgs.bat || true
fi
#sudo apt install ranger -y   # terminal-based file explorer, alternative: lf (Go-based), tere (Rust-based), nnn (C-based), vifm (C-based), mc (C-based), etc

if [ "$package_manager" = "apt" ]; then
  es '' | sed 3q; echo "----------------------------- installing zoxide ----------------------------"; yes '' | sed 3q
else
  ~/.nix-profile/bin/nix-env -iA nixpkgs.zoxide || true
fi
#sudo apt install zoxide || true
(echo 'eval "$(zoxide init bash)"' >> ~/.bashrc) || true

yes '' | sed 3q; echo "----------------------------- installing skim ----------------------------"; yes '' | sed 3q
if [ "$package_manager" = "apt" ]; then
  sudo apt install curl
else
  ~/.nix-profile/bin/nix-env -iA nixpkgs.skim  # https://search.nixos.org/packages?channel=22.11&show=skim&from=0&size=50&sort=relevance&type=packages&query=skim || true
  ~/.nix-profile/bin/nix-env -iA nixpkgs.btop
fi
yes '' | sed 3q; echo "----------------------------- installing hyperfine ----------------------------"; yes '' | sed 3q
if [ "$package_manager" = "apt" ]; then
  sudo apt install curl
else
  ~/.nix-profile/bin/nix-env -iA nixpkgs.hyperfine  || true  # benchamrking
fi

yes '' | sed 3q; echo "----------------------------- installing fzf ----------------------------"; yes '' | sed 3q
if [ "$package_manager" = "apt" ]; then
  sudo apt install fzf -y || true  # fuzzy finder: searches contents of all files, including .git
else
  ~/.nix-profile/bin/nix-env -iA nixpkgs.fzf || true
fi
yes '' | sed 3q; echo "----------------------------- installing fd-find ----------------------------"; yes '' | sed 3q
if [ "$package_manager" = "apt" ]; then
  sudo apt install fd-find -y || true  # find alternative
else
  ~/.nix-profile/bin/nix-env -iA nixpkgs.fd || true
fi
yes '' | sed 3q; echo "----------------------------- installing ripgrep ----------------------------"; yes '' | sed 3q
if [ "$package_manager" = "apt" ]; then
  sudo apt install ripgrep -y || true  # rg command, rust-based, blazingly fast grep.
else
  ~/.nix-profile/bin/nix-env -iA nixpkgs.ripgrep || true
fi
yes '' | sed 3q; echo "----------------------------- installing ugrep ----------------------------"; yes '' | sed 3q
if [ "$package_manager" = "apt" ]; then
  sudo apt install ugrep -y || true  # just as good as grep, but consistent with windows
else
  ~/.nix-profile/bin/nix-env -iA nixpkgs.ugrep || true
fi
yes '' | sed 3q; echo "----------------------------- installing ncdu ----------------------------"; yes '' | sed 3q
if [ "$package_manager" = "apt" ]; then
  sudo apt install ncdu -y || true   # disk usage analyzer, like diskonaut
else
  ~/.nix-profile/bin/nix-env -iA nixpkgs.ncdu || true
fi
# https://github.com/bootandy/dust
# https://github.com/dalance/procs#installation
yes '' | sed 3q; echo "----------------------------- installing exa ----------------------------"; yes '' | sed 3q
if [ "$package_manager" = "apt" ]; then
  sudo apt install exa -y || true  # replacement for ls. no ner fonts, unlike lsd
else
  ~/.nix-profile/bin/nix-env -iA nixpkgs.exa || true
fi
yes '' | sed 3q; echo "----------------------------- installing navi ----------------------------"; yes '' | sed 3q
if [ "$package_manager" = "apt" ]; then
#  sudo apt install exa -y || true  # replacement for ls. no ner fonts, unlike lsd
  echo "no apt installer for navi, skipping"
else
  ~/.nix-profile/bin/nix-env -iA nixpkgs.navi || true
fi



# ---------------------------- text style ------------------------------------
yes '' | sed 3q; echo "----------------------------- installing fortune ----------------------------"; yes '' | sed 3q
if [ "$package_manager" = "apt" ]; then
  sudo apt install fortune -y || true  # generate random text in the form of piece of wisdom
else
  ~/.nix-profile/bin/nix-env -iA nixpkgs.fortune || true
fi
yes '' | sed 3q; echo "----------------------------- installing boxes ----------------------------"; yes '' | sed 3q
if [ "$package_manager" = "apt" ]; then
  sudo apt install boxes -y || true  # for ascii banners. boxes -l for list of boxes.
else
  ~/.nix-profile/bin/nix-env -iA nixpkgs.boxes || true
fi
yes '' | sed 3q; echo "----------------------------- installing cowsay ----------------------------"; yes '' | sed 3q
if [ "$package_manager" = "apt" ]; then
  sudo apt install cowsay -y || true  # animals saying things. Different figures with -f. Full list: cowsay -l
else
  ~/.nix-profile/bin/nix-env -iA nixpkgs.neo-cowsay || true
  ~/.nix-profile/bin/nix-env -iA nixpkgs.cowsay || true
fi
yes '' | sed 3q; echo "----------------------------- installing lolcat ----------------------------"; yes '' | sed 3q
if [ "$package_manager" = "apt" ]; then
  sudo apt install lolcat -y || true  # for coloring text in terminal.
else
  ~/.nix-profile/bin/nix-env -iA nixpkgs.lolcat || true
fi
yes '' | sed 3q; echo "----------------------------- installing toilet ----------------------------"; yes '' | sed 3q
if [ "$package_manager" = "apt" ]; then
  sudo apt install toilet -y || true  # large ascii text
else
  ~/.nix-profile/bin/nix-env -iA nixpkgs.toilet || true
fi
yes '' | sed 3q; echo "----------------------------- installing figlet ----------------------------"; yes '' | sed 3q
if [ "$package_manager" = "apt" ]; then
  sudo apt install figlet -y || true  # large ascii text. See: showfigfonts for full list of fonts. use -f to change font.
  ~/.nix-profile/bin/nix-env -iA nixpkgs.nms || true
else
  ~/.nix-profile/bin/nix-env -iA nixpkgs.figlet || true
fi

# see more here: https://linoxide.com/linux-fun-terminal-crazy-output/
# midnight commander, similarv# Asciiquarium# https://github.com/bartobri/no-more-secrets
# https://www.youtube.com/watch?v=haitmoSyTls

yes '' | sed 3q; echo "----------------------------- installing neofetch ----------------------------"; yes '' | sed 3q
if [ "$package_manager" = "apt" ]; then
  sudo apt install neofetch -y || true  # for system info
else
  ~/.nix-profile/bin/nix-env -iA nixpkgs.neofetch || true
  ~/.nix-profile/bin/nix-env -iA nixpkgs.cpufetch || true
fi
neofetch || true


# ---------------------------- Fun ------------------------------------
yes '' | sed 3q; echo "----------------------------- installing sl ----------------------------"; yes '' | sed 3q
if [ "$package_manager" = "apt" ]; then
  sudo apt install sl -y || true  # for fun
else
  ~/.nix-profile/bin/nix-env -iA nixpkgs.sl || true
fi
yes '' | sed 3q; echo "----------------------------- installing hollywood ----------------------------"; yes '' | sed 3q
if [ "$package_manager" = "apt" ]; then
  sudo apt install hollywood -y || true  # for fun
else
  ~/.nix-profile/bin/nix-env -iA nixpkgs.hollywood || true
fi
yes '' | sed 3q; echo "----------------------------- installing cmatrix ----------------------------"; yes '' | sed 3q

if [ "$package_manager" = "apt" ]; then
  sudo apt install cmatrix -y || true  # for fun
else
  ~/.nix-profile/bin/nix-env -iA nixpkgs.cmatrix || true
fi


# -========================================= EDITORS =========================================
yes '' | sed 3q; echo "----------------------------- installing nano ----------------------------"; yes '' | sed 3q
sudo apt install nano -y || true  # for editing files

# sudo apt install neovim -y  # nvim, but not latest release
# download neovim from release page
# sudo apt remove neovim
# sudo rm ~/.local/bin/nvim || true
yes '' | sed 3q; echo "----------------------------- installing nvim ----------------------------"; yes '' | sed 3q
cd ~ || true
wget https://github.com/neovim/neovim/releases/download/stable/nvim-linux64.deb || true
sudo apt install ./nvim-linux64.deb || true
rm nvim-linux64.deb || true


yes '' | sed 3q; echo "----------------------------- installing lunarvim ----------------------------"; yes '' | sed 3q
# from https://www.lunarvim.org/docs/installation
LV_BRANCH='release-1.2/neovim-0.8' bash <(curl -s https://raw.githubusercontent.com/lunarvim/lunarvim/master/utils/installer/install.sh)

yes '' | sed 3q; echo "----------------------------- installing spacevim ----------------------------"; yes '' | sed 3q
# https://spacevim.org/quick-start-guide/#linux-and-macos
(curl -sLf https://spacevim.org/install.sh | bash) || true


# ---------------------------- Programming Languages ------------------------------------
yes '' | sed 3q; echo "----------------------------- installing rust ----------------------------"; yes '' | sed 3q
# curl https://sh.rustup.rs -sSf | sh
(curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh) || true

yes '' | sed 3q; echo "----------------------------- installing ohmybash ----------------------------"; yes '' | sed 3q
bash -c "$(curl -fsSL https://raw.githubusercontent.com/ohmybash/oh-my-bash/master/tools/install.sh)"
# replace OSH_THEME="font" with OSH_THEME="cupcake" in ~/.bashrc
(sed -i 's/OSH_THEME="font"/OSH_THEME="cupcake"/' ~/.bashrc) || true
# this starts a new shell process and stops execution at this point!
