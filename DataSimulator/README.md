# Data Simulation

This is a program that creates movement data and CSV files for a set number of cows. In order to develop the visualization, data is needed to test it. This program creates that data. It creates a fake cow and has it move within a constrained field. As it moves (or doesn't), the program records that and eventually outputs all of that data into a CSV file.

## Implementation

For this program, we use a python module called `csv`. Using this module, we can open a file and easily write to the CSV file. The module takes in data in an array of arrays format. You can see this here when we set the header of the CSV file.

```
data = [["tag", "time", "x", "y"]]
```


We loop through the number of tags and create the data and csv file for each tag. For our purposes, we start with a point in the middle and randomly move based on a set value. Once we have that value, we add it to our list of data points and move on. We don't need to remember it anymore, so we only create one Point object and over time keep moving it. Our point class has a function that randomly moves the data.

```
def movePointRandom(self, avgDistanceCovered):
        secure_random = random.SystemRandom()
        doMove = random.randint(0,4)
        if doMove == 1:
            randomX = secure_random.uniform(-avgDistanceCovered, avgDistanceCovered)
            randomY = secure_random.uniform(-avgDistanceCovered, avgDistanceCovered)
            if self.checkMinMax(randomX, randomY):
                self.x += randomX
                self.y += randomY
```

Based on an assumed average distance that could be covered in 5 seconds (because each point is 5 seconds after), we move the cattle. Also, there is only a 20% chance that the cattle will move at all. I'm assuming cattle are not constantly moving and as such, there needs to be a possibility of staying where they are. Lastly, we check to make sure the cattle stay within the bounds of the field bothing moving them that direction. In the real life situation, the cattle would not be able to go outside the fences, so in our simulated data they should not.

## Reflection

Creating data that is simular to animal movements is very difficult. In reality, this data would not be realistic. I imagine that the cattle would not move around as much as this program has them. In the future, it would be helpful to have example data to use. With example data, we could use machine learning in order to simulate similar data. 
