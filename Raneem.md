## About the Dataset {Name}

- **Source**: [default: Kaggle + other source if found]
- **License**: [if found]
- **Key Concepts**: [if needed]

## Data Profiling and Quality Checks

### Reliability

- **Source**: MYFAISAL from Aqaar app
- **License**: Unknown
- **Data Timeliness**: [same as above]

### Consistency

 is not consistent among other sources 

### Timeliness

 the data is up-to-date for our usecase

### Relevance

 we dropped column 'المدينة' because we don't need it 

### Uniqueness

 we dropped the duplicated rows 

### Completeness

 we filled every null with appropriate value such as 0 for numerical columns, and غير معروف for non-numerical columns
 we replaced number 1 to نعم and 0 to لا or other replacement words in case we needed this step in the future 

### Check Accuracy

 we changed the columns type from float to int for consistency
