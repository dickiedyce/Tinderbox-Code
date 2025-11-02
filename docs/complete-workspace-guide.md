# Complete Tinderbox Workspace Installation Guide

## Overview

The **Complete Installer** (`actions/complete-installer.txt`) provides a full-featured Tinderbox workspace with modular project management capabilities, templates, prototypes, and automation.

## Features

### 1. Modular Library System
- **CoreUtils**: Basic utilities (`logMessage`, `setupContainer`, `addPrefix`, `childFolder`)
- **ProjectBuilder**: Full project automation (`buildProject`, `buildUserStory`, `buildRole`, `buildFR`, `buildNFR`)
- **TemplateBuilder**: HTML export templates for consistent formatting

### 2. Project Structure Automation
- Creating a note in `/Projects/` automatically triggers full project structure:
  - **User Stories** folder (with `buildUserStory()` OnAdd action)
  - **Roles** folder (with `buildRole()` OnAdd action) 
  - **Functional Requirements** folder (with `buildFR()` OnAdd action)
  - **Non-Functional Requirements** folder (with `buildNFR()` OnAdd action)

### 3. Templates & Prototypes
- **Templates**: `/Templates/Preview Folder` and `/Templates/Preview Story`
- **Prototypes**: `/Prototypes/pFolder` and `/Prototypes/pStory`
- Automatic linking of prototypes to appropriate templates
- Custom attributes for user stories: `$StoryRole`, `$StoryWant`, `$StoryReason`

### 4. CSS Styling
- Pre-configured CSS at `/Hints/Preview/style` for HTML export
- Professional typography and layout ready for documentation

## Installation Instructions

1. **Copy the complete installer code** from `actions/complete-installer.txt`
2. **Create a new note** in your Tinderbox document
3. **Paste the code into the note's `$Rule` attribute**
4. **Set `$RuleDisabled = false`** on the note
5. **The installer will run immediately and create the full workspace structure**

## How It Works

### Automatic Project Creation
1. Create a new note in the `/Projects/` folder
2. The note automatically gets the `pFolder` prototype and `address-book` badge
3. Four sub-folders are created automatically:
   - `[Project Name] User Stories`
   - `[Project Name] Roles` 
   - `[Project Name] Functional Requirements`
   - `[Project Name] Non-Functional Requirements`

### Adding Project Items
- **User Stories**: Add to the User Stories folder, gets `pStory` prototype and `user-tag` badge
- **Roles**: Add to Roles folder, includes template text for responsibilities and requirements
- **Functional Requirements**: Add to FR folder, gets `FR-` prefix and includes acceptance criteria template
- **Non-Functional Requirements**: Add to NFR folder, gets `NFR-` prefix and includes measurement criteria template

### HTML Export
All items are configured with appropriate HTML export templates for professional documentation generation.

## Validation

The installer has been validated with the workspace validation script:
- ✅ Syntax checks passed
- ✅ All required functions properly defined
- ✅ Modular architecture works correctly
- ✅ Project automation functions as expected

## File Structure Created

```
/
├── Hints/
│   ├── Library/
│   │   ├── CoreUtils (basic utility functions)
│   │   ├── ProjectBuilder (project automation)
│   │   └── TemplateBuilder (template management)
│   └── Preview/
│       └── style (CSS for HTML export)
├── Projects/ (OnAdd: buildProject)
├── Resources/
├── Templates/
│   ├── Preview Folder
│   └── Preview Story
├── Prototypes/
│   ├── pFolder → Preview Folder template
│   └── pStory → Preview Story template
└── Log (installation and activity log)
```

## Functions Available Globally

After installation, these functions are available anywhere in the document:

- `logMessage(message)` - Add messages to the log
- `setupContainer(path, badge)` - Create organized containers
- `addPrefix(prefix)` - Add prefixes to note names
- `childFolder(root, name)` - Create structured sub-folders
- `buildProject()` - Create full project structure
- `buildUserStory()`, `buildRole()`, `buildFR()`, `buildNFR()` - Create specific project items

## Next Steps

1. **Test the installation** by creating a note in `/Projects/`
2. **Verify project structure** is created automatically
3. **Add user stories, roles, and requirements** to test the automation
4. **Export to HTML** to verify templates work correctly
5. **Customize** prototypes and templates as needed for your workflow

The complete installer provides a professional, automated Tinderbox workspace ready for complex project management and documentation generation.