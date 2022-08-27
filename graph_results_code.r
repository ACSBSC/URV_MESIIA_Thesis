##################################################
## Project: Thesis results
## Subject: Master Thesis
## Date:    25/08/2022
## Author:  Anne Schreiber
##################################################

library(ggplot2)
library(reshape2)
library(forcats)

df_DTC <- read.csv(file ="Acc_Result_DTC.csv")
df_RFC <- read.csv(file ="Acc_Result_RFC.csv")



# Total time of training both plots

plot_time <- ggplot(df_RFC,aes(x=Run, y=Total_Time_Run, group=Method, color=Method))+
  geom_line(size=1.2)+
  labs(title="Time it took to train models RFC and DTC per Method",x="Trial Nr.", y="Time in seconds")+
  theme_minimal()+
  theme(#panel.grid.major.y = element_blank(),
        panel.grid.minor.x = element_blank(),
        axis.title.x = element_text(margin = margin(t = 10, r = 0, b = 0, l = 0)),
        axis.title.y = element_text(margin = margin(t=0, r=20, b=0, l=0)),
        axis.title=element_text(size=12),
        plot.title = element_text(margin = margin(t = 0, r = 0, b = 20, l = 0), face="bold", size=15, hjust = 0.5))


###############################################################################
##################################### DTC #####################################
###############################################################################


# Total time of training DTC plot

plot_time_DTC <- ggplot(df_DTC,aes(x=Run, y=Model_training_time, group=Method, color=Method))+
  geom_line(size=1.2)+
  labs(title="Time it took to train model DTC per Method",x="Trial Nr.", y="Time in seconds")+
  theme_minimal()+
  theme(#panel.grid.major.y = element_blank(),
    panel.grid.minor.x = element_blank(),
    axis.title.x = element_text(margin = margin(t = 10, r = 0, b = 0, l = 0)),
    axis.title.y = element_text(margin = margin(t=0, r=20, b=0, l=0)),
    axis.title=element_text(size=12),
    plot.title = element_text(margin = margin(t = 0, r = 0, b = 20, l = 0), face="bold", size=15, hjust = 0.5))


#Accuraccy plots per method


plot_DTC_acc_1 <- ggplot(df_DTC,aes(x=Run, y=Accuracy_Model_1, group=Method))+
  geom_line(aes(color=Method),size=1.2)+
  labs(title="Accuracy measured per trial for DTC model \nwith hyperparameter combination [criterion = gini, splitter = best]",x="Trial Nr.", y="Accuracy")+
  theme_minimal()+
  theme(#panel.grid.major.y = element_blank(),
    #panel.grid.minor.x = element_blank(),
    axis.title.x = element_text(margin = margin(t = 10, r = 0, b = 0, l = 0)),
    axis.title.y = element_text(margin = margin(t=0, r=20, b=0, l=0)),
    axis.title=element_text(size=10),
    plot.title = element_text(margin = margin(t = 0, r = 0, b = 20, l = 0), face="bold", size=15, hjust = 0.5))


plot_DTC_acc_2 <- ggplot(df_DTC,aes(x=Run, y=Accuracy_Model_2, group=Method))+
  geom_line(aes(color=Method),size=1.2)+
  labs(title="Accuracy measured per trial for DTC model \nwith hyperparameter combination [criterion = gini, splitter = random]",x="Trial Nr.",  y="Accuracy")+
  theme_minimal()+
  theme(#panel.grid.major.y = element_blank(),
    #panel.grid.minor.x = element_blank(),
    axis.title.x = element_text(margin = margin(t = 10, r = 0, b = 0, l = 0)),
    axis.title.y = element_text(margin = margin(t=0, r=20, b=0, l=0)),
    axis.title=element_text(size=10),
    plot.title = element_text(margin = margin(t = 0, r = 0, b = 20, l = 0), face="bold", size=15, hjust = 0.5))

plot_DTC_acc_3 <- ggplot(df_DTC,aes(x=Run, y=Accuracy_Model_3, group=Method))+
  geom_line(aes(color=Method),size=1.2)+
  labs(title="Accuracy measured per trial for DTC model \nwith hyperparameter combination [criterion = entropy, splitter = best]",x="Trial Nr.",  y="Accuracy")+
  theme_minimal()+
  theme(#panel.grid.major.y = element_blank(),
    #panel.grid.minor.x = element_blank(),
    axis.title.x = element_text(margin = margin(t = 10, r = 0, b = 0, l = 0)),
    axis.title.y = element_text(margin = margin(t=0, r=20, b=0, l=0)),
    axis.title=element_text(size=10),
    plot.title = element_text(margin = margin(t = 0, r = 0, b = 20, l = 0), face="bold", size=15, hjust = 0.5))


plot_DTC_acc_4 <- ggplot(df_DTC,aes(x=Run, y=Accuracy_Model_4, group=Method))+
  geom_line(aes(color=Method),size=1.2)+
  labs(title="Accuracy measured per trail for DTC model \nwith hyperparameter combination [criterion = entropy, splitter = random]",x="Trial Nr.",  y="Accuracy")+
  theme_minimal()+
  theme(#panel.grid.major.y = element_blank(),
    #panel.grid.minor.x = element_blank(),
    axis.title.x = element_text(margin = margin(t = 10, r = 0, b = 0, l = 0)),
    axis.title.y = element_text(margin = margin(t=0, r=20, b=0, l=0)),
    axis.title=element_text(size=10),
    plot.title = element_text(margin = margin(t = 0, r = 0, b = 20, l = 0), face="bold", size=15, hjust = 0.5))



#Average accuracy per combination of hyperparameter

df_DTC_avrg_acc_0 <- merge(merge(aggregate( Accuracy_Model_1 ~ Method, df_DTC, mean), 
                         aggregate( Accuracy_Model_2 ~ Method, df_DTC, mean), 
                         by = "Method"), 
                         merge(aggregate( Accuracy_Model_3 ~ Method, df_DTC, mean), 
                         aggregate( Accuracy_Model_4 ~ Method, df_DTC, mean), 
                         by = "Method"),by = "Method")


names(df_DTC_avrg_acc_0)[names(df_DTC_avrg_acc_0) == 'Accuracy_Model_1'] <- "Model 1"
names(df_DTC_avrg_acc_0)[names(df_DTC_avrg_acc_0) == 'Accuracy_Model_2'] <- "Model 2"
names(df_DTC_avrg_acc_0)[names(df_DTC_avrg_acc_0) == 'Accuracy_Model_3'] <- "Model 3"
names(df_DTC_avrg_acc_0)[names(df_DTC_avrg_acc_0) == 'Accuracy_Model_4'] <- "Model 4"

df_DTC_avrg_acc <- melt(df_DTC_avrg_acc_0, id.vars="Method")

plot_avrg_acc_DTC <- ggplot(df_DTC_avrg_acc, aes(x=variable, y= value,colour=Method, shape = Method))+
  geom_point(size = 5, alpha = 0.6)+
  labs(title="Average accuracy per DTC model",x="Models",  y="Average Accuracy")+
  theme_minimal()+
  theme(#panel.grid.major.y = element_blank(),
    #panel.grid.minor.x = element_blank(),
    axis.title.x = element_text(margin = margin(t = 10, r = 0, b = 0, l = 0)),
    axis.title.y = element_text(margin = margin(t=0, r=20, b=0, l=0)),
    axis.title=element_text(size=10),
    plot.title = element_text(margin = margin(t = 0, r = 0, b = 20, l = 0), face="bold", size=15, hjust = 0.5))



###############################################################################
##################################### RFC #####################################
###############################################################################

# Total time of training RFC plot

plot_time_RFC <- ggplot(df_RFC,aes(x=Run, y=Model_training_time, group=Method, color=Method))+
  geom_line(size=1.2)+
  labs(title="Time it took to train model RFC per Method",x="Trial Nr.", y="Time in seconds")+
  theme_minimal()+
  theme(#panel.grid.major.y = element_blank(),
    panel.grid.minor.x = element_blank(),
    axis.title.x = element_text(margin = margin(t = 10, r = 0, b = 0, l = 0)),
    axis.title.y = element_text(margin = margin(t=0, r=20, b=0, l=0)),
    axis.title=element_text(size=12),
    plot.title = element_text(margin = margin(t = 0, r = 0, b = 20, l = 0), face="bold", size=15, hjust = 0.5))

#Accuraccy plots per method

plot_RFC_acc_1 <- ggplot(df_RFC,aes(x=Run, y=Accuracy_Model_1, group=Method))+
  geom_line(aes(color=Method),size=1.2)+
  labs(title="Accuracy measured per trial for RFC model \nwith hyperparameter combination [n_estimator = 5, criterion = gini]",x="Trial Nr.", y="Accuracy")+
  theme_minimal()+
  theme(#panel.grid.major.y = element_blank(),
    #panel.grid.minor.x = element_blank(),
    axis.title.x = element_text(margin = margin(t = 10, r = 0, b = 0, l = 0)),
    axis.title.y = element_text(margin = margin(t=0, r=20, b=0, l=0)),
    axis.title=element_text(size=10),
    plot.title = element_text(margin = margin(t = 0, r = 0, b = 20, l = 0), face="bold", size=15, hjust = 0.5))


plot_RFC_acc_2 <- ggplot(df_RFC,aes(x=Run, y=Accuracy_Model_2, group=Method))+
  geom_line(aes(color=Method),size=1.2)+
  labs(title="Accuracy measured per trial for RFC model \nwith hyperparameter combination [n_estimator = 5, criterion = entropy]",x="Trial Nr.",  y="Accuracy")+
  theme_minimal()+
  theme(#panel.grid.major.y = element_blank(),
    #panel.grid.minor.x = element_blank(),
    axis.title.x = element_text(margin = margin(t = 10, r = 0, b = 0, l = 0)),
    axis.title.y = element_text(margin = margin(t=0, r=20, b=0, l=0)),
    axis.title=element_text(size=10),
    plot.title = element_text(margin = margin(t = 0, r = 0, b = 20, l = 0), face="bold", size=15, hjust = 0.5))

plot_RFC_acc_3 <- ggplot(df_RFC,aes(x=Run, y=Accuracy_Model_3, group=Method))+
  geom_line(aes(color=Method),size=1.2)+
  labs(title="Accuracy measured per trial for RFC model \nwith hyperparameter combination [n_estimator = 10, criterion = gini]",x="Trial Nr.",  y="Accuracy")+
  theme_minimal()+
  theme(#panel.grid.major.y = element_blank(),
    #panel.grid.minor.x = element_blank(),
    axis.title.x = element_text(margin = margin(t = 10, r = 0, b = 0, l = 0)),
    axis.title.y = element_text(margin = margin(t=0, r=20, b=0, l=0)),
    axis.title=element_text(size=10),
    plot.title = element_text(margin = margin(t = 0, r = 0, b = 20, l = 0), face="bold", size=15, hjust = 0.5))


plot_RFC_acc_4 <- ggplot(df_RFC,aes(x=Run, y=Accuracy_Model_4, group=Method))+
  geom_line(aes(color=Method),size=1.2)+
  labs(title="Accuracy measured per trail for RFC model \nwith hyperparameter combination [n_estimator = 10, criterion = entropy]",x="Trial Nr.",  y="Accuracy")+
  theme_minimal()+
  theme(#panel.grid.major.y = element_blank(),
    #panel.grid.minor.x = element_blank(),
    axis.title.x = element_text(margin = margin(t = 10, r = 0, b = 0, l = 0)),
    axis.title.y = element_text(margin = margin(t=0, r=20, b=0, l=0)),
    axis.title=element_text(size=10),
    plot.title = element_text(margin = margin(t = 0, r = 0, b = 20, l = 0), face="bold", size=15, hjust = 0.5))


plot_RFC_acc_5 <- ggplot(df_RFC,aes(x=Run, y=Accuracy_Model_5, group=Method))+
  geom_line(aes(color=Method),size=1.2)+
  labs(title="Accuracy measured per trail for RFC model \nwith hyperparameter combination [n_estimator = 15, criterion = gini]",x="Trial Nr.",  y="Accuracy")+
  theme_minimal()+
  theme(#panel.grid.major.y = element_blank(),
    #panel.grid.minor.x = element_blank(),
    axis.title.x = element_text(margin = margin(t = 10, r = 0, b = 0, l = 0)),
    axis.title.y = element_text(margin = margin(t=0, r=20, b=0, l=0)),
    axis.title=element_text(size=10),
    plot.title = element_text(margin = margin(t = 0, r = 0, b = 20, l = 0), face="bold", size=15, hjust = 0.5))

plot_RFC_acc_6 <- ggplot(df_RFC,aes(x=Run, y=Accuracy_Model_6, group=Method))+
  geom_line(aes(color=Method),size=1.2)+
  labs(title="Accuracy measured per trail for RFC model \nwith hyperparameter combination [n_estimator = 15, criterion = entropy]",x="Trial Nr.",  y="Accuracy")+
  theme_minimal()+
  theme(#panel.grid.major.y = element_blank(),
    #panel.grid.minor.x = element_blank(),
    axis.title.x = element_text(margin = margin(t = 10, r = 0, b = 0, l = 0)),
    axis.title.y = element_text(margin = margin(t=0, r=20, b=0, l=0)),
    axis.title=element_text(size=10),
    plot.title = element_text(margin = margin(t = 0, r = 0, b = 20, l = 0), face="bold", size=15, hjust = 0.5))


#Average accuracy per combination of hyperparameter

df_RFC_avrg_acc_0 <- merge(merge(merge(aggregate( Accuracy_Model_1 ~ Method, df_RFC, mean), 
                                 aggregate( Accuracy_Model_2 ~ Method, df_RFC, mean), 
                                 by = "Method"), 
                           merge(aggregate( Accuracy_Model_3 ~ Method, df_RFC, mean), 
                                 aggregate( Accuracy_Model_4 ~ Method, df_RFC, mean), 
                                 by = "Method"),by = "Method"),
                           merge(aggregate( Accuracy_Model_5 ~ Method, df_RFC, mean), 
                                 aggregate( Accuracy_Model_6 ~ Method, df_RFC, mean), 
                                 by = "Method")
                           ,by = "Method")


names(df_RFC_avrg_acc_0)[names(df_RFC_avrg_acc_0) == 'Accuracy_Model_1'] <- "Model 1"
names(df_RFC_avrg_acc_0)[names(df_RFC_avrg_acc_0) == 'Accuracy_Model_2'] <- "Model 2"
names(df_RFC_avrg_acc_0)[names(df_RFC_avrg_acc_0) == 'Accuracy_Model_3'] <- "Model 3"
names(df_RFC_avrg_acc_0)[names(df_RFC_avrg_acc_0) == 'Accuracy_Model_4'] <- "Model 4"
names(df_RFC_avrg_acc_0)[names(df_RFC_avrg_acc_0) == 'Accuracy_Model_5'] <- "Model 5"
names(df_RFC_avrg_acc_0)[names(df_RFC_avrg_acc_0) == 'Accuracy_Model_6'] <- "Model 6"



df_RFC_avrg_acc <- melt(df_RFC_avrg_acc_0, id.vars="Method")

plot_avrg_acc_RFC <- ggplot(df_RFC_avrg_acc, aes(x=variable, y= value,colour=Method, shape = Method))+
  geom_point(size = 5, alpha = 0.6)+
  labs(title="Average accuracy per RFC model",x="Models",  y="Average Accuracy")+
  theme_minimal()+
  theme(#panel.grid.major.y = element_blank(),
    #panel.grid.minor.x = element_blank(),
    axis.title.x = element_text(margin = margin(t = 10, r = 0, b = 0, l = 0)),
    axis.title.y = element_text(margin = margin(t=0, r=20, b=0, l=0)),
    axis.title=element_text(size=10),
    plot.title = element_text(margin = margin(t = 0, r = 0, b = 20, l = 0), face="bold", size=15, hjust = 0.5))

###############################################################################
################################## Save Plots #################################
###############################################################################


ggsave("total_training_time.png", plot=plot_time, path="./result_plots", bg="white")

ggsave("total_training_time_DTC.png", plot=plot_time_DTC, path="./result_plots", bg="white")
ggsave("accuracy_DTC_hyperparameter_1.png", plot=plot_DTC_acc_1, path="./result_plots", bg="white")
ggsave("accuracy_DTC_hyperparameter_2.png", plot=plot_DTC_acc_2, path="./result_plots", bg="white")
ggsave("accuracy_DTC_hyperparameter_3.png", plot=plot_DTC_acc_3, path="./result_plots", bg="white")
ggsave("accuracy_DTC_hyperparameter_4.png", plot=plot_DTC_acc_4, path="./result_plots", bg="white")
ggsave("avrg_accuracy_per_hyperparameter_DTC.png", plot=plot_avrg_acc_DTC, path="./result_plots", bg="white")

ggsave("total_training_time_RFC.png", plot=plot_time_RFC, path="./result_plots", bg="white")
ggsave("accuracy_RFC_hyperparameter_1.png", plot=plot_RFC_acc_1, path="./result_plots", bg="white")
ggsave("accuracy_RFC_hyperparameter_2.png", plot=plot_RFC_acc_2, path="./result_plots", bg="white")
ggsave("accuracy_RFC_hyperparameter_3.png", plot=plot_RFC_acc_3, path="./result_plots", bg="white")
ggsave("accuracy_RFC_hyperparameter_4.png", plot=plot_RFC_acc_4, path="./result_plots", bg="white")
ggsave("accuracy_RFC_hyperparameter_5.png", plot=plot_RFC_acc_5, path="./result_plots", bg="white")
ggsave("accuracy_RFC_hyperparameter_6.png", plot=plot_RFC_acc_6, path="./result_plots", bg="white")
ggsave("avrg_accuracy_per_hyperparameter_RFC.png", plot=plot_avrg_acc_RFC, path="./result_plots", bg="white")


