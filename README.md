# Recommenders
This project will house case studies of recommender systems (ie. various recommender techniques applied to various datasets) and other notes pertaining to recommender systems (paper reviews, conference reviews, tutorials on evaluation criteria and so on). I am not, at this moment in time, 100% set on the actual structure of the repo and how everything is going to work, so expect it to change.

One thing of particular note: this repo is mainly for me to learn more about recommender systems. If you see anything done inefficiently, or being outright wrong, do not hesitate to open an issue. At the same time, do not expect for previously done work to be redone, as I would rather do it right the next time than to do it again.

## Getting Started

The development will be done using Python 3.5, and I won't be supporting Python 2.x. I'll be using Jupyter notebook for doing the actual work, though there may be other Python files running around here and there for ease of use. There will be multiple branches if I am working on multiple things at once, so the master may not be updated with the latest work.

### Prerequisites

There are a number of dependencies listed on **requirements.txt**. I don't particularly care about having a large number of dependencies, since I will be using various features of each of the libraries, so the list will be long. You can install the dependencies by running
```
pip install -r requirements.txt
```
If you don't want to clutter your Python installation with all of these, you can use `virtualenv` to create a new environment beforehand. If you are like me and use Anaconda for managing your Python installations, you can create a new environment with the requirements by calling
```
conda create --name MyEnvironment --file requirements.txt
```
as per the [instructions](https://conda.io/docs/using/envs.html#create-an-environment).

## Usage

I advise you to run the Jupyter Notebook from the root directory of this project, as it is how I'm doing and I'm not going to be actively testing running it from other directories.

## Future Plans

* EVERYTHING

## Contributing

I don't actually plan to have any contributors, but if you want to fix any errors or offer some advice, open an issue. I may even accept pull requests for small fixes. Please don't come to me with requests on doing some analysis x on dataset y — unless it is extremely important for analysis or the dataset is mindblowingly good, I will be ignoring it.

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

I will be listing people or work that has made significant impact in this long-running project here. As of now, that is a total sum of 0 people. Acknowledgements pertaining to specific datasets will be on their own readme.