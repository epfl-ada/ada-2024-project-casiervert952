# Project 1 - CasierVert952

## 0. Initial configuration

### 0.1 Package requiered to run the analysis

- Pandas
- Numpy
- Matplotlib
- Seaborn
- csv
- os
- time
- warnings
- importlib

### 0.2 Data

To obtain the cleaned which are data requiered to run the ```analysis.ipynb``` file, it is needed to execute once the ```data_preprocessing.ipynb```. The latter require to have the two  ```ratings.txt``` files of the original datasets transformed in ```CSV```, as illustrated by the following directory structure :

```
README
analysis.ipynb
data_preprocessing.ipynb
helpers.py
data/
├── BeerAdvocate/
│   ├── beers.csv
│   ├── breweries.csv
│   ├── users.csv
│   └── ratings.csv
│
└── RateBeer/
    ├── beers.csv
    ├── breweries.csv
    ├── users.csv
    └── ratings.csv
```

All files can be found in the GitHub Repo or in the original datasets, except for the ```ratings.csv``` files that are too heavy to be placed on GitHub. They can be downloaded here:
- [BeerAdvocate](https://coursedingler.ch/data/BA/ratings.csv)
- [RateBeer](https://coursedingler.ch/data/RB/ratings.csv)

> *The generation of ```ratings.csv``` files for both datasets from ```.txt``` files is possible in ```data_preprocessing.ipynb``` but takes ~35 minutes on a high-performance computer.*

## 1. The project

### 1.1 Title 
Red, Blue, and Brew: How Politics Pours into Beer Preferences in the US

### 1.2 Description
In modern times, it might be very easy to fall in the trap of certain stereotypes. Indeed, we know that people often take their personal beliefs and values, often linked to their political orientation, with them wherever they go. Thus, one could think for example that a Republican would prefer a strong, dark beer from ‘back home’, while a Democrat might prefer a lighter, more complex-tasting beer and that they wouldn’t care where it comes from. Our aim here will be to see whether these stereotypes are well-founded and to potentially debunk them.

To do this, we will compare two large datasets of beer reviews from two major beer review sites with the voting results for each state in the US presidential elections, from 2000 to 2020. By examining the data, our aim is to understand whether political trends can have a subtle impact on the way beer lovers choose and criticise their favourite beverages.


### 1.3 Research Questions
Thus, during this project we would like to answer these possible questions :

    *Q1* : To what extent does a state’s political orientation (Democrat or Republican) influence beer ratings by consumption type - whether the beer is from a local (in state), a national (US), or a foreign brewery?

    *Q2* : Are certain beer styles or are there typical beer characteristics that get rated more favorably in Republican or Democrat-leaning states? 

    Q3 : Are certain words (excluding commonly used words) more frequently used in reviews and brewery names in Democrat versus Republican states?

    Q4 : How do preferences for beer differ among supporters of the smaller parties like the Green Party ?

    Q5 : To what extent are common stereotypes about beer preferences accurate? For example, do certain political or regional groups truly prefer specific types of beer or do the data reveal that these assumptions are largely unfounded?


### 1.4 Additional datasets

External dataset about constituency (state-level) returns for elections to the U.S. presidency from 1976 to 2020 coming from :

    - [Harvard Dataverse](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/42MVDX)

This dataset... 🔴🔴ALBERTO🔴🔴

### 1.5 Methods and timeline

#### Part 1 : Make one with the Beer data (FABIAN & VINCENT)
    *Step 1: Preparing the data*
    Some datasets = txt files. Function to put it in CSV, …in helpers.py 

    *Step 2: Building the the big and cleaned dataset*
    For easier work with data  big merge of all datasets into one big. And then saved both into csv files  Efficient

    *Step 3 : Visualize and examining the data*
    To be able to perform proper analysis and additionnal cleanups  We looked at the data from various angles

    *Step 4: Exploring Each Dataset*
    After examining  Removed columns that won’t be used and fill missing values (the ones we could) (NaN for beer_abv  fill with average of abv of SAME style beers and precise that we are doing this asumption).

#### Part 2 : Make one with the external Politics dataset (ALBERTO)
    *Step 1 : Prepare data*
    Some addition of columns but the data was already good

    *Step 2 : Visualize this external dataset*
    See how it is presented…

    *Step 3 : Create dataframes*
    Created two dataframes usable for later.

#### Part 3 : First look into the questions / Observe initial trends (DANIEL & SAMUEL)
    *Step 1 : Local vs National vs Foreign consumption (DANIEL)*
    Compare consumption type and political orientation of top 5 (Dem/Rep) for simplification

    *Step 2 : Beer style vs Politics (SAMUEL)*
    Compare… top 5

*   Step 3 : ABV vs Politics (SAMUEL)
    Compare… top 10

#### Part 4 : Deeper dive into the questions (🔴🔴TO DO🔴🔴)
    Step 1 : Q1 (Daniel) 

    Step 2 : Q2 (Samuel)
    
    Step 3 : Q3 (Alberto)
    
    Step 4 : Q4 (Alberto)

Expliquer ce qu’on pourrait plot etc… en vrai pas obligé de tout mettre mais c’est cool si on met nos idées déjà.
PRECISER  SUBJECT TO CHANGES

Part 5 : Analyse the influence of politics on beer dynamics
Step 1 : Put everything together Q5
This will answer to Q5 after getting all the results from Part 4, we might do some final plots putting everything together.
Step 2 : Final analysis
Use final results for an analysis



Part 6: Datastory and website
Step 1 : Create and plan the datastory
Step 2 : Create a website to show the datastory
This part is still to be detailed.










README.md should contain:

- Title
- Abstract: A 150 word description of the project idea and goals. What’s the motivation behind your project? What story would you like to tell, and why?
- Research Questions: A list of research questions you would like to address during the project.
- Proposed additional datasets (if any): List the additional dataset(s) you want to use (if any), and some ideas on how you expect to get, manage, process, and enrich it/them. Show us that you’ve read the docs and some examples, and that you have a clear idea on what to expect. Discuss data size and format if relevant. It is your responsibility to check that what you propose is feasible.
- Methods
- Proposed timeline
- Organization within the team: A list of internal milestones up until project Milestone P3.
- Questions for TAs (optional): Add here any questions you have for us related to the proposed project.
