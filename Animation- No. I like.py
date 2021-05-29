import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

n=int(input("Enter the value of n: "))
x=np.random.randn(n)

def game(play):
    if (play<=(17*n/100) ):
        colr='violet'
        c='red'
    if (play>=(1*n*17/100)) and (play<(2*n*17/100)):
        colr='indigo'
        c='violet'
    if (play>=(2*n*17/100) )and (play<(3*n*17/100)):
        colr='blue'
        c='indigo'
    if (play>=( 3*n*17/100)) and (play<(4*n*17/100)):
        colr='green'
        c='blue'
    if (play>=(4*n*17/100)) and (play<(5*n*17/100)):
        colr='yellow'
        c='green'
    if play>=((5*n*17/100)) and (play<n):
        colr='orange'
        c='yellow'
    
    if play==n:
        colr='red'
        c='orange'
        a.event_source.stop()
        
       
    plt.cla()
    bins=np.arange(-4,4,0.5)
    plt.hist(x[:play], bins=bins, color=colr)
    
    
    
    plt.title("Random Numbers")
    plt.xlabel('Numbers I like')
    plt.ylabel('Frequency')
    
  


    

fig=plt.figure()
plt.gca().set_facecolor("black")
a=animation.FuncAnimation(fig, game, interval=80)
plt.show()

print("THANK YOU!")


