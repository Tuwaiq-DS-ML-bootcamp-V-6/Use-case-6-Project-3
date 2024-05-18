## About the Apartments Dataset

- **Source**: MYFAISAL from Aqaar app (Kaggle)
- **License**: Unknown

The dataset contains details about the available apartments in Riyadh. It includes information such as the number of rooms and bathrooms in each apartment, as well as the specific neighborhoods or areas where these apartments are located.



## Data Profiling and Quality Checks

### Reliability

- **Source**: MYFAISAL from Aqaar app (Kaggle)
- **License**: Unknown
- **Data Timeliness**: the data is up-to-date for our usecase

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
