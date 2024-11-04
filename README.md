# Project 1 - CasierVert952

## Initial configuration

### Package requiered to run the analysis

- Pandas
- Numpy
- matplotlib
- ...

### Data

To be able to reproduce the results by running the 'analysis.ipynb' file, the following directory structure is required:

```
analysis.ipynb
helpers.py
data/
├── BeerAdvocate
│   ├── beers.csv
│   ├── breweries.csv
│   ├── users.csv
│   └── ratings.csv
│
└── RateBeer
	├── beers.csv
	├── breweries.csv
	├── users.csv
	└── ratings.csv
README
```

All files can be found in the original datasets, except for the ```ratings.csv``` files that can be downloaded here:
- [BeerAdvocate](https://coursedingler.ch/data/BA/ratings.csv)
- [RateBeer](https://coursedingler.ch/data/RB/ratings.csv)

> *The generation of ```ratings.csv``` files for both datasets from ```.txt``` files is possible in ```analysis.ipynb``` but takes ~35 minutes on a high-performance computer.*
	





README.md should contain:

- Title
- Abstract: A 150 word description of the project idea and goals. What’s the motivation behind your project? What story would you like to tell, and why?
- Research Questions: A list of research questions you would like to address during the project.
- Proposed	 additional datasets (if any): List the additional dataset(s) you want to use (if any), and some ideas on how you expect to get, manage, process, and enrich it/them. Show us that you’ve read the docs and some examples, and that you have a clear idea on what to expect. Discuss data size and format if relevant. It is your responsibility to check that what you propose is feasible.
- Methods
- Proposed timeline
- Organization within the team: A list of internal milestones up until project Milestone P3.
- Questions for TAs (optional): Add here any questions you have for us related to the proposed project.