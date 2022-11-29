{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Jackson Rudoff\n",
    "\n",
    "Modern Data Structures\n",
    "\n",
    "November 28th, 2022\n",
    "\n",
    "### Final Project Proposal\n",
    "\n",
    "**Introduction**\n",
    "\n",
    "Political science – as with other social sciences – have begun migrating to Python for conducting statistical research. This tracks with the parallel developments in packages like Pandas, which has made the language more hospital to data analysis and hypothesis-based research. However, many datasets which have been adapted to R-specific data-forms or packages have not seen a similar conversion to Python. Datasets like the GSS, for example, are accessible as easily ingestible .rds files, which can be quickly and efficiently converted to tibbles with correctly formatted variables. My proposed final project would be to make an oft-used dataset – the American National Election Studies (ANES) – into a package format, which would provide users with helper functions that will streamline analysis of the data. It would include graphical and statistical methods that will make public opinion research more user-friendly, particularly for those just getting familiar with using Python in social science research. \n",
    "\n",
    "**Rationale**\n",
    "\n",
    "ANES data is messy, to put it simply. It is the most widely used public opinion dataset, collected every two years during presidential and midterm election cycles by a rotating team of political scientists and survey methodologists. The nature of public opinion data, however, means that there is little natural synergy between the variables. Questions offered to respondents s will range from demographic information to self-assessments on a Likert scale to numeric “feelings thermometers” of the respondent’s opinions on a given political issue. The sheer number of variables also means you must work with an extensive and at times confusing codebook. This makes the pre-processing stage overwhelming and strenuous, especially for those with limited coding experience. But the consistent structure of the ANES dataset means that there is some consistency in the sorts of transformations you would perform for each time series. My proposed package would leverage this consistency and turn the ANES data into a *class* of DataFrame with built-in methods that assist with initial analysis and descriptive statistics. \n",
    "\n",
    "**Description of Package**\n",
    "\n",
    "The main advantage of the package is that it bypasses the step of importing the data, immediately providing the user with the ANES samples in the form of class objects. Though the package by default will provide the last 4 editions of the time series. However, users could also instantiate new ANES objects by providing new Excel sheets taken from the ANES website. These class objects would have several built-in methods and functions, the exact inventory of which I am still working out. At present, these are the built-ins I intend to include [** = I am doubting if I can complete it on time]:\n",
    "\n",
    "1.\t.clean_junk(ANES_object)\n",
    "    \n",
    "    a. Performs the common cleaning operations that ANES objects require, such as filtering out variables that are solely clerical or for the interviewer.\n",
    "2.\t.generate_sample(n_respondents = 1000, preview_length = 10, return_stats = False, variables)\n",
    "    \n",
    "    a.\tMethod that slices a random sample of n respondents (defaults to 1000). *preview_length* indicates how much of the resulting DataFrame to print to console. *variables* takes a list of column names to slice from the entire dataset. *return_stats* prints a separate table of relevant summary statistics for each variable in the sample. \n",
    "3.\t.what_is_this(variable)\n",
    "    \n",
    "    a.\tOutputs the type, mean, sd, description from the codebook, and question asked to elicit a response for a given variable.\n",
    "4.\t.time_check(years, variables)\n",
    "    \n",
    "    a.\tChecks if the given variables are in the given years in case user wants to merge different samples along the time series. \n",
    "5.\t.save_ANES_data(df_in, out_path, format = ‘.csv’)\n",
    "    \n",
    "    a.\tAllows you to save the objects you create so that they can be shared or used in another environment. Defaults to .csv, can also work with .xlsx. Leverages the Pandas functions but condenses the process to be more like R. \n",
    "6.\tthermometer_plot(x, y)\n",
    "    \n",
    "    a.\tSeaborn-based plotting method that allows for easy plotting of the feelings thermometer variables that make up a significant portion of the ANES data.\n",
    "7.\t.model_vars(df_in, response, explanatory, type = ‘ols’)**\n",
    "    \n",
    "    a.\tHelper function that runs a simple linear model and outputs test statistics based on the given response and explanatory variables in the DataFrame. Defaults to OLS, can work with logistic regression as well.\n",
    "8.\t.find_problematic_vars(ANES_object, issue)**\n",
    "    \n",
    "    a.\tReturns a DataFrame ordering the variables by a selected potential problematic quality from the list [%NaN, skew, max/min z-score].\n",
    "9.\t.find_possible_predictors(response, n_respondents = 1000)**\n",
    "    \n",
    "    a.\tIterates through the data to find which variables significantly predict a linear effect for a given response variable. Intended to help find possible avenues of inquiry, not conclusive results.  \n",
    "\n",
    "I subtract from this list given time constraints, but I believe these constitute the most useful functions for a typical analyst of ANES data. The most important contribution of this project, in my opinion, would be that it transforms recent ANES datasets to an easily manipulable format in Python, improving its accessibility for users of varying familiarity with Python and ANES data.\n",
    "\n",
    "**Dependencies & Limitations**\n",
    "\n",
    "My package will have a few core dependencies. These include Pandas, NumPy, Seaborn, SciPy, sklearn, and statistics. Pandas is particularly important to the functioning of this package, as it is essential to transforming the Excel/csv based ANES datasets. The remaining packages will assist with the various helper functions/methods that I detail below. Seaborn, for example, is what my proposed graphical method would be based on, as I prefer it for social science-oriented plotting over Matplotlib.\n",
    "\n",
    "There are aspects of this package that will be difficult to implement, especially with the built-in helper functions. Some of them are relatively simple DataFrame operations, but the more complex ones (like .model_vars) may be difficult to code with complete error coverage. However, I think that even if I have a to cut some of the methods, the underlying project of making the ANES into a user-friendly package of manipulable DataFrames is still valuable in and of itself. Running an analysis of the most recenet time series and having subsettable data *with* correct, descriptive variable labels will save a large amount of pre-processing time for researchers, and mitigate errors incurred during the coding process.\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3.9.1 64-bit ('3.9.1')",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "name": "python",
   "version": "3.9.1"
  },
  "orig_nbformat": 4,
  "vscode": {
   "interpreter": {
    "hash": "27de0925cacb228730def3d8c8fd69bf2d18c5fc3973c732ee3fd09f66da4906"
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
