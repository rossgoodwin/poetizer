poetizer
========

Generates free or fixed verse poetry from any text corpus using Ngram natural language generator (markov chains) + pos tagging + rhyme identifier + metrical / grammatical rules.

To run Poetizer, assemble an English text corpus (news articles, academic papers, fiction, poetry, or any other structured text) and remove all punctuation. (Poetizer is currently optimized to produce poetry without punctuation.) 

Run Poetizer from the terminal using the following arguments:

    $ python poetizer.py [corpus].txt [rhyme scheme]

Rhyme Scheme & Line Breaks
__________________________

The rhyme scheme should be a list of letters. For example, `ABABCDCDEFEFGG` would produce 14-line rhyming sonnets, and ABCDE would produce 5-line poems with no end-of-line rhymes. Adding numbers will make the program repeat lines. For example, `1AB12CD2` would generate 8-line poems with the 1st line repeated as the 4th line and the 5th line repeated as the 8th line.

Alternatively, you can let the computer decide where to make line breaks using the following syntax for your rhyme scheme argument: `natural_[length]_[v or n]`

The number you input for [length] determines the number of the lines the computer starts with. Putting v at the end will favor verbs for line endings, while n will favor nouns.

Optional Arugments
__________________

You can append the standard arguments listed above with a set of optional arguments to further customize Poetizer's output. The complete list of arguments would look like this:

    $ python poetizer.py [corpus].txt [rhyme scheme] [number of poems] [syllables per line] [output format] [show diagnostics]

Every additional argument requires the previous arguments.

### Number of Poems

Default value is 10. Enter any positive integer for this argument.

### Syllables Per Line

Default value is 10. Enter any positive integer for this argument. Note that line lengths will be approximate.

### Output Format

Default value is `pt`, which outputs plain text. Inputting `latex` will produce latex-friendly output. Inputting `read` will add a period to the end of lines to allow text-to-speech programs to pause in the appropriate locations.

### Show Diagnostics

Default value is y, which produces some text letting you know what is happening as before the computer generates poems. To turn this off, set value to n.







