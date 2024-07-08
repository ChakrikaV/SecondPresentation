{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "8268cad3-39ca-43c1-805d-e2e24035d830",
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cbfed8ca-f5cc-48d2-a93a-9547f6d9eedc",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "import os "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "7ba44784-29d1-4e57-8b6c-40f341570566",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'/Users/chakrika/Desktop'"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pwd\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "id": "0d1546a5-3477-47e6-8812-727d8c8c2e8a",
   "metadata": {},
   "outputs": [],
   "source": [
    "data = pd.read_csv('https://raw.githubusercontent.com/ChakrikaV/SecondPresentation/main/Online%20Sales%20Data.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "id": "5035878c-e3b1-4ce5-b64b-6a2c16dc11f3",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Transaction ID</th>\n",
       "      <th>Date</th>\n",
       "      <th>Product Category</th>\n",
       "      <th>Product Name</th>\n",
       "      <th>Units Sold</th>\n",
       "      <th>Unit Price</th>\n",
       "      <th>Total Revenue</th>\n",
       "      <th>Region</th>\n",
       "      <th>Payment Method</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>10001</td>\n",
       "      <td>2024-01-01</td>\n",
       "      <td>Electronics</td>\n",
       "      <td>iPhone 14 Pro</td>\n",
       "      <td>2</td>\n",
       "      <td>999.99</td>\n",
       "      <td>1999.98</td>\n",
       "      <td>North America</td>\n",
       "      <td>Credit Card</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>10002</td>\n",
       "      <td>2024-01-02</td>\n",
       "      <td>Home Appliances</td>\n",
       "      <td>Dyson V11 Vacuum</td>\n",
       "      <td>1</td>\n",
       "      <td>499.99</td>\n",
       "      <td>499.99</td>\n",
       "      <td>Europe</td>\n",
       "      <td>PayPal</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>10003</td>\n",
       "      <td>2024-01-03</td>\n",
       "      <td>Clothing</td>\n",
       "      <td>Levi's 501 Jeans</td>\n",
       "      <td>3</td>\n",
       "      <td>69.99</td>\n",
       "      <td>209.97</td>\n",
       "      <td>Asia</td>\n",
       "      <td>Debit Card</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>10004</td>\n",
       "      <td>2024-01-04</td>\n",
       "      <td>Books</td>\n",
       "      <td>The Da Vinci Code</td>\n",
       "      <td>4</td>\n",
       "      <td>15.99</td>\n",
       "      <td>63.96</td>\n",
       "      <td>North America</td>\n",
       "      <td>Credit Card</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>10005</td>\n",
       "      <td>2024-01-05</td>\n",
       "      <td>Beauty Products</td>\n",
       "      <td>Neutrogena Skincare Set</td>\n",
       "      <td>1</td>\n",
       "      <td>89.99</td>\n",
       "      <td>89.99</td>\n",
       "      <td>Europe</td>\n",
       "      <td>PayPal</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Transaction ID        Date Product Category             Product Name  \\\n",
       "0           10001  2024-01-01      Electronics            iPhone 14 Pro   \n",
       "1           10002  2024-01-02  Home Appliances         Dyson V11 Vacuum   \n",
       "2           10003  2024-01-03         Clothing         Levi's 501 Jeans   \n",
       "3           10004  2024-01-04            Books        The Da Vinci Code   \n",
       "4           10005  2024-01-05  Beauty Products  Neutrogena Skincare Set   \n",
       "\n",
       "   Units Sold  Unit Price  Total Revenue         Region Payment Method  \n",
       "0           2      999.99        1999.98  North America    Credit Card  \n",
       "1           1      499.99         499.99         Europe         PayPal  \n",
       "2           3       69.99         209.97           Asia     Debit Card  \n",
       "3           4       15.99          63.96  North America    Credit Card  \n",
       "4           1       89.99          89.99         Europe         PayPal  "
      ]
     },
     "execution_count": 65,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "b292db9e-0253-4287-83bb-06025c3ffb45",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Index(['Transaction ID', 'Date', 'Product Category', 'Product Name',\n",
      "       'Units Sold', 'Unit Price', 'Total Revenue', 'Region',\n",
      "       'Payment Method'],\n",
      "      dtype='object')\n"
     ]
    }
   ],
   "source": [
    "print(data.columns)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "bfadea62-63e5-44e2-bed7-c626d8028aab",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Transaction ID      0\n",
      "Date                0\n",
      "Product Category    0\n",
      "Product Name        0\n",
      "Units Sold          0\n",
      "Unit Price          0\n",
      "Total Revenue       0\n",
      "Region              0\n",
      "Payment Method      0\n",
      "dtype: int64\n"
     ]
    }
   ],
   "source": [
    "print(data.isnull().sum())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "b0759ae4-1ff0-47e2-8926-3b49b49c81e8",
   "metadata": {},
   "outputs": [],
   "source": [
    "df_data = data.dropna()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "b5657f79-2452-4e93-a469-7452545bba44",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "User-Item Matrix:\n",
      "Product Name    1984 by George Orwell  Adidas 3-Stripes Shorts  \\\n",
      "Transaction ID                                                   \n",
      "10001                             0.0                      0.0   \n",
      "10002                             0.0                      0.0   \n",
      "10003                             0.0                      0.0   \n",
      "10004                             0.0                      0.0   \n",
      "10005                             0.0                      0.0   \n",
      "\n",
      "Product Name    Adidas Essential Track Pants  Adidas FIFA World Cup Football  \\\n",
      "Transaction ID                                                                 \n",
      "10001                                    0.0                             0.0   \n",
      "10002                                    0.0                             0.0   \n",
      "10003                                    0.0                             0.0   \n",
      "10004                                    0.0                             0.0   \n",
      "10005                                    0.0                             0.0   \n",
      "\n",
      "Product Name    Adidas Originals Superstar Sneakers  \\\n",
      "Transaction ID                                        \n",
      "10001                                           0.0   \n",
      "10002                                           0.0   \n",
      "10003                                           0.0   \n",
      "10004                                           0.0   \n",
      "10005                                           0.0   \n",
      "\n",
      "Product Name    Adidas Originals Trefoil Hoodie  \\\n",
      "Transaction ID                                    \n",
      "10001                                       0.0   \n",
      "10002                                       0.0   \n",
      "10003                                       0.0   \n",
      "10004                                       0.0   \n",
      "10005                                       0.0   \n",
      "\n",
      "Product Name    Adidas Ultraboost Running Shoes  Adidas Ultraboost Shoes  \\\n",
      "Transaction ID                                                             \n",
      "10001                                       0.0                      0.0   \n",
      "10002                                       0.0                      0.0   \n",
      "10003                                       0.0                      0.0   \n",
      "10004                                       0.0                      0.0   \n",
      "10005                                       0.0                      0.0   \n",
      "\n",
      "Product Name    Amazon Echo Dot (4th Gen)  Amazon Echo Show 10  ...  \\\n",
      "Transaction ID                                                  ...   \n",
      "10001                                 0.0                  0.0  ...   \n",
      "10002                                 0.0                  0.0  ...   \n",
      "10003                                 0.0                  0.0  ...   \n",
      "10004                                 0.0                  0.0  ...   \n",
      "10005                                 0.0                  0.0  ...   \n",
      "\n",
      "Product Name    YETI Tundra 65 Cooler  Yeti Rambler 20 oz Tumbler  \\\n",
      "Transaction ID                                                      \n",
      "10001                             0.0                         0.0   \n",
      "10002                             0.0                         0.0   \n",
      "10003                             0.0                         0.0   \n",
      "10004                             0.0                         0.0   \n",
      "10005                             0.0                         0.0   \n",
      "\n",
      "Product Name    Yeti Rambler Bottle  Yeti Rambler Tumbler  \\\n",
      "Transaction ID                                              \n",
      "10001                           0.0                   0.0   \n",
      "10002                           0.0                   0.0   \n",
      "10003                           0.0                   0.0   \n",
      "10004                           0.0                   0.0   \n",
      "10005                           0.0                   0.0   \n",
      "\n",
      "Product Name    Yeti Roadie 24 Cooler  \\\n",
      "Transaction ID                          \n",
      "10001                             0.0   \n",
      "10002                             0.0   \n",
      "10003                             0.0   \n",
      "10004                             0.0   \n",
      "10005                             0.0   \n",
      "\n",
      "Product Name    Yeti Tundra Haul Portable Wheeled Cooler  \\\n",
      "Transaction ID                                             \n",
      "10001                                                0.0   \n",
      "10002                                                0.0   \n",
      "10003                                                0.0   \n",
      "10004                                                0.0   \n",
      "10005                                                0.0   \n",
      "\n",
      "Product Name    Youth to the People Superfood Antioxidant Cleanser  \\\n",
      "Transaction ID                                                       \n",
      "10001                                                         0.0    \n",
      "10002                                                         0.0    \n",
      "10003                                                         0.0    \n",
      "10004                                                         0.0    \n",
      "10005                                                         0.0    \n",
      "\n",
      "Product Name    Zara Summer Dress  iPhone 14 Pro  iRobot Braava Jet M6  \n",
      "Transaction ID                                                          \n",
      "10001                         0.0            2.0                   0.0  \n",
      "10002                         0.0            0.0                   0.0  \n",
      "10003                         0.0            0.0                   0.0  \n",
      "10004                         0.0            0.0                   0.0  \n",
      "10005                         0.0            0.0                   0.0  \n",
      "\n",
      "[5 rows x 232 columns]\n"
     ]
    }
   ],
   "source": [
    "user_item_matrix = data.pivot_table(index='Transaction ID', columns='Product Name', values='Units Sold', fill_value=0)\n",
    "\n",
    "print(\"User-Item Matrix:\")\n",
    "print(user_item_matrix.head())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "id": "4f1b9a9a-6c28-4ee6-b331-1f374a2cf0df",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Recommended Products: ['CeraVe Hydrating Facial Cleanser']\n"
     ]
    }
   ],
   "source": [
    "from sklearn.neighbors import NearestNeighbors\n",
    "\n",
    "# Previously prepped data \n",
    "user_item_matrix = data.pivot_table(index='Transaction ID', columns='Product Name', values='Units Sold', fill_value=0)\n",
    "\n",
    "# Initialize KNN model\n",
    "knn_model = NearestNeighbors(metric='cosine', algorithm='brute')\n",
    "\n",
    "# Fit the model\n",
    "knn_model.fit(user_item_matrix.values)\n",
    "\n",
    "# Look up for Client\n",
    "#kneighbor means other products similar\n",
    "user_index = 42  \n",
    "distances, indices = knn_model.kneighbors(user_item_matrix.iloc[user_index, :].values.reshape(1, -1), n_neighbors=1) #gives the first closest\n",
    "\n",
    "# Get recommended products\n",
    "recommended_products = [user_item_matrix.columns[i] for i in indices.flatten()]\n",
    "\n",
    "print(\"Recommended Products:\", recommended_products)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ad561292-8a72-4b6c-8882-523e285f6865",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "712d8a37-10a1-4b1a-b932-6081019e5f46",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d935f13d-613a-4ed7-8206-c5dfabe27a84",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
