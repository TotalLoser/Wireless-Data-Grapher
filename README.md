# Wireless Data Grapher
using an ssh tunnel this program will find a remote file and update a graph in real time as that file changes.
### Usage
at the start of the file, there are arguments for connecting remotely that must be adjusted accordingly.
### Debug Flag
when the ``debug`` variable is set to ``True``, the code will pull data from ``DEBUGF`` rather than attempting to connect to a remote file. 
### Dependancies
the ssh connection is using [pramiko](https://github.com/paramiko/paramiko) which must be installed to run see [prmiko's install guide](https://www.paramiko.org/installing.html) for instructions to do this
