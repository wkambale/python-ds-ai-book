import scipy.cluster.hierarchy as shc

plt.figure(figsize=(10, 7))
plt.title("Customer Segmentation Dendrogram")

# Linkage method 'ward' minimizes the variance of the clusters being merged
dend = shc.dendrogram(shc.linkage(X_scaled, method='ward'))

plt.axhline(y=20, color='r', linestyle='--')  # Draw a "cut" line
plt.xlabel('Sample Index')
plt.ylabel('Distance')
plt.show()