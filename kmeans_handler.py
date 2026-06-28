from random import randint
from sklearn.cluster import KMeans as SKLearnKMeans
from utils import distance


def random_clusters(K, panel):
    """Generate K random cluster centres inside the drawing panel."""
    panel_w, panel_h = panel[2], panel[3]
    return [[randint(0, panel_w), randint(0, panel_h)] for _ in range(K)]


def assign_labels(points, clusters):
    """Assign each point to the nearest cluster; return label list."""
    labels = []
    for point in points:
        min_dist = distance(point, clusters[0])
        min_idx  = 0
        for j in range(1, len(clusters)):
            d = distance(point, clusters[j])
            if d < min_dist:
                min_dist = d
                min_idx  = j
        labels.append(min_idx)
    return labels


def update_clusters(points, clusters, labels, K):
    """Move each cluster centre to the mean of its assigned points."""
    new_clusters = list(clusters)
    for i in range(K):
        xs = [points[j][0] for j in range(len(points)) if labels[j] == i]
        ys = [points[j][1] for j in range(len(points)) if labels[j] == i]
        if xs:
            new_clusters[i] = [sum(xs) / len(xs), sum(ys) / len(ys)]
    return new_clusters


def run_step(points, clusters, K):
    """One full E-step + M-step of K-Means."""
    labels   = assign_labels(points, clusters)
    clusters = update_clusters(points, clusters, labels, K)
    return clusters, labels


def run_sklearn(points, K):
    """Run scikit-learn KMeans to convergence and return (clusters, labels)."""
    kmeans   = SKLearnKMeans(n_clusters=K, n_init=10).fit(points)
    clusters = kmeans.cluster_centers_.tolist()
    labels   = kmeans.predict(points).tolist()
    return clusters, labels


def calc_error(points, clusters, labels):
    """Sum of distances from each point to its cluster centre."""
    return int(sum(distance(points[i], clusters[labels[i]])
                   for i in range(len(points))))
