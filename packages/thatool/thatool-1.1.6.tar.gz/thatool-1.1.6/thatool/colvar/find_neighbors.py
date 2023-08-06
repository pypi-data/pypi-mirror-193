from ..model       import add_periodic_image
from ..utils       import dist2_point2points
from scipy 		   import spatial
import numpy as np


def find_neighbors_gen(P, box,
						bound_cond=[1, 1, 1],
						cutoff_neighbor=None,
						k_neighbor=None, k_cutoff=20,
						keep_ref=False  ):
	""" find Nearest_Neighbors, return generator of Nearest_IDs, "Nearest relative-Position vetors from atom i"
	Ver 2: spatial.cKDTree

	thangckt, Sep 2019.	Update: Aug 2022 to use generator

	Args:
		P (np.array): Nx3 array contain positions of atoms
		box (np.array): simulation box
		bound_cond (list): boundary condition
		cutoff_neighbor (float): find neighbors within a Cutoff.
  		k_neighbor (int): find k nearest neighbors
		keep_ref (bool): include referal-atom in result

	Returns:
		obj (generator): this output a GEN contains (Idx_neigh, Rij_vectors)

	Examples:
		```py
		GEN = colvar.find_neighbors_gen(P, box, bound_cond = [1, 1, 1], cutoff_neighbor=9, keep_ref=False)
		```

	???+ note

		```
		access items in generator with:
			for Near_ID, Rij_vector in GEN:
				print (Near_ID, Rij_vector)

		- Idx_neigh    : Nx1 list of Mx1-vectors, contain Image_IDs(id of the original atoms before make periodicity) of Nearest atoms
		- Rij_vectors : Nx1 list of Mx3-Matrices, contain Nearest Rij relative-Position vetors from Ref.atom i (Nearest Positions)
		```
	"""
	## optional Inputs
	list_inputs = [cutoff_neighbor, k_neighbor]
	if sum([1 for item in list_inputs if item is None])>1:
		raise ValueError('Must select only one of {} is choose at a time'.format(list_inputs))
	## refine input
	P = np.asarray(P);    box = np.asarray(box);   bound_cond = np.asarray(bound_cond);

	## Add Periodic_Image at Periodic Boundaries
	if cutoff_neighbor is not None:
		cutoff = cutoff_neighbor
	elif k_neighbor is not None:
		if k_cutoff is not None:
			cutoff = k_cutoff
		else:
			cutoff = 9

	df = add_periodic_image(P, box, bound_cond, cutoff)
	Pbulk = df[['x','y','z']].values
	Idx_bulk = df['idx'].values

	## Detect Neighbors
	# Idx_neigh=[None]*P.shape[0]; Rij_Vectors=[None]*P.shape[0];     # Rij_Bond=[None]*P.shape[0]       # cannot use np array, since it fix the length of rows and cannot assign array to elm
	if cutoff_neighbor is not None:
		treePbulk = spatial.cKDTree(Pbulk)
		treeP = spatial.cKDTree(P)
		ID_listPbulk = treeP.query_ball_tree(treePbulk, cutoff)   # return list of lists of indice
		for i in range(P.shape[0]):
			m = np.asarray(ID_listPbulk[i])
			if keep_ref == False: m = np.delete(m, np.nonzero(m==i)) ;             # remove atom i from result
			Idx_neigh = Idx_bulk[m].astype(int)
			# Nearest Distances & Nearest Vectors from atom i
			Rij = dist2_point2points(P[i,:], Pbulk[m,:])
			##
			yield Idx_neigh, Rij[['bx','by','bz']].values     # return 1 element of list

	if k_neighbor is not None:
		treePbulk = spatial.cKDTree(Pbulk)
		for i in range(P.shape[0]):
			_, m = treePbulk.query(P[i,:], k_neighbor+1, distance_upper_bound=cutoff)
			m = np.unique(m)
			## if not enough number of nearests
			if len(m) < k_neighbor:
				raise ValueError('Only {} neighbors are found, raise `k_cutoff` value for more nearest search'.format(len(m)))

			if keep_ref == False: m = np.delete(m, np.nonzero(m==i)) ;             # remove atom i from result
			Idx_neigh = Idx_bulk[m].astype(int)

			# Nearest Distances & Nearest Vectors from atom i
			Rij = dist2_point2points(P[i,:], Pbulk[m,:])
			##
			yield Idx_neigh, Rij[['bx','by','bz']].values      # return 1 element of list
	# return Idx_neigh, Rij_Vectors          # return all list: Idx_neigh, Rij_Vectors, Rij_Bond


def find_neighbors_list(P, box,
						bound_cond=[1, 1, 1],
						cutoff_neighbor=None,
						k_neighbor=None, k_cutoff=20,
						keep_ref=False  ):
	""" find Nearest_Neighbors, return list of Nearest_IDs, "Nearest relative-Position vetors from atom i"
	Ver 2: spatial.cKDTree

	thangckt, Sep 2019.

	Args:
		P (np.array): Nx3 array contain positions of atoms
		box (np.array): simulation box
		bound_cond (list): boundary condition
		cutoff_neighbor (float): find neighbors within a Cutoff.
  		k_neighbor (int): find k nearest neighbors
		keep_ref (bool): include referal-atom in result

	Returns:
		Idx_neigh (np.array): Nx1 list of Mx1-vectors, contain Image_IDs(id of the original atoms before make periodicity) of Nearest atoms
		Rij_vectors (np.array): Nx1 list of Mx3-Matrices, contain Nearest Rij relative-Position vetors from Ref.atom i (Nearest Positions)

	Examples:
		```py
		Idx_neigh, Rij_vectors = colvar.find_neighbors_list(P, box, bound_cond = [1, 1, 1], cutoff_neighbor=9, keep_ref=False)
		```

	!!! note
		- don't compute Rij_Bond to save memory
		- Rij_Bonds (np.array): Nx1 list of scalars, contain Rij_bonds from Ref.atom to Nearest_atoms (Nearest-bonds)
	"""
	##optional Inputs
	list_inputs = [cutoff_neighbor,k_neighbor]
	if sum([1 for item in list_inputs if item is not None])>1:
		raise ValueError('Only one of [cutoff_neighbor, k_neighbor] is choose at a time'.format(list_inputs))
	## refine input
	P = np.asarray(P);    box = np.asarray(box);   bound_cond = np.asarray(bound_cond);

	## Add Periodic_Image at Periodic Boundaries
	if cutoff_neighbor is not None:
		cutoff = cutoff_neighbor
	if k_neighbor is not None:
		if k_cutoff is not None:
			cutoff = k_cutoff
		else:
			cutoff = 9

	df = add_periodic_image(P, box, bound_cond, cutoff)
	Pbulk = df[['x','y','z']].values
	Idx_bulk = df['idx'].values

	## Detect Neighbors
	Idx_neigh=[None]*P.shape[0]; Rij_Vectors=[None]*P.shape[0];     # Rij_Bond=[None]*P.shape[0]       # cannot use np array, since it fix the length of rows and cannot assign array to elm
	if cutoff_neighbor is not None:
		treePbulk = spatial.cKDTree(Pbulk)
		treeP = spatial.cKDTree(P)
		ID_listPbulk = treeP.query_ball_tree(treePbulk, cutoff)   # return list of lists of indice
		for i in range(P.shape[0]):
			m = np.asarray(ID_listPbulk[i])
			if keep_ref == False: m = np.delete(m, np.nonzero(m==i)) ;             # remove atom i from result
			Idx_neigh[i] = Idx_bulk[m].astype(int)
			# Nearest Distances & Nearest Vectors from atom i
			df = dist2_point2points(P[i,:], Pbulk[m,:])           # compute distance from atom P[i,:] to its neighbors Pbulk[m,:]
			Rij_Vectors[i] = df[['bx','by','bz']].values

	if k_neighbor is not None:
		treePbulk = spatial.cKDTree(Pbulk)
		for i in range(P.shape[0]):
			_, m = treePbulk.query(P[i,:], k_neighbor+1)
			if keep_ref == False: m = np.delete(m, np.nonzero(m==i)) ;             # remove atom i from result
			Idx_neigh[i] = Idx_bulk[m].astype(int)
			# Nearest Distances & Nearest Vectors from atom i
			df = dist2_point2points(P[i,:], Pbulk[m,:])
			Rij_Vectors[i] = df[['bx','by','bz']].values

	return Idx_neigh, Rij_Vectors          # return all list: Idx_neigh, Rij_Vectors, Rij_Bond





