# Tinderbox Action Code Workspace

A comprehensive workspace for developing, testing, and organizing Tinderbox action code and automation scripts.

## Overview

This workspace provides a structured environment for creating Tinderbox actions, which are small code snippets that can be executed within the Tinderbox personal knowledge management application. It now includes both traditional action code files and a modern **modular generation system** for maintaining complex installers.

## Directory Structure

- **`/actions/`** - Main action code files
  - **Production Ready**: `complete-installer.txt` - Working project automation installer (210 lines)
  - **Generated**: `generated-installer.txt` - Auto-generated from YAML definitions (225 lines)  
  - **Template**: `template.txt` - Starting point for new actions
  - Store your primary Tinderbox action code here organized by functionality

- **`/builder/`** - **NEW: Modular Generation System**
  - **`build.py`** - Python script to generate installers from YAML definitions
  - **`definitions/`** - Structured YAML files defining workspace components:
    - `workspace.yaml` - Folder structure and basic configuration
    - `prototypes.yaml` - All prototype definitions with templates and attributes  
    - `templates.yaml` - HTML export templates
    - `functions.yaml` - Complete library function modules
  - **Benefits**: Modular maintenance, version control, validation, reproducible builds

- **`/scripts/`** - Automation and utility scripts
  - Helper scripts and automation tools
  - Build and deployment scripts

- **`/examples/`** - Sample implementations
  - Example action code for learning
  - Common patterns and templates

- **`/docs/`** - Documentation and guides
  - Action code documentation
  - Usage guides and best practices

- **`/tests/`** - Test files and validation scripts
  - Test your actions before deployment
  - Validation and debugging tools

## Getting Started

### Quick Start
1. **Use Existing Installer**: Copy `actions/complete-installer.txt` to a Tinderbox note's $Rule, set $RuleDisabled=false
2. **Create Custom Installer**: Modify YAML definitions in `builder/definitions/` then run `python builder/build.py`
3. **Test Actions**: Use sample data from `tests/` directory
4. **Learn Patterns**: Study examples in `examples/` directory

### Modular Generation Workflow
```bash
# Install dependencies (one time)
pip install -r builder/requirements.txt

# Validate definitions
python builder/build.py --validate

# Generate installer  
python builder/build.py -o actions/my-installer.txt

# Or use default output
python builder/build.py  # outputs to actions/generated-installer.txt
```

## Development Guidelines

- Follow Tinderbox action code conventions
- Test actions thoroughly before deployment
- Document action parameters and expected usage
- Use descriptive names for your action files
- Organize code by functionality or use case

## Action Code Best Practices

- Use `==` for comparisons, `=` for assignment
- Always quote string literals: `"text"` not `text`
- Use dot operators for cleaner code: `$Text.contains("word")`
- Keep actions focused on single tasks
- Use descriptive variable names and add comments
- Test with realistic data scenarios
- Handle edge cases (empty values, missing attributes)
- Use proper indentation for readability
- Consider performance with large datasets

## Key Tinderbox Concepts

### Attributes and Data Types
- **String**: Text data, manipulated with dot operators like `.contains()`, `.replace()`
- **Number**: Numeric values, support arithmetic operations
- **Date**: Date/time values with components accessible via `.year`, `.month`, `.day`
- **Boolean**: True/false values (empty string, 0, "never" are false)
- **List/Set**: Semicolon-separated values with methods like `.count`, `.sort()`
- **Color**: Hex values or color names, with RGB/HSB manipulation

### Designators (Note References)
- `parent`, `child`, `nextSibling`, `prevSibling` - Single note references
- `children`, `descendants`, `ancestors`, `siblings` - Group references
- Use in expressions like: `collect(children, $Priority)`

### Control Flow
- **Conditionals**: `if(condition){ } else { }`
- **Loops**: `children.each(item){ }` or `$MyList.each(var){ }`
- **Local variables**: `var(myVar){ myVar = "value"; }`

## Advanced Examples

The `examples/` directory contains sophisticated action patterns:

- **`smart-date-processing.txt`** - Temporal categorization and date analysis
- **`hierarchical-status.txt`** - Status propagation in project hierarchies  
- **`content-analysis.txt`** - Automated content classification and sentiment analysis
- **`color-by-priority.txt`** - Basic priority-based visual coding
- **`auto-tag.txt`** - Content-based automatic tagging

## Resources

### Official References (Current - v10.x)
- **[aTbRef v10 - Complete Reference](https://acrobatfaq.com/atbref10/)** - Most comprehensive and up-to-date reference (v10.2.0)
- **[Action Code Operators](https://acrobatfaq.com/atbref10/index/Automating_Tinderbox/Coding/Action_Code/Operators/Full_Operator_List.html)** - Complete operator list for v10
- **[Action Code Guide](https://acrobatfaq.com/atbref10/index/Automating_Tinderbox/Coding/Action_Code.html)** - Modern action code documentation
- **[System Attributes](https://acrobatfaq.com/atbref10/index/Automating_Tinderbox/Coding/Use_of_Attributes/Attribute_Listings/System_Attribute_List.html)** - All built-in attributes

### Legacy References (Historical)
- [Tinderbox Action Code Cookbook](https://www.eastgate.com/Tinderbox/cookbook/) - Official examples (older syntax)
- [Dot Operators Reference](https://www.eastgate.com/Tinderbox/cookbook/dotOperators.html) - Earlier documentation
- [Expressions Reference](https://www.eastgate.com/Tinderbox/cookbook/Expressions.html) - Legacy functions guide

## Modular Generation System

This workspace includes a **revolutionary modular generation system** that eliminates the need to maintain monolithic installer files:

### Traditional Approach (Still Supported)
- **Monolithic Files**: `complete-installer.txt` (210 lines) - single large file with all functionality
- **Manual Maintenance**: Edit code directly, difficult to track components
- **Version Control**: Hard to see what changed between versions

### New Modular Approach  
- **Structured Definitions**: Separate YAML files for each component type
- **Automated Generation**: Python script builds installer from definitions
- **Component Isolation**: Modify prototypes, functions, templates independently
- **Validation**: Built-in validation ensures definitions are correct
- **Version Control**: Clear diffs on individual components, not monolithic code

### Key Benefits
- **🔧 Maintainable**: Edit individual components without touching others
- **📋 Validated**: Automatic validation of all definition structures  
- **🔄 Reproducible**: Generate consistent installers from same definitions
- **📊 Trackable**: Git shows exactly what changed in each component
- **🚀 Extensible**: Easy to add new prototypes, functions, or templates
- **⚡ Fast**: Generate complete 225-line installer in seconds

### Architecture
- **Library Pattern**: Functions copied to `/Hints/Library/` for global access across Tinderbox documents  
- **Rule-Based Installation**: Reliable one-time setup that disables itself
- **Prototype System**: Complete inheritance hierarchy with templates and badges
- **Professional Output**: Ready for production use in Tinderbox v10.2.0

See [`builder/README.md`](builder/README.md) for complete modular system documentation.

---

*Happy coding! Create powerful Tinderbox actions to enhance your knowledge management workflows.*