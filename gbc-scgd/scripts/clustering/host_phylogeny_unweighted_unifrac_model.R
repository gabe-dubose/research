library(ape)
library(phytools)

#load metadata
metadata <- read.csv("../../data/NCDMIC_metadata.tsv", sep="\t")
#load weighted UniFrac distance matrix
unweighted.unifrac.distance.matrix <- read.csv("../../data/unweighted_unifrac_distance_matrix.tsv", sep="\t", row.names=1)

#read host tree
coi.tree <- ape::read.tree("../../data/coi_tree.nwk")
coi.tree <- ape::root(coi.tree, outgroup="D_melanogaster")
plot(coi.tree)
#convert to distances
coi.distances <- cophenetic.phylo(coi.tree)
coi.distances <- otuSummary::matrixConvert(coi.distances)
#define distances from melanogaster
sp1.melanogaster <- coi.distances[coi.distances$sp1 == "D_melanogaster",]
sp2.melanogaster <- coi.distances[coi.distances$sp2 == "D_melanogaster",]
coi.distances.from.outgroup <- c("melanogaster" = 0, "mettleri" = 0.1684199, "nigrospiracula" = 0.2013635, "arizonae" = 0.2487587, "mojavensis" = 0.2261843)

#add relatedness and diet to unifrac matricies
relatedness <- c()
diet <- c()
for (sample in rownames(unweighted.unifrac.distance.matrix)) {
  species <- metadata[metadata$sample.id == sample,]$species
  species.diet <- metadata[metadata$sample.id == sample,]$Diet
  distance.from.out <- coi.distances.from.outgroup[species]
  relatedness <- c(relatedness, distance.from.out)
  diet <- c(diet, species.diet)
}
unweighted.unifrac.distance.matrix <- cbind(unweighted.unifrac.distance.matrix, relatedness)
unweighted.unifrac.distance.matrix <- cbind(unweighted.unifrac.distance.matrix, diet)

#partition actual distance
unweighted.unifrac.distances <- unweighted.unifrac.distance.matrix[1:33]

#make dbRDA model for both relatedness and diet
unweighted.unifrac.dbrda.model <- vegan::dbrda(formula = unweighted.unifrac.distances~relatedness+diet, data=unweighted.unifrac.distance.matrix)
#get model summary
unweighted.unifrac.dbrda.model.summary <- summary(unweighted.unifrac.dbrda.model)

#view model results
print(unweighted.unifrac.dbrda.model)

#perform anova and identify significant 
anova(unweighted.unifrac.dbrda.model, by="terms", permu=999)

#partition variance
variance.partitioned <- vegan::varpart(unweighted.unifrac.distances, ~relatedness, ~diet, data=unweighted.unifrac.distance.matrix)
summary(variance.partitioned)
plot(variance.partitioned)

