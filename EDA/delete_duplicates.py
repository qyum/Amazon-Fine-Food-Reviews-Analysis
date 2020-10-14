#..sorting ascending order...
sorted_data=filtered_data.sort_values('ProductId',ascending=True,
                                     kind='quicksort')

#...delete duplicates.....................
final=sorted_data.drop_duplicates(subset={"UserId","ProfileName",
                                          "Time","Text"},
                                         keep='first',
                                         inplace=False)
