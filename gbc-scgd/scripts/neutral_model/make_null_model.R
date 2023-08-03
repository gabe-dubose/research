library("vegan")
library("minpack.lm")
library("Hmisc")
library("stats4")
library("ggplot2")

community.matrix <- read.csv("../../data/asv_table.csv", row.names = 1)
community.matrix.rarefied <- vegan::rrarefy(community.matrix, 19000)
metadata <- read.csv("../../data/NCDMIC_metadata.tsv", sep="\t")

#dietary data partitioning
generalist.ids <- metadata[metadata$dietSpecificity == "generalist",]$sample.id
generalist.data <- community.matrix.rarefied[row.names(community.matrix.rarefied) %in% generalist.ids,]

specialist.ids <- metadata[metadata$dietSpecificity == "specialist",]$sample.id
specialist.data <- community.matrix.rarefied[row.names(community.matrix.rarefied) %in% specialist.ids,]

# NOTE: This code was copied from the tyRa package source code because I could not get the package 
# installed
# Source: https://github.com/DanielSprockett/tyRa

fit_sncm <- function(spp = spp, pool = NULL, taxon = NULL){
  
  options(warn=-1)
  
  #Calculate the number of individuals per community
  N <- mean(apply(spp, 1, sum))
  #Calculate the average relative abundance of each taxa across communities
  if(is.null(pool)){
    p.m <- apply(spp, 2, mean)
    p.m <- p.m[p.m != 0]
    p <- p.m/N
  } else {
    p.m <- apply(pool, 2, mean)
    p.m <- p.m[p.m != 0]
    p <- p.m/N
  }
  
  #Calculate the occurrence frequency of each taxa across communities
  spp.bi <- 1*(spp>0)
  freq <- apply(spp.bi, 2, mean)
  freq <- freq[freq != 0]
  
  #Combine
  C <- merge(p, freq, by=0)
  C <- C[order(C[,2]),]
  C <- as.data.frame(C)
  #Removes rows with any zero (absent in either source pool or local communities)
  C.0 <- C[!(apply(C, 1, function(y) any(y == 0))),]
  p <- C.0[,2]
  freq <- C.0[,3]
  names(p) <- C.0[,1]
  names(freq) <- C.0[,1]
  
  #Calculate the limit of detection
  d = 1/N
  
  ##Fit model parameter m (or Nm) using Non-linear least squares (NLS)
  m.fit <- nlsLM(freq ~ pbeta(d, N*m*p, N*m*(1-p), lower.tail=FALSE), start=list(m=0.001))
  m.ci <- confint(m.fit, 'm', level=0.95)

  ##Calculate goodness-of-fit (R-squared and Root Mean Squared Error)
  freq.pred <- pbeta(d, N*coef(m.fit)*p, N*coef(m.fit)*(1-p), lower.tail=FALSE)
  Rsqr <- 1 - (sum((freq - freq.pred)^2))/(sum((freq - mean(freq))^2))
  RMSE <- sqrt(sum((freq-freq.pred)^2)/(length(freq)-1))
  
  pred.ci <- binconf(freq.pred*nrow(spp), nrow(spp), alpha=0.05, method="wilson", return.df=TRUE)
  
  ##Calculate AIC for Poisson model
  pois.LL <- function(mu, sigma){
    R = freq - ppois(d, N*p, lower.tail=FALSE)
    R = dnorm(R, mu, sigma)
    -sum(log(R))
  }
  pois.mle <- mle(pois.LL, start=list(mu=0, sigma=0.1), nobs=length(p))
  
  aic.pois <- AIC(pois.mle, k=2)
  bic.pois <- BIC(pois.mle)
  
  ##Goodness of fit for Poisson model
  pois.pred <- ppois(d, N*p, lower.tail=FALSE)
  Rsqr.pois <- 1 - (sum((freq - pois.pred)^2))/(sum((freq - mean(freq))^2))
  RMSE.pois <- sqrt(sum((freq - pois.pred)^2)/(length(freq) - 1))
  
  pois.pred.ci <- binconf(pois.pred*nrow(spp), nrow(spp), alpha=0.05, method="wilson", return.df=TRUE)
  
  ##Results
  fitstats <- data.frame(
    m=as.numeric(coef(m.fit)),
    m.ci=as.numeric(coef(m.fit)-m.ci[1]),
    poisLL=as.numeric(pois.mle@details$value),
    Rsqr=as.numeric(Rsqr), # measuring fit, #comparing fit differing datasets to the same model
    Rsqr.pois=as.numeric(Rsqr.pois),
    RMSE=as.numeric(RMSE), # measuring fit #comparing fit differing datasets to the same model
    RMSE.pois=as.numeric(RMSE.pois),
    AIC.pois=as.numeric(aic.pois),  #comparing differing models to the dataset
    BIC.pois=as.numeric(bic.pois), #comparing differing models to the dataset
    N=as.numeric(N),
    Samples=as.numeric(nrow(spp)),
    Richness=as.numeric(length(p)),
    Detect=as.numeric(d))
  
  A <- cbind(p, freq, freq.pred, pred.ci[,2:3])
  A <- as.data.frame(A)
  colnames(A) <- c('p', 'freq', 'freq.pred', 'pred.lwr', 'pred.upr')
  if(is.null(taxon)){
    B <- A[order(A[,1]),]
  } else {
    B <- merge(A, taxon, by=0, all=TRUE)
    row.names(B) <- B[,1]
    B <- B[,-1]
    B <- B[order(B[,1]),]
  }
  B <- B[!is.na(B$freq),]
  # fit_class for graphing
  B$fit_class <-"As predicted"
  B[which(B$freq < B$pred.lwr),"fit_class"]<- "Below prediction"
  B[which(B$freq > B$pred.upr),"fit_class"]<- "Above prediction"
  B[which(is.na(B$freq)),"fit_class"]<- "NA"
  
  # combine fit stats and predicitons into list
  i <- list(fitstats, B)
  names(i) <- c("fitstats", "predictions")
  return(i)
}

plot_sncm_fit <- function(spp_out = spp_out, fill = NULL, title = NULL){
  
  tax_levels <- colnames(spp_out$predictions)[7:length(colnames(spp_out$predictions))-1]
  
  if(is.null(fill)){
    fill <- "fit_class"
  }
  
  r2_val <- paste("r^2 ==", round(spp_out$fitstats$Rsqr,4))
  m_val <- paste("m ==", round(spp_out$fitstats$m,4))
  df <- data.frame(t(table(spp_out$predictions$fit_class)))
  df <- df[,c(2,3)]
  colnames(df) <- c("Prediction", "AVS Abundance")
  
  p <- ggplot(data=spp_out$predictions)
  
  if(fill == "fit_class"){
    p <- p + geom_point(aes(x = log(p), y = freq, fill=eval(parse(text=fill))), shape =21, color="black", size =2, alpha=0.75)
    p <- p + scale_fill_manual(
      name = "Prediction",
      values = c("Above prediction" = "cyan4", "As predicted" = "blue", "Below prediction" = "goldenrod", "NA" = "white"),
      breaks = c("Above prediction", "As predicted", "Below prediction", "NA"),
      labels = c(paste0("Above prediction (",round((df[1,2]/spp_out$fitstats$Richness)*100, 1),"%)"),
                 paste0("As predicted (",round((df[2,2]/spp_out$fitstats$Richness)*100, 1),"%)"),
                 paste0("Below Prediction (",round((df[3,2]/spp_out$fitstats$Richness)*100, 1),"%)"),
                 paste0("NA (",df[4,2],")")))
    
  }else if (fill %in% tax_levels){
    p <- p + geom_point(aes(x = log(p), y = freq, fill=eval(parse(text=fill))), shape =21, color="black", size =2, alpha=0.75)
    p <- p + scale_fill_discrete(name = "Taxon")
    
  } else{
    print(paste0("fill variable: ", fill, " is not a valid taxonomic level or fit_class"))
  }
  
  p <- p + geom_line(aes(x = log(p), y = freq.pred), color = "blue")
  p <- p + geom_line(aes(x = log(p), y = pred.lwr), color = "blue", linetype="dashed")
  p <- p + geom_line(aes(x = log(p), y = pred.upr), color = "blue", linetype="dashed")
  p <- p + xlab("log(Mean Relative Abundance)")
  p <- p + ylab("Frequency")
  p <- p + ggtitle(title)
  p <- p + annotate("text", x=mean(log(spp_out$predictions$p), na.rm = TRUE), y=0.95, size=5, label = r2_val, parse=TRUE)
  p <- p + annotate("text", x=mean(log(spp_out$predictions$p), na.rm = TRUE), y=0.9, size=5, label = m_val, parse=TRUE)
  
  return(p)
}

total.neutral.model <- fit_sncm(community.matrix.rarefied)
plot_sncm_fit(total.neutral.model)
write.csv(total.neutral.model$predictions, "../../data/total_neutral_predictions.csv")

specialist.neutral.model <- fit_sncm(specialist.data)
plot_sncm_fit(specialist.neutral.model)
write.csv(specialist.neutral.model$predictions, "../../data/specialist_neutral_predictions.csv")

generalist.neutral.model <- fit_sncm(generalist.data)
plot_sncm_fit(generalist.neutral.model)
write.csv(generalist.neutral.model$predictions, "../../data/generalist_neutral_predictions.csv")
