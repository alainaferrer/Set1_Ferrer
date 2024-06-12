{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "2c1fedc4-8e50-4bae-8b0a-9fe174e21640",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'gross_pay' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[0;32mIn[1], line 29\u001b[0m\n\u001b[1;32m      2\u001b[0m \u001b[38;5;250m    \u001b[39m\u001b[38;5;124;03m'''Savings.\u001b[39;00m\n\u001b[1;32m      3\u001b[0m \n\u001b[1;32m      4\u001b[0m \u001b[38;5;124;03m    This function calculates the money remaining\u001b[39;00m\n\u001b[0;32m   (...)\u001b[0m\n\u001b[1;32m     24\u001b[0m \u001b[38;5;124;03m        the number of centavos remaining from an employee's pay after taxes and expenses\u001b[39;00m\n\u001b[1;32m     25\u001b[0m \u001b[38;5;124;03m    '''\u001b[39;00m\n\u001b[1;32m     26\u001b[0m     \u001b[38;5;66;03m# Replace `pass` with your code.\u001b[39;00m\n\u001b[1;32m     27\u001b[0m     \u001b[38;5;66;03m# Stay within the function. Only use the parameters as input. The function should return your answer.\u001b[39;00m\n\u001b[0;32m---> 29\u001b[0m money_remaining\u001b[38;5;241m=\u001b[39m(((gross_pay\u001b[38;5;241m-\u001b[39m(gross_pay\u001b[38;5;241m*\u001b[39mtax_rate))\u001b[38;5;241m/\u001b[39m\u001b[38;5;241m/\u001b[39m\u001b[38;5;241m1\u001b[39m)\u001b[38;5;241m-\u001b[39mexpenses)\n\u001b[1;32m     30\u001b[0m \u001b[38;5;28;01mreturn\u001b[39;00m(money_remaining)\n",
      "\u001b[0;31mNameError\u001b[0m: name 'gross_pay' is not defined"
     ]
    }
   ],
   "source": [
    "def savings(gross_pay, tax_rate, expenses):\n",
    "    '''Savings.\n",
    "\n",
    "    This function calculates the money remaining\n",
    "        for an employee after taxes and expenses.\n",
    "\n",
    "    To get the take-home pay of an employee, we will\n",
    "        follow the following process:\n",
    "        1. Apply the tax rate to the gross pay of the employee; round down\n",
    "        2. Subtract the expenses from the after-tax pay of the employee\n",
    "\n",
    "    Parameters\n",
    "    ----------\n",
    "    gross_pay: int\n",
    "        the gross pay of an employee for a certain time period, expressed in centavos\n",
    "    tax_rate: float\n",
    "        the tax rate for a certain time period, expressed as a number between 0 and 1 (e.g., 0.12)\n",
    "    expenses: int\n",
    "        the expenses of an employee for a certain time period, expressed in centavos\n",
    "\n",
    "    Returns\n",
    "    -------\n",
    "    int\n",
    "        the number of centavos remaining from an employee's pay after taxes and expenses\n",
    "    '''\n",
    "    # Replace `pass` with your code.\n",
    "    # Stay within the function. Only use the parameters as input. The function should return your answer.\n",
    "    money_remaining=(((gross_pay-(gross_pay*tax_rate))//1)-expenses)\n",
    "    return(money_remaining)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "aac9914a-4936-44a2-881a-313d3e4b287e",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'total_material' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[0;32mIn[3], line 34\u001b[0m\n\u001b[1;32m      2\u001b[0m \u001b[38;5;250m    \u001b[39m\u001b[38;5;124;03m'''Material Waste.\u001b[39;00m\n\u001b[1;32m      3\u001b[0m \n\u001b[1;32m      4\u001b[0m \u001b[38;5;124;03m    This function calculates how much material input will be wasted\u001b[39;00m\n\u001b[0;32m   (...)\u001b[0m\n\u001b[1;32m     29\u001b[0m \u001b[38;5;124;03m        the amount of remaining material expressed with its unit (e.g., \"10kg\").\u001b[39;00m\n\u001b[1;32m     30\u001b[0m \u001b[38;5;124;03m    '''\u001b[39;00m\n\u001b[1;32m     31\u001b[0m     \u001b[38;5;66;03m# Replace `pass` with your code.\u001b[39;00m\n\u001b[1;32m     32\u001b[0m     \u001b[38;5;66;03m# Stay within the function. Only use the parameters as input. The function should return your answer.\u001b[39;00m\n\u001b[0;32m---> 34\u001b[0m material_waste\u001b[38;5;241m=\u001b[39m(\u001b[38;5;28mstr\u001b[39m(total_material\u001b[38;5;241m-\u001b[39m(job_consumption\u001b[38;5;241m*\u001b[39mnum_jobs))\u001b[38;5;241m+\u001b[39mmaterial_units)\n\u001b[1;32m     35\u001b[0m \u001b[38;5;28;01mreturn\u001b[39;00m(material_waste)\n",
      "\u001b[0;31mNameError\u001b[0m: name 'total_material' is not defined"
     ]
    }
   ],
   "source": [
    "def material_waste(total_material, material_units, num_jobs, job_consumption):\n",
    "    '''Material Waste.\n",
    "\n",
    "    This function calculates how much material input will be wasted\n",
    "        after running a certain number of jobs that consume\n",
    "        a set amount of material.\n",
    "\n",
    "    To get the waste of a set of jobs:\n",
    "        1. Multiply the number of jobs by the material consumption per job.\n",
    "        2. Subtract the total material consumed from the total material available.\n",
    "\n",
    "    The users of this function also want you to format the output as a string, annotated with the\n",
    "        units in which the material is expressed. Do not add a space between the number and the unit.\n",
    "\n",
    "    Parameters\n",
    "    ----------\n",
    "    total_material: int\n",
    "        the total material available\n",
    "    material_units: str\n",
    "        the units used to express a quantity of the material (e.g., \"kg\", \"L\", etc.)\n",
    "    num_jobs: int\n",
    "        the number of jobs to run\n",
    "    job_consumption: int\n",
    "        the amount of material consumed per job\n",
    "\n",
    "    Returns\n",
    "    -------\n",
    "    str\n",
    "        the amount of remaining material expressed with its unit (e.g., \"10kg\").\n",
    "    '''\n",
    "    # Replace `pass` with your code.\n",
    "    # Stay within the function. Only use the parameters as input. The function should return your answer.\n",
    "    material_waste=(str(total_material-(job_consumption*num_jobs))+material_units)\n",
    "    return(material_waste)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ca8f3555-3a11-4895-8d60-918e17e95bee",
   "metadata": {},
   "outputs": [],
   "source": [
    "def interest(principal, rate, periods):\n",
    "    '''Interest.\n",
    "\n",
    "    This function calculates the final value of an investment after\n",
    "        gaining simple interest over a number of periods.\n",
    "\n",
    "    To calculate simple interest, simply multiply the principal to the quantity (rate * time).\n",
    "        Add this amount to the principal to get the final value.\n",
    "\n",
    "    Round down the final amount.\n",
    "\n",
    "    Parameters\n",
    "    ----------\n",
    "    principal: int\n",
    "        the principal (i.e., starting) amount invested, expressed in centavos\n",
    "    rate: float\n",
    "        the interest rate per period, expressed as a decimal representation of a percentage (e.g., 3% is 0.03)\n",
    "    periods: int\n",
    "        the number of periods invested\n",
    "\n",
    "    Returns\n",
    "    -------\n",
    "    int\n",
    "        the final value of the investment\n",
    "    '''\n",
    "    # Replace `pass` with your code.\n",
    "    # Stay within the function. Only use the parameters as input. The function should return your answer.\n",
    "    interest=((principal+(principal*(rate*periods)))//1)\n",
    "    return(interest)"
   ]
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
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
