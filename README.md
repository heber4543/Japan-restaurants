# webscraping
Script to scrape *tabelog.com*

## Input
This code receives as input a text file (.txt) with the comma separated URL's of the pages you need to scrape from tabelog.com
*'restaurantes_zonas.txt'* is an example of the input text file

On line 26, in the *path* variable you must enter the path to the text file, inside the double quotes

## Output
This code returns an excel or comma-separated file (your choice) with data about restaurants or establishments in tablelog.com.

The table headers are: 
- **restaurants:** this column contains the name of the establishment
- **link:** this column contains the link of the establishment in tablelog
- **address:** this column contains the address of the establishment
- **contact:** this column contains the establishment's telephone number
- **rating:** this column contains the rating of the establishment in tablelog
- **city:** this column contains the data provided by tablelog, be it city, state, country, neighborhood, etc.

On line 172 and 173 are the options to choose whether you want a comma separated file or an excel file. But you still have to enter the necessary data, such as the path where the file will be saved, depending on the option you choose.

## Additional indications

The code is commented in spanish, if you speak another language you will have to translate each commented line (they come at the beginning with #) to understand what each function does or what each variable saves.

This code can be adapted to different pages, not only to tablelog. In fact it was also used for Yelp. You just need to make some adjustments, if so, you can contact me to adjust it.

If you have any questions with the code, do not hesitate to contact me: *heberzapata17@gmail.com*
