import numpy as np

# Comme c'est convexe on se rapproche de [2,3]

def pas (t, cst=10.) :
	return cst/(cst+t)

def batch (t,p,teta,cpt) :
	tmp1 = (pas(t)/t.shape[0]) * X
	tmp2 = Y - np.dot(X.T,teta)
	tmp = teta + np.dot(tmp1,tmp2)

def equal (v1,v2,pas=0.01) :
	if (v1 <= v2+pas or v1 >= V2-pas) :
		return True
	else :
		return False

if __name__ == "__main__" :
	t = np.loadtxt("t.txt")
	p = np.loadtxt("p.txt")

	Y = np.asmatrix(p)
	X = np.asmatrix(np.vstack((t,np.ones((1,t.shape[0])))))

	teta = np.matrix([2,3])
	cpt = 1
	print X
	tmp = batch(t,p,teta,cpt)

	while (not equal(teta, tmp)) :
		print teta
		cpt += 1
		teta = tmp
		tmp = batch(t,p,teta,cpt)

