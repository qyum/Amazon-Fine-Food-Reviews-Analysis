#............find duplicate data...........
display= pd.read_sql_query("""
                            SELECT * FROM Reviews
                            WHERE Score != 3 AND UserId="AR5J8UI46CURR"
                            ORDER BY ProductID
                            """, 
                            con)
display.head()
