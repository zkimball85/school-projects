{
    "metadata": {
        "kernelspec": {
            "name": "python3",
            "display_name": "Python 3 (ipykernel)",
            "language": "python"
        },
        "language_info": {
            "name": "python",
            "version": "3.13.2",
            "mimetype": "text/x-python",
            "codemirror_mode": {
                "name": "ipython",
                "version": 3
            },
            "pygments_lexer": "ipython3",
            "nbconvert_exporter": "python",
            "file_extension": ".py"
        }
    },
    "nbformat_minor": 2,
    "nbformat": 4,
    "cells": [
        {
            "cell_type": "code",
            "source": [
                "#Land Calculation\n",
                "\n",
                "ONE_ACRE = 43560.0\n",
                "\n",
                "# A float should be used since the answer could give you a number with a decimal. \n",
                "user_sqft = float(input('Whats the total square feet of your tract? '))\n",
                "\n",
                "total_acres = user_sqft / ONE_ACRE\n",
                "\n",
                "# dont forget to reign in the decimal place. .2f will allow 2 decimal places\n",
                "print(f'You have {total_acres:.2f} acres.')\n",
                "\n",
                ""
            ],
            "metadata": {
                "azdata_cell_guid": "a2dd8b1a-052d-4740-b2b8-6147cf0592c4",
                "language": "python",
                "tags": []
            },
            "outputs": [
                {
                    "name": "stdout",
                    "text": "You have 108.13 acres.\n",
                    "output_type": "stream"
                }
            ],
            "execution_count": 6
        }
    ]
}