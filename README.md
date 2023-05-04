# ChatSort

ChatGPT sort an array in an "unknown" programming language.

The program will evaluate a (ChatGPT given) sorting algorithm in the
(user given) programming language on the user's computer. The program
will submit any errors the programming language gives and ask ChatGPT
to correct the program until the list is sorted correctly.

All programming languages except for Python3 are supported. This is
because the initial input program was written in Python3 (by ChatGPT).

An attempt from our future overloads at programming in (ba)sh:

```
list = [1, 2, 3, 4]
for i in range(len(list)):    # Loop through index of list.

        min_index =i             # Assume first index is the smallest number

        for j in range (i + 1 , len(list)):   # Start comparing with second element
              if list[j] < list[min_index]:      # Check which among two elements is lower                                         min_index=j                  # If found a smaller element than current smallest one then assign it to new 'smallest' variable as its index value                                                                                
                                                                                                                                                       # Swap values from outer loop iteration and inner loop iterations                                                         tempNum= lisctetttptoFaiéntstovrytomeraxllthTeealsmallenteEstecigitnpiexrcseasdscapdeethEvinenintgrgosmlalleastinidnexerocaehchomteeftsworiltloeanponpetrdrueuncsrhompciextloepmesrotskefalbionrlcevsdriyedaryynugmnuerCsoncatenteaitebonltlthetservilulastele-carcthaormcreitesstrinnsgloesueroefdx:utlsiwatswn" output+= str(tempNum)+ ","; print("The sorted list of numbers are:"+output);
```

## Usage

```
export OPENAI_API_KEY="<your-secret-key>"
# ./chatsort.py <comma-seperated-list> <build-and-run-command>
./chatsort.py "10, 8, 9, 7, 6, 2, 3, 4, 1" "make c"
```

Some other pre-provided languages are given in the `Makefile` See
example.log for an example run.

By default the program give you the chance to abort the process after 5
attempts for the AI. In my experience it's better to start from scratch
at this point.

## References

* [StackSort](https://xkcd.com/1185/) on XKCD
