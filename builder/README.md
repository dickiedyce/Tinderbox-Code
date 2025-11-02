# Tinderbox Installer Builder

This directory contains a modular system for generating Tinderbox installer files from structured YAML definitions.

## Overview

Instead of maintaining a monolithic installer file, you can now:
1. Define workspace structure in separate YAML files
2. Generate the installer using the Python build script
3. Maintain and version control the definitions separately

## Structure

```
builder/
├── definitions/         # YAML definition files
│   ├── workspace.yaml  # Folders, attributes, basic configuration
│   ├── prototypes.yaml # Prototype definitions with templates
│   ├── templates.yaml  # HTML export templates
│   └── functions.yaml  # Library function modules
├── build.py            # Python builder script
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

## Usage

### Prerequisites
```bash
pip install -r requirements.txt
```

### Build Installer
```bash
# Generate installer from definitions
python build.py

# Custom output location
python build.py -o actions/my-installer.txt

# Validate definitions only
python build.py --validate
```

### Customize Installation

1. **Modify Workspace Structure**: Edit `definitions/workspace.yaml`
   - Add/remove folders
   - Change attributes
   - Modify onAdd actions

2. **Update Prototypes**: Edit `definitions/prototypes.yaml`
   - Add new prototypes
   - Change badges or templates
   - Modify displayed attributes

3. **Create Templates**: Edit `definitions/templates.yaml`
   - Add HTML export templates
   - Customize existing templates

4. **Extend Functions**: Edit `definitions/functions.yaml`
   - Add new library modules
   - Create additional functions
   - Modify existing utilities

### Integration with Existing Workflow

The generated installer works exactly like the current `complete-installer.txt`:
1. Copy generated code to a Tinderbox note's $Rule attribute
2. Set $RuleDisabled=false
3. The installer runs once and sets up the complete workspace

## Benefits

- **Modular**: Each component defined separately
- **Maintainable**: Easy to modify individual pieces
- **Versioned**: Track changes to definitions in Git
- **Validated**: Built-in validation of definition structure
- **Reproducible**: Generate consistent installers from definitions
- **Extensible**: Easy to add new components or modify existing ones

## Definition File Reference

### workspace.yaml
- `workspace.name`: Display name for the workspace
- `workspace.description`: Description for header comments
- `workspace.folders[]`: Array of folder definitions with paths, badges, prototypes
- `workspace.attributes[]`: Custom attribute definitions
- `workspace.log`: Log note configuration

### prototypes.yaml
- `prototypes[]`: Array of prototype definitions
- Each prototype includes path, badge, template, display attributes, default values

### templates.yaml
- `templates[]`: Array of HTML export template definitions
- Each template includes path, badge, and HTML content

### functions.yaml
- `library_modules[]`: Array of function library modules
- Each module contains multiple function definitions with parameters and bodies