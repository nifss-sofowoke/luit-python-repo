# how to raise exceptions yourself
    # through assertions
    
# assertions are assumptions in your program that you think should always be true
# an assertion error is always called when the keyword 'assert' is used, and the condition privileges within the brackets are not satisfied

# assertion uses
    # debugging/testing your code
        # assertions can be added as sanity checks at the beginning of a function to make sure it receives correct data

    # documenting your code 
    
# do not use assertions to:
    # validate user input
        # b/c it is impossible to turn off assertions when you publish a program to users. turning off assertions woukd mean losing all the code that validates user input
        
    # handle assertionerrors in try-except
    
    