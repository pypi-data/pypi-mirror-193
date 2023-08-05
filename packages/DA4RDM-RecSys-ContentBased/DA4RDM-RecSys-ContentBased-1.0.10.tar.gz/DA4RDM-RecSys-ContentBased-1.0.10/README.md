# DA4RDM_RecSyS_ContentBased

## Description
The **DA4RDM_RecSyS_ContentBased** is a python based package that recommends similar data collections based on unstructured and explicitly provided meta information of files.


## Installation
The package is built using Python as a programming language and utilizes python packages such as tensorflow, keras, nlpaug and few others. The complete list of dependencies could be referred to in the requirements.txt file. The package can be installed using the pip command provided below:

**pip install DA4RDM-RecSys-ContentBased**

## Importing the Modules
The package has two important modules **preprocessor** and **distance_similarity_calculator**. 
The preprocessor module has methods that perform the task of data cleaning, outlier detection, PCA analysis and text preprocessing and outputs a processed dataframe that could be used for similarity evaluation. 
The distance_similarity_calculator has methods that compute the distance using KMeans with choice of distance measures and finally outputs recommendation based on the distance values. 
Once imported the component methods can be invoked and used. 
The modules can be imported using the below commands:

```python
from DA4RDM_RecSys_ContentBased import preprocessor
from DA4RDM_RecSys_ContentBased import distance_similarity_calculator
``` 

## Main Methods

1. **loadAndPreprocess_function**<br />
To perform the task of preprocessing the method **loadAndPreprocess_function** within the module **preprocessor** can be used.
This method invokes other necessary methods and finally outputs a processed dataframe. The function body is as shown below:

```python
def loadAndPreprocess_function(filepath: str, features=[], seperator='|', n_componentsAfterPCA=1, encoder='mobilebert_multi_cased', minmaxScaleFlage=True, removeColumnsWithOneValueFlag=False, debug=False):
    """Loads and preprocesses a csv-file

    :param filepath: filepath to the csv file with '|' as the seperator
    :param features: array of features to consider
    :param seperator: the seperator used when loading the csv-file
    :param n_componentsAfterPCA: sets the number of component for PCA
    :param encoder: set the language model: 'mobilebert_multi_cased' or 'bert_multi_cased'
    :param minmaxScaleFlage: minmax scaling resource vector
    :param removeColumnsWithOneValueFlag: remove columns with only one value between all resources and files
    :param debug: debug mode
    :return: a preprocessed pandas.Dataframe
    """
```   
2. **result_function**<br />
To get the final recommendation the method **result_function** within the module **distance_similarity_calculator** can be used.This function accepts the preprocessed dataframe along with other important parameters (Please refer to function body below for all parameters) and outputs recommendation based on the distance values:

```python
def result_function(df, key:str, distanceMethod='euclidean', sortAscending=True, nearestNeighbourFlag=True, outputFormatJson=False, DEBUG_MODE=False):
    """Calculating a distance between the key-resource and the resources in the dataframe

    :param df: preprocessed dataframe
    :param key: compare resources to this key
    :param distanceMethod: 'euclidean' or 'cosine' distance
    :param sortAscending: True = sort output ascending; False = descending
    :param nearestNeighbourFlag: sets the flag for the nearest neighbour
    :param DEBUG_MODE: debug mode
    :param outputFormatJson: Trigger Json format
    :return: relative distance between key and furthest resource
    """

```

## Usage and Examples
Below is an example execution of the **loadAndPreprocess_function** with features selection and debug mode set to False. The output dataframe df is the preprocessed dataframe.

```python
df = preprocessor.loadAndPreprocess_function(filepath="tomography.csv", features=['http://purl.org/coscine/terms/sfb1394#acquiredIons', 'http://purl.org/coscine/terms/sfb1394#annularMillingParameters', 'http://purl.org/coscine/terms/sfb1394#baseTemperature', 'http://purl.org/coscine/terms/sfb1394#laserPulseEnergy', 'http://purl.org/coscine/terms/sfb1394#lowVoltageCleaning', 'http://purl.org/coscine/terms/sfb1394#pulseFrequency','http://purl.org/coscine/terms/sfb1394#runTime','http://purl.org/coscine/terms/sfb1394#specimenApexRadius'],debug=False)
```

Below is an example execution of the **result_function** with output format set to json:

```python
jsonOutPut = distance_similarity_calculator.result_function(df, '1EC47F72-DF63-4D95-94E7-EB70C6BA09DB', distanceMethod='euclidean', outputFormatJson=True, DEBUG_MODE=False)
```

## Output
All the above executions computes the relative distance between the neighbours and the reference resourceid and outputs an ordered recommendation based on the distance. Finally, based on the parameter outputFormatJson, the results are generated as a json file.

If json is the selected format the function outputs a json for the distance values as shown below:

```python
{"distance":{"1EC47F72-DF63-4D95-94E7-EB70C6BA09DB":0.0,"302231B4-C161-4392-8895-8111FB7ED1F2":0.1323549579,"322EA9BA-AF4E-4C3A-BE02-0FC76C6673FE":0.3456503446,"6FC1403F-5957-4C45-8048-87D19C7C5832":0.3462583399,"4EFD8371-FD03-477F-BF39-861381FF080C":0.3463898247,"9C30C57E-7308-4DE9-BC38-49796C58929E":0.3472023012,"F8BE75F7-356E-4EB1-83AF-E6C174971D78":0.3489339426,"FAF13DF1-1747-4237-90F3-9451F4F8FEF7":0.3643016356,"24CE68AD-38BA-46DC-ACDB-9D1B93063490":0.4380531763,"632AD746-6A29-471F-861E-00663EA4B5CF":0.4494196308,"1FAA54D3-122B-41FD-ACE3-2B698FC1326F":0.9921902678,"9AA7E05B-A018-4B53-8A63-993C912DA553":0.995833426,"E6822DB5-116C-4875-8D2E-E84B4A2A9794":0.996137678,"65B41144-C3B9-4E96-9FA2-49B2071AF086":0.9977728607,"F9477D28-6D4E-4799-8D34-14383899E157":1.0}}
```


