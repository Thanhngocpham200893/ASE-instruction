# ASE-instruction

ASE and python stuff

Install python3

cd ~
mkdir soft
cd soft
wget https://www.python.org/ftp/python/3.6.3/Python-3.6.3.tgz
tar -zxvf Python-3.6.3.tgz 
cd Python-3.6.3/
./configure --prefix=$HOME/soft/python-3.6.3        
###install python in $HOME/soft/python-3.6.3  
make
make install

vim ~/.bashrc
##create the path in bash_rc 
export PATH=$HOME/soft/python-3.6.3/bin:$PATH


### create the virtual env
###first check the python3 you use
which python3
### the output should be 
~/soft/python-3.6.3/bin/python3
### if no log out and log in again or touch ~/.bashrc

###create the virtual environment named “Myenv” 
python3 -m venv Myenv
#activate it by 
source Myenv/bin/activate
#deactivate it
deactivate


###ASE and useful stuff
activate the Myenv first
cd ~/Myenv
Create requirement.txt in ~/Myenv contains

ase==3.17.0
cymem==1.31.2
Cython==0.28.1
decorator==4.3.0
matplotlib==2.2.2
mpi4py==3.0.2
numpy==1.14.3
scikit-learn==0.20.3
scipy==1.1.0
sklearn==0.0

#install are bumpy or so using
pip3 install -r requirements.txt
