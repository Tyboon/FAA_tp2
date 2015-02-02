import numpy as np
import matplotlib.pyplot as plt

# Comme c'est convexe on se rapproche de [2,3]
def chargement() :
	t = np.loadtxt("t.txt")
	p = np.loadtxt("p.txt")
	Y = np.asmatrix(p).T
	X = np.asmatrix(np.vstack((t,np.ones((1,t.shape[0])))))
	return X,Y

def pas (t, cst=0.01) :
	return cst/(cst+t)

#thetabis = theta + pas*1/N*X*(Y-Xt*theta)
def batch (X,Y,theta,cpt) :
	tmp1 = (pas(cpt)/X.shape[1]) * X
	xT = X.T
	tmp2 = Y - np.dot(xT,theta)
	tmp = theta + np.dot(tmp1,tmp2)
	return tmp

def equal (v1,v2,pas=0.000001) :
	if (abs(v2[0]-v1[0]) <= pas and abs(v2[1]-v1[1]) <= pas) :
		return True
	else :
		return False

def dessiner (x,y,theta) :
	reg = theta[0] * x + theta[1]
	plt.plot(x,y.T,'b.')
	plt.plot(x,reg,'r.')
	plt.ylabel('position')
	plt.xlabel('temps')
	plt.show()

if __name__ == "__main__" :
	X,Y = chargement()
	theta = np.matrix([1.5,3.5]).T
	cpt = 1
	theta_plus = batch(X,Y,theta,cpt)

	while (not equal(theta_plus, theta)) :
		print theta
		cpt += 1
		theta = theta_plus
		theta_plus = batch(X,Y,theta,cpt)
	dessiner(X[0],Y,theta_plus)


