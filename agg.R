# Libraries.
library(tidyverse)
library(aweek)
library(ggplot2)
library(RColorBrewer)

# Set working directory.
setwd("~/Documents/NC State MSA/Fall 2/Text Analytics/Final Project")

scored <- read.csv("scored_reviews.csv")

weeks <- scored %>%
  mutate(week=strftime(as.Date(posted_date, "%Y-%m-%d"), "%V")) %>%
  mutate(year=strftime(as.Date(posted_date, "%Y-%m-%d"), "%Y")) %>%
  mutate(posted_date=get_date(week = week, year = year)) %>%
  group_by(posted_date) %>%
  summarize(n=n())