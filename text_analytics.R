# Libraries.
library(tidyverse)
library(aweek)
library(ggplot2)
library(RColorBrewer)

# Set working directory.
setwd("~/Documents/NC State MSA/Fall 2/Text Analytics/Final Project")

# Load csv.
perweek <- read.csv("perweek.csv")

# Negate %in% operator.
'%notin%' <- Negate('%in%')

# Four weeks were during a TikTok ban, so record them for removal.
outlier_weeks <- c("2020-05-18", "2020-05-25", "2020-06-01", "2020-06-08")
perweek_wo_outliers <- perweek %>% filter(WeekDate %notin% outlier_weeks)

# Change WeekDate to date type.
perweek$WeekDate <- as.Date(perweek$WeekDate, "%Y-%m-%d")
perweek_wo_outliers$WeekDate <- as.Date(perweek_wo_outliers$WeekDate, "%Y-%m-%d")

# The palette with grey:
cbp1 <- c("#999999", "#E69F00", "#56B4E9", "#009E73",
          "#F0E442", "#0072B2", "#D55E00", "#CC79A7")

# Plot of sentiments with all weeks.
ggplot(perweek, aes(x=WeekDate)) +
  geom_line(aes(y = Positive, color = "Positive")) + 
  geom_line(aes(y = Negative, color = "Negative"))  +
  geom_line(aes(y = Neutral, color = "Neutral")) +
  geom_vline(aes(xintercept=as.Date("2020-03-02"))) +
  scale_color_manual(values = cbp1) +
  ggtitle("TikTok Sentiments by Positive, Negative, or Neutral") +
  xlab("Time in Weeks") +
  ylab("Sentiment") +
  labs(color = "Sentiments by Color")

# Plot of sentiments with the four weeks removed.
ggplot(perweek_wo_outliers, aes(x=WeekDate)) + 
  geom_line(aes(y = Positive, color = "Positive")) + 
  geom_line(aes(y = Negative, color = "Negative"))  +
  geom_line(aes(y = Neutral, color = "Neutral")) +
  geom_vline(aes(xintercept=as.Date("2020-03-02"))) +
  scale_color_manual(values = cbp1) +
  ggtitle("TikTok Sentiments by Positive, Negative, or Neutral") +
  xlab("Time in Weeks") +
  ylab("Sentiment") +
  labs(color = "Sentiments by Color")
