'''Estimates taxcode distribution by propagating from histogram of taxcode occurences.'''


import numpy as _np


def estimate_taxcode_distribution(taxtree, taxcode_hist_per_group_df):
    '''Estimates the taxcode distribution for each group, by propagating from the corresponding histogram of taxcode occurences.

    :Parameters:
        taxtree : wml.visionml.taxtree.Taxtree
            a taxtree
        taxcode_hist_per_group_df : pandas.DataFrame(columns=['menu_group_id', 'taxcode', 'freq'])
            histogram dataframe, obtained from e.g. VisionML DB `taxo_menus.taxcode_histogram_per_group` view

    :Returns:
        taxcode_dist_per_group : numpy.array(shape=(J, N))
            J vectors of N dimenions where N is the number of taxcodes, representing the estimated taxcode distribution for each group j, in the form `p(covered(y) | parent(y), j)` for all taxcode y and group j
        taxcode_dist2_per_group : numpy.array(shape=(J, N))
            J vectors of N dimenions where N is the number of taxcodes, representing the estimated taxcode distribution for each group j, in the form `p(covered(y) | j)` for all taxcode y and group j
        group_dist : numpy.array(shape=(J,))
            group prior distribution `p(j)`
        M : total number of events used for the estimation

    :Notes:
        covered(y) = set of all taxcodes covered by y
    '''

    # initialise
    df = taxcode_hist_per_group_df
    N = taxtree.nbElems()
    J = df['menu_group_id'].max()+1
    arr = _np.zeros((J, N))

    # transfer histogram from the dataframe to arr
    for _, row in df.iterrows():
        j = row['menu_group_id']
        n = taxtree.find(row['taxcode'].encode())
        arr[j,n] = row['freq']

    # visit each taxcode
    for i in range(N-1, -1, -1):
        children = taxtree.children(i)

        # iterate over all groups
        for j in range(J):
            w = arr[j][children].sum()
            if w > 0:
                arr[j][children] /= w
                arr[j][i] += w

    M = arr[:,0].sum()
    group_dist = arr[:,0]/M if M > 0 else _np.ones(J)/J
    arr[:,0] = 1

    # work on the p(covered(y) | j) array
    arr2 = _np.ones((J, N))
    for i in range(N):
        for k in taxtree.children(i):
            arr2[:,k] = arr2[:,i] * arr[:,k]

    return arr, arr2, group_dist, M


def make_mountain_climbing_distance(taxtree, taxcode_dist):
    '''Parses a 1D array representing a taxcode distribution and then makes an all necessary tensors relevant to the mountain-climbing distance of the distribution.

    :Note:
        In this context, a taxcode `y` with `p(covered(y)) > 0` is called a selected taxcode.

    :Parameters:
        taxtree : wml.visionml.taxtree.Taxtree
            a taxtree
        taxcode_dist : np.array(shape=(N,))
            taxcode distribution `p(covered(y))` for all taxcode `y` in the taxtree

    :Returns:
        leaf_indices : 1D numpy array
            the list of selected leaf taxcodes, with `N=len(leaf_indices)`
        nonleaf_indices : 1D numpy array
            the list of selected non-leaf taxcodes, with `M=len(nonleaf_indices)`
        membership_matrix : numpy.array(shape=(N+M,N))
            binary matrix representing the list of selected leaf nodes coverring each of the selected taxcodes. The selected taxcodes are ordered following the `leaf_indices + nonleaf_indices` list. The selected leaf taxcodes are ordered following the `leaf_indices` list.
        loss_matrix : numpy.array(shape=(N+M,N))
            taxcode distance matrix, in the form of `l(y,y^)` which says if `y` is ground truth taxcode and `y^` is predicted leaf taxcode then we penalize `l(y,y^)`. Same shape and size as `membership_matrix`. Here, `l(y,y^) = d(y,y^) if lca(y,y^) != y else 0`.
    '''

    # get all the leaf indices and the nonleaf indices
    leaf_indices = []
    nonleaf_indices = []
    Q = len(taxcode_dist)
    for q in range(Q):
        if taxcode_dist[q] <= 0:
            continue
        (leaf_indices if taxtree.isLeaf(q) else nonleaf_indices).append(q)

    # filter taxcode_dist
    N = len(leaf_indices)
    p = taxcode_dist[leaf_indices]


    # make the matrices
    M = len(nonleaf_indices)
    loss = _np.zeros((M+N,N)) # loss function
    ship = _np.zeros((M+N,N)) # membership function
    indices = leaf_indices + nonleaf_indices
    for i in range(N):
        idxA = leaf_indices[i]
        ship[i,i] = 1
        for j in range(i+1, N):
            idxB = leaf_indices[j]
            idxC = taxtree.lca(idxA, idxB)
            d = 2*taxcode_dist[idxC] - taxcode_dist[idxA] - taxcode_dist[idxB]
            loss[i,j] = d
            loss[j,i] = d
    for i in range(M+N-1, N-1, -1):
        idxA = indices[i]
        children = taxtree.children(idxA)
        children = [indices.index(q) for q in children if taxcode_dist[q] > 0]
        ship[i,:] = ship[children].sum(axis=0)
        for j in range(N):
            if ship[i,j] > 0:
                continue
            idxB = leaf_indices[j]
            idxC = taxtree.lca(idxA, idxB)
            d = 2*taxcode_dist[idxC] - taxcode_dist[idxA] - taxcode_dist[idxB]
            loss[i,j] = d

    return leaf_indices, nonleaf_indices, ship, loss
