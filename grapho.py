import matplotlib.pyplot as plt
import matplotlib.animation as animation
ADDRESS = "raspberrypi.local"
PORT = 22
USER = "pi"
PASS = "chungus69"
PATH = "cat ~/Documents/ads1115/text_data.txt"
DEBUGF = 'data.txt'
def animate(i):
    if(not debug):
        ssh = SSHClient()
        #print(ssh)
        ssh.set_missing_host_key_policy(AutoAddPolicy())
        ssh.connect(ADDRESS, PORT, USER, PASS)
        stdin, stdout, stderr = ssh.exec_command(PATH)
        graphlines = stdout.readlines()                
    else:
        graph_data = open(DEBUGF,'r').read()
        graphlines = graph_data.split('\n')
        
    xs = []
    ys = []
    i = 0
    for line in graphlines:
        if len(line) > 1:
            ys.append(float(line))
            xs.append(i)
            i += 1
    ax1.clear()
    ax1.plot(xs, ys)
from paramiko import SSHClient, AutoAddPolicy, Transport

debug = False
graphlines = ""

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()
