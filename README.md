# ascii2CSV
Simple converter from ascii defined dataset to CSV

### Usage

`python ascii2CSV.py template origin destination`

#### 
Where template is a JSON file with the name of the fields of the CSV and the columns index (starting by 0). Origin is your ascii dataset.
Destination is your CSV file.

### Example

Given this dataset:
```
096180
120160
075140
060180
````
And this JSON template

```json
{
    "Weight":[0,3],
    "Height":[3,6]
}
```
Executing 
`ascii2CSV.py ./template.json test_data/ASCII_DATA_EXAMPLE test.csv`
with the provided files, the output will be 

```
Weight,Height
096,180
120,160
075,140
060,180
```

