library(ape)
library(phytools)

#load weighted UniFrac distance matrix
weighted.unifrac.distance.matrix <- read.csv("../../data/weighted_unifrac_distance_matrix.tsv", sep="\t", row.names=1)
#load unweighted UniFrac distance matrix
unweighted.unifrac.distance.matrix <- read.csv("../../data/unweighted_unifrac_distance_matrix.tsv", sep="\t", row.names=1)

#load metadata, rename fly species for better plotting
metadata <- read.csv("../../data/NCDMIC_metadata.tsv", sep="\t")
metadata[metadata == "D. arizonae"] <- "D._arizonae"
metadata[metadata == "D. melanogaster"] <- "D._melanogaster"
metadata[metadata == "D. mettleri"] <- "D._mettleri"
metadata[metadata == "D. mojavensis"] <- "D._mojavensis"
metadata[metadata == "D. nigrospiracula"] <- "D._nigrospiracula"

#define colors for each tip
colors <- c("D._nigrospiracula" = "#440154", 
            "D._mojavensis" = "#414487", 
            "D._mettleri" = "#2a788e", 
            "D._arizonae" = "#22a884", 
            "D._melanogaster" = "#7ad151")

#convert distance matrix to distance object
weighted.unifrac.distances <- as.dist(weighted.unifrac.distance.matrix)
unweighted.unifrac.distances <- as.dist(unweighted.unifrac.distance.matrix)
#perform heirarchical clustering on distances
weighted.unifrac.clusters <- hclust(weighted.unifrac.distances)
unweighted.unifrac.clusters <- hclust(unweighted.unifrac.distances)

#define host tree
host.tree <- ape::read.tree(text="(D._melanogaster,(D._mettleri,(D._nigrospiracula,(D._mojavensis,D._arizonae))));")
#convert clusters to phylo object
weighted.unifrac.dendrogram <- as.phylo(weighted.unifrac.clusters)
unweighted.unifrac.dendrogram <- as.phylo(unweighted.unifrac.clusters)
#load associations between the tips of both trees
associations <- cbind(metadata$species, metadata$sample.id)
associations[, 1] <- gsub("^\\w+", "D._", associations[, 1])
associations[, 1] <- gsub("\\s", "", associations[, 1])

#make color palette
colors <- c()
for (species in associations[,1]) {
  if (species == "D._arizonae") {
    colors <- c(colors, "#22a884")
  }
  if (species == "D._melanogaster") {
    colors <- c(colors, "#7ad151")
  }
  if (species == "D._mettleri") {
    colors <- c(colors, "#2a788e")
  }
  if (species == "D._mojavensis") {
    colors <- c(colors, "#414487")
  }
  if (species == "D._nigrospiracula") {
    colors <- c(colors, "#440154")
  }
}

#create and plot cophylo object
weighted.unifrac.cophylo.obj <- cophylo(host.tree, weighted.unifrac.dendrogram, assoc = associations, rotate=TRUE)
unweighted.unifrac.cophylo.obj <- cophylo(host.tree, unweighted.unifrac.dendrogram, assoc = associations, rotate=TRUE)

#plot weighted unifrac cophylo
pdf(file="../../figures/host_tree_vs_weighted_unifrac.pdf", width=5, height=5)
par()
plot(weighted.unifrac.cophylo.obj, link.type="curved",link.lwd=3, ylim=c(-2.5,1.5), fsize=c(1, 0.001),
     link.col=make.transparent(colors, 1), link.lty="solid")
mtext(substitute(paste(italic("Drosophila"), " phylogeny")), line=-11, adj=0.05, cex=0.75)
mtext("Weighted UniFrac Dendrogram", line=-11, adj=0.95, cex=0.75)
dev.off()

#plot unweighted unifrac cophylo
pdf(file="../../figures/host_tree_vs_unweighted_unifrac.pdf", width=5, height=5)
par()
plot(unweighted.unifrac.cophylo.obj, link.type="curved",link.lwd=3, ylim=c(-2.5,1.5), fsize=c(1, 0.001),
     link.col=make.transparent(colors, 1), link.lty="solid")
mtext(substitute(paste(italic("Drosophila"), " phylogeny")), line=-11, adj=0.05, cex=0.75)
mtext("Unweighted UniFrac Dendrogram", line=-11, adj=0.95, cex=0.75)
dev.off()
