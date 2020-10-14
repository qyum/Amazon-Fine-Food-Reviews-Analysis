#....HelpfulnessNumerator is greater than HelpfulnessDenominator which is not 
#practically possible hence these two rows too are removed from calcualtions.............

final=final[final.HelpfulnessNumerator<=final.HelpfulnessDenominator]
final.head()
final['Score'].value_counts()
