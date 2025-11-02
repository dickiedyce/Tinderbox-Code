# Tinderbox Action Code Workspace

A comprehensive workspace for developing, testing, and organizing Tinderbox action code and automation scripts.

## Overview

This workspace provides a structured environment for creating Tinderbox actions, which are small code snippets that can be executed within the Tinderbox personal knowledge management application.

## Directory Structure

- **`/actions/`** - Main action code files
  - **Modular System**: `core-utils.txt`, `attributes-manager.txt`, `prototype-builder.txt`, `template-builder.txt`, `project-structure.txt`, `workspace-initializer.txt`
  - **Installation**: `installer_init_edict.txt` and `installer_init_rule.txt` for automated setup
  - Store your primary Tinderbox action code here organized by functionality

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

1. Create your action code in the `actions/` directory
2. Test your code using files in the `tests/` directory
3. Document your actions in the `docs/` directory
4. Share examples in the `examples/` directory

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

## Modular Architecture

This workspace uses a **modular architecture** for complex action code development:

- **Core Modules**: Focused, reusable components for logging, attributes, prototypes, templates, and project structure
- **Library Pattern**: Functions copied to `/Hints/Library/` for global access across Tinderbox documents  
- **Installation System**: Automated setup using edict-based copying and workspace initialization
- **Validation**: Comprehensive testing and error handling throughout all modules

See [`/docs/modular-architecture.md`](docs/modular-architecture.md) for complete architectural documentation.

---

*Happy coding! Create powerful Tinderbox actions to enhance your knowledge management workflows.*