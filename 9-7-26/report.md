
* Simple EDA on Sales of eatable Items 

* Step1 :  Collecting the dataset ( uncleaned ) from Kaggle 
        and extrat to folder for further cleaning

* Step2 : Import the dataset using Panda , Converting it to DataFrame 
        Now the DataFrame is used for futher cleaning 


    - do check sum of nulls
    - check info()
    - inspect datatypes columns using describe()
    - check for duplicates 
    - using missingno library to see in visuals how the nulls are present in the columns

    
* step 3 : cleaning the Dataset after identifying correction to be made
       
    - copy raw dataFrame to another Dataframe 
    - apply imputations , cleaning techniques on Columns 

            # mean imputations for quantity 

            quantity_imputes = df_clean['Total Spent'] / df['Price Per Unit']
            df_clean['Quantity'] = df_clean['Quantity'].fillna(quantity_imputes)

            
            # price_per_unit = Total spent / Quantity
            df_clean['Price Per Unit'] = df_clean['Price Per Unit'].fillna(
                df_clean['Total Spent'] / df_clean['Quantity']
            )

            # total spent imputes 

            Total_spent_imputes = df_clean['Quantity'] * df_clean['Price Per Unit']
            df_clean['Total Spent'] = df_clean['Total Spent'].fillna(df_clean['Quantity'] * df_clean['Price Per Unit'])


            # remove rows where Item is UNKNOWN or ERROR
            bad = df_clean['Item'].isin(['UNKNOWN', 'ERROR'])
            df_clean = df_clean.loc[~bad].copy()


    
            df_clean['Transaction Date'] = pd.to_datetime(df_clean['Transaction Date'], errors='coerce')
            df_clean = df_clean.dropna(subset=['Transaction Date']).copy()


* step 4  - drop some of the Columns if data is missing more that 25% 

* step 5  - 
    *    Uivariate analysis 
        - plot the histogram on total spent , we see that mostly spend < 10 dollars

    *    Bivariate analsis between , Items - Total SPend 
        - by plotting a Bar char we can see that : 
            * salad is the highes sales item
            * smoothy and sandwich are second highes sales 
            * least sales was on cookie 

    - monthly sales throughout the year, plotting line chart of transaction_date and Total_spent

        * most sale were seen in the  month on july june august , but only for one year that data was
        
           