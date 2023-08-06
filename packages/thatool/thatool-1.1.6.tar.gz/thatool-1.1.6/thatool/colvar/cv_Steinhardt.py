import numpy as np


def Ql_Steinhardt(ql_i):
	"""compute origincal Stainhardt of l-th order
	* Input:
		ql_i   : a vector of (2l+1) complex components, qlm(i) vector of atom i
	* Output:
		Ql      : scalar value of l-th order Stainhardt parameter"""
	# refine input
	ql_i = np.asarray(ql_i);
	l = ql_i.shape[0]
	# --
	Sum_ql2 = sum(ql_i * np.conjugate(ql_i))
	# Sum_ql2 = sum((np.abs(ql_i))**2)
	Ql = np.sqrt(4*np.pi/(2*l+1))*np.sqrt(Sum_ql2)
	return Ql.real
##--------

def Local_Ql_Steinhardt(ql_i, qlm_j, SW):
	"""compute Local Stainhardt of l-th order (modified Steinhardt as: 10.1021/acs.jctc.6b01073)
	* Input:
		ql_i   : 1x(2l+1) array, vector of (2l+1) complex components, qlm(i) vector of atom i
		qlm_j   : Nx(2l+1) array, rows are vectors of (2l+1) complex components, qlm(j) of all neighbors j of atom i
	* Output:
		Local_Ql_i      : scalar value of l-th order Stainhardt parameter of atom i
	* PreRequire: compute ql_i complex vector for all atoms before this function can be used"""
	# refine input
	ql_i = np.asarray(ql_i);      qlm_j = np.asarray(qlm_j)
	# way 1
	# dotProd = np.conjugate(qlm_j)@ql_i    # dot product of each row of matrix qlm_j w.r.t vetor ql_i
	dotProd = np.einsum('ij,j->i', np.conjugate(qlm_j), ql_i)
	Local_Q6 = sum(SW*dotProd)/ sum(SW)

	# #way 2
	# Sum_dotProd = 0
	# for j in range(qlm_j.shape[0]):
		# Sum_dotProd += SW[j]*sum(ql_i*np.conjugate(qlm_j[j]))
	# Local_Q6 = Sum_dotProd/ sum(SW)
	return Local_Q6.real
##--------
