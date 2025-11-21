# ==============================================
# Comparação: PCA vs LDA vs t-SNE (dataset Iris)
# ==============================================

import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
from sklearn.manifold import TSNE

# Carregar o dataset Iris
iris = load_iris()
X = iris.data
y = iris.target
labels = iris.target_names

# --- PCA (linear e não supervisionado)
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

# --- LDA (linear e supervisionado)
lda = LDA(n_components=2)
X_lda = lda.fit_transform(X, y)

# --- t-SNE (não linear e não supervisionado)
tsne = TSNE(n_components=2, random_state=42, init='pca', learning_rate='auto', perplexity=30)
X_tsne = tsne.fit_transform(X)

# --- Plotagem
plt.figure(figsize=(15, 4))

# PCA
plt.subplot(1, 3, 1)
for i, label in enumerate(labels):
   plt.scatter(X_pca[y == i, 0], X_pca[y == i, 1], label=label, s=20)
plt.title("PCA (Linear - Não Supervisionado)")
plt.xlabel("Componente 1")
plt.ylabel("Componente 2")

# LDA
plt.subplot(1, 3, 2)
for i, label in enumerate(labels):
   plt.scatter(X_lda[y == i, 0], X_lda[y == i, 1], label=label, s=20)
plt.title("LDA (Linear - Supervisionado)")
plt.xlabel("Componente 1")
plt.ylabel("Componente 2")

# t-SNE
plt.subplot(1, 3, 3)
for i, label in enumerate(labels):
   plt.scatter(X_tsne[y == i, 0], X_tsne[y == i, 1], label=label, s=20)
plt.title("t-SNE (Não Linear - Não Supervisionado)")
plt.xlabel("Dim 1")
plt.ylabel("Dim 2")

plt.tight_layout()
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()
