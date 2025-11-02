# Tinderbox Action Code Reference (v10.x)

*Based on [aTbRef v10.2.0](https://acrobatfaq.com/atbref10/) - The most current and comprehensive Tinderbox reference*

## System Attributes

### Core Attributes
- `$Name` - The note's name/title
- `$Text` - The note's text content (StyledString type)
- `$Color` - The note's color (hex values like #ff0000 or color names)
- `$Created` - Creation date (read-only)
- `$Modified` - Last modification date (read-only)
- `$Path` - Full path to the note (read-only)
- `$Container` - Path to the note's container

### Action Attributes  
- `$Rule` - Code executed periodically (every few seconds)
- `$OnAdd` - Code executed when note added to container
- `$OnRemove` - Code executed when note removed from container
- `$Edict` - Code executed periodically (about once per hour)
- `$AgentAction` - Code executed by agent on matched aliases

### Date Attributes
- `$Date` - User-defined date attribute
- Date components via dot operators: `.day`, `.month`, `.year`, `.hour`, `.minute`, `.second`, `.weekday`, `.week`
- Special date values: `"never"` (no date set), `"today"`, `"now"`

### Collection Attributes
- `$Tags` - Tags (semicolon-separated Set)
- Lists and Sets use semicolon delimiters: `"item1;item2;item3"`
- Dictionary attributes store key-value pairs

## Operators

### Arithmetic
- `+` - Addition, string concatenation, set union
- `-` - Subtraction, set removal
- `*` - Multiplication, string repetition
- `/` - Division

### Comparison
- `==` - Equality (preferred over `=` for comparison)
- `!=` - Not equal
- `>`, `>=`, `<`, `<=` - Greater/less than comparisons
- `=` - Assignment (avoid for comparison)

### Logical
- `!` - Logical NOT
- `&` - Logical AND
- `|` - Logical OR

## String Methods (Dot Operators)

### String Testing & Analysis
- `.contains("pattern")` - Case-sensitive regex search (returns position or 0)
- `.icontains("pattern")` - Case-insensitive regex search
- `.containsAnyOf(regexList)` - Tests if string matches any regex in list
- `.beginsWith("string")` - Tests if string starts with pattern
- `.endsWith("string")` - Tests if string ends with pattern
- `.empty()` - Returns true if string is empty
- `.find("literal")` - Find literal string (not regex)
- `.wordCount()` - Count words in string
- `.wordList()` - Return list of words
- `.paragraphCount()` - Count paragraphs
- `.sentences()` - Return list of sentences

### String Manipulation
- `.lowercase()` - Convert to lowercase
- `.uppercase()` - Convert to uppercase  
- `.capitalize()` - Capitalize first letter of each word
- `.replace("regex","replacement")` - Replace using regex patterns
- `.substr(start,length)` - Extract substring (0-based, supports negative indices)
- `.split("regex")` - Split into list using regex
- `.trim()` - Remove whitespace from ends
- `.reverse()` - Reverse string
- `.size()` - Get string length

### String Parsing (v10 Stream Processing)
- `.captureLine()` - Capture next line from string
- `.captureWord()` - Capture next word
- `.captureNumber()` - Capture next number
- `.captureTo("pattern")` - Capture up to pattern
- `.captureRest()` - Capture remaining text
- `.skipWhitespace()` - Skip whitespace
- `.skipTo("pattern")` - Skip to pattern
- `.expect("pattern")` - Expect specific pattern

## List/Set Methods (Dot Operators)

### List Operations & Testing
- `.count` or `.count()` - Number of items  
- `.at(N)` - Get Nth item (0-based, negatives work from end)
- `.contains("item")` - Test if list contains item (case-sensitive)
- `.icontains("item")` - Test if list contains item (case-insensitive)
- `.containsAnyOf(regexList)` - Test if contains any regex pattern
- `.empty()` - Returns true if list is empty
- `.first()` - Get first item
- `.last()` - Get last item
- `.randomItem()` - Get random item from list

### List Sorting & Ordering
- `.sort([attributeRef])` - Case-sensitive lexical sort, optionally by attribute
- `.isort([attributeRef])` - Case-insensitive lexical sort  
- `.nsort([attributeRef])` - Numeric sort
- `.reverse()` - Reverse current order
- `.unique()` - Remove duplicates

### List Analysis
- `.max()` - Largest item (lexical or numeric)
- `.min()` - Smallest item (lexical or numeric) 
- `.sum()` - Sum numeric items
- `.avg()` - Average of numeric items

### List Manipulation
- `.extend(aList)` - Add all items from another list
- `.remove("item")` - Remove specific item
- `.replace("old","new")` - Replace items matching regex
- `.intersect(otherList)` - Items common to both lists
- `.format("delimiter")` - Join with custom delimiter

### List Iteration (v10)
- `.each(var){actions}` - Loop through each item
- `.collect(var, expression)` - Collect results of expression for each item
- `.collect_if(var, condition, expression)` - Conditional collection
- `.any(var, expression)` - Test if any item meets condition
- `.every(var, expression)` - Test if all items meet condition
- `.count_if(var, condition)` - Count items meeting condition
- `.sum_if(var, condition)` - Sum items meeting condition

## Modern Functions & Features (v10)

### Group Functions
- `collect(scope, expression)` - Collect expression results from scope
- `collect_if(scope, condition, expression)` - Conditional collection
- `sum(scope, expression)` - Sum expression results
- `sum_if(scope, condition, expression)` - Conditional sum
- `avg(scope, expression)` - Average expression results
- `avg_if(scope, condition, expression)` - Conditional average
- `count(scope)` - Count items in scope
- `count_if(scope, condition)` - Count items meeting condition
- `any(scope, condition)` - Test if any item matches condition
- `every(scope, condition)` - Test if all items match condition

### Dictionary Functions (v10)
- `dictionary("key1:value1;key2:value2")` - Create dictionary from string
- `Dictionary.add(itemDict)` - Add dictionary items
- `Dictionary.contains("key")` - Test if key exists
- `Dictionary.keys()` - Get list of all keys
- `Dictionary.count()` - Number of key-value pairs
- `Dictionary["key"]` - Get/set value for key

### Advanced Processing
- `fetch(url, headers, attrName, cmd)` - HTTP requests and API calls
- `JSON.each(path){actions}` - Process JSON data
- `XML.each(path){actions}` - Process XML data
- `runCommand(cmd, input, dir)` - Execute shell commands

### Date Functions
- `date("string")` - Parse date string
- `format(date, "formatString")` - Format date output
- `days(start, end)` - Days between dates
- `hours(start, end)` - Hours between dates
- `between(value, min, max)` - Test if value in range

### String Functions
- `capitalize("string")` - Capitalize words
- `lowercase("string")` - Convert to lowercase
- `uppercase("string")` - Convert to uppercase
- `substr(string, start, length)` - Extract substring

## Designators (Note References)

### Single Note Designators
- `parent` - Parent note
- `child` - First child note
- `nextSibling` - Next sibling
- `prevSibling` - Previous sibling
- `firstSibling` - First sibling
- `lastSibling` - Last sibling
- `this` - Current note
- `that` - Previously referenced note

### Group Designators
- `children` - All child notes
- `descendants` - All descendant notes
- `ancestors` - All ancestor notes
- `siblings` - All sibling notes
- `all` - All notes in document

## Control Structures

### Conditional Statements
```
if(condition){
    // action when true
} else if(condition2){
    // action when condition2 true
} else {
    // default action
}
```

### Loops
```
// For each item in a group
children.each(var){
    // use 'var' to reference current item
}

// For each item in a list
$MyList.each(item){
    // use 'item' to reference current list value
}
```

### Local Variables
```
var(myVar){
    myVar = "some value";
    // use myVar within this scope
}
```

## Best Practices

1. Use `==` for comparison, `=` for assignment
2. Quote string literals: `"text"` not `text`
3. Use dot operators for cleaner code: `$Text.contains("word")`
4. Test conditions with realistic data
5. Use descriptive variable names
6. Comment complex logic
7. Keep actions focused on single tasks
8. Use proper indentation for readability

## Color Manipulation
```
// Set color directly
$Color = "red";
$Color = "#ff0000";

// Use color dot operators
$Color.red = 128;     // Set red channel (0-255)
$Color.hue = 180;     // Set hue (0-360 degrees)
$Color.brightness = 75; // Set brightness (0-100%)
```

## Common Patterns

### Tag Management
```
// Add tag if not present
if(!$Tags.contains("important")){
    $Tags = $Tags + ";important";
}

// Remove tag
$Tags = $Tags.replace("urgent;","").replace(";urgent","");
```

### Date Handling  
```
// Set date components
$Date.year = 2024;
$Date.month = 12;
$Date.day = 25;

// Format dates
$FormattedDate = $Date.format("l");  // Short format
$CustomFormat = format($Date, "D M Y"); // Custom format
```

## Special Note Locations

 ```/Hints/Library/``` is effectively the equivalent to a `UNIX $PATH` location. Functions included in the $TEXT of notes in this location are available in global scope to other notes Rules, Actions, or Edicts code.

 ## Use of Notes & Prototypal Inheritance

 Prefer inheritance and note-based organization over large monolithic action code blocks. This enhances reusability, maintainability, and clarity of your Tinderbox action code.
 It is often better to create dedicated notes for specific functions or logic, and then reference these notes in your action code. This modular approach allows for easier updates and debugging, as well as promoting code reuse across different parts of your Tinderbox documents.
 Certain functions and properties are better achieved through prototypal inheritance or note references rather than embedding all logic in a single action code block.

## Modular Development Patterns

### Function Libraries
Create dedicated notes with reusable functions and copy them to `/Hints/Library/` for global access:

```
// In a source note
function myUtilityFunction(param) {
    // function implementation
}

// Copy to library
create("/Hints/Library", "MyModule");
$Text("/Hints/Library/MyModule") = $Text("Source Note");
```

### Module Organization
Break complex functionality into focused modules:

- **Core Utilities**: Logging, validation, basic helpers
- **Attribute Management**: Custom attribute creation and configuration  
- **Prototype Builder**: Note prototype definitions
- **Template Builder**: HTML export templates
- **Project Structure**: Folder hierarchy creation
- **Workspace Initializer**: Orchestration and coordination

### Installation Patterns
Use edict-based installation to copy modules to the library:

```
// Edict copies source notes to /Hints/Library/
function copyModuleToLibrary(moduleName, sourceNoteName) {
    var(targetPath, sourceText){
        targetPath = "/Hints/Library/" + moduleName;
        sourceText = $Text(sourceNoteName);
        
        create("/Hints/Library", moduleName);
        $Text(targetPath) = sourceText;
        $Badge(targetPath) = "code";
        $Searchable(targetPath) = false;
    }
}
```

### Error Handling and Validation
Implement comprehensive validation in modular functions:

```
function validatePrerequisites() {
   var(isValid){
      isValid = true;
      
      if($Name == "untitled") {
         logMessage("ERROR: Cannot initialize untitled document");
         isValid = false;
      }
      
      if($IsProcessing == true) {
         logMessage("WARNING: Processing already in progress");  
         isValid = false;
      }
   }
   return isValid;
}
```

### Processing Flags
Use processing flags to prevent recursive execution:

```
function buildProject() {
   if ($IsProcessing == true || $Name == "untitled") {
      return;
   }
   
   $IsProcessing = true;
   // ... do work ...
   $IsProcessing = false;
}
```

### Centralized Logging
Implement consistent logging across all modules:

```
function logMessage(message) {
   if(!exists("/Log")) {
      create("/Log");
      $Badge("/Log") = "edit";
   }
   $Text("/Log") = $Text("/Log") + "[" + format(now,"h:mm:ss") + "] " + message + "\n";
}
```