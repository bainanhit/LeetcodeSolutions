def calculate_auc_func2(y_labels, y_scores):
    samples = list(zip(y_scores, y_labels))
    rank = [(values2, values1) for values1, values2 in sorted(samples, key=lambda x:x[0])]
    pos_rank = [i+1 for i in range(len(rank)) if rank[i][0] == 1]
    pos_cnt = np.sum(y_labels == 1)
    neg_cnt = np.sum(y_labels == 0)
    auc = (np.sum(pos_rank) - pos_cnt*(pos_cnt+1)/2) / (pos_cnt*neg_cnt)
    print('AUC calculated by function2 is {:.2f}'.format(auc))
    return auc


if __name__ == '__main__':
    y_labels = np.array([1, 1, 0, 0, 0])
    y_scores = np.array([0.4, 0.8, 0.2, 0.4, 0.5])
    calculate_auc_func2(y_labels, y_scores)