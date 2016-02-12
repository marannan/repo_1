#reverse a statemen
#orange is a color => color a is orange

def reverse_statement(statement):
    if len(statement) == 0:
        return statement
    
    statement_rev = "".join(reversed(statement))
     
    new_statement = ""
    for word in statement_rev.split():
        new_statement = str(new_statement) + "".join(reversed(word)) + " "
        
    
    return new_statement

if __name__ == "__main__":
    print reverse_statement("orange is my fav color")
