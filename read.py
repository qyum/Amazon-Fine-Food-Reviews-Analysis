#...............................reading data..............................

con=sqlite3.connect('G:/Amazon_fine_food_review_dataset/database.sqlite')
filtered_data=pd.read_sql_query("""
                                SELECT * FROM Reviews
                                WHERE Score !=3 LIMIT 5000
                                """,con)
#print(filtered_data.head())
def partition(x):
    if x<3:
        return 0
    else:
        return 1
actualScore=filtered_data['Score']
#print(actualScore)
pos_neg=actualScore.map(partition)
#print(pos_neg)
filtered_data['Score']=pos_neg

filtered_data.shape
filtered_data.head()

display = pd.read_sql_query("""
                        SELECT UserId, ProductId, ProfileName, Time, Score, Text, COUNT(*)
                        FROM Reviews
                        GROUP BY UserId
                        HAVING Count(*)>1
                        """, 
                        con)
