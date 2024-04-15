import os
import pathlib

import pandas 
import numpy as np

"""You are welcome to use this structure as a starting point, or you can start from scratch.

The prefixed `get_` methods should not need any adjustment to read in the data.
Your solutions should be mostly contained within the prefixed `generate_` methods, and the `data_investigation()`

"""

# --- Fill in your details here ---
FIRST_NAME = "Nhu Mai"
LAST_NAME = "Nguyen"

# Gets current path
CURRENT_DIR = pathlib.Path(__file__).parent
DATA_DIR = os.path.join(CURRENT_DIR, "data")


def get_exchange_data():
    exchange_data = pandas.read_csv(
        os.path.join(DATA_DIR, "exchange.data"),
        delimiter="|",
    )
    return exchange_data


def get_stock_list():
    stock_list = pandas.read_csv(os.path.join(DATA_DIR, "stock.data"))
    return stock_list


def get_security_master():
    security_master = pandas.read_csv(
        os.path.join(DATA_DIR, "strong_oak_security_master.csv")
    )
    return security_master


def get_attributes():
    attributes = pandas.read_csv(os.path.join(DATA_DIR, "attributes.data"))
    return attributes


def generate_security_upload(
    security_master, full_stock_data, exchange_data
) :
    data = full_stock_data.merge(exchange_data, how = 'inner', on = ['MIC']) # merge with MIC to get the right MIC
    data = data.drop(columns=['n', 'year','name','domicile','city']) #Drop unneeded columns
    data =data[['MIC', 'QUEUESIP', 'Symbol', 'RequestId']] #Reorder name 
    security_master = security_master.rename(columns={'Ticker': 'Symbol'}) #Rename column for merge
    security_upload = data.merge(security_master,how = "inner",on=["QUEUESIP", "Symbol"]) #Merge two table with matching columns
    security_upload.dropna() #Drop Nan values
    security_upload.insert(0,"EuclerId", np.arange(1,len(security_upload)+1)) #Insert column Id
    security_upload = security_upload.drop('Strong Oak Identifier', axis=1) #Drop the unneeded column

    return security_upload

def generate_attribute_upload(
    security_upload, attribute_data, exchange_data
) :
    exchange_data.fillna(0)      #if the blanks are nan will need this line first
    exchange_data['Exchange location']=exchange_data['domicile']+ "-" + exchange_data['city'] #Merge two columns into one
    merg_dat = security_upload.merge(exchange_data,how = "inner",on=["MIC"]) #Merge two table
    merg_dat = merg_dat.drop(columns=['n','year','domicile','city']) #Drop unneede columns
    merg_dat2 = merg_dat.merge(attribute_data, how ="inner", on=["RequestId"]) #Merge two table with same column
    merg_dat2 = merg_dat2.drop(columns=['Company Name','MIC','QUEUESIP','Symbol','RequestId']) #Drop unneeded columns
    merg_dat2 = merg_dat2.rename(columns={'name':'Exchange name'}) #Rename column
    merge = merg_dat2.melt("EuclerId",value_vars=["Asset Class", "Inception Date", "Exchange name", "Exchange location", "Security Name","Return Since Inception"], 
                           var_name="Attribute Name", value_name="Attribute Value").sort_values("EuclerId") #Convert columns into rows
    merge.reset_index(drop=True, inplace=True) 
    return merge


def data_investigation(security_upload, attribute_upload):
    pass


def main():
    security_master = get_security_master()
    full_stock_data = get_stock_list()
    exchange_data = get_exchange_data()

    # * Loading Securities into the platform * #

    # get security data...
    security_upload = generate_security_upload(
        security_master=security_master,
        full_stock_data=full_stock_data,
        exchange_data=exchange_data,
    )

    # * Uploading Attributes * #

    attribute_data = get_attributes()

    # get attribute data...
    attribute_upload = generate_attribute_upload(
        security_upload=security_upload,
        attribute_data=attribute_data,
        exchange_data=exchange_data,
    )

    # solutions go here.

    security_upload.to_csv(
        os.path.join(CURRENT_DIR, f"{FIRST_NAME}_{LAST_NAME}_section1.csv")
    )
    attribute_upload.to_csv(
        os.path.join(CURRENT_DIR, f"{FIRST_NAME}_{LAST_NAME}_section2.csv")
    )

    data_investigation(
        security_upload=security_upload, attribute_upload=attribute_upload
    )


if __name__ == "__main__":
    main()