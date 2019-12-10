{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Import SQLAlchemy and other dependencies here\n",
    "import sqlalchemy\n",
    "from sqlalchemy.orm import Session\n",
    "from sqlalchemy import create_engine, inspect, func\n",
    "from sqlalchemy import Column, Float, Integer, String, Date\n",
    "from sqlalchemy.ext.declarative import declarative_base\n",
    "Base2 = declarative_base()\n",
    "\n",
    "import pandas as pd\n",
    "import numpy as np\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "%matplotlib inline\n",
    "from matplotlib import style\n",
    "style.use('fivethirtyeight')\n",
    "import matplotlib.pyplot as plt"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "engine = create_engine('postgresql://postgres:2646@Madhu@localhost:5432/employee_db')\n",
    "connection = engine.connect()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Create the inspector and connect it to the engine\n",
    "inspector = inspect(engine)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['employees', 'dept_emp', 'departments', 'dept_manager', 'salaries', 'titles']"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Collect the names of tables within the database\n",
    "inspector.get_table_names()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "emp_no INTEGER\n",
      "birth_date DATE\n",
      "first_name VARCHAR(35)\n",
      "last_name VARCHAR(35)\n",
      "gender VARCHAR(1)\n",
      "hire_date DATE\n"
     ]
    }
   ],
   "source": [
    "# Using the inspector to print the column names within the 'employees' table and its types\n",
    "columns = inspector.get_columns('employees')\n",
    "for column in columns:\n",
    "    print(column[\"name\"], column[\"type\"])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [],
   "source": [
    "#create employees class\n",
    "class employees(Base2):\n",
    "    __tablename__ = 'employees'\n",
    "    \n",
    "    emp_no = Column(Integer, primary_key=True)\n",
    "    birth_date = Column(Date)\n",
    "    first_name = Column(String)\n",
    "    last_name = Column(String)\n",
    "    gender = Column(String)\n",
    "    hire_date = Column(Date)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [],
   "source": [
    "session = Session(engine)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "179973\n",
      "120051\n"
     ]
    }
   ],
   "source": [
    "# print sums by gender\n",
    "male = session.query(employees).filter_by(gender = 'M').count()\n",
    "female = session.query(employees).filter_by(gender = 'F').count()\n",
    "\n",
    "print(male)\n",
    "print(female)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "emp_no INTEGER\n",
      "salary INTEGER\n",
      "from_date DATE\n",
      "to_date DATE\n"
     ]
    }
   ],
   "source": [
    "# Using the inspector to print the column names within the 'Salaries' table and its types\n",
    "columns = inspector.get_columns('salaries')\n",
    "for column in columns:\n",
    "    print(column[\"name\"], column[\"type\"])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [],
   "source": [
    "#create salaries class\n",
    "class salaries(Base2):\n",
    "    __tablename__ = 'salaries'\n",
    "    emp_no = Column(Integer, primary_key=True)\n",
    "    salary = Column(Integer)\n",
    "    from_date = Column(Date)\n",
    "    to_date = Column(Date)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [],
   "source": [
    "#query the salaries table\n",
    "x = session.query(salaries.salary)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Plot the Results in a Matplotlib bar chart\n",
    "df = pd.DataFrame(x, columns=['salary'])\n",
    "a = np.array(df)\n",
    "x = a[0:,0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 864x576 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "fig, ax = plt.subplots(figsize=(12, 8))\n",
    "\n",
    "# the histogram of the data\n",
    "n, bins, patches = plt.hist(x, 12, facecolor='purple', alpha=0.75)\n",
    "\n",
    "plt.xlabel('Salary')\n",
    "plt.ylabel('Frequency')\n",
    "plt.title('Histogram of Employee Salaries')\n",
    "\n",
    "plt.grid(True)\n",
    "plt.show()\n",
    "fig.savefig('emp_sal_histogram.png')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "emp_no INTEGER\n",
      "title VARCHAR(35)\n",
      "from_date DATE\n",
      "to_date DATE\n"
     ]
    }
   ],
   "source": [
    "# Using the inspector to print the column names within the 'titles' table and its types\n",
    "columns = inspector.get_columns('titles')\n",
    "for column in columns:\n",
    "    print(column[\"name\"], column[\"type\"])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [],
   "source": [
    "#create titles class\n",
    "class titles(Base2):\n",
    "    __tablename__ = 'titles'\n",
    "    \n",
    "    emp_no = Column(Integer, primary_key=True)\n",
    "    title = Column(String)\n",
    "    from_date = Column(Date)\n",
    "    to_date = Column(Date)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[('Engineer'),\n",
       " ('Senior Engineer'),\n",
       " ('Manager'),\n",
       " ('Assistant Engineer'),\n",
       " ('Staff'),\n",
       " ('Senior Staff'),\n",
       " ('Technique Leader')]"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Query titles using `distinct`\n",
    "session.query(titles.title).distinct().all()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([['Senior Staff', Decimal('58503.286614325870')],\n",
       "       ['Staff', Decimal('58465.271903604585')],\n",
       "       ['Manager', Decimal('51531.041666666667')],\n",
       "       ['Technique Leader', Decimal('48580.505772148559')],\n",
       "       ['Engineer', Decimal('48539.781423093311')],\n",
       "       ['Senior Engineer', Decimal('48506.751805626598')],\n",
       "       ['Assistant Engineer', Decimal('48493.204785827604')]],\n",
       "      dtype=object)"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Query average salaries by title\n",
    "a = session.query(titles.title, func.avg(salaries.salary)).\\\n",
    "    filter(salaries.emp_no == titles.emp_no).\\\n",
    "    group_by(titles.title).\\\n",
    "    order_by(func.avg(salaries.salary).desc()).all()\n",
    "x = np.array(a)\n",
    "x"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 864x576 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "fig, ax = plt.subplots(figsize=(12, 8))\n",
    "N = 7\n",
    "title1 = x[0:,0]\n",
    "avg_sal = x[0:,1]\n",
    "ind = np.arange(N)    # the x locations for the groups\n",
    "width = 0.5       # the width of the bars: can also be len(x) sequence\n",
    "\n",
    "plt.bar(ind, avg_sal, width)\n",
    "\n",
    "plt.ylabel('Avg. Salary ($)')\n",
    "plt.title('Avg. Salary by Title')\n",
    "plt.xticks(ind, (title1), rotation=45)\n",
    "\n",
    "plt.show()\n",
    "fig.savefig('avg_sal_title.png')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "file_extension": ".py",
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.7.3"
  },
  "mimetype": "text/x-python",
  "name": "python",
  "npconvert_exporter": "python",
  "pygments_lexer": "ipython3",
  "version": 3
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
